---
name: hardened_clean_architecture
version: 5.0.0
description: "v5.0 — Universal Cognitive Parity & Concurrency Kernel. Manual prático de engenharia de software defensiva, Clean Architecture desacoplada, tipagem estrita via uniões discriminadas Result/Option de zero alocação, FsLockEngine (O_CREAT|O_EXCL), DeterministicAtomicSwap com dupla atestação SHA-256 pré e pós-swap e erradicação definitiva de stubs e exceções não capturadas."
---

# Hardened Clean Architecture & Defensive Concurrency Playbook — v5.0 (Universal Cognitive Parity & Concurrency Kernel)

Manual de implementação de engenharia de software em nível de produção sênior. Estabelece padrões determinísticos para segregação de camadas arquiteturais, manipulação tipada de erros sem exceções cegas, controle semafórico de concorrência no filesystem (`FsLockEngine`), persistência atômica com atestação criptográfica dupla (`DeterministicAtomicSwap`) e eliminação absoluta de stubs e exceções não capturadas.

> **Salvaguarda v5.0 — Ativação Compulsória Universal:**
> Na v5.0.0, as salvaguardas de Clean Architecture Defensiva e Concurrency Kernel desta skill são disparadas compulsoriamente a qualquer interação operacional que toque arquivos de código ou arquitetura — sem distinção de escopo ou complexidade. O conceito de "ajuste simples" que dispensa Result<T,E>/Option<T>, FsLockEngine, DeterministicAtomicSwap ou testes estritos está terminantemente extinto.

---

## 1. Topologia Limpa de Camadas Desacopladas

Toda interação que realize mutação em código ou arquitetura deve separar responsabilidades em três camadas fundamentais:

```text
src/
├── core/                  # Camada 1: Domínio Puro (Entidades, Regras de Negócio, Interfaces de Repositório)
│   ├── entities/          # Tipos puros, immutability, invariantes de negócio
│   └── ports/             # Contratos abstratos (interfaces) sem acoplamento a banco ou rede
│
├── use_cases/             # Camada 2: Aplicação & Orquestração
│   ├── createOrder.ts     # Fluxos de execução coordenando domínio e portas
│   └── syncTelemetry.ts   # Orquestração assíncrona
│
├── adapters/              # Camada 3: Infraestrutura, I/O & Frameworks
│   ├── storage/           # Implementação real de repositórios (SQLite, Postgres, FileSystem)
│   ├── api/               # Roteadores HTTP, handlers de WebSocket, schemas de payload
│   └── ui/                # Componentes visuais desacoplados da lógica de infra
```

---

## 2. Tratamento Tipado de Erros com o Padrão Result<T, E> e Option<T> de Zero Alocação

O uso de `try/catch` genérico, blocos vazios `catch (e) {}` ou exceções não capturadas (`throw new Error`) é expressamente proibido na v5.0. Todas as operações com possibilidade de falha devem explicitar suas ramificações em tempo de compilação através de uniões discriminadas literais congeladas em memória (`Result<T, E>` e `Option<T>`), garantindo monomorfismo nos call-sites do V8 e zero alocação de classes:

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
 * Força a exaustividade em tempo de compilação para uniões discriminadas.
 */
