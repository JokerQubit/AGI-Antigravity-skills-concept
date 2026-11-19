---
name: hardened_clean_architecture
version: 6.0.0
description: "Use when building, refactoring, or reviewing backend services, APIs, domain logic, file persistence, concurrency locks, or TypeScript/Node modules. Enforces decoupled Clean Architecture (core/use_cases/adapters), zero-allocation Result<T,E>/Option<T> error handling, DeterministicAtomicSwap with dual SHA-256 verification, FsLockEngine (O_CREAT|O_EXCL), full-jitter backoff polling, and strict zero-stub production code."
---

# Hardened Clean Architecture & Defensive Concurrency — Hyper-Cortex v6.0

Playbook de engenharia de software defensiva em nível de produção. Define padrões determinísticos para separação de camadas, tratamento tipado de erros sem exceções não capturadas, exclusão mútua no filesystem (`FsLockEngine`), persistência atômica com dupla verificação criptográfica (`DeterministicAtomicSwap`) e erradicação absoluta de stubs.

> **Escopo Universal & Roteamento v6.0:** Aplicável a qualquer alteração em código de produção, APIs, domínio ou persistência — inclusive correções pontuais. Para orquestração multiagente e travas de contrato entre workers, consulte `swarm_orchestration` e `rules/`. Para auditoria independente pós-implementação, acione `forensic_adversarial_auditor`.
> - **Modelagem de Domínio & Concorrência Crítica:** **Gemini 4 Neon High** (`gemini-4-neon-high`)
> - **Implementação Paralela de Camadas & Adaptadores:** **Hydrogen 4 XHigh** (`gemini-4-hydrogen-xhigh`) ou **Hydrogen 4 High** (`gemini-4-hydrogen-high`)

---

## 1. Topologia Limpa de Camadas Desacopladas

Toda base de código ou mutação arquitetural deve isolar responsabilidades em três camadas unidirecionais (adaptadores dependem de portas do núcleo; o núcleo nunca importa infraestrutura):

```text
src/
├── core/                  # Camada 1: Domínio Puro (Entidades, Invariantes, Interfaces/Portas)
│   ├── entities/          # Tipos puros, imutabilidade, validação de invariantes
│   ├── types/             # Result<T, E>, Option<T>, erros discriminados
│   └── ports/             # Contratos abstratos (interfaces) sem acoplamento a I/O
│
├── use_cases/             # Camada 2: Aplicação & Orquestração
│   ├── createOrder.ts     # Fluxos coordenando entidades e portas injetadas
│   └── syncTelemetry.ts   # Orquestração assíncrona determinística
│
└── adapters/              # Camada 3: Infraestrutura, I/O & UI
    ├── storage/           # Repositórios concretos (SQLite, Postgres, FileSystem)
    ├── api/               # Roteadores HTTP, handlers WebSocket, validação de payload
    └── ui/                # Componentes visuais desacoplados da lógica de infra
```

---

## 2. Tratamento Tipado de Erros: `Result<T, E>` e `Option<T>` de Zero Alocação

O uso de `catch (e) {}` vazio, retorno ambíguo de `null` para falhas de infraestrutura ou lançamento de exceções não tipadas (`throw new Error`) em fluxos esperados é proibido. Operações falíveis explicitam todas as ramificações em tempo de compilação via uniões discriminadas congeladas (monomórficas em V8, sem alocação de classes):

```typescript
// src/core/types/result.ts

export type Result<T, E> =
  | { readonly ok: true; readonly value: T; readonly error?: never }
  | { readonly ok: false; readonly error: E; readonly value?: never };

export type Option<T> =
  | { readonly isSome: true; readonly value: T }
  | { readonly isSome: false; readonly value?: never };

// Singleton imutável para Option.None (Zero Alocação de Objeto)
export const NONE: Option<never> = Object.freeze({ isSome: false });

export const Ok = <T>(value: T): Result<T, never> => ({
  ok: true,
  value,
});

export const Err = <E>(error: E): Result<never, E> => ({
  ok: false,
  error,
});

export const Some = <T>(value: T): Option<T> => ({
  isSome: true,
  value,
});

export const None = <T = never>(): Option<T> => NONE;

/**
 * Garante exaustividade em tempo de compilação para uniões discriminadas.
 */
export function assertNever(x: never): never {
  throw new Error(`Exaustividade violada! Valor inesperado: ${JSON.stringify(x)}`);
}
```

### Invariante de Fronteira Segura
Toda fronteira com APIs externas, filesystem, parsing JSON ou drivers de banco deve encapsular falhas em `try/catch` local na camada de adaptador e retornar `Result<T, E>` tipado para os casos de uso.

