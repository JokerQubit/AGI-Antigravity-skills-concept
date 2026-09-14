---
name: browser_visual_reasoning
description: "v4.0 — Universal Cognitive Parity — Inspeção Perceptual Adversarial no Chrome Real. Manual técnico de inspeção perceptual obrigatória via browser-mcp (Agent360). Governa a captura de telas, diagnóstico de console, verificação do Padrão dos Titãs e o ciclo de retroalimentação fractal executado pelo Subagente Juiz Independente na Época IV — acionado compulsoriamente a cada interação operacional sem distinção de escopo."
---

# Browser Visual Reasoning & Perceptual Critique Playbook (v4.0 — Universal Cognitive Parity — Inspeção Perceptual Adversarial no Chrome Real)

Manual prático de validação visual e raciocínio em tempo de execução via navegador real do usuário, utilizando a infraestrutura do **Browser MCP** ([Agent360](https://github.com/agent360dk/browser-mcp)). Estabelece o portão mecânico inviolável: **a homologação só ocorre se o Subagente Juiz Independente na Época IV inspecionar a aplicação no Chrome real, diagnosticar zero erros/warnings no console, confirmar o Padrão dos Titãs e aprovar o padrão estético de classe mundial.**

> **v4.0.0 — Universal Cognitive Parity:** Na v4.0.0, a inspeção perceptual no Chrome real via browser-mcp é acionada compulsoriamente pela Época IV a cada interação operacional — sem distinção entre "pequeno componente" e "plataforma completa". Não existe entrega que dispense a Passada 4 do Gauntlet com telemetria de zero erros no console.

---

## 1. Arquitetura do Browser MCP no Antigravity

O **Browser MCP** opera em duas metades conectadas localmente:
1. **Extensão do Chrome:** Localizada em `~/.browser-mcp/extension` (ou Chrome Web Store), com controle da sessão real do usuário (cookies, autenticação, abas e renderização nativa de GPU).
2. **Servidor MCP Local (`mcp_config.json`):** Executado via `npx -y @agent360/browser-mcp@latest`, expondo ferramentas de automação, diagnóstico e inspeção visual ao agente.

### Inicialização e Verificação de Conexão:
- O servidor MCP é inicializado automaticamente pelo Antigravity através de `mcp_config.json`.
- Para confirmar a conectividade, o subagente auditor solicita screenshot da aba ativa no Chrome (`browser_screenshot`).

---

## 2. A Lei da Verificação Visual Obrigatória pelo Subagente Juiz (The Perceptual Gate)

- **Veto Absoluto à Entrega Cega e à Auto-Aprovação:** É terminantemente proibido concluir uma tarefa ou declarar código homologado sem que o Subagente Juiz Independente tenha aberto e examinado visualmente a aplicação renderizada no navegador real na Época IV.
- **Mandato de Contexto Limpo (v4.0 — Invariante Absoluto):** O subagente Red Team Juiz DEVE obrigatoriamente operar em contexto limpo, sem qualquer apego ao código gerado pelo Agente Principal. Ele não conhece intenções do autor, não absorve boas intenções e não concede crédito por esforço — somente pelo resultado verificável no Chrome real. Qualquer desvio deste mandato invalida o veredito.
- **Trindade de Ferramentas Obrigatórias (Zero Exceções):** Em toda auditoria de Época IV, o subagente juiz DEVE invocar as três ferramentas a seguir sem exceção:
  1. `browser_navigate` — Navegar explicitamente até a URL da aplicação em execução.
  2. `browser_screenshot` — Capturar evidência visual em repouso, durante interação e em estados dinâmicos.
  3. `browser_console_logs` — Extrair telemetria completa de console para confirmar zero erros, zero warnings críticos e zero 404s.
- **Procedimento de Validação em Tempo de Execução:**
  1. Subir o servidor de desenvolvimento local da aplicação (ex: `npm run dev`, `python -m http.server`, `vite`).
  2. Navegar no Chrome para a URL local (`http://localhost:3000`, `http://localhost:5173`, etc.) via `browser_navigate`.
  3. Capturar screenshots de alta resolução da página em repouso, durante rolagem e em estados interativos (modais, menus, gavetas).
  4. Extrair os logs de console da aba (`browser_console_logs`) para confirmar **zero erros de JavaScript, zero warnings de hidratação e zero requisições 404 de mídia**.
  5. Inspecionar a fluidez cinemática e ausência de travamentos.


---

## 3. Matriz de Avaliação Perceptual Adversarial (O Padrão dos Titãs)

Ao examinar as capturas e os logs, o subagente juiz aplica os seguintes critérios inegociáveis:

| Dimensão Perceptual | Pergunta de Avaliação Crítica | Tolerância / Veredito |
|---|---|---|
| **Cinemática dos Titãs (Linear/Apple/Stripe)** | As micro-interações, gavetas e modais utilizam física dinâmica de molas de 2ª ordem (`framer-motion`) ou recorrem ao menor denominador comum (`transition-all duration-300` / CSS rígido)? | Zero tolerância a CSS medíocre (`NON_ACCEPTANCE_AMATEUR_CSS_TRANSITION`). |
| **Direção de Fotografia & Mídia** | As imagens parecem fotografia analógica autêntica (Hasselblad/Leica) ou há SVGs genéricos, emojis, caixas vazias ou glifos/caracteres especiais (`↗`, `→`, `✹`, `·`, `—`, `❚❚`, `▶`) usados como ícones? | Zero tolerância a SVGs, emojis ou glifos como ícones (`NON_ACCEPTANCE_UNICODE_GLYPH_ICON_FRAUD`). |
| **Integridade de Vídeo** | Vídeos em loop reproduzem suavemente com poster estático local (zero telas pretas)? | Zero tolerância a vídeo quebrado ou animação sintética de imagem por script. |
| **Hierarquia Tipográfica & Profundidade** | A tipografia monumental, os contrastes e o respiro espacial transmitem padrão Awwwards Site of the Day / Red Dot? | Rejeição imediata se parecer dashboard cinza estéril. |
| **Arquitetura Perceptual Sênior** | A interface expressa maturidade e dignidade com respiro generoso, ou parece um template amador de IA com caixas repetitivas e brinquedos simulados? | Zero tolerância a clichês amadores de UI Kits (`NON_ACCEPTANCE_AMATEUR_UI_TRAP`). |
| **Acústica Tátil** | Interações de clique e transição disparam micro-áudio físico real (Foley/YouTube) ou há bipes sintéticos de script? | Rejeição se houver som senoidal robótico. |
| **Realidade Corporativa Institucional** | O site/sistema parece construído para uma empresa multinacional real de mercado ou para uma "demo fictícia infantil"? | Veto absoluto a "Lorem Ipsum" ou "Empresa Fake". |
| **Console & Rede** | Há alguma exceção não tratada, warning de chave do React, erro de CORS ou recurso 404? | Zero erros no console. |

---

## 4. O Ciclo de Retroalimentação Fractal para Perfeccionismo Absoluto

Se a inspeção visual e o diagnóstico de console revelarem **qualquer falha, mediocridade visual, quebra de layout ou falta de fluidez**:

```text
[Inspeção Visual no Navegador Real pelo Subagente Juiz via browser-mcp]
                               │
                               ▼
              ┌─────────────────────────────────┐
              │ O entregável atinge o padrão    │
              │ dos Titãs AAA sem falhas?       │
              └──────────────┬──────────────────┘
                             │
                  ┌──────────┴──────────┐
                  ▼                     ▼
               [ SIM ]               [ NÃO ]
                  │                     │
                  ▼                     ▼
       ┌─────────────────────┐ ┌──────────────────────────────────────────────┐
       │ Homologação Final:  │ │ DISPARO DE RETROALIMENTAÇÃO FRACTAL:         │
       │ Emissão de Sign-Off │ │ 1. Emissão de [HARD REJECT: RESTART CYCLE]   │
       │ da Época IV com     │ │ 2. Reabertura compulsória da ÉPOCA I         │
       │ screenshots reais.  │ │ 3. Geração de novos nós atômicos (N >= 100)  │
       └─────────────────────┘ │    dissecando os modos de falha              │
                               │ 4. Síntese de novo plano na ÉPOCA II         │
                               │ 5. Reconstrução física direta na ÉPOCA III   │
                               │ 6. Nova auditoria independente na ÉPOCA IV   │
                               └──────────────────────────────────────────────┘
```

- **Invariante da Auto-Evolução:** O sistema nunca se contenta com uma primeira versão mediana. O ciclo de retroalimentação força o refinamento recursivo até o ápice do design e da engenharia mundial.

---

## 5. Checklist Forense de Inspeção Perceptual (Binário — Lei 41)

> Executado pelo subagente Red Team Juiz na Época IV. Um único item reprovado dispara `[HARD REJECT]`.

- [ ] **Zero Erros no Console:** `browser_console_logs` retorna zero entradas de nível `error`.
- [ ] **Zero Warnings Críticos:** zero `warning` de hidratação SSR, memory leak, CORS ou deprecation grave.
- [ ] **Zero Assets 404:** zero requisições HTTP com status 404 na aba Network do DevTools.
- [ ] **60fps Verificado:** gravação do DevTools Performance mostra zero dropped frames por mais de 100ms contínuos.
- [ ] **Layout Sem Shift (CLS = 0):** zero Cumulative Layout Shift; elementos não saltam após carregamento inicial.
- [ ] **Contraste WCAG AA:** contrastes de texto verificados visualmente no screenshot; mínimo 4.5:1 para texto normal.
- [ ] **Fotografia Real Renderizada:** screenshots confirmam imagens fotográficas editoriais reais — zero placeholder, SVG genérico ou fundo sólido vazio.
- [ ] **Animações Fluidas:** screenshot ou recording confirma transições sem frame-drop visível; zero `transition-all duration-300` detectado via DevTools Animations.
- [ ] **Física de Molas Confirmada:** inspeção visual confirma comportamento de spring (overshoot natural) em componentes interativos — não movimento linear duro.

