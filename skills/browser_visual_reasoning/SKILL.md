---
name: browser_visual_reasoning
description: Manual técnico de inspeção perceptual em navegador real via browser-mcp (Agent360). Governa a captura de telas, diagnóstico de console, verificação do Padrão dos Titãs e o ciclo de retroalimentação fractal executado pelo Subagente Juiz Independente na Época IV.
---

# Browser Visual Reasoning & Perceptual Critique Playbook (v3.0)

Manual prático de validação visual e raciocínio em tempo de execução via navegador real do usuário, utilizando a infraestrutura do **Browser MCP** ([Agent360](https://github.com/agent360dk/browser-mcp)). Estabelece o portão mecânico inviolável: **a homologação só ocorre se o Subagente Juiz Independente na Época IV inspecionar a aplicação no Chrome real, diagnosticar zero erros/warnings no console, confirmar o Padrão dos Titãs e aprovar o padrão estético de classe mundial.**

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
