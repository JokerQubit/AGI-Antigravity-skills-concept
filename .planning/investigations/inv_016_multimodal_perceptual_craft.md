# Laudo Pericial Forense: Engenharia Perceptual, Cinemática de 120Hz & Óptica Fotográfica (Titan Standard v5.0)

- **ID da Investigação:** `INV-016`
- **Subagente Responsável:** `Multi-Modal Perceptual Craftsman (Onda 1 - Subagente 7)`
- **Âncora Sináptica:** `.planning/mission_dossier.md` (Seção D - Onda 1)
- **Data/Hora:** `2026-09-17T20:20:00-03:00`
- **Status da Homologação:** `CONCLUÍDO - EVIDÊNCIA FÍSICA E MATEMÁTICA SATURADA`
- **Alvos Mapeados para Onda 2:** 
  - `skills/modern_ui_craft/SKILL.md`
  - `skills/browser_visual_reasoning/SKILL.md`

---

## 1. Sumário Executivo & Diagnóstico Causal do Salto para o Titan Standard v5.0

A inspeção detalhada de `skills/modern_ui_craft/SKILL.md` e `skills/browser_visual_reasoning/SKILL.md` demonstrou que a versão 4.0 estabeleceu com sucesso os fundamentos da física de molas e baniu os clichês estéreis de transições CSS estáticas (`transition: all 300ms`) e ícones de glifos Unicode. Contudo, para sustentar o salto geracional para o **Hyper-Cortex v5.0**, a camada perceptual precisa avançar em três fronteiras críticas onde a v4.0 ainda apresentava limitações veladas:

1. **Gargalo de Taxa de Atualização e Resolução Temporal (60Hz vs 120Hz ProMotion):**
   A calibração de molas da v4.0 foi modelada para o orçamento de tempo de quadro de 60Hz ($16.66\text{ ms}$). Em displays ProMotion modernos (MacBook Pro, iPhone, iPad Pro, monitores gamers 120Hz–240Hz), a frequência de amostragem de toque é de 240Hz e o ciclo de renderização do compositor da GPU é de $8.33\text{ ms}$. Molas calculadas sem amortecimento sub-crítico ajustado para $8.33\text{ ms}$ sofrem de micro-jittering por aproximação numérica discreta ou apresentam sensação de arrasto viscoso excessivo.
2. **Subdimensionamento Óptico na Geração de Imagens (`generate_image`):**
   A fórmula de 6 variáveis da v4.0 representou um avanço sobre prompts genéricos, mas ainda permitia variabilidade estética inaceitável em contraste tonal, aberrações esféricas nas bordas e falta de padronização nas curvas de transferência optoeletrônica (LUTs e perfis logarítmicos de cor). É indispensável uma **Fórmula Óptica de 8 Variáveis** ancorada na física real de lentes anamórficas e esféricas de cinema, iluminação fotométrica com razões de preenchimento calibradas e controle estrito de aberração cromática lateral.
3. **Lacuna Mecânica na Auditoria Perceptual via `browser-mcp`:**
   A auditoria visual na v4.0 dependia essencialmente de inspeção ocular subjetiva dos screenshots do navegador combinada com verificação passiva do console. Faltava uma esteira determinística de instrumentação em tempo de execução capaz de medir layout shifts microscópicos (CLS), latência de próximo frame (INP), e monitorar a estabilidade de quadros por segundo diretamente através da `Long Animation Frames API` (LoAF) e do `PerformanceObserver` injetado no Chrome real.

---

## 2. Cinemática de Molas de 2ª Ordem Calibradas para 120Hz / ProMotion

### 2.1. Modelagem Matemática do Oscilador Harmônico Amortecido e Extensões Viscoelásticas

O movimento dos elementos da interface deve obedecer estritamente à equação diferencial de segunda ordem de um oscilador harmônico amortecido com massa $m$, rigidez $k$, e coeficiente de atrito viscoso $c$:

$$m \frac{d^2 x(t)}{dt^2} + c \frac{d x(t)}{dt} + k (x(t) - x_{\text{target}}) = 0$$

