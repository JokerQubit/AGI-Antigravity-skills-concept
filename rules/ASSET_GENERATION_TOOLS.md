---
description: Universal Multimodal Asset & Data Generation Cheatsheet
trigger: always_on
---

# 🛠️ MULTIMODAL ASSET & DATA GENERATION CHEATSHEET

> **PROTOCOLO OBRIGATÓRIO:** Todo ativo, modelo ou dado deve ser gerado, prospectado ou consumido via ferramentas com rigor de engenharia. Proibido o uso de links externos quebrados, placeholders e primitivos sintéticos toscos.


## 🖼️ 1. ATIVOS VISUAIS 2D, ÍCONES & TEXTURAS PBR → Tool: `generate_image` (Nano Banana Engine)

> 🔴 **PROIBIÇÃO DE LINKS EXTERNOS QUEBRADOS & PLACEHOLDERS:**
> - Proibido usar links externos (Unsplash, Placeholder, Wikimedia, GitHub raw, etc.).
> - Proibido deixar tags `<img>` vazias, placeholders ou `// TODO`.
> - **MANDATÓRIO:** Todo elemento visual customizado DEVE ser gerado localmente via `generate_image` (Nano Banana Engine) ou incorporado como asset estruturado no repositório.

### A. Imagens 2D, Keyframes, Avatares e Banners (Fórmula Sênior Fotorealista)
- **Uso:** UI Hero Banners, Keyframes 2D, Avatares, Cards, Elementos de Composição.
- **🚫 PROIBIÇÕES ABSOLUTAS:** Proibido o uso de chavões artificiais (`"realistic, 8k, photorealistic, hyper detailed, unreal engine, octane render, masterpiece"`).
- **✅ FÓRMULA DE FOTOREALISMO SÊNIOR (6 PILARES ÓPTICOS):**
  $$\text{Prompt} = \text{Sensor/Óptica (Arri/Hasselblad)} + \text{Física de Materiais (Imperfeições)} + \text{Luz de Estúdio (Chiaroscuro 3200K)} + \text{Película (Kodak Vision3/Portra)} + \text{Composição/Negative Space}$$
- **Exemplo Master:**
  - `Prompt:` `"Editorial architectural photograph of the Louvre glass pyramid at night during a gentle Parisian rain, warm 3000K tungsten internal spotlighting illuminating the geometric lattice, water droplets creating refractive caustics on glass panels, wet dark granite courtyard reflecting warm light, cool atmospheric mist, shot on Arri Alexa 65 with 35mm Panavision Anamorphic lens, Kodak Vision3 500T color science, fine organic 35mm film grain, 16:9 widescreen, zero artificial glow."`
  - `ImageName:` "<snake_case_nome_max_3_palavras>"
  - `AspectRatio:` "16:9" | "1:1" | "9:16" | "4:3" | "3:4"
- **Workflow:** O artifact gerado vai para `brain/<conv-id>/`. Copie para `public/images/` (ou `assets/images/`) e referencie no HTML/CSS via caminho local relativo.

### B. Texturas PBR e Backgrounds Seamless
- **Uso:** Superfícies em 3D (Three.js/WebGL/Babylon) ou fundos em CSS.
- **Sintaxe de Prompt:**
  - `Prompt:` "flat top-down orthographic 90-degree view, seamless tileable <MATERIAL (e.g. honed porous travertine stone with micro-pitting / brushed dark titanium with directional machining marks)> texture, PBR albedo map, uniform diffuse studio lighting, zero perspective distortion, zero shadows, 35mm film scan quality"
  - `ImageName:` "texture_<material>"
  - `AspectRatio:` "1:1"