export function assertNever(x: never): never {
  throw new Error(`Exaustividade violada! Valor inesperado: ${JSON.stringify(x)}`);
}
```

### Invariante de Zero Exceções Não Capturadas:
Toda fronteira com APIs de terceiros, subsistemas de I/O ou parsing JSON deve ser encapsulada em funções seguras que capturam falhas e retornam `Result<T, E>`. Disparar exceções não tratadas no runtime constitui quebra da cadeia fiduciária e desotimiza o motor de execução.

---

## 3. Validação Determinística de Atomic Swap com Verificação Dupla SHA-256 (`DeterministicAtomicSwap`)

Para prevenir corrupção de arquivos, leituras parciais concorrentes ou perda de dados por falha de cache do sistema operacional, toda gravação no disco opera obrigatoriamente através do padrão `DeterministicAtomicSwap` com máquina de estados de 6 fases:

1. **Staging no Mesmo Volume:** Gera arquivo temporário no mesmo diretório pai (`<target>.tmp.<pid>.<time>.<rand>`), prevenindo erros `EXDEV` de travessia de volumes.
2. **Flush Físico:** Grava payload integral e invoca compulsoriamente `fs.fsyncSync(fd)` para forçar a controladora a persistir os bytes no disco físico.
3. **Atestação Pré-Swap:** Computa o hash SHA-256 do arquivo temporário e confronta com o hash do buffer em memória antes da renomeação.
4. **Substituição Atômica:** Executa `fs.renameSync` (operação atômica $O(1)$ de ponteiro no MFT/inode do SO).
5. **Atestação Pós-Swap:** Lê o arquivo final gravado no caminho de destino e valida novamente o hash SHA-256 físico contra o esperado.
6. **Recibo Fiduciário de Integridade:** Emite `AtomicWriteReceipt` contendo o hash criptográfico e metadados de commit.

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
   * Executa a substituição atômica com garantia transacional e dupla atestação de hash SHA-256.
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

    // 1. Gera arquivo temporário no mesmo volume e diretório (Invariante de Mesmo Volume)
    const tempSuffix = `${process.pid}.${Date.now()}.${crypto.randomBytes(4).toString('hex')}`;
    const tempPath = `${targetPath}.tmp.${tempSuffix}`;

    try {
      // 2. Grava integralmente no arquivo de isolamento e força flush físico no disco
      const fd = fs.openSync(tempPath, 'w', 0o666);
      try {
        fs.writeFileSync(fd, payloadBuffer);
        fs.fsyncSync(fd); // Força liberação de cache no subsistema de armazenamento
      } finally {
        fs.closeSync(fd);
      }

      // 3. Verificação de integridade pré-swap
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

      // 4. Troca atômica de ponteiro de diretório no sistema de arquivos
      try {
        fs.renameSync(tempPath, targetPath);
      } catch (renameErr: any) {
        try {
          fs.unlinkSync(tempPath);
        } catch {}
        return Err({
          code: 'FS_RENAME_FAILED',
          originalError: renameErr instanceof Error ? renameErr : new Error(String(renameErr)),
        });
      }

      // 5. Verificação determinística pós-swap no arquivo final consolidado
      const verifiedBytes = fs.readFileSync(targetPath);
      const postSwapHash = crypto.createHash('sha256').update(verifiedBytes).digest('hex');

      if (postSwapHash !== expectedSha256) {
        return Err({
          code: 'POST_SWAP_VERIFICATION_FAILED',
          expectedHash: expectedSha256,
          readHash: postSwapHash,
        });
      }

      // 6. Recibo fiduciário de commit
      return Ok({
        targetPath,
        byteLength: payloadBuffer.length,
        sha256: postSwapHash,
        committedAt: Date.now(),
      });
    } catch (stagingErr: any) {
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

## 4. Protocolo de Bloqueio Semafórico & Exclusão Mútua no Filesystem (`FsLockEngine`)

Em ambientes com múltiplos subagentes concorrentes disputando arquivos compartilhados (`synaptic_bus.json`, `.planning/expediente_state.json`), a exclusão mútua é garantida pela primitiva atômica indivisível do SO: `O_CREAT | O_EXCL` (flag `'wx'`).

### Características do `FsLockEngine`:
1. **Atomicidade em Kernel:** `fs.openSync(lockPath, 'wx')` cria o arquivo de trava e obtém o descritor de arquivo em uma única operação indivisível no MFT/inode. Se já existir, falha imediatamente com `EEXIST` (zero TOCTOU).
2. **Cabeçalho de Metadados de Lock:** O arquivo `.lock` contém versão, recurso alvo, timestamp de aquisição, TTL em ms, PID do processo proprietário e assinatura de arrendamento criptográfica (`leaseSignature`).
3. **Detecção e Quebra Determinística de Stale Locks (Orphan Clearing):**
   - Se `Date.now() - acquiredAt > ttlMs`, o lock expirou fiduciariamente.
   - Testa a liveness do processo via `process.kill(ownerPid, 0)`. Se o PID estiver extinto, o lock é classificado como `ZOMBIE_ORPHAN` e removido via `fs.unlinkSync`.
4. **Liberação Fiduciária Segura:** A liberação confronta a `leaseSignature` para evitar que um subagente expire e libere acidentalmente o lock adquirido por outro par.
5. **Backoff com Full Jitter:** Desincroniza rajadas concorrentes evitando tempestade de concorrência (*Thundering Herd Problem*).

```typescript
// src/core/concurrency/FsLockEngine.ts
import * as fs from 'fs';
import * as path from 'path';
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
   * Tenta adquirir o lock exclusivo para o arquivo alvo usando a primitiva O_CREAT | O_EXCL (flag 'wx').
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
      lockVersion: '5.0.0',
      resourcePath: targetFilePath,
      acquiredAt: now,
      ttlMs,
      ownerSubagentId,
      ownerPid: pid,
      leaseSignature,
    };

    const payload = JSON.stringify(metadata, null, 2);

    try {
      // 1. Primitiva atômica do kernel do SO: falha instantânea se já existir
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
    } catch (error: any) {
      if (error.code === 'EEXIST') {
        // 2. O arquivo de lock existe. Avaliar se o lock está órfão (stale)
        const staleEval = this.evaluateAndRecoverStaleLock(lockPath, now);
        if (!staleEval.ok) {
          return Err(staleEval.error);
        }

        // Se conseguiu desobstruir o lock órfão, tenta uma única reaquisição direta
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
        } catch (retryError: any) {
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
        message: String(error.message || error),
      });
    }
  }

  /**
   * Avalia a obsolescência de um lock e desobstrui se o processo original expirou ou morreu.
   */
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
        // Quebra atômica de lock órfão
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
    } catch (e: any) {
      return Err({
        code: 'STALE_LOCK_RECOVERY_FAILED',
        cause: String(e.message || e),
      });
    }
  }

  /**
   * Liberação segura de lock validando a assinatura de arrendamento (evita liberar lock alheio).
   */
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
      // Falha silenciosa de liberação não deve quebrar a esteira fiduciária
    }
  }

  /**
   * Testa a vitalidade do processo no Windows/POSIX sem emitir sinal letal.
   */
  private static isProcessAlive(pid: number): boolean {
    try {
      process.kill(pid, 0);
      return true;
    } catch (e: any) {
      return e.code === 'EPERM'; // Existe, mas pertence a outro usuário
    }
  }

  /**
   * Calcula delay de backoff exponencial decorrelacionado com Full Jitter.
   */
  public static calculateJitterDelay(attempt: number, baseMs = 50, maxMs = 2500): number {
    const exponential = Math.min(maxMs, baseMs * Math.pow(2, attempt));
    return Math.floor(Math.random() * exponential);
  }
}
```

---

## 5. Concorrência Assíncrona Determinística (Anti-Sleep Polling & Full Jitter)

É proibido utilizar loops ativos baseados em `sleep` (`while (true) { await sleep(1000); }`). Quando for necessário monitorar alterações ou executar polling com resiliência, aplique **Backoff Exponencial com Jitter** ou canais orientados a eventos:

```typescript
// src/lib/resilientPolling.ts
export interface BackoffOptions {
  initialDelayMs: number;
  maxDelayMs: number;
  maxAttempts: number;
  backoffFactor: number;
}

