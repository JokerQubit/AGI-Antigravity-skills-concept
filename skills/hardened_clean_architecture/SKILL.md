---
name: hardened_clean_architecture
version: 4.0.0
description: "v4.0 — Universal Cognitive Parity & Structured Neural Planning Mesh. Manual prático de engenharia de software defensiva, Clean Architecture desacoplada, tipagem estrita via uniões discriminadas Result/Option, Atomic Swap de persistência e erradicação definitiva de stubs. Ativado compulsoriamente em toda mutação de código ou arquitetura, sem distinção de escopo."
---

# Hardened Clean Architecture & Defensive Code Playbook — v4.0 (Universal Cognitive Parity & Structured Neural Planning Mesh)

Manual de implementação de engenharia de software em nível de produção sênior. Estabelece padrões determinísticos para segregação de camadas arquiteturais, manipulação tipada de erros sem exceções cegas, persistência atômica e eliminação absoluta de stubs e esqueletos no código.

> **Salvaguarda v4.0 — Ativação Compulsória Universal:**
> Na v4.0.0, as salvaguardas de Clean Architecture Defensiva desta skill são disparadas compulsoriamente a qualquer interação operacional que toque arquivos de código ou arquitetura — sem distinção de escopo ou complexidade. O conceito de "ajuste cirúrgico simples" que dispensa Result<T,E>, Atomic Swap ou testes está terminantemente extinto.

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

## 2. Tratamento Tipado de Erros com o Padrão Result<T, E>

O uso de `try/catch` genérico ou blocos vazios `catch (e) {}` é expressamente proibido. Todas as operações com possibilidade de falha devem retornar uma união discriminada tipada:

```typescript
// src/core/result.ts
export type Result<T, E = Error> =
  | { success: true; value: T; error?: never }
  | { success: false; error: E; value?: never };

export const Ok = <T>(value: T): Result<T, never> => ({
  success: true,
  value,
});

export const Err = <E>(error: E): Result<never, E> => ({
  success: false,
  error,
});

// Exemplo Prático de Uso no Domínio:
export interface OrderValidationError {
  code: 'INVALID_ITEM_COUNT' | 'MINIMUM_ORDER_UNMET' | 'NEGATIVE_PRICE';
  message: string;
}

export function validateOrderTotal(itemsCount: number, totalCents: number): Result<number, OrderValidationError> {
  if (itemsCount <= 0) {
    return Err({ code: 'INVALID_ITEM_COUNT', message: 'Pedido deve conter pelo menos 1 item.' });
  }
  if (totalCents < 1500) {
    return Err({ code: 'MINIMUM_ORDER_UNMET', message: 'Pedido mínimo é de R$ 15,00.' });
  }
  return Ok(totalCents);
}
```

---

## 3. Padrão de Gravação Atômica no Disco (Atomic Swap Pattern)

Para prevenir arquivos corrompidos ou incompletos caso o processo seja interrompido abruptamente, toda gravação de dados críticos deve utilizar o padrão de swap atômico:

### Implementação em TypeScript / Node.js:
```typescript
// src/adapters/storage/atomicWriter.ts
import { promises as fs } from 'fs';
import * as path from 'path';
import { randomBytes } from 'crypto';

export async function writeAtomicFile(targetPath: string, content: string | Buffer): Promise<void> {
  const dir = path.dirname(targetPath);
  await fs.mkdir(dir, { recursive: true });

  // 1. Gera nome de arquivo temporário único no mesmo diretório/volume
  const tempSuffix = randomBytes(4).toString('hex');
  const tempPath = `${targetPath}.tmp.${tempSuffix}`;

  try {
    // 2. Grava 100% dos dados no arquivo temporário
    await fs.writeFile(tempPath, content, { encoding: 'utf-8', mode: 0o644 });

    // 3. Força a troca atômica no sistema de arquivos
    await fs.rename(tempPath, targetPath);
  } catch (error) {
    // 4. Limpa o arquivo temporário em caso de falha
    try {
      await fs.unlink(tempPath);
    } catch {
      // Ignora erro de limpeza se o arquivo não tiver sido criado
    }
    throw error;
  }
}
```

---

## 4. Concorrência Assíncrona Determinística (Anti-Sleep Polling)

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

## 5. Implementação Completa Zero-Stub & Pedagogia Contrastiva (Lei 36)

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

## 6. Orquestração e Codificação Concorrente por Subagentes Motores 1:1 (Node-by-Node Subagent Craft & Motor Mandate)

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

## 7. Checklist Forense de Clean Architecture (Binário — Lei 41)

> Auditado item a item pelo Red Team Juiz na Época IV. Um único item marcado como aprovado sem evidência física no disco dispara `[HARD REJECT: FRAUDULENT_CHECKLIST_SIGNOFF]`.

- [ ] **Result<T,E> / Option<T>:** zero `any`, `unknown`, casts inseguros ou `throw` implícito sem captura.
- [ ] **Zero-Stub:** zero `TODO`, `pass`, `return null`, `{}` vazio, `...`, mocks de produção.
- [ ] **Atomic Swap:** toda escrita em disco usa swap atômico (escrever em arquivo temp → renomear atomicamente via `fs.renameSync`).
- [ ] **Portas Desacopladas:** interfaces em `src/core/ports/`; implementações em `src/adapters/`; zero import cruzado entre camadas.
- [ ] **Idempotência:** toda operação mutadora é idempotente; re-execução não produz estado inconsistente.
- [ ] **Cobertura de Tipos Discriminados:** unions discriminadas para todos os estados de erro/sucesso do domínio.
- [ ] **Zero Vazamento de Domínio:** termos de governança interna do agente ("Época", "Zero-Stub", "Gauntlet") não aparecem em interfaces de usuário, logs de produção ou APIs externas.
- [ ] **Telemetria Zero Erros:** build limpo (`$LASTEXITCODE === 0`); zero erros/warnings no console do navegador (`browser_console_logs`).
- [ ] **Mandato do Artífice Motor:** arquivos de portas, entidades e adaptadores gravados diretamente no disco pelos subagentes 1:1 via ferramentas de escrita; zero digitação manual pelo Agente Principal.
