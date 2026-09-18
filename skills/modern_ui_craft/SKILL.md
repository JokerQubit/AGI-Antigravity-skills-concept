---
name: modern_ui_craft
version: 5.0.0
description: "v5.0 — Universal Cognitive Parity — Craft Perceptual dos Titãs. Playbook técnico de excelência em Design de Interfaces e Engenharia Perceptual no Padrão dos Titãs (Linear, Apple, Stripe, Instagram). Governa a cinemática tátil com física de molas de 2ª ordem calibradas para 120Hz/ProMotion (damping ratio sub-crítico 0.72-0.86, k/m < 57600), fórmula fotográfica de 8 variáveis para generate_image, glassmorphism especular, telemetria perceptual de runtime (CLS=0.000 / INP <= 16ms) e micro-ativos táteis reais. Ativado compulsoriamente em toda interação visual, layout ou animação — sem exceção de escopo."
---

# Modern UI Craft & Studio Aesthetics Engineering Playbook — v5.0 (Universal Cognitive Parity — Craft Perceptual dos Titãs)

Na v5.0.0, o craft perceptual desta skill é ativado compulsoriamente em toda interação que toque qualquer componente visual, layout ou animação — sem distinção entre "micro-ajuste de CSS" e "grande redesign". A dicotomia de escopo está extinta: não existe ajuste de UI que não exija física de molas de 2ª ordem calibrada para 120Hz/ProMotion, isolamento de GPU compositor e latência tátil sub-16ms.

Manual prático de engenharia perceptual e design de interfaces de padrão de excelência internacional (referências Awwwards Site of the Day, Red Dot, Apple Human Interface Guidelines, Linear e Stripe). Abrange a cinemática tátil de 120Hz/ProMotion baseada em **física dinâmica de molas de 2ª ordem com amortecimento sub-crítico ($\zeta \in [0.72, 0.86]$)**, direção de arte fotográfica de 8 variáveis via `generate_image`, telemetria automatizada de runtime no Chrome real (CLS=0.000 / INP $\le$ 16ms), erradicação de vetores estéreis e glifos Unicode como ícones, e layouts fluidos contínuos.

---

## 1. O Paradigma dos Titãs: Linear, Apple, Stripe & Instagram (Banimento do CSS Básico)

A esmagadora maioria das aplicações comuns comete o pecado da mediocridade visual ao assumir transições duras em CSS puro:
```css
/* TERMINANTEMENTE PROIBIDO PARA COMPONENTES DINÂMICOS E INTERATIVOS */
transition: all 300ms ease-in-out;
```
Curvas de Bézier cúbicas estáticas soam mecânicas, artificiais e congeladas. Os líderes mundiais da experiência digital utilizam **física dinâmica de molas (Spring Physics)**, onde cada elemento se comporta como uma massa física real sujeita a forças, amortecimento e transferência inercial de energia.

### 1.1. Modelagem Matemática do Oscilador Harmônico Amortecido e Extensões Viscoelásticas

O movimento dos componentes deve obedecer estritamente à equação diferencial de segunda ordem de um oscilador harmônico amortecido com massa $m$, rigidez $k$ e coeficiente de amortecimento viscoso $c$:

$$m \frac{d^2 x(t)}{dt^2} + c \frac{d x(t)}{dt} + k (x(t) - x_{\text{target}}) = 0$$

Definindo a frequência natural não-amortecida $\omega_0$ e a razão de amortecimento $\zeta$ (*damping ratio*):

$$\omega_0 = \sqrt{\frac{k}{m}}, \quad \zeta = \frac{c}{2 \sqrt{k \cdot m}}$$

Para interfaces de toque e resposta tátil de alto escalão (Linear, Apple, Stripe), o sistema **jamais** opera em regime sobre-amortecido ($\zeta > 1.0$) nem em amortecimento crítico puro ($\zeta = 1.0$) em gestos dinâmicos. A v5.0 impõe a calibração em regime **sub-crítico precisamente delimitado**:

