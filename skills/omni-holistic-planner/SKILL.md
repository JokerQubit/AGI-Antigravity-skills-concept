---
name: omni-holistic-planner
description: MANDATORY. Master AGI/ASI Autonomous Planning & Latent Context Expansion Engine (X -> X ∪ Y). Intercepts any project or feature request, expands unsaid context across 10 enterprise dimensions (Branding, Architecture, Security, Legal, Logistics, Multi-State UX, Competitor Benchmarking, Real Assets, SEO, and Empirical Verification), and generates a zero-laziness production blueprint before execution.
---

# 🌐 OMNI-HOLISTIC PLANNER: Autonomous Latent Expansion ($X \to X \cup Y$)

> 🔴 **DOGMA CENTRAL:** Proibido planejar ou executar sistemas simplificados, hardcoded, com mocks estáticos ou escopo raso.
> Quando o usuário solicita uma semente $X$, o motor AGI/ASI DEVE expandir $X$ para a totalidade do universo latente $Y$ ($X \to X \cup Y$), cobrindo todos os pilares que não foram explicitamente mencionados e comparando o sistema contra o estado-da-arte mundial absoluto.

---

## 1. O Princípio da Expansão Latente ($X \to X \cup Y$)

O modelo tradicional falha porque sofre de **mínimo esforço probabilístico** (responde apenas ao texto superficial $X$). O **Omni-Holistic Planner** obriga o agente a projetar a arquitetura completa de uma corporação real de ponta através de 10 Dimensões Universais:

```
                  ┌──────────────────────────────────────────────┐
                  │          SEMENTE DO USUÁRIO (X)              │
                  │   "Faça um site de venda de celulares"       │
                  └──────────────────────┬───────────────────────┘
                                         │
                 ▼▼▼ EXPANSÃO LATENTE OMNI (X ∪ Y) ▼▼▼
  ┌────────────────────────┬────────────────────────┬────────────────────────┐
  │ 1. Branding & Ident.   │ 2. Benchmarking Apple  │ 3. Full-Stack Data     │
  │    (Logo, Design Token)│    (Awwwards/Pinterest)│    (Postgres/Redis/WS) │
  ├────────────────────────┼────────────────────────┼────────────────────────┤
  │ 4. Cyber Defense       │ 5. Supply Chain / Log. │ 6. Multi-State UX      │
  │    (OWASP, Anti-Fraud) │    (Correios, Tracking)│    (Client & Admin ERP)│
  ├────────────────────────┼────────────────────────┼────────────────────────┤
  │ 7. Legal & Fiscal      │ 8. Marketing & SEO     │ 9. Real Local Assets   │
  │    (LGPD/GDPR, NFe)    │    (OpenGraph, Funnel) │    (Nano Banana Engine)│
  ├────────────────────────┴────────────────────────┴────────────────────────┤
  │ 10. Empirical Evidence Gate & Invariance Testing ($Q \ge 9.0/10$)        │
  └──────────────────────────────────────────────────────────────────────────┘
```

---

## 2. A Matriz dos 10 Pilares de Planejamento Holístico

Antes de escrever qualquer linha de código ou layout, o agente DEVE documentar no artifact `implementation_plan.md` todos os 10 setores com profundidade de produção:

### 🏛️ Pilar 1: Identidade Corporativa, Branding & Design System
- **Identidade Visual:** Nome de marca de alto impacto, logotipo minimalista de vetor/PNG gerado via `generate_image` (fundo transparente, paleta HSL balanceada).
- **Design Tokens:** Tipografia monumental (Google Fonts), escalas de espaçamento (4px/8px grid), tokens semânticos (`--bg-primary`, `--surface-elevated`, `--accent-subtle`), glassmorphism e micro-interações sem clichês.

### 🏆 Pilar 2: State-of-the-Art Benchmarking (Referência Global)
- **Comparativo de Mercado:** Benchmark contra líderes de classe mundial (ex: Apple para design de produto e transições fluidas, Stripe para checkout e DX, Linear para densidade de dados e fluidez de navegação).
- **Inspiração Conceitual:** Análise de referências de UI/UX (Awwwards, Pinterest, Mobbin, Behance) documentando o padrão estético esperado.

### 🛡️ Pilar 3: Segurança Ofensiva, Defesa Cibernética & Resiliência
- **OWASP Top 10 Proteção Ativa:** Proteção contra SQLi via queries parametrizadas/ORMs tipados, XSS sanitization (DOMPurify), CSP (Content Security Policy) estrito, CSRF tokens e CORS restritivo.
- **Autenticação & Autorização:** RBAC (Role-Based Access Control) granular (Cliente, Vendedor, Gerente, SuperAdmin), JWT seguro em cookies HTTP-only `SameSite=Strict` e Rate Limiting por IP/Token.
- **Prevenção de Fraude & Bots:** Validação de payload no servidor, idempotência em requisições de pagamento (`Idempotency-Key`), auditoria de logs criptográficos.

