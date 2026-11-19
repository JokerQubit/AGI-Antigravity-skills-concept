---
name: browser_visual_reasoning
version: 6.0.0
description: "Use when verifying, testing, inspecting, or debugging any web app, frontend, SPA, or CEF UI in a real browser. Runs runtime perceptual and functional QA via browser-mcp (browser_navigate, browser_execute_script, browser_screenshot, browser_console_logs), injects perceptual_audit.js for 120Hz/60Hz frame-drop, CLS=0.000, INP<=16ms, and Long Task telemetry, checks multi-viewport responsiveness, and enforces zero console errors or 404 assets."
---

# Browser Visual Reasoning & 120Hz Perceptual Telemetry — Hyper-Cortex v6.0

Playbook de validação visual, funcional e cinemática em navegador real via **Browser MCP** (`@agent360/browser-mcp`). Estabelece o portão empírico de runtime: **nenhuma interface web é homologada sem inspeção no Chrome real por um verificador em contexto limpo medindo $CLS = 0.000$, $INP \le 16\text{ms}$, estabilidade a 120Hz/60Hz e zero erros/404s no console.**

> **Integração & Roteamento v6.0:** Acione esta skill sempre que construir, alterar ou depurar UIs web/CEF. Para padrões de design/animação, consulte `modern_ui_craft`; para áudio tátil, consulte `tactile_audio_sfx`; para protocolo de auditoria completa, consulte `forensic_adversarial_auditor`.
> - **Verificação Padrão de Runtime:** **Hydrogen 4 High** (`gemini-4-hydrogen-high`)
> - **Auditoria Perceptual Profunda / Causa Raiz de Regressões:** **Gemini 4 Neon High** (`gemini-4-neon-high`)
> - **Correções Paralelas de UI:** **Hydrogen 4 XHigh** (`gemini-4-hydrogen-xhigh`)

---

## 1. Arquitetura do Browser MCP no Antigravity

O **Browser MCP** conecta duas pontas locais:
1. **Extensão do Chrome:** Em `~/.browser-mcp/extension` (ou Chrome Web Store), controlando a sessão real acelerada por GPU.
2. **Servidor MCP Local (`mcp_config.json`):** Executado via `npx -y @agent360/browser-mcp@latest`, expondo navegação, execução de scripts, screenshots e logs de console.

Para checar conectividade antes da auditoria, solicite um `browser_screenshot` da aba ativa.

---

## 2. Portão de Verificação Visual Independente

- **Contexto Limpo Obrigatório:** O agente/verificador que audita a renderização não deve apenas confiar no código escrito; ele inspeciona o resultado real no navegador sem presumir sucesso.
- **Sequência Obrigatória de 4 Ferramentas:**
  1. `browser_navigate` — Abrir a URL da aplicação em execução.
  2. `browser_execute_script` — Injetar `perceptual_audit.js` durante interações ativas para medir CLS, Long Tasks e estabilidade de frames a 120Hz/60Hz.
  3. `browser_screenshot` — Capturar evidência visual multi-viewport (Desktop, Tablet, Mobile) em repouso e em estados interativos.
  4. `browser_console_logs` — Confirmar ausência total de erros, warnings críticos e falhas 404.

### Procedimento Padrão de Validação
1. Subir o servidor local da aplicação (ex: `npm run dev`, `vite`).
2. Navegar até a URL local com `browser_navigate`.
3. Capturar screenshots em repouso em múltiplos viewports via `browser_screenshot`.
4. Executar `perceptual_audit.js` via `browser_execute_script` enquanto aciona cliques, hovers, modais e scroll.
5. Auditar `browser_console_logs`.
6. Aprovar somente se todas as métricas e verificações visuais passarem.

---

## 3. Matriz de Avaliação Perceptual em Runtime

| Dimensão | Critério Técnico & Telemetria | Condição de Reprovação |
|---|---|---|
| **Cinemática 120Hz / ProMotion** | Molas de 2ª ordem (`motionTokens` de `modern_ui_craft`, $\zeta \in [0.72, 0.86]$, $k/m < 57600$). | Presença de `transition: all 300ms ease-in-out` ou curvas duras em componentes dinâmicos. |
| **Isolamento de GPU & Zero Reflow** | Animações restritas a `transform` e `opacity` com `will-change: transform`. | Layout thrashing ou animação de `width`, `height`, `top`, `margin`, `padding`. |
| **Cumulative Layout Shift (CLS)** | `report.cls.value === 0.000`. | Qualquer deslocamento visual ($CLS > 0.000$) durante carga de fontes ou imagens. |
| **Interaction to Next Paint (INP)** | Resposta visual ao input $\le 16\text{ms}$. | Atraso perceptível entre clique/toque e pintura do próximo frame. |
| **Direção Fotográfica & Controles** | Imagens editoriais reais (8 variáveis de `modern_ui_craft`) e micro-renders 1:1 / tipografia suíça. | Clichês neon/hologramas de IA, glifos Unicode (`▶`, `❚❚`, `→`) ou emojis como botões. |
| **Vídeo & Foley Real** | `<video>` com `poster` local; áudio via `scripts/sfx_tool.py` + `SpatialSoundManager` (`tactile_audio_sfx`). | Tela preta em vídeo ou síntese sonora via `OscillatorNode`/`Math.sin`. |
| **Conteúdo Real de Produção** | Copy e dados coerentes com o produto final. | Presença de "Lorem Ipsum" ou placeholders inacabados. |
| **Console & Rede DevTools** | `browser_console_logs` limpo (0 `error`, 0 warnings críticos, 0 404). | Qualquer exceção não tratada, warning de hidratação ou asset 404. |

