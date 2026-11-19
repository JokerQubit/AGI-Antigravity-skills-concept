---
name: modern_ui_craft
version: 6.0.0
description: "Use when building, styling, or refining UI components, web pages, layouts, animations, micro-interactions, dashboards, or generating product visuals. Enforces 120Hz/ProMotion 2nd-order spring physics (sub-critical damping 0.72-0.86, k/m < 57600) via framer-motion, GPU compositor isolation (transform/opacity), 8-variable optical photography prompts for generate_image, machined 1:1 control micro-renders instead of generic SVGs/Unicode glyphs, real poster-backed video, and CLS=0.000 / INP<=16ms runtime targets."
---

# Modern UI Craft & Perceptual Engineering — Hyper-Cortex v6.0

Playbook de engenharia perceptual e design de interfaces em padrão de excelência (referências Linear, Apple, Stripe, Teenage Engineering). Governa cinemática tátil de 120Hz/ProMotion baseada em **física dinâmica de molas de 2ª ordem com amortecimento sub-crítico ($\zeta \in [0.72, 0.86]$)**, isolamento na thread do compositor da GPU, direção fotográfica de 8 variáveis via `generate_image`, micro-renders táteis dedicados e metas objetivas de runtime (`CLS = 0.000`, `INP <= 16ms`).

> **Escopo Universal & Roteamento v6.0:** Aplicável a qualquer alteração visual, componente interativo, layout ou animação — sem distinção entre "ajuste rápido de CSS" e "redesign completo". Para verificação real no Chrome via `browser-mcp` e script `perceptual_audit.js`, acione `browser_visual_reasoning`; para feedback sonoro tátil, acione `tactile_audio_sfx`.
> - **Implementação Paralela de Componentes & Motion:** **Hydrogen 4 XHigh** (`gemini-4-hydrogen-xhigh`) ou **Hydrogen 4 High** (`gemini-4-hydrogen-high`)
> - **Arquitetura Visual Complexa & Auditoria Perceptual Final:** **Gemini 4 Neon High** (`gemini-4-neon-high`)

---

## 1. Cinemática dos Titãs: Física de Molas de 2ª Ordem (120Hz / ProMotion)

Transições estáticas em CSS genérico perdem conservação de momento quando interrompidas e geram sensação mecânica:
```css
/* PROIBIDO EM COMPONENTES DINÂMICOS E INTERATIVOS */
transition: all 300ms ease-in-out;
```

### 1.1. Modelagem Matemática do Oscilador Harmônico Amortecido

Todo movimento interativo segue a equação diferencial de 2ª ordem com massa $m$, rigidez $k$ e coeficiente de amortecimento viscoso $c$:

$$m \frac{d^2 x(t)}{dt^2} + c \frac{d x(t)}{dt} + k (x(t) - x_{\text{target}}) = 0$$

Frequência natural não-amortecida $\omega_0$ e razão de amortecimento $\zeta$ (*damping ratio*):

$$\omega_0 = \sqrt{\frac{k}{m}}, \quad \zeta = \frac{c}{2 \sqrt{k \cdot m}}$$

Para resposta tátil orgânica em gestos dinâmicos, opera-se em regime **sub-crítico calibrado**:

$$\zeta \in [0.72, 0.86]$$

Nesse regime, o *overshoot* permanece controlado entre $2.5\%$ e $5.8\%$, com tempo de estabilização $t_s \approx \frac{4}{\zeta \omega_0}$. A solução analítica com velocidade inicial de arraste $v_0$ é:

$$x(t) = x_{\text{target}} + e^{-\zeta \omega_0 t} \left[ (x_0 - x_{\text{target}}) \cos(\omega_d t) + \frac{v_0 + \zeta \omega_0 (x_0 - x_{\text{target}})}{\omega_d} \sin(\omega_d t) \right]$$

onde $\omega_d = \omega_0 \sqrt{1 - \zeta^2}$.

### 1.2. Estabilidade Numérica a 120Hz ($\Delta t = 8.33\text{ ms}$)