### ⚡ Pilar 4: Arquitetura Full-Stack, Schemas & Zero-Mock Data
- **Banco de Dados Real & Relacional/NoSQL:** Esquema normalizado (PostgreSQL / SQLite com Drizzle/Prisma/Kysely), migrations automatizadas e índices para queries de alta performance.
- **Proibição de Dados Falsos Estáticos:** Proibido `const PRODUCTS = [...]` estático para fingir funcionalidade. Implementar geradores dinâmicos com validade estatística ou consumir APIs reais / endpoints REST / WebSockets.
- **Cache & Concorrência:** Estratégia de cache (Redis / In-memory LRU) com invalidação atômica e locks otimistas para evitar concorrência em estoque.

### 🚚 Pilar 5: Logística, Supply Chain & Operações
- **Modelo Operacional:** Definição clara do modelo de distribuição (Estoque Próprio, Fulfillment, Cross-Docking ou Dropshipping integrado com APIs de fornecedores).
- **Cálculo de Frete & Rastreamento:** Integração com APIs de frete (Correios, Melhor Envio, FedEx, DHL), cálculo volumétrico dinâmico, prazos por CEP e Webhooks para atualização de status de entrega.
- **Gestão de Inventário:** Bloqueio temporário de estoque durante o checkout (TTL de reserva de 15 minutos), alertas de estoque baixo e logística reversa de trocas/devoluções.

### 👥 Pilar 6: Experiência Multi-Público (Client Journey & Admin ERP/CRM)
- **Jornada do Cliente (B2C):** Catálogo com filtros facetados avançados (preço, marca, RAM, armazenamento, cor), busca instantânea full-text com debounce, comparador lado a lado de produtos, carrinho reativo, cálculo dinâmico de parcelamento com juros e checkout transparente em 3 passos.
- **Painel Administrativo (ERP/CRM):** Dashboard gerencial com telemetria em tempo real (faturamento, ticket médio, taxa de conversão, curva ABC de produtos), controle de estoque com CRUD dinâmico, gestão de pedidos com atualização de status, e CRM para SAC e suporte ao cliente.

### 📜 Pilar 7: Compliance Legal, Fiscal & Termos de Uso
- **Privacidade & Proteção de Dados:** Termos de Uso e Política de Privacidade estritos em conformidade com LGPD (Lei Geral de Proteção de Dados) e GDPR, gestão de consentimento de cookies e endpoint para exclusão de dados do titular.
- **Emissão Fiscal & Tributação:** Arquitetura para emissão de Nota Fiscal Eletrônica (NFe), cálculo de impostos (ICMS, DIFAL, PIS, COFINS) e armazenamento seguro de XMLs fiscais.
- **Direito do Consumidor:** Termos de garantia (garantia legal de 90 dias + garantia contratual de 12 meses), política de arrependimento (7 dias) e regras de estorno.

### 📈 Pilar 8: Engenharia de Marketing, SEO & Telemetria
- **SEO Semântico Avançado:** Estrutura HTML5 com Schema.org JSON-LD (`Product`, `Offer`, `AggregateRating`, `Organization`), OpenGraph dinâmico para redes sociais e sitemap.xml automatizado.
- **Performance & Core Web Vitals:** Otimização para LCP < 1.2s, FID/INP < 50ms, CLS = 0, lazy-loading nativo de imagens e compressão WebP/AVIF.
- **Telemetria de Eventos:** Pipeline de eventos de produto (Visualização de Item, Adição ao Carrinho, Início de Checkout, Conversão) para analytics e remarketing.

### 🎨 Pilar 9: Ativos Multimodais Autênticos & Locais
- **Ativos Visuais 2D:** Todos os banners, produtos, logos e ícones customizados DEVEM ser gerados localmente via `generate_image` (Nano Banana Engine) ou incorporados com links relativos locais. Proibido Unsplash/Placeholders externos.
- **Texturas PBR & Modelos 3D:** Se houver visualização 3D de produto (ex: visualizador 360° do celular em Three.js/WebGL), utilizar malhas e shaders de alta fidelidade com reflexo realista de vidro e metal.

### 🔬 Pilar 10: Popperian Verification, Invariância & Evidence Gate
- **Verificação Automatizada:** Testes unitários de lógica de negócio, testes de integração de API e validação de invariantes numéricas (ex: total do pedido == soma dos itens + frete - descontos).
- **Inspeção Visual Multi-Estado:** Validação em tela cheia Full HD (1920x1080) com inspeção dos PNGs gerados via `view_file` e correção de no mínimo 3 críticas visuais.
- **Nota de Qualidade $Q \ge 9.0/10$:** Proibido finalizar sem conformidade total com o `one-shot-ultra-loop-engine`.

---

## 3. Protocolo de Execução do Omni-Holistic Planner

Ao receber qualquer tarefa que envolva criação, concepção ou planejamento de sistema:

1. **Ativar o Motor de Expansão:** Imediatamente decomponha o pedido em um `implementation_plan.md` contendo as 10 Dimensões.
2. **Benchmark Ativo:** Pesquise na web referências de design, engenharia e segurança dos líderes globais do setor.
3. **Gerar Ativos de Suporte:** Dispare a geração de logos e imagens locais para alimentar a interface desde o primeiro frame.
4. **Validar Sem Atalhos:** Construa o sistema completo, sem linhas omitidas (`// TODO`), sem mocks estáticos e com testes passando.
