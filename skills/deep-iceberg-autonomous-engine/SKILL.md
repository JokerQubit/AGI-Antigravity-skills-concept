---
name: deep-iceberg-autonomous-engine
description: MANDATORY. Master AGI/ASI Deep Iceberg Engine (100% Depth Mandate). Prohibits stopping at the 5% surface level (naive UI, happy-path, static mocks). Enforces the 7 Deep Layers of production engineering (Causal DAG, Chaos/Idempotency, Tactile Sonification, Zero-Latency Optimistic UI, Telemetric Observability HUD, Immutability/Event Sourcing, and Self-Healing Offline-First Resilience).
---

# 🧊 DEEP ICEBERG AUTONOMOUS ENGINE: The 100% Depth Mandate

> 🔴 **DOGMA CENTRAL:** É terminantemente proibido parar nos 5% do topo do iceberg (gerar apenas HTML/CSS básico, telas estáticas ou código que só funciona no "caminho feliz").
> O agente DEVE penetrar até a base profunda de 100% da arquitetura, implementando as 7 Camadas Ocultas de Engenharia de Missão Crítica.

---

## 1. A Topologia das 7 Camadas Profundas do Iceberg

```
════════════════════════════════════════════════════════════════════════════════════
                        AS 7 CAMADAS DE PROFUNDIDADE AGI/ASI
════════════════════════════════════════════════════════════════════════════════════
├── 🧠 L1: GRAFO CAUSAL & EFEITOS DE 2ª E 3ª ORDEM (Dependency DAG)
├── 💥 L2: ENGENHARIA DO CAOS, IDEMPOTÊNCIA & CIRCUIT BREAKERS (Antifragility)
├── 🌊 L3: MICRO-FÍSICA TÁTIL, MOLA REAL & SONIFICAÇÃO HÁPTICA (WebAudio)
├── ⚡ L4: PREFETCHING PREDITIVO DE INTENÇÃO & LATÊNCIA ZERO (0ms Optimistic UI)
├── 📊 L5: OBSERVABILIDADE OPERACIONAL & TELEMETRIA DE NEGÓCIO AO VIVO (HUD)
├── 🧬 L6: SCHEMAS COM AUDITORIA IMUTÁVEL & SOFT-DELETES (Event Sourcing)
└── 🛡️ L7: SISTEMAS AUTO-REGENERATIVOS OFFLINE-FIRST (Self-Healing & Sync)
════════════════════════════════════════════════════════════════════════════════════
```

---

## 2. As 7 Camadas Ocultas Obrigatórias

### 🧠 Camada 1: Grafo Causal e Consequências de 2ª e 3ª Ordem (DAG)
- **Proibição:** Tratar recursos como ilhas isoladas.
- **Mandato:** Mapear o Grafo de Dependências Acíclico (DAG) completo. Se o usuário executa uma mutação $A$, o sistema deve disparar as reações em cascata:
  - *Ordem 1:* Atualização de estado local imediata.
  - *Ordem 2:* Recálculo de frete volumétrico, alíquotas fiscais (DIFAL/ICMS), cupons e descontos progressivos.
  - *Ordem 3:* Sincronização de broadcast via WebSockets e bloqueio de concorrência no inventário.

### 💥 Camada 2: Engenharia do Caos, Idempotência e Circuit Breakers
- **Proibição:** Programar apenas o "Caminho Feliz" (*Happy Path*).
- **Mandato:** Blindagem antifrágil contra falhas do mundo real:
  - **Idempotência Estrita:** Todo envio de formulário financeiro, pedido ou transação DEVE carregar um cabeçalho/token de idempotência (`Idempotency-Key` com UUID v4) para evitar cobrança dupla em cliques repetidos ou reenvios.
  - **Circuit Breakers & Fallbacks:** Se qualquer API externa ou microsserviço falhar ou demorar mais de 3000ms, o sistema chaveia automaticamente para um provedor secundário ou ativa um modo degradado gracioso sem travar a interface.
  - **Locks Otimistas:** Transações de estoque ou agendamento usam versionamento (`version_id` / CAS - Compare-And-Swap) para eliminar race conditions em compras simultâneas.