---

## 3. Persistência Atômica com Dupla Atestação SHA-256 (`DeterministicAtomicSwap`)

Para prevenir truncamento de arquivos, leituras parciais concorrentes ou perda de dados em cache do SO, toda gravação crítica em disco executa o ciclo de 6 fases do `DeterministicAtomicSwap`:

1. **Staging no Mesmo Volume:** Cria arquivo temporário no mesmo diretório pai (`<target>.tmp.<pid>.<time>.<rand>`), prevenindo erros `EXDEV`.
2. **Flush Físico:** Grava o payload integral e invoca `fs.fsyncSync(fd)` para persistência física na controladora.
3. **Atestação Pré-Swap:** Calcula o SHA-256 do arquivo temporário e compara com o buffer em memória antes da troca.
4. **Substituição Atômica:** Executa `fs.renameSync` (troca atômica $O(1)$ de ponteiro no inode/MFT).
5. **Atestação Pós-Swap:** Relê o destino consolidado e valida novamente o SHA-256 físico contra o esperado.
6. **Recibo Fiduciário:** Emite `AtomicWriteReceipt` com metadados e hash consolidado.

```typescript
// src/core/concurrency/DeterministicAtomicSwap.ts
import * as fs from 'fs';
import * as path from 'path';
import * as crypto from 'crypto';
import { Result, Ok, Err } from '../types/result';

export interface AtomicWriteReceipt {
  readonly targetPath: string;
  readonly byteLength: number;
  readonly sha256: string;
  readonly committedAt: number;
}

export type AtomicSwapError =
  | { code: 'PRE_SWAP_HASH_MISMATCH'; expectedHash: string; actualHash: string }
  | { code: 'POST_SWAP_VERIFICATION_FAILED'; expectedHash: string; readHash: string }
  | { code: 'FS_RENAME_FAILED'; originalError: Error }
  | { code: 'FS_STAGING_ERROR'; originalError: Error };

export class DeterministicAtomicSwap {
  /**
   * Executa substituição atômica em disco com dupla atestação SHA-256.
   */
  public static writeAtomicVerified(
    targetPath: string,
    content: string | Buffer
  ): Result<AtomicWriteReceipt, AtomicSwapError> {
    const dir = path.dirname(targetPath);
    if (!fs.existsSync(dir)) {
      fs.mkdirSync(dir, { recursive: true });
    }

    const payloadBuffer = Buffer.isBuffer(content) ? content : Buffer.from(content, 'utf-8');
    const expectedSha256 = crypto.createHash('sha256').update(payloadBuffer).digest('hex');

    // 1. Arquivo temporário no mesmo volume e diretório (evita EXDEV)
    const tempSuffix = `${process.pid}.${Date.now()}.${crypto.randomBytes(4).toString('hex')}`;
    const tempPath = `${targetPath}.tmp.${tempSuffix}`;

    try {
      // 2. Gravação integral + flush físico
      const fd = fs.openSync(tempPath, 'w', 0o666);
      try {
        fs.writeFileSync(fd, payloadBuffer);
        fs.fsyncSync(fd);
      } finally {
        fs.closeSync(fd);
      }

      // 3. Atestação pré-swap
      const stagedBytes = fs.readFileSync(tempPath);
      const stagedHash = crypto.createHash('sha256').update(stagedBytes).digest('hex');

      if (stagedHash !== expectedSha256) {
        try {
          fs.unlinkSync(tempPath);
        } catch {}
        return Err({
          code: 'PRE_SWAP_HASH_MISMATCH',
          expectedHash: expectedSha256,
          actualHash: stagedHash,
        });
      }

      // 4. Troca atômica no filesystem
      try {
        fs.renameSync(tempPath, targetPath);
      } catch (renameErr: unknown) {
        try {
          fs.unlinkSync(tempPath);
        } catch {}
        return Err({
          code: 'FS_RENAME_FAILED',
          originalError: renameErr instanceof Error ? renameErr : new Error(String(renameErr)),
        });
      }

      // 5. Atestação pós-swap
      const verifiedBytes = fs.readFileSync(targetPath);
      const postSwapHash = crypto.createHash('sha256').update(verifiedBytes).digest('hex');

      if (postSwapHash !== expectedSha256) {
        return Err({
          code: 'POST_SWAP_VERIFICATION_FAILED',
          expectedHash: expectedSha256,
          readHash: postSwapHash,
        });
      }

      // 6. Recibo de integridade
      return Ok({
        targetPath,
        byteLength: payloadBuffer.length,
        sha256: postSwapHash,
        committedAt: Date.now(),
      });
    } catch (stagingErr: unknown) {
      try {
        if (fs.existsSync(tempPath)) {
          fs.unlinkSync(tempPath);
        }
      } catch {}
      return Err({
        code: 'FS_STAGING_ERROR',
        originalError: stagingErr instanceof Error ? stagingErr : new Error(String(stagingErr)),
      });
    }
  }
}
```