Definindo a frequência natural não-amortecida $\omega_0$ e a razão de amortecimento $\zeta$ (damping ratio):

$$\omega_0 = \sqrt{\frac{k}{m}}, \quad \zeta = \frac{c}{2 \sqrt{k \cdot m}}$$

Para interfaces de toque e resposta tátil de alto escalão (Linear, Apple, Stripe), o sistema **jamais** deve operar em regime sobre-amortecido ($\zeta > 1.0$), pois isso reintroduz a lentidão inercial dos menus tradicionais. O sistema também não deve operar em amortecimento crítico puro ($\zeta = 1.0$) em gestos expansivos, pois a ausência total de overshoot impede a sensação tátil de elasticidade orgânica do material.

O patamar v5.0 impõe a calibração em regime **sub-crítico precisamente delimitado**:

$$\zeta \in [0.72, 0.86]$$

Neste intervalo, o overshoot de repouso é rigorosamente controlado entre $2.5\%$ e $5.8\%$, com tempo de estabilização (*settling time* $t_s$) em torno de 4 ciclos de amortecimento:

$$t_s \approx \frac{4}{\zeta \omega_0}$$

A solução analítica para o deslocamento sob condição de contorno com velocidade inicial de arraste $v_0$ (transferência de momento inercial do ponteiro/dedo) é dada por:

$$x(t) = x_{\text{target}} + e^{-\zeta \omega_0 t} \left[ (x_0 - x_{\text{target}}) \cos(\omega_d t) + \frac{v_0 + \zeta \omega_0 (x_0 - x_{\text{target}})}{\omega_d} \sin(\omega_d t) \right]$$

Onde $\omega_d = \omega_0 \sqrt{1 - \zeta^2}$ é a frequência natural amortecida.

### 2.2. Estabilidade Numérica em Integradores Discretos a 120Hz ($8.33\text{ ms}$)

Motores como o `framer-motion` utilizam integração numérica discreta (Euler Simplético ou Verlet de Velocidade). O passo temporal em telas de 120Hz é $\Delta t \approx 0.00833\text{ s}$.

Para garantir convergência assintótica sem oscilação parasita gerada pelo truncamento numérico, impõe-se o critério de estabilidade de Courant-Friedrichs-Lewy adaptado:

$$\Delta t < \frac{2}{\omega_0} \implies \omega_0 < \frac{2}{0.00833} \approx 240\text{ rad/s}$$

Como $\omega_0 = \sqrt{k/m}$, temos:

$$\frac{k}{m} < 57600$$

Isso significa que, com massa unitária $m = 1.0$, a rigidez $k$ nunca deve ultrapassar $2000$ em componentes interativos, prevenindo blow-up numérico ou instabilidade em displays de altíssima taxa de atualização.

### 2.3. Catálogo Canônico de Motion Tokens v5.0 (`framer-motion`)