Em displays ProMotion de 120Hz ($\Delta t \approx 0.00833\text{ s}$), integradores discretos (Euler Simplético / Verlet do `framer-motion`) exigem o critério adaptado de Courant-Friedrichs-Lewy para evitar oscilação numérica parasita:

$$\Delta t < \frac{2}{\omega_0} \implies \omega_0 < \frac{2}{0.00833} \approx 240\text{ rad/s} \implies \frac{k}{m} < 57600$$

Com massa unitária $m = 1.0$, a rigidez $k$ não deve ultrapassar $2000$ em componentes interativos.

### 1.3. Exemplar Contrastivo de Cinemática Interativa

#### ❌ WRONG (Transição Estática & Reflow):
```css
.card {
  transition: all 0.3s ease-in-out;
}
.card:hover {
  transform: translateY(-4px);
}
```
**Autópsia:** (1) Perde momento angular/linear se o ponteiro sair antes de 300ms; (2) `ease-in-out` introduz atraso perceptível no início do gesto; (3) `transition: all` monitora propriedades de layout além de `transform`.

#### ✅ CORRECT (Mola de 2ª Ordem Isolada na GPU a 120Hz):
```tsx
<motion.div
  whileHover={{ y: -4, scale: 1.01 }}
  whileTap={{ scale: 0.98 }}
  transition={motionTokens.stripeTactile}
  style={{ willChange: 'transform' }}
>
```

### 1.4. Catálogo Canônico de Motion Tokens (`framer-motion`)

```typescript
// src/lib/motionTokens.ts
import { Transition } from 'framer-motion';

/**
 * Titan Motion Tokens — Hyper-Cortex v6.0
 * Calibrados para 120Hz/ProMotion com conservação de momento v0.
 */
export const motionTokens = {
  /**
   * 1. Linear Snappy (Paletas de comando, modais rápidos, tooltips)
   * k = 520, c = 38, m = 0.75 => omega_0 = 26.33 rad/s, zeta = 0.96
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
   * 2. Apple Fluid ProMotion (Sheets, gavetas de inspeção, cards expansíveis)
   * k = 380, c = 30, m = 0.9 => omega_0 = 20.54 rad/s, zeta = 0.81
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
   * 3. Stripe Tactile Micro (Botões, toggles, chips segmentados)
   * k = 680, c = 42, m = 0.55 => omega_0 = 35.16 rad/s, zeta = 0.86
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
   * 4. Kinetic RubberBand Dismiss (Gestos de arraste com desaceleração viscoelástica)
   * k = 260, c = 24, m = 1.1 => omega_0 = 15.37 rad/s, zeta = 0.71
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
   * 5. Shared Morph Dynamic (Transições layoutId entre estados)
   * k = 440, c = 34, m = 0.8 => omega_0 = 23.45 rad/s, zeta = 0.90
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

## 2. Componentes Dinâmicos & Isolamento de GPU Compositor

Toda animação interativa deve operar estritamente sobre propriedades aceleradas por hardware (`transform`, `opacity`), evitando mutações que disparem reflow (`width`, `height`, `top`, `margin`, `padding`):

### 2.1. Botão Tátil com Retorno Inercial
```tsx
import React from 'react';
import { motion } from 'framer-motion';
import { motionTokens } from '../lib/motionTokens';

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
      transition={motionTokens.stripeTactile}
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

### 2.2. Indicador Ativo com Shared Layout Contínuo (`layoutId`)
```tsx
import { motion } from 'framer-motion';
import { motionTokens } from '../lib/motionTokens';

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
        transition={motionTokens.linearSnappy}
        className="absolute inset-0 rounded-full border border-white/15 bg-white/10 shadow-[0_4px_20px_rgba(0,0,0,0.5)] backdrop-blur-md"
      />
    )}
    <span className="relative z-10">{label}</span>
  </button>
);
```