export async function pollUntilReady<T>(
  checkFn: () => Promise<T | null>,
  options: BackoffOptions = { initialDelayMs: 200, maxDelayMs: 5000, maxAttempts: 10, backoffFactor: 1.5 }
): Promise<T> {
  let attempt = 0;
  let delay = options.initialDelayMs;

  while (attempt < options.maxAttempts) {
    const result = await checkFn();
    if (result !== null) {
      return result;
    }

    attempt++;
    if (attempt >= options.maxAttempts) {
      throw new Error(`Operação atingiu timeout após ${options.maxAttempts} tentativas.`);
    }

    // Aplica jitter aleatório (+- 15%) para evitar tempestades de requisições sincronizadas
    const jitter = delay * (0.85 + Math.random() * 0.3);
    await new Promise((resolve) => setTimeout(resolve, jitter));

    delay = Math.min(delay * options.backoffFactor, options.maxDelayMs);
  }

  throw new Error('Falha de concorrência indeterminada.');
}
```

---

## 6. Implementação Completa Zero-Stub & Pedagogia Contrastiva (Lei 36)

Todo método, classe ou função persistido em arquivos de produção deve conter sua implementação real completa, livre de esqueletos, stubs ou atalhos fáceis — **em toda e qualquer interação que realize mutação em código ou arquitetura, sem distinção de escopo ou complexidade**. O código deve satisfazer o padrão dos Titãs por meio de contraste cirúrgico:

### [EXEMPLAR CONTRASTIVO 1: SERVIÇO DE DOMÍNIO & TRATAMENTO DE ERROS]

#### ❌ WRONG (Anti-Pattern: Menor Denominador Comum da Web):
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

##### 🔬 Autópsia de Falha Post-Mortem:
1. **Vulnerabilidade Crítica de SQL Injection:** Concatenação direta de strings sem parametrização ou sanitização tipada.
2. **Degradação de Tipos e Nil Deception:** Retornar `null` em caso de erro faz o chamador assumir que o usuário não existe quando, na verdade, o banco pode ter falhado por timeout ou crash de rede.
3. **Engolimento Silencioso de Exceções:** `console.error` seguido de `return null` destrói o rastro de depuração e mascara a indisponibilidade de infraestrutura.
4. **Acoplamento Global Indireto:** Acesso direto a uma variável global `db` em vez de receber uma porta abstrata (`UserRepository`) por injeção de dependência.
5. **Stub Oculto:** O comentário `// TODO: implementar cache redis` posterga responsabilidades essenciais de desempenho.