---

## 4. Exclusão Mútua no Filesystem (`FsLockEngine`)

Quando múltiplos processos ou workers concorrentes acessam arquivos compartilhados (ex: `synaptic_bus.json`, `.planning/thought_graph.json`, `.planning/ledger/`), a exclusão mútua é garantida pela primitiva indivisível do kernel `O_CREAT | O_EXCL` (flag `'wx'`):

1. **Atomicidade em Kernel:** `fs.openSync(lockPath, 'wx')` cria o `.lock` em operação única; se existir, falha com `EEXIST` (zero TOCTOU).
2. **Metadados de Lease:** O `.lock` registra versão, recurso, `acquiredAt`, `ttlMs`, `ownerPid` e `leaseSignature`.
3. **Recuperação Determinística de Stale Locks:** Se `Date.now() - acquiredAt > ttlMs` ou `!isProcessAlive(ownerPid)` via `process.kill(pid, 0)`, o lock órfão é removido com segurança.
4. **Liberação Segura:** Valida `leaseSignature` antes de remover o `.lock`, impedindo que um processo expire e remova o lock adquirido por outro par.
5. **Backoff com Full Jitter:** Desincroniza tentativas concorrentes evitando *Thundering Herd*.

```typescript
// src/core/concurrency/FsLockEngine.ts
import * as fs from 'fs';
import * as crypto from 'crypto';
import { Result, Ok, Err } from '../types/result';

export interface LockMetadata {
  lockVersion: string;
  resourcePath: string;
  acquiredAt: number;
  ttlMs: number;
  ownerSubagentId: string;
  ownerPid: number;
  leaseSignature: string;
}

export type LockAcquisitionError =
  | { code: 'RESOURCE_LOCKED'; resource: string; holderPid: number; remainingTtlMs: number }
  | { code: 'STALE_LOCK_RECOVERY_FAILED'; cause: string }
  | { code: 'IO_SYSTEM_ERROR'; message: string };

export class FsLockEngine {
  private static readonly LOCK_EXTENSION = '.lock';
  private static readonly DEFAULT_TTL_MS = 15000;

  /**
   * Adquire lock exclusivo para o arquivo alvo usando O_CREAT | O_EXCL (flag 'wx').
   */
  public static acquireLock(
    targetFilePath: string,
    ownerSubagentId: string,
    ttlMs: number = this.DEFAULT_TTL_MS
  ): Result<{ lockPath: string; release: () => void }, LockAcquisitionError> {
    const lockPath = `${targetFilePath}${this.LOCK_EXTENSION}`;
    const now = Date.now();
    const pid = process.pid;
    const leaseSignature = crypto.randomBytes(16).toString('hex');

    const metadata: LockMetadata = {
      lockVersion: '6.0.0',
      resourcePath: targetFilePath,
      acquiredAt: now,
      ttlMs,
      ownerSubagentId,
      ownerPid: pid,
      leaseSignature,
    };

    const payload = JSON.stringify(metadata, null, 2);

    try {
      const fd = fs.openSync(lockPath, 'wx');
      try {
        fs.writeFileSync(fd, payload, 'utf-8');
        fs.fsyncSync(fd);
      } finally {
        fs.closeSync(fd);
      }

      return Ok({
        lockPath,
        release: () => {
          this.releaseLock(lockPath, leaseSignature);
        },
      });
    } catch (error: unknown) {
      const errCode = (error as NodeJS.ErrnoException)?.code;
      if (errCode === 'EEXIST') {
        const staleEval = this.evaluateAndRecoverStaleLock(lockPath, now);
        if (!staleEval.ok) {
          return Err(staleEval.error);
        }

        try {
          const retryFd = fs.openSync(lockPath, 'wx');
          try {
            fs.writeFileSync(retryFd, payload, 'utf-8');
            fs.fsyncSync(retryFd);
          } finally {
            fs.closeSync(retryFd);
          }
          return Ok({
            lockPath,
            release: () => {
              this.releaseLock(lockPath, leaseSignature);
            },
          });
        } catch {
          return Err({
            code: 'RESOURCE_LOCKED',
            resource: targetFilePath,
            holderPid: -1,
            remainingTtlMs: ttlMs,
          });
        }
      }

      return Err({
        code: 'IO_SYSTEM_ERROR',
        message: error instanceof Error ? error.message : String(error),
      });
    }
  }

  private static evaluateAndRecoverStaleLock(
    lockPath: string,
    currentTimeMs: number
  ): Result<void, LockAcquisitionError> {
    try {
      if (!fs.existsSync(lockPath)) {
        return Ok(undefined);
      }

      const rawContent = fs.readFileSync(lockPath, 'utf-8');
      const meta: LockMetadata = JSON.parse(rawContent);

      const isExpired = currentTimeMs - meta.acquiredAt > meta.ttlMs;
      const isProcessDead = !this.isProcessAlive(meta.ownerPid);

      if (isExpired || isProcessDead) {
        fs.unlinkSync(lockPath);
        return Ok(undefined);
      }

      const remainingTtl = Math.max(0, meta.ttlMs - (currentTimeMs - meta.acquiredAt));
      return Err({
        code: 'RESOURCE_LOCKED',
        resource: meta.resourcePath,
        holderPid: meta.ownerPid,
        remainingTtlMs: remainingTtl,
      });
    } catch (e: unknown) {
      return Err({
        code: 'STALE_LOCK_RECOVERY_FAILED',
        cause: e instanceof Error ? e.message : String(e),
      });
    }
  }

  public static releaseLock(lockPath: string, leaseSignature: string): void {
    try {
      if (fs.existsSync(lockPath)) {
        const rawContent = fs.readFileSync(lockPath, 'utf-8');
        const meta: LockMetadata = JSON.parse(rawContent);
        if (meta.leaseSignature === leaseSignature) {
          fs.unlinkSync(lockPath);
        }
      }
    } catch {
      // Falha ao liberar lock já expirado/removido não deve interromper o fluxo
    }
  }

  private static isProcessAlive(pid: number): boolean {
    try {
      process.kill(pid, 0);
      return true;
    } catch (e: unknown) {
      return (e as NodeJS.ErrnoException)?.code === 'EPERM';
    }
  }

  public static calculateJitterDelay(attempt: number, baseMs = 50, maxMs = 2500): number {
    const exponential = Math.min(maxMs, baseMs * Math.pow(2, attempt));
    return Math.floor(Math.random() * exponential);
  }
}
```