### 2.3. Drawer Deslizante com Gesto de Arraste (Rubber-Banding)
```tsx
import { AnimatePresence, motion } from 'framer-motion';
import { motionTokens } from '../lib/motionTokens';

interface DrawerProps {
  isOpen: boolean;
  onClose: () => void;
  children: React.ReactNode;
}

export const TitanDrawer: React.FC<DrawerProps> = ({ isOpen, onClose, children }) => (
  <AnimatePresence>
    {isOpen && (
      <>
        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          exit={{ opacity: 0 }}
          transition={{ duration: 0.2 }}
          onClick={onClose}
          className="fixed inset-0 z-40 bg-black/60 backdrop-blur-sm"
        />

        <motion.div
          initial={{ x: '100%' }}
          animate={{ x: 0 }}
          exit={{ x: '100%' }}
          transition={motionTokens.appleFluid}
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

## 3. Direção de Arte Fotográfica & Fórmula Óptica de 8 Variáveis (`generate_image`)

- **Proibido:** Circuitos neon azul/ciano genéricos, gráficos isométricos flutuantes com nós brilhantes, cubos holográficos, arte sci-fi clichê e texto ilegível gerado por IA.
- **Padrão Exigido:** Fotografia real de estúdio industrial / editorial de produto (Wallpaper*, Monocle, Apple, Stripe Press, Teenage Engineering).

Toda chamada a `generate_image` compõe o prompt obedecendo à **Fórmula Óptica de 8 Variáveis**:

$$\text{Prompt} = V_1 + V_2 + V_3 + V_4 + V_5 + V_6 + V_7 + V_8$$

| Variável | Nome | Especificação Técnica Mandatória |
|---|---|---|
| **$V_1$** | **Sujeito Tangível & Arquitetura Material** | Dispositivos físicos, consoles em alumínio CNC 6061-T6, módulos com botões mecânicos, estações de engenharia com cabos de silicone e displays com vidro nano-texture. |
| **$V_2$** | **Corpo de Câmera & Sensor Físico** | `Hasselblad H6D-100c medium format (53.4 x 40.0mm sensor)`, `Phase One IQ4 150MP`, `Leica M11-P with Summilux glass`, ou `Sony A7R V BSI sensor`. |
| **$V_3$** | **Lente Prime & Profundidade de Campo** | `50mm f/1.2 prime lens`, `85mm f/1.4 Otus`, `90mm f/2.8 Macro lens`, com queda de foco (*focus falloff*) e bokeh natural explícitos. |
| **$V_4$** | **Fisiologia de Iluminação & Fotometria** | Luz chave difusa via softbox 120cm a 45°, *rim light* rasante a 135° gerando reflexo especular em chanfros, e preenchimento 1:4 (3200K tungstênio vs 5600K daylight). |
| **$V_5$** | **Micro-Aberrações Ópticas Naturais** | Sutil aberração cromática lateral em alto contraste especular, micro-vinheta óptica de 0.3EV nos cantos, difração real nas bordas de abertura. |
| **$V_6$** | **Ciência de Cor & Perfis LUT** | `Kodak Vision3 500T 5219 color science`, `Fujifilm Pro 400H cooler midtones`, ou `ARRI Alexa LogC highlight roll-off with rich shadow retention`. |
| **$V_7$** | **Acabamento Superficial & Tátil** | Vidro borossilicato jateado fosco, titânio anodizado escurecido, cerâmica de zircônia escovada, silicone vulcanizado fosco com micro-relevo. |
| **$V_8$** | **Invariante Negativo Anti-Clichê** | `no neon glowing circuits, no sci-fi floating holograms, no isometric 3D glowing nodes, no floating cubes, no cheesy AI art, no surreal glowing particles, no fake cybernetic lines, no illegible typography, no watermarks, realistic industrial studio photography only`. |

---

## 4. Micro-Renders Fotográficos de Controles (Banimento de SVGs Genéricos & Glifos Unicode)

- Proibido usar emojis, glifos Unicode (`↗`, `→`, `✹`, `❚❚`, `▶`) ou pacotes vetoriais genéricos para controles táteis de assinatura da interface.
- Controles funcionais de destaque devem usar **micro-renders fotográficos dedicados 1:1** (gerados via `generate_image` com lente macro) ou **tipografia suíça autêntica**.

### Biblioteca Canônica de Micro-Ativos (`AspectRatio: '1:1'`)

- **Play Button:**
  ```text
  Macro industrial studio photograph of a minimal solid equilateral play triangle control sculpted in matte black obsidian with ultra-fine chamfered edge reflection, solitary key light at 45 degrees, subtle metallic sheen. Shot on Hasselblad H6D-100c with 90mm macro lens at f/4, clean charcoal studio backdrop, centered square asset, razor-sharp edge contrast, no text, no watermark, industrial design product photography.
  ```
- **Pause Button:**
  ```text
  Macro studio product photograph of dual parallel vertical control bars sculpted from brushed space-gray dark titanium, micro-beveled specular highlights on upper edges, soft diffused top softbox lighting. Shot on Leica M11 with 60mm macro lens at f/2.8, dark textured slate background, centered square icon medallion, tactile metallic feel, no text, no watermark.
  ```
- **Expand / Directional Arrow:**
  ```text
  Macro photograph of a precision engineered directional arrow glyph precision-milled from solid bead-blasted aluminum, razor-sharp perimeter chamfer reflecting studio rim lighting. Shot on Sony A7R V with 90mm f/2.8 macro lens, dark volcanic ash surface, perfectly centered 1:1 ratio, crisp optical clarity, tactile physical artifact, no text, no watermark.
  ```
- **Settings / Rotor Gear:**
  ```text
  Extreme macro photograph of an authentic miniature watchmaker gear rotor with knurled tactile teeth machined from brushed bronze and black ceramic, centered macro perspective with soft specular reflections on teeth crowns. Shot on Hasselblad H6D-100c at f/5.6, deep dark studio backdrop, 1:1 aspect ratio, high-end mechanical engineering artifact, no text, no watermark.
  ```

---

## 5. Protocolo de Vídeo Cinemático Real & Grão Analógico

1. **Zero Vídeo Sintético por Script:** Proibido simular vídeo via pan/zoom em imagens estáticas (ffmpeg/canvas).
2. **Geração Real + Poster Local:** Redija o prompt cinemático em inglês (câmera contínua, lente anamórfica, 4K, sem texto) para geração externa e aplique `<video src="..." poster="...">` apontando para uma imagem estática local de alta resolução (zero telas pretas no carregamento).
3. **Overlay de Grão Analógico em CSS Puro:**
```css
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