---

#### ✅ CORRECT (Padrão Titã: Hardened Clean Architecture & Result<T, E>):
```typescript
import { Result, Ok, Err } from '../result';
import { User, UserId } from '../entities/User';
import { UserRepository } from '../ports/UserRepository';

export type GetUserError =
  | { code: 'INVALID_ID_FORMAT'; message: string }
  | { code: 'USER_NOT_FOUND'; userId: string }
  | { code: 'STORAGE_UNAVAILABLE'; cause: Error };

export class UserService {
  constructor(private readonly repository: UserRepository) {}

  async getUser(rawId: string): Promise<Result<User, GetUserError>> {
    const idValidation = UserId.create(rawId);
    if (!idValidation.success) {
      return Err({
        code: 'INVALID_ID_FORMAT',
        message: idValidation.error.message,
      });
    }

    try {
      const user = await this.repository.findById(idValidation.value);
      if (!user) {
        return Err({
          code: 'USER_NOT_FOUND',
          userId: rawId,
        });
      }
      return Ok(user);
    } catch (error) {
      return Err({
        code: 'STORAGE_UNAVAILABLE',
        cause: error instanceof Error ? error : new Error(String(error)),
      });
    }
  }
}
```

---

### [EXEMPLAR CONTRASTIVO 2: PERSISTÊNCIA ATÔMICA VS. CORRUPÇÃO DE ARQUIVO]

#### ❌ WRONG (Anti-Pattern: Escrita Direta Não-Atômica):
```typescript
import fs from 'fs';

export function saveSettings(filePath: string, data: object): void {
  // Escrita ingênua direta: se a energia cair ou o processo for morto aqui,
  // o arquivo fica vazio ou corrompido com meio payload gravado.
  fs.writeFileSync(filePath, JSON.stringify(data, null, 2), 'utf-8');
}
```

##### 🔬 Autópsia de Falha Post-Mortem:
1. **Corrupção Imediata por Truncamento:** `writeFileSync` trunca o arquivo antes de começar a gravar os novos bytes. Qualquer interrupção resulta em perda total dos dados.
2. **Race Conditions Não Gerenciadas:** Leitores concorrentes leem payloads parciais e inválidos durante a janela de gravação.

---

#### ✅ CORRECT (Padrão Titã: Atomic Swap com Transacionalidade POSIX):
```typescript
import fs from 'fs';
import path from 'path';
import crypto from 'crypto';

export function saveSettingsAtomic(targetPath: string, data: unknown): void {
  const serialized = JSON.stringify(data, null, 2);
  const tempPath = `${targetPath}.${crypto.randomBytes(6).toString('hex')}.tmp`;
  const dir = path.dirname(targetPath);

  if (!fs.existsSync(dir)) {
    fs.mkdirSync(dir, { recursive: true });
  }

  // 1. Gravação integral no arquivo temporário isolado
  const fd = fs.openSync(tempPath, 'w');
  try {
    fs.writeFileSync(fd, serialized, 'utf-8');
    fs.fsyncSync(fd); // Força a liberação física dos buffers da controladora
  } finally {
    fs.closeSync(fd);
  }

  // 2. Troca atômica garantida pelo sistema operacional (invariante POSIX/Win32)
  fs.renameSync(tempPath, targetPath);
}
```

---

## 7. Orquestração e Codificação Concorrente por Subagentes Motores 1:1 (Node-by-Node Subagent Craft & Motor Mandate)

Na fase de escrita de código (Época III), **subagentes especializados DEVEM ser despachados como artífices motores para codificar e mutacionar diretamente os arquivos físicos no disco**:

1. **Veto ao Resumo Reducionista & Handoff de Alta Fidelidade:** Resumir nós ou laudos periciais em texto raso dilui micro-decisões, fórmulas e tratamentos de borda. Subagentes codificadores recebem o laudo bruto (`[INVESTIGATION_REPORT_PATH]`) ou o nó designado em `.planning/nodes/` e devem lê-lo na íntegra via `view_file` como sua primeira ação motora.
2. **Contratos Compartilhados & Synaptic Mutex:** Contratos estruturais (`src/core/ports/`, `src/core/types/`) são despachados na Onda base sob `CONTRACT_HOLD` no `synaptic_bus.json`. Os subagentes motores gravam diretamente os arquivos de contrato e validam a compilação. Somente após a liberação determinística `CONTRACT_STABLE (GO)`, os adaptadores consumidores são despachados na onda seguinte.
3. **Despacho Concorrente Atômico 1:1 com Mandato do Artífice Motor (`TypeName: "self"`, `[ACTION_MODE: PHYSICAL_MUTATION]`):**
   - Cada subagente motor recebe a responsabilidade atômica 1:1 de implementar e mutacionar fisicamente no disco exatamente UM arquivo ou nó designado (ex: Subagente 1 grava a Entidade do Domínio via `write_to_file`/`replace_file_content`; Subagente 2 grava o Storage Adapter).
   - É terminantemente proibido ao subagente devolver blocos de código em markdown no `send_message`. O subagente DEVE executar a mutação física chamando diretamente as ferramentas de escrita em sua própria sessão.
   - Todo código é 100% operacional, isomórfico e zero-stub (proibido `pass`, `// TODO`, `return null`, `{}`).
4. **Validação e Arbitragem pelo Chief Architect (Veto ao Parent Digitador):**
   - O Agente Principal atua exclusivamente como árbitro, orquestrador e validador fiduciário: verifica a consistência cruzada, valida a compilação (`npx tsc --noEmit`) e executa a suíte de testes.
   - É expressamente proibido ao Agente Principal digitar, copiar ou aplicar código pelos subagentes (`[HARD REJECT: ADVISORY_CODE_DUMP]`). Toda mutação física é de responsabilidade estrita dos subagentes motores 1:1.
   - Preparação do repositório para a submissão obrigatória ao **Subagente Juiz Independente na Época IV** (que conduzirá a inspeção visual e diagnósticos via `browser-mcp`).

---

## 8. Checklist Forense de Concorrência & Clean Architecture v5.0 (Binário — Lei 41)

> Auditado item a item pelo Red Team Juiz na Época IV. Um único item marcado como aprovado sem evidência física no disco dispara `[HARD REJECT: FRAUDULENT_CHECKLIST_SIGNOFF]`.

- [ ] **Result<T,E> / Option<T> Zero-Allocation:** zero `any`, casts inseguros ou `throw` sem captura; `assertNever` para exaustividade em compilação; zero exceções não tipadas.
- [ ] **Zero-Stub Permanente:** zero `TODO`, `pass`, `return null`, `{}` vazio, `...`, mocks de produção.
- [ ] **DeterministicAtomicSwap:** toda escrita crítica em disco utiliza substituição atômica com dupla atestação SHA-256 (pré e pós swap), `fsyncSync` físico compulsório e garantia de mesmo volume (`EXDEV` prevenido).
- [ ] **FsLockEngine (O_CREAT | O_EXCL):** concorrência de filesystem mediada por locks com flag `'wx'`, cabeçalho `LockMetadata`, verificação de liveness de PID (`process.kill(pid, 0)`) e purga determinística de stale locks.
- [ ] **Portas Desacopladas:** interfaces em `src/core/ports/`; implementações em `src/adapters/`; zero import cruzado entre camadas.
- [ ] **Concorrência Determinística & Full Jitter:** zero loops `sleep` cegos; backoff exponencial decorrelacionado com jitter para mitigar o *Thundering Herd Problem*.
- [ ] **Cobertura de Tipos Discriminados:** uniões discriminadas literais para todos os estados de sucesso e erro do domínio.
- [ ] **Zero Vazamento de Domínio:** termos de governança interna do agente ("Época", "Zero-Stub", "Gauntlet") não aparecem em interfaces de usuário, logs de produção ou APIs externas.
- [ ] **Telemetria Zero Erros:** build limpo (`$LASTEXITCODE === 0`); zero erros/warnings no console do navegador (`browser_console_logs`).
- [ ] **Mandato do Artífice Motor Cumprido:** arquivos gravados diretamente no disco pelos subagentes motores 1:1 via ferramentas de escrita (`replace_file_content` / `write_to_file`); zero código em markdown devolvido via `send_message`; zero digitação manual pelo Agente Principal.