### C. Ícones 3D Customizados, Emblemas Isométricos & Alpha Isolation
- **Uso:** Ícones táteis de navegação, cards de features, emblemas de produtos e indicadores de métricas.
- **Sintaxe de Prompt:**
  - `Prompt:` "Minimalist 3D isometric emblem of a <ICON_CONCEPT>, sculpted in heavy frosted translucent optical glass with an internal glowing amber laser core, dark brushed titanium rim, isolated on pure solid white background, soft studio ground contact shadow, macro Hasselblad 100MP, ultra-crisp edges, 1:1 aspect ratio"
  - `ImageName:` "icon_<concept>"
  - `AspectRatio:` "1:1"
- **Processamento:** Isole a transparência do fundo via script Python de alpha thresholding (`extract_icon_alpha.py`) e aplique micro-interações táteis (3D tilt, magnetic pull, dynamic drop-shadow).

---

## 🧊 2. MODELOS 3D, CAD & ATIVOS ESPACIAIS → Prospecção Multimodal & Download

- **Uso:** Qualquer cena 3D, visualização científica, simulação, engenharia, CAD ou jogo. Proibido cubos/esferas rudimentares onde ativos de produção são esperados. Proibido download cego de modelo aleatório sem inspeção visual prévia.
- **Skill:** `skills/sketchfab-prospecting-protocol/SKILL.md`
- **Passo 1 (Catálogo Visual de Candidatos):** Chame subagent (`invoke_subagent` com `TypeName: "research"`, `Role: "3D Spatial Asset Researcher"`) ou utilize `search_web` / MCP tools para buscar modelos em repositórios abertos (Sketchfab, Poly Haven, NASA 3D, ambientCG) e extrair metadados/thumbnails de 3 a 5 candidatos.
- **Passo 2 (Avaliação de Topologia & PBR):** Avalie os candidatos quanto ao estilo estético, mapas PBR completos (Albedo, Normal, Roughness, Metalness) e orçamento poligonal ($< 50\text{k} - 100\text{k}$ polígonos para web/tempo real).
- **Passo 3 (Download & Normalização Métrica):** Baixe em formato `.glb`/`.gltf` para `public/models/`. Aplique obrigatoriamente a função de normalização de escala por Bounding Box (`THREE.Box3`) ajustando as dimensões para metros reais e centralizando o pivô na base.

---

## 🔮 3. ILUMINAÇÃO FOTORREALISTA, SHADERS PROCEDURAIS & PARALLAX MAPPING → Motor Omni Flash

- **Uso:** Iluminação IBL, Janelas com salas virtuais (Matrix Awakens), paisagens com profundidade (Depth Parallax), superfícies táteis (POM), Volumétricos e Raymarching.
- **Skill:** `skills/omni-multimodal-spatial-engine/SKILL.md`
- **Diretrizes Mandatórias de Renderização:**
  1. **Image-Based Lighting (IBL):** Obrigatório carregar HDRI (`RGBELoader`) para reflexos e iluminação ambiente física. Proibido iluminação direta crua sem environment map.
  2. **Tone Mapping:** `renderer.toneMapping = THREE.ACESFilmicToneMapping` com `toneMappingExposure = 1.0`.
  3. **Pós-processamento:** `EffectComposer` com `GTAOPass`/`SSAOPass` para sombras de contato e `UnrealBloomPass` sutil (strength: 0.15).
  4. **Interior Mapping (Estilo Matrix UE5):** Para janelas de edifícios e vitrines, usar shader de Ray-Box Intersection em Tangent Space (cômodos 3D virtuais com zero polígonos adicionais).
  5. **Depth-Map 2.5D Parallax:** Para vistas panorâmicas de janelas (montanhas, florestas, horizontes), usar Depth Map shader para que o fundo se mova dinamicamente com a câmera.

---

## 🎵 4. ÁUDIO REAL, TELEMETRIA ACÚSTICA & SINAL → Prospecção & Processamento

- **Uso:** Efeitos sonoros, ambientação, telemetria de áudio, sonificação de dados e sound design.
- **Classificação Dual Mandatória:**
  - **Micro-interações de UI / Feedback Háptico (< 50ms):** Permitido WebAudio API (`AudioContext`) para cliques mecânicos, beeps táteis de hover/press e feedback sonoro instantâneo de interface.
  - **Ambientação, SFX de Produção e Telemetria de Domínio:** Expressamente PROIBIDO o uso de osciladores sintéticos rudimentares. É MANDATÓRIO prospectar e extrair áudio autêntico do YouTube via `skills/youtube-audio-prospecting/SKILL.md`.