---

## 5. Concorrência Assíncrona Determinística (Anti-Sleep Polling & Full Jitter)

Proibido usar loops ativos com intervalo fixo (`while (true) { await sleep(1000); }`). Quando polling for inevitável (preferir eventos/watchers sempre que possível), aplique **Backoff Exponencial com Jitter** retornando `Result<T, PollingError>`:

```typescript
// src/lib/resilientPolling.ts
import { Result, Ok, Err } from '../core/types/result';

export interface BackoffOptions {
  initialDelayMs: number;
  maxDelayMs: number;
  maxAttempts: number;
  backoffFactor: number;
}

export type PollingError =
  | { code: 'POLLING_TIMEOUT'; attempts: number }
  | { code: 'CHECK_FAILED'; cause: Error };

export async function pollUntilReady<T>(
  checkFn: () => Promise<T | null>,
  options: BackoffOptions = { initialDelayMs: 200, maxDelayMs: 5000, maxAttempts: 10, backoffFactor: 1.5 }
): Promise<Result<T, PollingError>> {
  let attempt = 0;
  let delay = options.initialDelayMs;

  while (attempt < options.maxAttempts) {
    try {
      const result = await checkFn();
      if (result !== null) {
        return Ok(result);
      }
    } catch (err: unknown) {
      return Err({
        code: 'CHECK_FAILED',
        cause: err instanceof Error ? err : new Error(String(err)),
      });
    }

    attempt++;
    if (attempt >= options.maxAttempts) {
      return Err({ code: 'POLLING_TIMEOUT', attempts: options.maxAttempts });
    }

    // Jitter aleatório (+-15%) para evitar tempestades de requisições sincronizadas
    const jitter = delay * (0.85 + Math.random() * 0.3);
    await new Promise((resolve) => setTimeout(resolve, jitter));
    delay = Math.min(delay * options.backoffFactor, options.maxDelayMs);
  }

  return Err({ code: 'POLLING_TIMEOUT', attempts: options.maxAttempts });
}
```

---

## 6. Implementação Completa Zero-Stub & Pedagogia Contrastiva

Todo código persistido em arquivos de produção deve ser completo e funcional — zero `TODO`, `pass`, `return null` disfarçando falha ou mocks em produção.