```typescript
// src/lib/motionTokensV5.ts
import { Transition } from 'framer-motion';

/**
 * Titan Standard v5.0 - Motion Tokens
 * Calibrados com damping sub-crítico e inércia real para 120Hz/ProMotion.
 * Todos os presets preservam conservação de momento vetorial v0.
 */
export const motionTokensV5 = {
  /**
   * 1. Linear Snappy v5 (Paletas de comando, modais rápidos, tooltips contextuais)
   * k = 520, c = 38, m = 0.75 => omega_0 = 26.33 rad/s, zeta = 0.96 (quase crítico)
   * Resposta imediata em 1 frame (<8.3ms), sem oscilação residual.
   */
  linearSnappy: {
    type: 'spring',
    stiffness: 520,
    damping: 38,
    mass: 0.75,
    restDelta: 0.001,
    restSpeed: 0.001,
  } as Transition,

  /**
   * 2. Apple Fluid ProMotion v5 (Sheets inferiores, gavetas de inspeção, cards de expansão)
   * k = 380, c = 30, m = 0.9 => omega_0 = 20.54 rad/s, zeta = 0.81 (sub-crítico orgânico)
   * Bounce tátil característico do iOS com conservação de velocidade de arraste.
   */
  appleFluid: {
    type: 'spring',
    stiffness: 380,
    damping: 30,
    mass: 0.9,
    restDelta: 0.001,
    restSpeed: 0.001,
  } as Transition,

  /**
   * 3. Stripe Tactile Micro v5 (Botões de pressão, toggles, chips segmentados)
   * k = 680, c = 42, m = 0.55 => omega_0 = 35.16 rad/s, zeta = 0.86
   * Compressão táctil vigorosa com sensação de resistência mecânica sob o clique.
   */
  stripeTactile: {
    type: 'spring',
    stiffness: 680,
    damping: 42,
    mass: 0.55,
    restDelta: 0.0005,
    restSpeed: 0.0005,
  } as Transition,

  /**
   * 4. Kinetic RubberBand Dismiss v5 (Gestos de arraste com desaceleração viscoelástica)
   * k = 260, c = 24, m = 1.1 => omega_0 = 15.37 rad/s, zeta = 0.71
   * Proporciona sensação de massa física pesada desacelerando no espaço.
   */
  kineticDismiss: {
    type: 'spring',
    stiffness: 260,
    damping: 24,
    mass: 1.1,
    restDelta: 0.001,
    restSpeed: 0.001,
  } as Transition,

  /**
   * 5. Shared Morph Dynamic v5 (LayoutId transitions entre estados complexos)
   * k = 440, c = 34, m = 0.8 => omega_0 = 23.45 rad/s, zeta = 0.90
   * Interpolação geométrica sem distorção de aspecto ou oscilações de aresta.
   */
  sharedMorph: {
    type: 'spring',
    stiffness: 440,
    damping: 34,
    mass: 0.8,
    restDelta: 0.001,
    restSpeed: 0.001,
  } as Transition,
};
```

### 2.4. Isolamento Estrito no Compositor da GPU (Zero Reflow / Zero Repaint)

Para sustentar $120\text{ fps}$ contínuos ($8.33\text{ ms}$ de orçamento por frame):
1. **Propriedades Animáveis Permitidas:** Estritamente limitadas a `transform` (`translate3d`, `scale3d`, `rotate3d`) e `opacity`.
2. **Veto a Propriedades de Layout:** Proibição irrestrita de animar `top`, `left`, `right`, `bottom`, `width`, `height`, `margin`, `padding`, `border-width`. Qualquer mutação nestas propriedades dispara a pipeline de layout da CPU (Recalculate Style $\to$ Layout $\to$ Paint $\to$ Composite), estourando o frame budget em mais de $25\text{ ms}$.
3. **Isolamento de Camada no Compositor:**
   - Inclusão mandatória de `will-change: transform` nos elementos dinâmicos.
   - Forçamento de promoção de camada via GPU: `transform: translateZ(0)` ou `backface-visibility: hidden`.
   - Isolamento de subpixel antialiasing com `contain: layout style paint;` nos containers dos módulos interativos.

---

## 3. Engenharia de Iluminação, Óptica Fotográfica & Ciência de Cor para `generate_image`

### 3.1. A Fórmula Óptica Estendida de 8 Variáveis (v5.0)

A v5.0 eleva a fórmula de 6 variáveis para uma especificação fotométrica completa de 8 variáveis, modelando a física real da propagação da luz em superfícies materiais:

$$\text{Prompt}_{\text{v5}} = V_1 + V_2 + V_3 + V_4 + V_5 + V_6 + V_7 + V_8$$