---

## 4. Script Canônico de Profiling Perceptual (`perceptual_audit.js`)

Injetar via `browser_execute_script` para amostrar CLS, Long Tasks e taxa de quadros durante 1000ms:

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

    // 2. Monitorar Long Tasks
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

      // Orçamento por frame: > 10ms a 120Hz (ou > 18ms a 60Hz)
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

## 5. Fronteira Operacional Cross-Platform

Aplique `browser-mcp` onde há renderização web real:
1. **Aplicações Web & SPAs:** Inspeção completa multi-viewport via Chrome real, `perceptual_audit.js`, screenshots e DevTools.
2. **Ambientes Híbridos com CEF (Chromium Embedded Framework):** Em ecossistemas como MTA:SA com browsers CEF locais, o `browser-mcp` audita as páginas HTML/JS do resource.
3. **Interfaces Nativas DirectX 9 / HLSL / Game Engines:** Para UIs desenhadas puramente via DX GUI / shaders nativos, substitua o browser pela validação estática de compilação HLSL SM 2.0/3.0, integridade do `meta.xml` e auditoria de alocações em render loops (`onClientRender`). Nunca tente forçar bibliotecas DOM/CSS em engines nativas.

---

## 6. Ciclo de Retroalimentação em Malha Fechada (Hyper-Cortex v6.0)

```text
[Inspeção no Chrome Real via browser-mcp (perceptual_audit.js + screenshots + console)]
                                        │
                                        ▼
                       ┌─────────────────────────────────┐
                       │ CLS = 0.000, INP <= 16ms,       │
                       │ 120Hz/60Hz estável, 0 erros e   │
                       │ craft visual/sonoro validado?   │
                       └────────────────┬────────────────┘
                                        │
                           ┌────────────┴────────────┐
                           ▼                         ▼
                        [ SIM ]                    [ NÃO ]
                           │                         │
                           ▼                         ▼
                ┌─────────────────────┐   ┌──────────────────────────────────────────┐
                │ Sign-Off Aprovado   │   │ Relatório Objetivo de Falha:             │
                │ com telemetria real │   │ 1. Registrar métrica/DOM/console exato   │
                │ e screenshots.      │   │ 2. Causa raiz (Gemini 4 Neon High se     │
                └─────────────────────┘   │    sistêmica) + fix (Hydrogen 4 XHigh)   │
                                          │ 3. Revalidar do zero no Chrome real      │
                                          └──────────────────────────────────────────┘
```

Para falhas sistêmicas ou multi-módulo, escale a análise estrutural via `fractal_thought_graph` e o Gauntlet completo via `forensic_adversarial_auditor`.

---

## 7. Checklist Forense de Inspeção Perceptual (10 Critérios Binários)

- [ ] **Zero Erros no Console:** `browser_console_logs` sem entradas de nível `error`.
- [ ] **Zero Warnings Críticos:** zero warnings de hidratação SSR, memory leak, CORS ou deprecation.
- [ ] **Zero Assets 404:** zero requisições com status 404.
- [ ] **120Hz/60Hz Estável:** `report.fps.droppedFrames === 0` em repouso e `avgFps` compatível com o display.
- [ ] **CLS = 0.000:** `report.cls.value === 0.000`; zero saltos de layout.
- [ ] **INP <= 16ms:** resposta visual imediata em cliques e toques.
- [ ] **Isolamento de GPU:** animações restritas a `transform` e `opacity` com `will-change: transform`.
- [ ] **Direção Óptica Real:** screenshots confirmam ativos fotográficos limpos sem clichês de IA ou glifos Unicode fingindo ícones.
- [ ] **Física de Molas Confirmada:** movimento fluido ($\zeta \in [0.72, 0.86]$) sem transições lineares duras.
- [ ] **Multi-Viewport Responsivo:** layouts verificados em Desktop, Tablet e Mobile sem quebras ou overflow horizontal.