$$\zeta \in [0.72, 0.86]$$

Neste intervalo, o overshoot de repouso é rigorosamente controlado entre $2.5\%$ e $5.8\%$, com tempo de estabilização (*settling time* $t_s$) em torno de 4 ciclos:

$$t_s \approx \frac{4}{\zeta \omega_0}$$

A solução analítica para o deslocamento com velocidade inicial de arraste $v_0$ (transferência inercial do cursor ou toque) é dada por:

$$x(t) = x_{\text{target}} + e^{-\zeta \omega_0 t} \left[ (x_0 - x_{\text{target}}) \cos(\omega_d t) + \frac{v_0 + \zeta \omega_0 (x_0 - x_{\text{target}})}{\omega_d} \sin(\omega_d t) \right]$$

onde $\omega_d = \omega_0 \sqrt{1 - \zeta^2}$ é a frequência natural amortecida.

### 1.2. Estabilidade Numérica em Integradores Discretos a 120Hz ($8.33\text{ ms}$)

Motores de animação como o `framer-motion` utilizam integração numérica discreta (Euler Simplético / Verlet). Em displays ProMotion de 120Hz, o passo temporal é $\Delta t \approx 0.00833\text{ s}$.

Para garantir convergência assintótica sem instabilidades ou oscilações parasitas geradas por truncamento numérico, impõe-se o critério de estabilidade de Courant-Friedrichs-Lewy adaptado:

$$\Delta t < \frac{2}{\omega_0} \implies \omega_0 < \frac{2}{0.00833} \approx 240\text{ rad/s}$$

Como $\omega_0 = \sqrt{k/m}$, impõe-se a invariante inegociável:

$$\frac{k}{m} < 57600$$

Com massa unitária $m = 1.0$, a rigidez $k$ nunca ultrapassa $2000$ em componentes interativos, prevenindo blow-up numérico e jittering em telas de alta frequência.

### 1.3. [EXEMPLAR CONTRASTIVO DE UI: CINEMÁTICA INTERATIVA (Lei 36)]

#### ❌ WRONG (Anti-Pattern: Transição Dura & Amadora):
```css
.card {
  transition: all 0.3s ease-in-out;
}
.card:hover {
  transform: translateY(-4px);
}
```

##### 🔬 Autópsia de Falha Post-Mortem:
1. **Perda de Conservação de Momento:** Se o ponteiro entrar e sair antes dos 300ms, a curva estática sofre corte brusco (*clipping visual*), sem amortecer a velocidade residual.
2. **Latência Tátil Perceptível (>50ms):** A curva ease-in-out desacelera no início da interação, transmitindo uma sensação de lentidão e peso morto sob o toque.
3. **Pena de Layout Reflow:** `transition: all` observa todas as propriedades calculadas (incluindo dimensões e bordas), disparando reflows contínuos de layout na thread principal da CPU.

---

#### ✅ CORRECT (Padrão Titã: Mola de 2ª Ordem Isolada na GPU a 120Hz):
```tsx
<motion.div
  whileHover={{ y: -4, scale: 1.01 }}
  whileTap={{ scale: 0.98 }}
  transition={motionTokensV5.stripeTactile}
  style={{ willChange: 'transform' }}
>
```

### 1.4. Catálogo Canônico de Motion Tokens v5.0 (`framer-motion`)

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

---

## 2. Componentes Dinâmicos com Física dos Titãs & GPU Compositor Isolation

**v5.0 — Universal Parity Invariant:** `framer-motion` com física de molas de 2ª ordem calibradas para 120Hz/ProMotion (stiffness, damping, mass explícitos, $\zeta \in [0.72, 0.86]$, $k/m < 57600$) e isolamento de GPU compositor são aplicados **sempre, em qualquer componente interativo**, sem exceção de escopo ou porte. A distinção entre "componente simples" e "componente dinâmico" está extinta. Toda animação — sem exceção — opera estritamente sobre propriedades aceleradas por hardware (`transform`, `opacity`), isoladas na thread do compositor da GPU para garantir 60fps/120fps sem engasgos de reflow:

### 1. Botão Tátil com Retorno Inercial Orgânico:
```tsx
import React from 'react';
import { motion } from 'framer-motion';
import { motionTokensV5 } from '../lib/motionTokensV5';

interface TitanButtonProps {
  children: React.ReactNode;
  onClick?: () => void;
  iconSrc?: string;
}

export const TitanButton: React.FC<TitanButtonProps> = ({ children, onClick, iconSrc }) => {
  return (
    <motion.button
      onClick={onClick}
      whileHover={{ scale: 1.025, y: -1.5 }}
      whileTap={{ scale: 0.96, y: 0.5 }}
      transition={motionTokensV5.stripeTactile}
      className="group relative flex items-center gap-3 rounded-full border border-white/12 bg-white/[0.04] px-6 py-3 font-mono text-xs uppercase tracking-widest text-white shadow-xl backdrop-blur-xl will-change-transform hover:border-white/30 hover:bg-white/[0.08]"
    >
      <span className="tracking-[0.18em]">{children}</span>
      {iconSrc && (
        <img
          src={iconSrc}
          alt=""
          className="h-3.5 w-3.5 object-contain transition-transform group-hover:scale-110"
        />
      )}
    </motion.button>
  );
};
```

### 2. Indicador Ativo com Shared Layout Contínuo (`layoutId`):
Elimina cortes secos entre abas e seletores:
```tsx
import { motion } from 'framer-motion';
import { motionTokensV5 } from '../lib/motionTokensV5';

interface TabItemProps {
  label: string;
  isActive: boolean;
  onSelect: () => void;
}

export const TabItem: React.FC<TabItemProps> = ({ label, isActive, onSelect }) => (
  <button
    onClick={onSelect}
    className="relative px-5 py-2.5 text-xs font-mono uppercase tracking-wider text-slate-300 transition-colors hover:text-white"
  >
    {isActive && (
      <motion.div
        layoutId="activePill"
        transition={motionTokensV5.linearSnappy}
        className="absolute inset-0 rounded-full border border-white/15 bg-white/10 shadow-[0_4px_20px_rgba(0,0,0,0.5)] backdrop-blur-md"
      />
    )}
    <span className="relative z-10">{label}</span>
  </button>
);
```

### 3. Modal / Drawer Deslizante com Gesto de Arraste (Rubber-Banding):
```tsx
import { AnimatePresence, motion } from 'framer-motion';
import { motionTokensV5 } from '../lib/motionTokensV5';

interface DrawerProps {
  isOpen: boolean;
  onClose: () => void;
  children: React.ReactNode;
}

export const TitanDrawer: React.FC<DrawerProps> = ({ isOpen, onClose, children }) => (
  <AnimatePresence>
    {isOpen && (
      <>
        {/* Backdrop com desfoque progressivo */}
        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          exit={{ opacity: 0 }}
          transition={{ duration: 0.2 }}
          onClick={onClose}
          className="fixed inset-0 z-40 bg-black/60 backdrop-blur-sm"
        />

        {/* Painel Tátil com física Apple Fluid e gesto de arrastar para fechar */}
        <motion.div
          initial={{ x: '100%' }}
          animate={{ x: 0 }}
          exit={{ x: '100%' }}
          transition={motionTokensV5.appleFluid}
          drag="x"
          dragConstraints={{ left: 0 }}
          dragElastic={{ left: 0.05, right: 0.5 }}
          onDragEnd={(_, info) => {
            if (info.offset.x > 120 || info.velocity.x > 500) {
              onClose();
            }
          }}
          className="fixed bottom-0 right-0 top-0 z-50 w-full max-w-md border-l border-white/10 bg-[#0C0F17]/95 p-8 shadow-2xl backdrop-blur-2xl will-change-transform"
        >
          {children}
        </motion.div>
      </>
    )}
  </AnimatePresence>
);
```