### Exemplar 1: Serviço de Domínio & Tratamento Tipado de Erros

#### ❌ WRONG (Anti-Pattern):
```typescript
export class UserService {
  async getUser(id: string) {
    try {
      // TODO: implementar cache redis
      const res = await db.query('SELECT * FROM users WHERE id = ' + id);
      return res.rows[0];
    } catch (e) {
      console.error('Erro ao buscar usuario:', e);
      return null;
    }
  }
}
```
**Por que falha:** (1) SQL injection por concatenação; (2) `return null` confunde usuário inexistente com queda do banco; (3) engolimento silencioso de exceção; (4) acoplamento direto ao global `db` em vez de porta injetada; (5) stub `// TODO` em produção.

#### ✅ CORRECT (Hardened Clean Architecture & `Result<T, E>`):
```typescript
import { Result, Ok, Err } from '../core/types/result';
import { User, UserId } from '../core/entities/User';
import { UserRepository } from '../core/ports/UserRepository';

export type GetUserError =
  | { code: 'INVALID_ID_FORMAT'; message: string }
  | { code: 'USER_NOT_FOUND'; userId: string }
  | { code: 'STORAGE_UNAVAILABLE'; cause: Error };

export class UserService {
  constructor(private readonly repository: UserRepository) {}

  async getUser(rawId: string): Promise<Result<User, GetUserError>> {
    const idValidation = UserId.create(rawId);
    if (!idValidation.ok) {
      return Err({
        code: 'INVALID_ID_FORMAT',
        message: idValidation.error.message,
      });
    }

    try {
      const user = await this.repository.findById(idValidation.value);
      if (!user) {
        return Err({ code: 'USER_NOT_FOUND', userId: rawId });
      }
      return Ok(user);
    } catch (error: unknown) {
      return Err({
        code: 'STORAGE_UNAVAILABLE',
        cause: error instanceof Error ? error : new Error(String(error)),
      });
    }
  }
}
```

### Exemplar 2: Persistência Atômica vs. Corrupção por Escrita Direta

#### ❌ WRONG (Escrita direta trunca arquivo em falha parcial):
```typescript
import fs from 'fs';

export function saveSettings(filePath: string, data: object): void {
  fs.writeFileSync(filePath, JSON.stringify(data, null, 2), 'utf-8');
}
```

#### ✅ CORRECT (`DeterministicAtomicSwap` com dupla verificação SHA-256):
```typescript
import { DeterministicAtomicSwap, AtomicWriteReceipt, AtomicSwapError } from '../core/concurrency/DeterministicAtomicSwap';
import { Result } from '../core/types/result';

export function saveSettingsAtomic(
  targetPath: string,
  data: unknown
): Result<AtomicWriteReceipt, AtomicSwapError> {
  return DeterministicAtomicSwap.writeAtomicVerified(
    targetPath,
    JSON.stringify(data, null, 2)
  );
}
```

---

## 7. Checklist Forense de Concorrência & Clean Architecture (Binário)

Auditado por verificador independente (`forensic_adversarial_auditor`) com evidência direta no disco:

- [ ] **`Result<T,E>` / `Option<T>` Zero-Allocation:** zero `any`, casts inseguros ou exceções não capturadas em fronteiras de I/O; `assertNever` para exaustividade em uniões discriminadas.
- [ ] **Zero-Stub Permanente:** zero `TODO`, `pass`, `return null` para erros, `{}` vazio ou mocks em código de produção.
- [ ] **`DeterministicAtomicSwap`:** gravações críticas em disco usam staging no mesmo volume, `fsyncSync`, `fs.renameSync` e dupla verificação SHA-256 pré e pós-swap.
- [ ] **`FsLockEngine` (`O_CREAT | O_EXCL`):** concorrência de arquivos mediada por lock `'wx'` com `LockMetadata`, verificação de PID ativo e limpeza determinística de stale locks.
- [ ] **Portas Desacopladas:** interfaces em `core/ports/`; implementações concretas em `adapters/`; zero importação reversa do núcleo para infraestrutura.
- [ ] **Polling Resiliente:** zero loops `sleep` fixos; backoff exponencial com jitter ou fluxo orientado a eventos.
- [ ] **Zero Vazamento Interno:** nenhum termo interno de orquestração/auditoria aparece em UIs, logs de usuário ou respostas de API.
- [ ] **Build & Testes Limpos:** compilação/typecheck sem erros (`npx tsc --noEmit`, `$LASTEXITCODE === 0`) e testes da unidade passando após a última edição.