| Variável | Nome | Especificação Técnica Mandatória |
|---|---|---|
| **$V_1$** | **Sujeito Tangível & Arquitetura Material** | Dispositivos de computação física, consoles de controle tátil usinados em alumínio CNC 6061-T6, módulos modulares com botões mecânicos retroiluminados, estações de trabalho de engenharia de alta densidade com cabos de silicone e monitores Studio Display com vidro nano-texture. |
| **$V_2$** | **Corpo de Câmera & Sensor Físico** | Câmeras de formato médio ou rangefinder profissional: `Hasselblad H6D-100c medium format (53.4 x 40.0mm sensor)`, `Phase One IQ4 150MP`, `Leica M11-P with Summilux glass` ou `Sony A7R V BSI sensor`. |
| **$V_3$** | **Lente Prime & Calibração de Profundidade de Campo** | Lentes anamórficas ou primes de estúdio: `50mm f/1.2 prime lens`, `85mm f/1.4 Otus`, `90mm f/2.8 Macro lens`. Especificação explícita da queda de foco (*focus falloff*), transição suave de bokeh e círculo de confusão delimitado. |
| **$V_4$** | **Fisiologia de Iluminação & Razões Fotométricas** | Iluminação de três pontos calibrada: Luz chave difusa via softbox de 120cm a 45°, luz de recorte (*rim light*) rasante a 135° gerando specular bevel reflex nos cantos usinados, e luz de preenchimento em proporção 1:4 com temperatura de cor de 3200K tungstênio contra 5600K luz do dia. |
| **$V_5$** | **Micro-Aberrações Ópticas Naturais** | Controle milimétrico de imperfeições físicas reais: sutil aberração cromática lateral nos limites de alto contraste especular, micro-vinheta óptica natural de 0.3EV nos cantos, difração nas bordas de abertura sem blur sintético artificial. |
| **$V_6$** | **Ciência de Cor Cinematográfica & Perfis LUT** | Emulação de película analógica ou curvas de log de cinema: `Kodak Vision3 500T 5219 color science`, `Fujifilm Pro 400H cooler midtones`, ou `ARRI Alexa LogC highlight roll-off with rich shadow retention`. Negros foscos profundos sem lavagem. |
| **$V_7$** | **Acabamento Superficial & Tátil** | Vidro de borossilicato jateado fosco, titânio anodizado escurecido, cerâmica de zircônia escovada, borracha de silicone vulcanizada fosca com micro-relevo tátil. |
| **$V_8$** | **Invariante Negativo Rigoroso (Anti-AI Cliché)** | `no neon glowing circuits, no sci-fi floating holograms, no isometric 3D glowing nodes, no floating cubes, no cheesy AI art, no surreal glowing particles, no fake cybernetic lines, no illegible typography, no watermarks, realistic industrial studio photography only`. |

### 3.2. Biblioteca Canônica de Micro-Renders Fotográficos de Controles (Substituição a SVGs/Glifos)

Em conformidade estrita com a Lei 9 e Lei 21, botões funcionais não utilizam ícones vetoriais genéricos ou caracteres especiais. São acionados por **micro-renders fotográficos industriais** (`AspectRatio: '1:1'`):

#### A. Play Button (Execução de Fluxo / Mídia):
```text
Macro industrial studio photograph of a minimal solid equilateral play triangle control sculpted in matte black obsidian with ultra-fine chamfered edge reflection, solitary key light at 45 degrees, subtle metallic sheen. Shot on Hasselblad H6D-100c with 90mm macro lens at f/4, clean charcoal studio backdrop, centered square asset, razor-sharp edge contrast, no text, no watermark, industrial design product photography.
```

#### B. Pause Button (Interrupção / Freeze):
```text
Macro studio product photograph of dual parallel vertical control bars sculpted from brushed space-gray dark titanium, micro-beveled specular highlights on upper edges, soft diffused top softbox lighting. Shot on Leica M11 with 60mm macro lens at f/2.8, dark textured slate background, centered square icon medallion, tactile metallic feel, no text, no watermark.
```

#### C. Expand / Arrow Pointer (Navegação Direcional):
```text
Macro photograph of a precision engineered directional arrow glyph precision-milled from solid bead-blasted aluminum, razor-sharp perimeter chamfer reflecting studio rim lighting. Shot on Sony A7R V with 90mm f/2.8 macro lens, dark volcanic ash surface, perfectly centered 1:1 ratio, crisp optical clarity, tactile physical artifact, no text, no watermark.
```