---

## 3. Direção de Arte Fotográfica & Engenharia Óptica para `generate_image`

### O Banimento Inegociável dos Clichês de IA Genérica:
- **TERMINANTEMENTE PROIBIDO:** Circuitos brilhantes neon azul/ciano, gráficos isométricos flutuantes com nós brilhantes, chips cósmicos, cubos holográficos, ilustrações pseudo-futuristas de ficção científica barata, e textos ilegíveis gerados pela IA. Imagens com esse padrão denunciam "IA genérica amadora" e destroem a credibilidade de qualquer produto.
- **O PADRÃO OBRIGATÓRIO (FOTOGRAFIA REALISTA & EDITORIAL PROFISSIONAL):** Toda imagem gerada deve se assemelhar a uma **fotografia real autêntica de classe mundial** (publicada em revistas de design de produto como Wallpaper*, Monocle, publicações da Apple, Stripe Press, Linear ou Teenage Engineering) ou a um **design editorial de produto de altíssima fidelidade**.

### A Fórmula Óptica Estendida de 8 Variáveis (v5.0):

Para garantir realismo palpável, profundidade óptica, física real de iluminação e textura orgânica, toda chamada a `generate_image` deve obedecer compulsoriamente à **Fórmula Óptica de 8 Variáveis**:

$$\text{Prompt}_{\text{v5}} = V_1 + V_2 + V_3 + V_4 + V_5 + V_6 + V_7 + V_8$$

| Variável | Nome | Especificação Técnica Mandatória |
|---|---|---|
| **$V_1$** | **Sujeito Tangível & Arquitetura Material** | Dispositivos de computação física, consoles de controle tátil usinados em alumínio CNC 6061-T6, módulos com botões mecânicos retroiluminados, estações de trabalho de engenharia de alta densidade com cabos de silicone e monitores Studio Display com vidro nano-texture. |
| **$V_2$** | **Corpo de Câmera & Sensor Físico** | Câmeras de formato médio ou rangefinder profissional: `Hasselblad H6D-100c medium format (53.4 x 40.0mm sensor)`, `Phase One IQ4 150MP`, `Leica M11-P with Summilux glass` ou `Sony A7R V BSI sensor`. |
| **$V_3$** | **Lente Prime & Profundidade de Campo** | Lentes anamórficas ou primes de estúdio: `50mm f/1.2 prime lens`, `85mm f/1.4 Otus`, `90mm f/2.8 Macro lens`. Especificação explícita da queda de foco (*focus falloff*), transição suave de bokeh e círculo de confusão delimitado. |
| **$V_4$** | **Fisiologia de Iluminação & Razões Fotométricas** | Iluminação de três pontos calibrada: Luz chave difusa via softbox de 120cm a 45°, luz de recorte (*rim light*) rasante a 135° gerando specular bevel reflex nos cantos usinados, e luz de preenchimento em proporção 1:4 com temperatura de cor de 3200K tungstênio contra 5600K luz do dia. |
| **$V_5$** | **Micro-Aberrações Ópticas Naturais** | Controle milimétrico de imperfeições físicas reais: sutil aberração cromática lateral nos limites de alto contraste especular, micro-vinheta óptica natural de 0.3EV nos cantos, difração nas bordas de abertura sem blur sintético artificial. |
| **$V_6$** | **Ciência de Cor Cinematográfica & Perfis LUT** | Emulação de película analógica ou curvas de log de cinema: `Kodak Vision3 500T 5219 color science`, `Fujifilm Pro 400H cooler midtones`, ou `ARRI Alexa LogC highlight roll-off with rich shadow retention`. Negros foscos profundos sem lavagem. |
| **$V_7$** | **Acabamento Superficial & Tátil** | Vidro de borossilicato jateado fosco, titânio anodizado escurecido, cerâmica de zircônia escovada, borracha de silicone vulcanizada fosca com micro-relevo tátil. |
| **$V_8$** | **Invariante Negativo Rigoroso (Anti-AI Cliché)** | `no neon glowing circuits, no sci-fi floating holograms, no isometric 3D glowing nodes, no floating cubes, no cheesy AI art, no surreal glowing particles, no fake cybernetic lines, no illegible typography, no watermarks, realistic industrial studio photography only`. |

