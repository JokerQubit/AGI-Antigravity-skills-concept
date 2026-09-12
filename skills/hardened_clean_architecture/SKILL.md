---
name: hardened_clean_architecture
description: Manual prático de engenharia de software defensiva, Clean Architecture desacoplada, tipagem estrita via uniões discriminadas Result/Option, Atomic Swap de persistência e erradicação definitiva de stubs.
---

# Hardened Clean Architecture & Defensive Code Playbook

Manual de implementação de engenharia de software em nível de produção sênior. Estabelece padrões determinísticos para segregação de camadas arquiteturais, manipulação tipada de erros sem exceções cegas, persistência atômica e eliminação absoluta de stubs e esqueletos no código.

---

## 1. Topologia Limpa de Camadas Desacopladas

Toda aplicação com lógica de domínio complexa deve separar responsabilidades em três camadas fundamentais:

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

## 5. Implementação Completa Zero-Stub (Banimento de Esqueletos)

Todo método ou função persistido em arquivos de produção deve conter sua implementação real completa:

* **PROIBIDO:**
  ```typescript
  export class UserService {
    async getUser(id: string) {
      // TODO: implementar busca no banco
      return null;
    }
  }
  ```
* **OBRIGATÓRIO:**
  ```typescript
  export class UserService {
    constructor(private readonly repository: UserRepository) {}

    async getUser(id: string): Promise<Result<User, UserNotFoundError>> {
      if (!id || id.trim().length === 0) {
        return Err(new UserNotFoundError('ID de usuário inválido.'));
      }
      const user = await this.repository.findById(id);
      if (!user) {
        return Err(new UserNotFoundError(`Usuário com ID ${id} não localizado.`));
      }
      return Ok(user);
    }
  }
  ```

---

## 6. Orquestração e Codificação Concorrente por Subagentes por Nó (Node-by-Node Subagent Craft)

Na fase de escrita de código (Época III), **subagentes especializados DEVEM ser despachados para codificar os nós físicos no disco**:

1. **Veto ao Resumo Reducionista:** Resumir 100+ nós em um texto raso faz o agente esquecer 90% das micro-decisões, fórmulas, tokens e tratamentos de borda saturados na Época I. É expressamente proibido ao Agente Principal ignorar os nós e codificar tudo sozinho na thread principal.
2. **Contratos Compartilhados como Base Invariante:** Antes de despachar os subagentes de codificação, o Agente Principal (Chief Systems Architect) define e grava as tipagens e interfaces centrais em `src/core/ports/` e `src/core/types/` a partir das `exported_primitives` do `graph.json`. Isso elimina qualquer risco de divergência de imports ou contratos.
3. **Despacho Concorrente Atômico 1:1 de Subagentes por Nó (`invoke_subagent` com `TypeName: "self"`):**
   - Cada subagente recebe a responsabilidade atômica 1:1 de implementar o código referente a um nó específico designado (ex: Subagente 1 codifica a Entidade do Domínio a partir de `node_001_domain_entity.md`; Subagente 2 codifica o Storage Adapter a partir de `node_002_storage_adapter.md`). É proibido agrupar múltiplos nós sob um único subagente codificador.
   - Cada subagente lê diretamente o arquivo exato do nó designado em `.planning/nodes/`, implementando 100% da lógica detalhada sem atalhos ou stubs.
4. **Integração Física pelo Chief Architect:** O Agente Principal integra os módulos, valida a compilação cruzada (`npx tsc --noEmit`), tipos estritos e execução dos testes nativos, preparando o repositório para a submissão obrigatória ao **Subagente Juiz Independente na Época IV** (que conduzirá a inspeção visual e diagnósticos via `browser-mcp`).

