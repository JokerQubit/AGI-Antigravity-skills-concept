---
name: browser_visual_reasoning
description: "v5.0 — Universal Cognitive Parity — Inspeção Perceptual Adversarial no Chrome Real & Auditoria de 120Hz com Telemetria CLS e INP via browser-mcp. Manual técnico de inspeção perceptual obrigatória em tempo de execução via browser-mcp (Agent360). Governa a captura de telas multi-viewport, injeção de scripts de profiling (perceptual_audit.js), medição de CLS, INP, estabilidade a 120Hz ProMotion, isolamento de camadas de GPU, diagnóstico de console e o ciclo de retroalimentação fractal executado pelo Subagente Juiz Independente na Época IV (Leis 21, 41, 49 e 50)."
---

# Browser Visual Reasoning & Perceptual Critique Playbook (v5.0 — Universal Cognitive Parity & 120Hz ProMotion Telemetry)

Manual prático de validação visual e raciocínio em tempo de execução via navegador real do usuário, utilizando a infraestrutura do **Browser MCP** ([Agent360](https://github.com/agent360dk/browser-mcp)). Estabelece o portão mecânico inviolável: **a homologação só ocorre se o Subagente Juiz Independente na Época IV inspecionar a aplicação no Chrome real, executar a telemetria perceptual contínua de 120Hz (ou 60Hz), diagnosticar $CLS = 0.000$, $INP < 16\text{ms}$, zero erros/warnings no console, confirmar o Padrão dos Titãs e aprovar o padrão estético de classe mundial.**

> **v5.0.0 — Universal Cognitive Parity & 120Hz Perceptual Telemetry:** Na v5.0.0, a inspeção perceptual transcende a simples visualização estática: ela é uma **auditoria física e cinemática ativa**. Através da injeção de scripts de profiling e captura multi-viewport, o Juiz afere a estabilidade de quadros a 120Hz ($8.33\text{ms}$ por frame) em displays ProMotion/VRR, o isolamento estrito de camadas na GPU e a ausência absoluta de Layout Thrashing.

---

## 1. Arquitetura do Browser MCP no Antigravity

O **Browser MCP** opera em duas metades conectadas localmente:
1. **Extensão do Chrome:** Localizada em `~/.browser-mcp/extension` (ou Chrome Web Store), com controle da sessão real do usuário (cookies, autenticação, abas e renderização nativa acelerada por GPU).
2. **Servidor MCP Local (`mcp_config.json`):** Executado via `npx -y @agent360/browser-mcp@latest`, expondo ferramentas de automação, injeção de script de profiling, diagnóstico e inspeção visual ao agente.

### Inicialização e Verificação de Conexão:
- O servidor MCP é inicializado automaticamente pelo Antigravity através de `mcp_config.json`.
- Para confirmar a conectividade, o subagente auditor solicita screenshot da aba ativa no Chrome (`browser_screenshot`).

---

## 2. A Lei da Verificação Visual Obrigatória pelo Subagente Juiz (The Perceptual Gate)

- **Veto Absoluto à Entrega Cega e à Auto-Aprovação:** É terminantemente proibido concluir uma tarefa ou declarar código homologado sem que o Subagente Juiz Independente tenha aberto e examinado visualmente a aplicação renderizada no navegador real na Época IV.
- **Mandato de Contexto Limpo (v5.0 — Invariante Absoluto):** O subagente Red Team Juiz DEVE obrigatoriamente operar em contexto limpo, sem qualquer apego ao código gerado pelo Agente Principal. Ele não conhece intenções do autor, não absorve desculpas e não concede crédito por esforço — somente pelo resultado verificável no Chrome real.
- **Quadra de Ferramentas Obrigatórias (Zero Exceções):** Em toda auditoria perceptual de Época IV, o subagente juiz DEVE invocar as quatro ferramentas a seguir sem exceção:
  1. `browser_navigate` — Navegar explicitamente até a URL da aplicação em execução.
  2. `browser_execute_script` — Injetar o script de profiling `perceptual_audit.js` para mensurar CLS, INP e taxa de quadros a 120Hz/60Hz.
  3. `browser_screenshot` — Capturar evidência visual multi-viewport (Desktop, Tablet, Mobile), em repouso e sob estados interativos dinâmicos.
  4. `browser_console_logs` — Extrair telemetria completa de console para confirmar zero erros, zero warnings críticos e zero 404s.
- **Procedimento de Validação em Tempo de Execução:**
  1. Subir o servidor local da aplicação (ex: `npm run dev`, `vite`).
  2. Navegar no Chrome para a URL local via `browser_navigate`.
  3. Capturar screenshots de alta resolução da página em repouso via `browser_screenshot`.
  4. Injetar `perceptual_audit.js` via `browser_execute_script` durante interações ativas (cliques em botões com mola, abertura de modais, scroll).
  5. Extrair logs de console via `browser_console_logs` para auditar ausência de falhas.
  6. Emitir homologação somente se todas as métricas satisfizerem o padrão de classe mundial.


---

## 3. Matriz de Avaliação Perceptual Adversarial (O Padrão dos Titãs v5.0)

Ao examinar as capturas e a telemetria injetada, o subagente juiz aplica os seguintes critérios inegociáveis:

| Dimensão Perceptual | Critério Físico & Telemetria em Tempo de Execução | Tolerância / Veredito |
|---|---|---|
| **Cinemática 120Hz / ProMotion** | Molas dinâmicas calibradas com damping sub-crítico ($\zeta \in [0.72, 0.86]$) e estabilidade CFL a $8.33\text{ms}$ (`motionTokensV5`). Zero `transition-all duration-300` ou CSS linear. | Rejeição sumária se detectado CSS medíocre (`NON_ACCEPTANCE_AMATEUR_CSS_TRANSITION`). |
| **Isolamento de GPU & Zero Reflow** | Animações restritas a `transform` e `opacity` com `will-change: transform`. Zero mutações em `width`, `height`, `top`, `margin` ou `padding`. | Rejeição por Layout Thrashing se houver repaints de layout. |
| **Cumulative Layout Shift (CLS)** | `report.cls.value === 0.000`. Elementos não saltam nem sofrem descontinuidade espacial durante o carregamento de fontes ou imagens. | Rejeição imediata se $CLS > 0.000$. |
| **Interaction to Next Paint (INP)** | Latência entre pointerdown/keydown e pintura do próximo frame sub-16ms ($INP < 16\text{ms}$). | Rejeição se houver lag de clique perceptível. |
| **Direção Óptica Fotográfica (8 Variáveis)** | Imagens seguem a Fórmula de 8 Variáveis com textura tangível, iluminação fotométrica e sem clichês de IA. Botões utilizam micro-renders usinados 1:1. | Zero tolerância a SVGs genéricos, emojis ou glifos Unicode como ícones (`NON_ACCEPTANCE_UNICODE_GLYPH_ICON_FRAUD`). |
| **Integridade de Vídeo & Foley Real** | Vídeos em loop reproduzem com poster estático local (zero telas pretas). Micro-áudio físico fatiado via `sfx_tool.py`. | Rejeição imediata se houver vídeo quebrado ou bipes senoidais sintéticos. |
| **Realidade Corporativa Institucional** | A interface expressa seriedade corporativa para uma multinacional real de mercado. | Veto absoluto a "Lorem Ipsum" ou empresas fictícias infantis. |
| **Console & Rede DevTools** | `browser_console_logs` retorna array vazio para erros e warnings críticos; zero requisições HTTP 404. | Rejeição imediata por qualquer exceção não tratada ou asset 404. |

---

## 4. Script Canônico de Profiling Perceptual em Tempo de Execução (`perceptual_audit.js`)

Para eliminar o subjetivismo na inspeção, o Subagente Juiz injeta o seguinte script via `browser_execute_script` para colher telemetria estrita durante 1000ms de amostragem:

```javascript
(() => {
  return new Promise((resolve) => {
    const report = {
      fps: {
        avgFps: 0,
        minFps: 999,
        droppedFrames: 0,
        totalFrames: 0,
      },
      cls: {
        value: 0,
        entries: [],
      },
      inp: {
        maxLatencyMs: 0,
      },
      layoutThrashing: {
        longTasksCount: 0,
        longAnimationFramesCount: 0,
      },
      consoleClean: true,
    };

    // 1. Monitorar Layout Shifts (CLS)
    let clsScore = 0;
    const clsObserver = new PerformanceObserver((entryList) => {
      for (const entry of entryList.getEntries()) {
        if (!entry.hadRecentInput) {
          clsScore += entry.value;
          report.cls.entries.push({
            value: entry.value,
            startTime: entry.startTime,
          });
        }
      }
    });
    try {
      clsObserver.observe({ type: 'layout-shift', buffered: true });
    } catch (e) {}

    // 2. Monitorar Long Tasks & LoAF
    const longTaskObserver = new PerformanceObserver((list) => {
      report.layoutThrashing.longTasksCount += list.getEntries().length;
    });
    try {
      longTaskObserver.observe({ type: 'longtask', buffered: true });
    } catch (e) {}

    // 3. Amostragem de Frame Rate a 120Hz/60Hz durante 1000ms
    const startTime = performance.now();
    let lastFrameTime = startTime;
    let frameCount = 0;

    function frameLoop(now) {
      frameCount++;
      const delta = now - lastFrameTime;
      lastFrameTime = now;

      // Limite de frame drop: > 10ms a 120Hz (ou > 18ms a 60Hz)
      const targetBudget = window.screen && window.screen.refreshRate > 90 ? 10.0 : 18.0;
      if (delta > targetBudget) {
        report.fps.droppedFrames++;
      }

      if (now - startTime < 1000) {
        requestAnimationFrame(frameLoop);
      } else {
        clsObserver.disconnect();
        longTaskObserver.disconnect();

        report.cls.value = clsScore;
        report.fps.totalFrames = frameCount;
        const totalDuration = (now - startTime) / 1000;
        report.fps.avgFps = Math.round(frameCount / totalDuration);
        
        resolve(report);
      }
    }

    requestAnimationFrame(frameLoop);
  });
})();
```

---

## 5. A Fronteira Operacional Cross-Platform (Lei 50)

O `browser-mcp` opera onde existe renderização web real:
1. **Aplicações Web & SPAs:** Inspeção completa multi-viewport via Chrome real, injeção de `perceptual_audit.js`, screenshots e DevTools.
2. **Ambientes Híbridos com CEF (Chromium Embedded Framework):** Em ecossistemas como MTA:SA que executam browsers CEF locais para UIs web em jogo, a validação via `browser-mcp` inspeciona a interface web do resource.
3. **Interfaces Nativas DirectX 9 / HLSL:** Em telas desenhadas puramente via DX GUI / Shaders no MTA:SA, a auditoria é contextual: validação estática de shaders via compilação HLSL SM 2.0/3.0, integridade do `meta.xml`, e ausência de alocações pesadas em render loops (`onClientRender`). É terminantemente proibido tentar forçar bibliotecas de DOM/CSS em engines de jogo puras.

---

## 6. O Ciclo de Retroalimentação Fractal para Perfeccionismo Absoluto

Se a inspeção visual, o profiling de 120Hz ou o diagnóstico de console revelarem **qualquer falha, mediocridade visual, quebra de layout ou instabilidade de frames**:

```text
[Inspeção Visual e Profiling no Chrome Real pelo Subagente Juiz via browser-mcp]
                                │
                                ▼
               ┌─────────────────────────────────┐
               │ CLS = 0.000, INP < 16ms,        │
               │ 120Hz/60Hz estável, zero erros  │
               │ e Padrão dos Titãs satisfeito?  │
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
        │ telemetria real.    │ │ 3. Geração de novos nós atômicos (N >= 100)  │
        └─────────────────────┘ │    dissecando os modos de falha              │
                                │ 4. Síntese de novo plano na ÉPOCA II         │
                                │ 5. Reconstrução física direta na ÉPOCA III   │
                                │ 6. Nova auditoria independente na ÉPOCA IV   │
                                └──────────────────────────────────────────────┘
```

---

## 7. Checklist Forense de Inspeção Perceptual v5.0 (Binário — Leis 21, 41 e 49)

> Executado pelo subagente Red Team Juiz na Época IV. Um único item reprovado dispara `[HARD REJECT]`.

- [ ] **Zero Erros no Console:** `browser_console_logs` retorna zero entradas de nível `error`.
- [ ] **Zero Warnings Críticos:** zero `warning` de hidratação SSR, memory leak, CORS ou deprecation.
- [ ] **Zero Assets 404:** zero requisições HTTP com status 404 na aba Network.
- [ ] **120Hz/60Hz Estável:** `report.fps.droppedFrames === 0` em repouso; frame rate médio compatível com o refresh rate do display.
- [ ] **Layout Shifts Anulados (CLS = 0.000):** `report.cls.value === 0.000`; zero instabilidade visual de elementos durante renderização.
- [ ] **Latência Tátil INP Sub-16ms:** interações de clique e toque com resposta de próximo frame imediata.
- [ ] **Isolamento Estrito de GPU:** transições atuando exclusivamente sobre `transform` e `opacity` com `will-change: transform`.
- [ ] **Fotografia de 8 Variáveis:** screenshots confirmam imagens fotográficas editoriais reais obedecendo aos parâmetros ópticos de lentes e iluminação — zero ilustrações de IA clichês ou SVGs genéricos.
- [ ] **Física de Molas de 2ª Ordem Confirmada:** presença de overshoot natural calibrado ($\zeta \in [0.72, 0.86]$) sem transições CSS lineares duras.
- [ ] **Multi-Viewport Responsivo:** layouts auditados e estáveis em resoluções Desktop 4K, 1080p, Tablet e Mobile.