---

## 4. Banimento Absoluto de SVGs, Emojis e Glifos como Ícones: Micro-Renders Fotográficos

### A Proibição Inegociável:
- Proibido usar pacotes vetoriais SVG genéricos (Heroicons, Lucide simples), emojis do sistema e **glifos Unicode** (`↗`, `→`, `✹`, `·`, `—`, `❚❚`, `▶`, `GLYPH_MAP`) para fingir ícones de interface.
- Todo controle funcional deve utilizar **micro-imagens/renders fotorealistas dedicados** (gerados via `generate_image` com lente macro de 90mm, aspecto `1:1`, materiais físicos como vidro fosco refrativo, titânio escovado e obsidiana polida) ou **tipografia textual autêntica com design suíço**.

### Biblioteca Canônica de Prompts de Micro-Ativos Fotográficos (`AspectRatio: '1:1'`):

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

## 5. Protocolo de Vídeo Cinemático Real (Gemini + Local Poster Fallback)

1. **Banimento de Animação Sintética por Script:** Proibido interpolar imagens estáticas via scripts de pan/zoom (ffmpeg, canvas) para simular vídeos falsos.
2. **Prompt ao Usuário no Gemini:** Redigir o prompt cinemático ultra-detalhado em inglês (câmera contínua, lente anamórfica, iluminação volumétrica, resolução 4K, no text) e solicitar ao usuário que gere o arquivo `.mp4` no Gemini / Google AI Studio.
3. **Poster Local Imediato (Zero Black Screens):** Implementar o `<video src="..." poster="...">` com o atributo `poster` apontando para a imagem de alta resolução persistida no disco, garantindo acabamento estético perfeito desde o primeiro milissegundo de build.

---

## 6. Overlay de Grão Analógico em CSS Puro

```css
/* Inserido no body ou container raiz */
.film-grain-overlay {
  position: fixed;
  inset: 0;
  width: 100vw;
  height: 100vh;
  pointer-events: none;
  z-index: 9999;
  opacity: 0.035;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 512 512' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.8' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)'/%3E%3C/svg%3E");
}
```

---

## 7. Protocolo de Auditoria Perceptual Automatizada no Chrome Real via `browser-mcp`

### 7.1. Injeção de Telemetria de Runtime (CLS=0.000 / INP $\le$ 16ms / 120Hz)

Para eliminar a subjetividade na validação perceptual, o Subagente Auditor da Época IV injeta o script de profiling `perceptual_audit.js` no Chrome real através de `browser_execute_script`. O script monitora deterministicamente:
1. **Cumulative Layout Shift (CLS):** Exige $CLS = 0.000$.
2. **Interaction to Next Paint (INP):** Latência tátil sub-16ms ($INP \le 16\text{ ms}$).
3. **Estabilidade de Frame Rate (Frame Drops):** Amostragem contínua a 120Hz/60Hz durante interações táteis.
4. **Layout Thrashing & Long Tasks:** Verificação de Long Tasks e Long Animation Frames (LoAF).

### 7.2. Script Canônico de Telemetria de Renderização (`perceptual_audit.js`)

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

### 7.3. Matriz Forense de Veto Adversarial (Checklist Binário da Passada 4 do Gauntlet v5.0)

