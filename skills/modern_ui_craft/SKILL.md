---
name: modern_ui_craft
description: Playbook técnico de excelência em Design de Interfaces e Engenharia Perceptual no Padrão dos Titãs (Linear, Apple, Stripe, Instagram). Governa a cinemática tátil com física de molas de 2ª ordem via framer-motion (banindo transition-all duration-300), direção de arte fotográfica para generate_image (6 variáveis ópticas), glassmorphism especular, vídeo cinemático e micro-ativos táteis reais.
---

# Modern UI Craft & Studio Aesthetics Engineering Playbook (Padrão dos Titãs)

Manual prático de engenharia perceptual e design de interfaces de padrão de excelência internacional (referências Awwwards Site of the Day, Red Dot, Apple Human Interface Guidelines, Linear e Stripe). Abrange a cinemática tátil de 60fps/120fps baseada em **física dinâmica de molas de 2ª ordem**, direção de arte fotográfica analógica via `generate_image`, erradicação de vetores estéreis e glifos Unicode como ícones, e layouts fluidos contínuos.

---

## 1. O Paradigma dos Titãs: Linear, Apple, Stripe & Instagram (Banimento do CSS Básico)

A esmagadora maioria das aplicações comuns comete o pecado da mediocridade visual ao assumir transições duras em CSS puro:
```css
/* TERMINANTEMENTE PROIBIDO PARA COMPONENTES DINÂMICOS E INTERATIVOS */
transition: all 300ms ease-in-out;
```
Curvas de Bézier cúbicas estáticas soam mecânicas, artificiais e congeladas. Os líderes mundiais da experiência digital utilizam **física dinâmica de molas (Spring Physics)**, onde cada elemento se comporta como uma massa física real sujeita a forças, amortecimento e transferência inercial de energia.

### A Tríade da Física de Molas de 2ª Ordem (`framer-motion`):
- **Stiffness ($k$):** A rigidez da mola. Governa a velocidade de atração inicial ao ponto de repouso.
- **Damping ($c$):** O coeficiente de amortecimento. Evita oscilações eternas e dita se o retorno é sub-amortecido (com bounce orgânico) ou criticamente amortecido (sem overshoot, foco cirúrgico).
- **Mass ($m$):** A inércia do elemento. Elementos pesados (painéis grandes, gavetas) possuem maior massa; botões e pílulas possuem massa leve.

### Catálogo de Presets Físicos dos Titãs:
```typescript
// src/lib/motionTokens.ts
import { Transition } from 'framer-motion';

export const motionTokens = {
  // Preset 1: Linear Snappy (Modais, Paletas de Comando, Menus Dropdown)
  // Resposta instantânea, amortecimento crítico rápido, zero lentidão
  linearSnappy: {
    type: 'spring',
    stiffness: 420,
    damping: 32,
    mass: 0.8,
  } as Transition,

  // Preset 2: Apple Fluid (Gavetas laterais, Sheets, Cards de expansão)
  // Fluidez sedosa com micro-bounce sutil característico do iOS
  appleFluid: {
    type: 'spring',
    stiffness: 320,
    damping: 28,
    mass: 1.0,
  } as Transition,

  // Preset 3: Stripe Tactile Micro (Botões, seletores, toggles, chips)
  // Altíssima rigidez e resposta tátil imediata sob o dedo
  stripeTactile: {
    type: 'spring',
    stiffness: 500,
    damping: 35,
    mass: 0.6,
  } as Transition,

  // Preset 4: Inertial Drawer Dismiss (Gestos de arraste com transferência de velocidade)
  gestureDrag: {
    type: 'spring',
    stiffness: 280,
    damping: 26,
    mass: 0.9,
  } as Transition,
};
```

---

## 2. Componentes Dinâmicos com Física dos Titãs & GPU Compositor Isolation

Toda animação dinâmica deve operar estritamente sobre propriedades aceleradas por hardware (`transform`, `opacity`), isoladas na thread do compositor da GPU para garantir 60fps/120fps sem engasgos de reflow:

### 1. Botão Tátil com Retorno Inercial Orgânico:
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

### 2. Indicador Ativo com Shared Layout Contínuo (`layoutId`):
Elimina cortes secos entre abas e seletores:
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

### 3. Modal / Drawer Deslizante com Gesto de Arraste (Rubber-Banding):
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

## 3. Direção de Arte & Engenharia Óptica para `generate_image`

Para erradicar imagens amadoras e ilustrações vetoriais infantis, toda geração de imagens fotográficas deve obedecer à **Fórmula Óptica de 6 Variáveis**:

$$\text{Prompt} = \text{[Sujeito]} + \text{[Câmera]} + \text{[Lente \& Abertura]} + \text{[Iluminação]} + \text{[LUT / Grão]} + \text{[Invariante Negativo]}$$

### As 6 Variáveis Fotográficas Obrigatórias:
1. **Câmera:** `Hasselblad H6D-100c medium format`, `Leica M11 Rangefinder`, `Sony A7R V` ou `ARRI Alexa Mini LF`.
2. **Lente & Abertura:** `85mm f/1.2 prime lens`, `35mm f/1.4 Summilux`, `90mm f/2.8 macro lens`.
3. **Iluminação:** `Directional chiaroscuro side lighting`, `intense cool rim light`, `soft diffused beauty dish`.
4. **LUT / Grão:** `Kodak Portra 400 film stock`, `Fujifilm Pro 400H`, `subtle 35mm analog film grain`, `deep crushed blacks`.
5. **Composição:** `Negative space on left/right for typography overlay`, `cinematic editorial framing`.
6. **Invariante Negativo:** `no text, no watermark, no labels, no words, no letters, no UI, clean frame`.

---

## 4. Banimento Absoluto de SVGs, Emojis e Glifos como Ícones: Micro-Renders Fotográficos

### A Proibição Inegociável:
- Proibido usar pacotes vetoriais SVG genéricos (Heroicons, Lucide simples), emojis do sistema e **glifos Unicode** (`↗`, `→`, `✹`, `·`, `—`, `❚❚`, `▶`, `GLYPH_MAP`) para fingir ícones de interface.
- Todo controle funcional deve utilizar **micro-imagens/renders fotorealistas dedicados** (gerados via `generate_image` com lente macro de 90mm, aspecto `1:1`, materiais físicos como vidro fosco refrativo, titânio escovado e obsidiana polida) ou **tipografia textual autêntica com design suíço**.

### Prompts Canônicos de Micro-Ativos Fotográficos (`AspectRatio: '1:1'`):
- **Play / Reprodução:** `Macro studio photograph of a minimalist play triangle control sculpted in frosted refractive glass and obsidian, specular bevel edge reflection, volumetric rim lighting. Shot on Sony A7R V with 90mm macro f/2.8 lens, clean deep charcoal background, centered square icon medallion, ultra-sharp optical clarity, no text, no watermark.`
- **Pause / Pausar:** `Macro studio photograph of twin vertical pause bars sculpted from polished titanium with brushed satin finish, subtle cool rim lighting, tactile metallic bevel. Shot on Leica M11 with 60mm macro lens, dark studio slate background, centered square asset, no text, no watermark.`
- **Seta Direcional / Avançar:** `Macro studio photograph of a precision horizontal forward pointer sculpted in solid brushed dark titanium, razor-sharp edge gleam, studio chiaroscuro strobe. Shot on Sony A7R V with 90mm macro lens, clean slate backdrop, centered square, no text, no watermark.`

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