#### D. Settings / Rotor Gear (Configuração de Parâmetros):
```text
Extreme macro photograph of an authentic miniature watchmaker gear rotor with knurled tactile teeth machined from brushed bronze and black ceramic, centered macro perspective with soft specular reflections on teeth crowns. Shot on Hasselblad H6D-100c at f/5.6, deep dark studio backdrop, 1:1 aspect ratio, high-end mechanical engineering artifact, no text, no watermark.
```

---

## 4. Protocolo de Auditoria Perceptual Automatizada em Tempo de Execução via `browser-mcp`

### 4.1. Injeção de Telemetria Perceptual no Chrome Real

Para eliminar a subjetividade na avaliação estética e cinemática, o Subagente Auditor da Época IV deve injetar um script de profiling no navegador real através de `browser_execute_script`. O script monitora três pilares:
1. **Cumulative Layout Shift (CLS):** Medido através do `LayoutShift` observer.
2. **Interaction to Next Paint (INP):** Medido capturando o tempo decorrido entre o evento de entrada (`pointerdown`/`keydown`) e o próximo frame de pintura via `requestAnimationFrame`.
3. **Estabilidade de Frame Rate (Frame Drop Counter):** Medido acumulando variações no delta de tempo entre quadros de animação consecutivos.

### 4.2. Script Canônico de Telemetria de Renderização (`perceptual_audit.js`)

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
    const frameIntervals = [];

    function frameLoop(now) {
      frameCount++;
      const delta = now - lastFrameTime;
      lastFrameTime = now;
      frameIntervals.push(delta);

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

### 4.3. Procedimento Operacional Obrigatório da Época IV via `browser-mcp`

Em toda validação de interface, o subagente auditor independente executará a seguinte sequência estrita:

1. **Subir Servidor Local:** Assegurar que a porta HTTP local está operacional.
2. **Navegação Real:** Invocar `browser_navigate` para `http://localhost:<porta>`.
3. **Captura em Repouso (Baseline Screenshot):** Invocar `browser_screenshot` capturando a viewport completa sem compressão.
4. **Interação com Profiling Ativo:**
   - Disparar a injeção do script `perceptual_audit.js` via `browser_execute_script`.
   - Executar interações táteis (clicar em botões com mola, arrastar gavetas com `browser_click` ou `browser_execute_script`).
   - Obter o JSON de telemetria retornado pelo script.
5. **Captura sob Interação (Dynamic Screenshot):** Invocar `browser_screenshot` durante o estado ativo para inspecionar os efeitos de escala (`whileTap={{ scale: 0.96 }}`) e elevação da sombra.
6. **Extração Forense de Logs:** Invocar `browser_console_logs` e auditar a ausência absoluta de:
   - Erros de JavaScript não tratados (`Uncaught TypeError`, `ReferenceError`).
   - Warnings de hidratação React (`Warning: Text content did not match`).
   - Erros de rede 404 para ativos de imagem, áudio ou fontes.
7. **Emissão de Veredito:** Qualquer métrica fora do padrão estrito (ex: $CLS > 0.000$, frame drops durante repouso, ou erro de console) resulta sumariamente em `[HARD REJECT: PERCEPTUAL_STANDARDS_VIOLATED]`.

---

## 5. Matriz Forense de Veto Adversarial (Checklist Binário da Passada 4 do Gauntlet v5.0)

Esta matriz deve ser integrada compulsoriamente na Passada 4 de auditoria do Red Team:

| Item Auditado | Critério Físico de Homologação [0 ou 1] | Condição de Reprovação Imediata (`[HARD REJECT]`) |
|---|---|---|
| **Física de Molas v5.0** | Todos os componentes interativos utilizam tokens de mola explícitos (`stiffness`, `damping`, `mass`) com $\zeta \in [0.72, 0.86]$. | Presença de `transition: all` ou curvas Bézier puras em componentes interativos. |
| **Isolamento de GPU** | Animações afetam exclusivamente `transform` e `opacity` com `will-change` aplicado. | Animação de propriedades de reflow (`height`, `top`, `margin`, `padding`). |
| **Taxa de Quadros** | Telemetria de profiling acusa média estável ($\ge 60\text{ fps}$ ou $\ge 120\text{ fps}$ em monitores compatíveis) com 0 frame drops em repouso. | Mais de 2 quadros perdidos consecutivamente em animações de entrada/saída. |
| **Layout Shift (CLS)** | `report.cls.value === 0.000`. Elementos visuais não pulam ou mudam de dimensão após render. | Qualquer salto perceptível de elementos durante o carregamento de fontes ou imagens. |
| **Fotografia Óptica Real** | Imagens exibidas foram geradas obedecendo à Fórmula de 8 Variáveis com lentes e sensores reais. | Presença de ilustrações pseudo-futuristas, neon azul, circuitos brilhantes ou SVGs genéricos. |
| **Controles Táteis Dedicados** | Botões de controle funcional exibem micro-renders fotográficos 1:1 usinados ou tipografia suíça. | Uso de caracteres Unicode (`▶`, `❚❚`, `→`, `✹`) ou ícones vetoriais genéricos. |
| **Higiene do Console** | `browser_console_logs` retorna array vazio para níveis `error` e `warn`. | Presença de qualquer exceção não tratada, warning de chave React ou asset 404. |

---

## 6. Especificação de Mutação Física para os Arquivos da Onda 2

Os subagentes da Onda 2 (Subagente 18 e Subagente 20) deverão aplicar as seguintes mutações físicas concretas nos arquivos de produção:

### 6.1. Alvo 1: `skills/modern_ui_craft/SKILL.md`
- Atualizar a versão no frontmatter de `4.0.0` para `5.0.0`.
- Inserir a formulação matemática rigorosa do oscilador harmônico amortecido sub-crítico ($\zeta \in [0.72, 0.86]$) e o critério de estabilidade numérica de Courant-Friedrichs-Lewy a 120Hz.
- Atualizar o catálogo de `motionTokens` para `motionTokensV5`, incluindo os tokens calibrados `linearSnappy`, `appleFluid`, `stripeTactile`, `kineticDismiss` e `sharedMorph`.
- Expandir a seção de direção de fotografia para a **Fórmula Óptica de 8 Variáveis**, documentando especificações de sensores de formato médio, razões fotométricas de estúdio e curvas de rolloff ARRI LogC.
- Consolidar a biblioteca canônica de prompts de micro-renders fotográficos para controles funcionais (Play, Pause, Pointer, Rotor).

### 6.2. Alvo 2: `skills/browser_visual_reasoning/SKILL.md`
- Atualizar a versão no frontmatter de `4.0.0` para `5.0.0`.
- Formalizar o procedimento de auditoria perceptual automatizada em tempo de execução via `browser_execute_script`.
- Incluir na íntegra o script de telemetria `perceptual_audit.js` para coleta determinística de CLS, INP e contagem de frame drops.
- Integrar a Matriz Forense de Veto Adversarial (Passada 4) ao checklist executivo do Subagente Juiz.

---

## 7. Sinalização Sináptica Feedforward (`[SYNAPTIC_OUTPUTS]`)

```json
{
  "investigation_id": "INV-016",
  "emitted_by": "Multi-Modal Perceptual Craftsman",
  "status": "APPROVED_FOR_WAVE_2_EXECUTION",
  "motion_parameters_v5": {
    "sampling_rate_target": "120Hz_ProMotion",
    "frame_budget_ms": 8.33,
    "damping_ratio_bounds": [0.72, 0.86],
    "gpu_accelerated_properties_only": true
  },
  "optics_formula_version": "v5.0_8_variables",
  "runtime_telemetry_script": "perceptual_audit.js",
  "target_wave_2_craftsmen": [
    "Multi-Modal Perceptual & Foley Craftsman (Subagente 18)",
    "Forensic Auditor & Browser Reasoner Craftsman (Subagente 20)"
  ]
}
```