| Item Auditado | Critério Físico de Homologação [0 ou 1] | Condição de Reprovação Imediata (`[HARD REJECT]`) |
|---|---|---|
| **Física de Molas v5.0** | Todos os componentes interativos utilizam tokens de mola explícitos (`stiffness`, `damping`, `mass`) com $\zeta \in [0.72, 0.86]$ e $k/m < 57600$. | Presença de `transition: all` ou curvas Bézier puras em componentes interativos. |
| **Isolamento de GPU** | Animações afetam exclusivamente `transform` e `opacity` com `will-change` aplicado. | Animação de propriedades de reflow (`height`, `top`, `margin`, `padding`). |
| **Taxa de Quadros** | Telemetria de profiling acusa média estável ($\ge 60\text{ fps}$ ou $\ge 120\text{ fps}$ em monitores compatíveis) com 0 frame drops em repouso. | Mais de 2 quadros perdidos consecutivamente em animações de entrada/saída. |
| **Layout Shift (CLS)** | `report.cls.value === 0.000`. Elementos visuais não pulam ou mudam de dimensão após render. | Qualquer salto perceptível de elementos durante o carregamento de fontes ou imagens ($CLS > 0.000$). |
| **Latência Tátil (INP)** | `report.inp.maxLatencyMs <= 16ms`. Resposta visual sub-16ms. | Latência tátil $> 16\text{ms}$ em interações com botões ou modais. |
| **Fotografia Óptica Real** | Imagens exibidas foram geradas obedecendo à Fórmula de 8 Variáveis com lentes e sensores reais. | Presença de ilustrações pseudo-futuristas, neon azul, circuitos brilhantes ou SVGs genéricos. |
| **Controles Táteis Dedicados** | Botões de controle funcional exibem micro-renders fotográficos 1:1 usinados ou tipografia suíça. | Uso de caracteres Unicode (`▶`, `❚❚`, `→`, `✹`) ou ícones vetoriais genéricos. |
| **Higiene do Console** | `browser_console_logs` retorna array vazio para níveis `error` e `warn`. | Presença de qualquer exceção não tratada, warning de chave React ou asset 404. |

---

## Checklist Forense de UI Craft (Binário — Leis 21 & 41)
> Auditado pelo Red Team Juiz na Época IV via browser-mcp. Um único item fraudado dispara `[HARD REJECT: FRAUDULENT_CHECKLIST_SIGNOFF]`.

- [ ] **Física de Molas de 2ª Ordem 120Hz:** `framer-motion` com `motionTokensV5`, amortecimento sub-crítico ($\zeta \in [0.72, 0.86]$), $k/m < 57600$; zero `transition-all duration-300`.
- [ ] **Isolamento de Thread/GPU:** zero layout thrashing; animações restritas a `transform` e `opacity`; `will-change: transform` aplicado cirurgicamente.
- [ ] **Telemetria de Runtime CLS=0.000:** `report.cls.value === 0.000` comprovado via injeção de `perceptual_audit.js` no Chrome real.
- [ ] **Latência Tátil INP $\le$ 16ms:** resposta visual ao input em $\le 16\text{ms}$ (1 frame a 60fps / sub-frame a 120fps); zero atraso perceptível sob clique ou toque.
- [ ] **Fotografia Óptica Real (8 Variáveis):** `generate_image` com câmera (Hasselblad/Leica/Sony A7R), lente prime, abertura, iluminação três pontos, LUT cinematográfico, materialidade e negativo rigoroso; zero SVG genérico, emoji ou glifo Unicode como controle.
- [ ] **Micro-Renders Fotográficos de Controles:** botões funcionais utilizam micro-renders dedicados 1:1 usinados em obsidian/titânio ou tipografia suíça autêntica.
- [ ] **Banimento de Clichês de IA:** zero circuitos neon azul/ciano, hologramas flutuantes, cubos de energia ou ilustrações isométricas com texto ilegível.
- [ ] **Rubber-Banding & Gestos Diretos:** direct manipulation com rubber-banding real em listas/carrosséis; zero scroll snap estático.
- [ ] **120fps/60fps no Chrome Real:** zero dropped frames na gravação do DevTools Performance; verificado via `browser-mcp` screenshot e script de telemetria.
- [ ] **Zero Erros no Console:** zero warnings, zero 404s de assets, zero unhandled promise rejections; verificado via `browser_console_logs`.