### 🌊 Camada 3: Micro-Física Tátil e Sonificação Sensorial (WebAudio)
- **Proibição:** Componentes rígidos, estáticos, sem inércia física ou som.
- **Mandato:** Transformação da interface em um objeto físico vivo:
  - **Física de Molas (*Spring Dynamics*):** Modais, cards e transições utilizam curvas de aceleração física baseadas em molas ($f = -kx - cv$) com amortecimento suave.
  - **Iluminação Especular Dinâmica:** Superfícies e botões com gradientes de borda (*rim light*) que recalculam vetores de luz conforme a posição $(X, Y)$ do cursor do usuário.
  - **Síntese Háptica WebAudio:** Micro-feedback sonoro sintetizado em tempo real via WebAudio API (ondas senoidais com decaimento exponencial orgânico de 20ms a 60ms) para confirmação de ações de alto valor (adicionar ao carrinho, alternar filtros, compra aprovada).

### ⚡ Camada 4: Prefetching Preditivo e Latência Zero (0ms Optimistic UI)
- **Proibição:** Telas de espera (*loaders*) desnecessárias a cada clique.
- **Mandato:** Antecipação ativa de intenção:
  - **Hover-Intent Preloading:** Quando o cursor do mouse se aproxima de um link, produto ou aba, os dados e imagens são pré-carregados na memória silenciosamente antes do clique ocorrer.
  - **UI Otimista (0ms):** Ações do usuário refletem instantaneamente na tela; a confirmação de rede ocorre em segundo plano. Em caso raro de erro, a interface executa um *rollback* visual suave com notificação explicativa.

### 📊 Camada 5: Observabilidade Operacional e Telemetria de Negócios (HUD)
- **Proibição:** Sistemas sem monitoramento analítico ou visibilidade de métricas.
- **Mandato:** Instrumentação de produção embutida:
  - **HUD de Telemetria:** Painel administrativo em tempo real exibindo métricas de saúde técnica (FPS, LCP, INP, CLS, taxa de erro HTTP 5xx) e métricas de negócio (conversão do funil, volume de transações, ticket médio).
  - **Breadcrumbs de Erro:** Captura estruturada de ações que antecederam qualquer exceção para diagnóstico imediato.

### 🧬 Camada 6: Trilha de Auditoria Imutável (Event Sourcing & Soft Deletes)
- **Proibição:** `DELETE FROM` direto ou mutação destrutiva de histórico.
- **Mandato:** Governança e integridade imutável:
  - **Soft Deletes:** Entidades recebem marcação temporal `deleted_at` com recuperação facilitada.
  - **Livro-Razão de Eventos (Event Ledger):** Todas as alterações de preços, status de pedidos e permissões são salvas em um log append-only com hash criptográfico, IP e timestamp ISO-8601.

### 🛡️ Camada 7: Sistemas Auto-Regenerativos e Offline-First
- **Proibição:** "Sem conexão com a internet" quebrando a usabilidade do app.
- **Mandato:** Resiliência contínua:
  - **Cache Local Reativo:** Armazenamento em IndexedDB / localStorage de catálogo e carrinho de compras.
  - **Fila de Sincronização em Background (Background Sync):** Requisições feitas sem internet são enfileiradas e despachadas automaticamente no momento exato em que o sinal de rede retornar.

---

## 3. Protocolo de Integração nos Ciclos de Construção

Sempre que qualquer sistema, aplicação web, jogo, engine ou microsserviço for construído:
1. O agente DEVE verificar a presença ativa das 7 Camadas de Profundidade.
2. O Red Team (`adversarial-tribunal`) DEVE auditar especificamente se o sistema implementou as camadas L1 a L7 ou se tentou burlar com soluções de superfície.
3. Se qualquer uma das 7 camadas estiver ausente em um projeto não-trivial, o projeto é rejeitado antes da liberação final.