## 6. Telemetria de Runtime & Verificação via `browser_visual_reasoning`

Toda interface web construída com esta skill deve ser validada no Chrome real pelo verificador independente seguindo o protocolo e o script `perceptual_audit.js` definidos em `browser_visual_reasoning`:

| Métrica | Meta Obrigatória | Condição de Reprovação |
|---|---|---|
| **CLS** | `0.000` | Qualquer salto de layout durante carga de fontes/imagens |
| **INP** | `<= 16ms` | Latência tátil perceptível em cliques, hovers ou modais |
| **Frame Rate** | `120Hz / 60Hz` estável | `droppedFrames > 0` em repouso ou reflow por propriedades não-GPU |
| **Console & Rede** | `0` erros, `0` warnings, `0` 404 | Qualquer exceção, warning de hidratação ou asset ausente |

---

## 7. Checklist Forense de UI Craft (Binário)

- [ ] **Molas de 2ª Ordem 120Hz:** `framer-motion` com `motionTokens` ($\zeta \in [0.72, 0.86]$, $k/m < 57600$); zero `transition: all 300ms ease-in-out`.
- [ ] **Isolamento de GPU:** animações restritas a `transform` e `opacity` com `will-change: transform`.
- [ ] **CLS = 0.000 & INP <= 16ms:** comprovados em runtime via `perceptual_audit.js` (skill `browser_visual_reasoning`).
- [ ] **Fotografia de 8 Variáveis:** imagens geradas com câmera, lente prime, iluminação 3-pontos, LUT e negativo rigoroso; zero clichês neon/isométricos.
- [ ] **Controles Táteis Dedicados:** micro-renders 1:1 usinados ou tipografia suíça; zero glifos Unicode (`▶`, `❚❚`, `→`) ou emojis como ícones de UI.
- [ ] **Gestos & Rubber-Banding:** manipulação direta fluida em drawers/listas interativas.
- [ ] **Console Limpo no Chrome Real:** zero erros, zero warnings críticos e zero 404s via `browser_console_logs`.