- **Skill:** `skills/youtube-audio-prospecting/SKILL.md`
- **Passo 1 (Pesquisa de Referência):** Utilize `search_web` ou subagent `research` para identificar fontes de áudio de alta fidelidade no YouTube e repositórios multimídia autênticos.
- **Passo 2 (Extração & Processamento):** Baixe e processe via `yt-dlp` / `ffmpeg` / `pydub` convertendo para formatos web (`.ogg` / `.mp3` / `.wav`).
- **Passo 3 (Integração):** Salve em `public/audio/` ou `assets/audio/` e integre no motor de áudio com controle de ganho, atenuação espacial e loop suave.

---

## 📡 5. DADOS OPERACIONAIS & STREAMS EM TEMPO REAL → Prospecção Tecnológica

- **Uso:** Backends, bots, dashboards analíticos, monitoramento, sistemas quantitativos ou científicos.
- **Skill:** `skills/technological-prospecting/SKILL.md`
- **Princípio:** Conexão direta a endpoints REST, WebSockets, gRPC, RPCs ou streams de telemetria reais com tratamento resiliente de desconexão e rate-limiting.

---

## 🎬 6. VÍDEO CINEMATOGRÁFICO & LOOPS ESPACIAIS → Gemini Omni & Veo Video Engine

- **Uso:** Hero video loops, vitrines animadas de produtos, backgrounds imersivos e texturas de vídeo para WebGL/Three.js. Proibido stock footage genérico ou vídeos com visual plástico/sintético.
- **Skill:** `skills/gemini-omni-video-generation/SKILL.md`
- **🚫 Termos Banidos:** `"ultra realistic, 8k, photorealistic, hyper detailed, unreal engine, octane render, masterpiece"`.
- **✅ Fórmula de Fotorealismo Sênior (Master Cinematography Codex):**
  $$\text{Prompt}_{\text{Veo}} = \text{Sensor/Lente (Arri Alexa 65 / Panavision 40mm)} + \text{Micro-Dinâmica Fluida} + \text{Física de Materiais} + \text{Luz (Chiaroscuro 3200K)} + \text{Película Kodak Vision3} + \text{Inércia Steadicam 24fps}$$
- **Workflow Web:** Geração obrigatória do poster frame de alta resolução via `generate_image` + Container HTML5 com `playsinline autoplay muted loop preload="metadata"` e camada óptica de vinheta em CSS Liquid Glass.

---

## ⚡ 7. MÍDIAS CINÉTICAS INTERATIVAS, SCROLLYTELLING & VÍDEO SCRUBBING → Motor Kinetic Web

- **Uso:** Sincronização de vídeo por rolagem (video scrubbing), capítulos editoriais de scrollytelling com sticky pin, parallax multicamada, revelação via `clip-path` expansivo e cards com 3D tilt por cursor.
- **Skill:** `skills/interactive-kinetic-media-engine/SKILL.md`
- **Diretrizes Mandatórias de Interatividade:**
  1. **Física de Interpolação Linear (Lerp):** Vídeos acionados por scroll e planos de parallax devem rodar dentro de um loop de `requestAnimationFrame` com amortecimento inercial ($\lambda \approx 0.075 - 0.1$). Proibido salto abrupto de frames.
  2. **Scrollytelling Sticky Viewport:** O container visual deve permanecer fixo (`position: sticky; top: 0; height: 100vh;`) enquanto a trilha narrativa vertical é percorrida pelo usuário.
  3. **Cursor Micro-Interactions:** Cards e elementos nobres devem responder ao cursor com perspectiva 3D (`perspective(1000px) rotateX(...) rotateY(...)`) e spotlight óptico translúcido.

