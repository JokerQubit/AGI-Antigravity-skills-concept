---
name: visual-synthesis-engine
description: MANDATORY. Use for any visual asset generation, web app design, frontend UI panels, CSS styling, glassmorphism components, graphics, HTML layouts, or AAA WebGL environments (Bloom, Fog, PBR).
---

# Visual Synthesis Engine — Design System Protocol

## Core Directive
When asked to create visual assets, graphics, banners, UI designs, or WebGL environments, you must follow a modern, premium design system. Avoid generic, plain, or cluttered visual designs. Always enforce clean minimalist principles, glassmorphism UI elements, dark mode aesthetics, and crisp contrast.

> [!IMPORTANT]
> **MANDATORY LOCAL ASSET GENERATION (NANO BANANA ENGINE / `generate_image`):**
> - You are **STRICTLY PROHIBITED** from using external image URLs (e.g., Unsplash, Placeholders, Wikimedia, CDN links) or skipping visual creation.
> - Whenever a project requires an image, illustration, avatar, card art, hero banner, icon, or texture, you **MUST** generate it locally using the `generate_image` tool (powered by the Nano Banana Engine).
> - Generating visual mockups during planning is forbidden; invoke `generate_image` during the *implementation phase* to produce real, usable assets.

## 1. AAA Graphics & WebGL Post-Processing (NEW MANDATE)
If developing a 3D environment or game (e.g., Three.js, React Three Fiber, WebGL):
- **ALWAYS Inject Realism by Default:** You are required to implement Post-Processing, Bloom (EffectComposer/UnrealBloomPass), Atmospheric Fog (`THREE.FogExp2`), and Soft Shadows.
- **PBR (Physically Based Rendering):** Always use `MeshStandardMaterial` or `MeshPhysicalMaterial` with appropriate roughness and metalness. Never use `MeshBasicMaterial` for final assets.
- **Lighting Rig:** Set up HDR environment maps (HDRI) or elaborate cinematic lighting rigs (Directional Light with cascaded shadows, Ambient Light, and colored Point Lights for rim lighting).

## 2. Design Aesthetics & Visual Guidelines (UI/Web)
- **Glassmorphism & Frosted Layers:** Utilize translucent cards, blurred backgrounds (`backdrop-filter`), subtle borders (`rgba(255,255,255,0.1)`), and soft ambient drop-shadows.
- **Color Palettes:** Curate sleek dark mode backgrounds (deep charcoal, midnight blue, slate) paired with glowing neon accents (cyan, magenta, electric purple, emerald).
- **Composition & Layout:** Maintain wide breathing room (whitespace), strong typographic hierarchy, and clear focal points. Never clutter the visual space.

## 3. Anti-Generic 5-Pillar Prompting Formula (`generate_image` / Nano Banana)

> 🔴 **BAN ON GENERIC BUZZWORDS:**
> Prohibited from writing empty generic prompts like `"cool spaceship, 8k, beautiful, realistic"`. 
> Generic prompts produce average, plastic, cliché results. You MUST engineer prompts across **5 concrete physical & optical pillars**:

```
[1. Micro-Detail Specificity] 
  + [2. Material & Surface Physics] 
  + [3. Cinematic Lighting & Optics] 
  + [4. Artistic Lineage / Direction] 
  + [5. Composition & Negative Space]
```

### The 5 Pillars of Non-Generic Visual Engineering:
1. **Pillar 1: Micro-Detail Specificity (Imperfections & Real-World Wear):**
   - Instead of "a robot", specify: *"Heavy bipedal industrial loader mech with exposed copper hydraulic lines, heat-discolored exhaust vents, scratched yellow hazard decals, and matte gunmetal chassis."*
2. **Pillar 2: Material & Surface Physics:**
   - Instead of "metal/glass", specify: *"Smoked frosted polycarbonate, weathered forged carbon fiber weave, brushed oxidized titanium with purple anodized edge wear, or damp porous basalt stone."*
3. **Pillar 3: Lighting Architecture & Optics:**
   - Specify real lighting setups: *"Volumetric god rays through dense particulate fog, harsh single directional key light with subtle electric-blue rim lighting, chiaroscuro contrast, anamorphic 35mm lens, shallow depth of field (f/1.4)."*
4. **Pillar 4: Artistic Lineage & Cinematic Aesthetics:**
   - Anchor the style: *"Syd Mead industrial concept art"*, *"Denis Villeneuve monumental sci-fi cinematography"*, *"Bauhaus minimalist functionalism"*, *"Moebius clean architectural line-art"*, *"Macro studio product photography on Hasselblad 100MP"*.
5. **Pillar 5: Composition & Negative Space Discipline:**
   - **For Icons / Avatares / Props:** *"Centered isolated subject, dramatic negative space, clean solid dark matte background, soft studio ground shadow, zero visual clutter."*
   - **For Seamless PBR Textures:** *"Flat top-down orthographic 90-degree view, seamless tileable pattern, uniform diffuse studio lighting, zero perspective distortion, zero shadows."*

### Comparison Matrix: Generic vs Bespoke AAA Prompts

| Asset Type | ❌ Generic / Cliché Prompt (Banned) | ✅ Bespoke AAA Non-Generic Prompt (Mandatory) |
|---|---|---|
| **Hero Background** | `"Dark space background, stars, nebula, 8k"` | `"Cinematic deep space vista, dense cosmic dust nebula with deep violet and obsidian tones, backlit by a distant blinding white dwarf star, subtle anamorphic lens streak, ultra-wide 16:9, Arri Alexa cinematography"` |
| **Seamless Texture** | `"Metal texture seamless"` | `"Orthographic top-down seamless texture of weathered industrial dark steel plates with recessed hexagonal bolts and subtle oil sheen, uniform diffuse lighting, tileable 1:1, PBR albedo map"` |
| **Logo / Icon** | `"Cyberpunk logo icon"` | `"Minimalist 3D isometric emblem of an optical quantum processor, frosted translucent glass with an internal glowing amber phosphor grid, soft studio rim lighting, isolated on solid pure black background, 1:1 square"` |
| **Character Avatar** | `"Cool cyber hacker portrait"` | `"Close-up editorial portrait of a cybernetic technician, subtle matte-black titanium facial augmentations with tiny fiber-optic indicator LEDs, dramatic side rim light, moody chiaroscuro shadow, 85mm portrait lens"` |


## 4. Asset Lifecycle & Repository Integration
- **Storage:** Immediately copy/move generated images from artifact directory to `public/images/` or `assets/` within the target project using native shell tools (`Copy-Item`).
- **No Dummy Placeholders:** Never use placeholder image URLs or text descriptions where an actual visual asset is requested. Autonomously generate isolated visual elements via `generate_image` (Nano Banana Engine).

## 5. MANDATORY Post-Render Visual Verification
After any visual asset is generated, CSS is written, or WebGL scene is composed, you MUST:
1. **Invoke `browser` subagent** (`invoke_subagent` tool with `TypeName: browser`) to capture a live screenshot of the rendered result in the running dev server.
2. **Run `view_file` on the screenshot `.png`** — reading text output is NOT sufficient.
3. **Emit a 3-Point Red Team critique** on the screenshot: identify at minimum 3 specific flaws (color contrast, font quality, missing depth/shadows, flat textures, broken layout).
4. **Fix the 3 flaws** before declaring the visual task complete.

**FORBIDDEN:** Claiming "the UI looks great" or "the scene renders correctly" based purely on reading your own code. Evidence must be a real screenshot inspected via `view_file`.

---

## 6. The Anti-AI-Look Protocol (De-Artificialization Manifesto)

### Part A: Eliminating the "AI Look" in Web & UI Design
1. **BANNED UI AI-Clichés:**
   - 🚫 No purple/violet gradients on generic dark backgrounds (`#0a0a0a` + neon purple).
   - 🚫 No floating pill badges with pulsing dots (`✨ AI Powered Platform`) right above headlines.
   - 🚫 No hollow grid-line overlays (`background-image: linear-gradient(...)` fake meshes).
   - 🚫 No generic bento boxes filled with unrelated icons and empty buzzwords ("Fast", "Secure").
   - 🚫 No generic AI copy ("Empower your workflow with cutting-edge intelligence").
2. **MANDATORY Human-Crafted Aesthetic Principles (Stripe / Linear / Teenage Engineering Tier):**
   - **Editorial & Restrained Color Palettes:** Warm charcoal (`hsl(220, 13%, 12%)`), deep slate, off-white typography (`#f3f4f6`), and exactly ONE high-impact accent color (e.g., industrial safety orange, emerald, or cadmium yellow).
   - **High-Density Typography:** Use premium font pairings (Inter Display, Syne, Geist, Neue Montreal, Instrument Serif) with tight negative tracking (`letter-spacing: -0.03em`) on large headings and strict line-height hierarchy.
   - **Subtle Layered Elevation:** Multi-stop subtle box shadows (`0 1px 2px rgba(0,0,0,0.1), 0 8px 24px rgba(0,0,0,0.2)`) and translucent hairline borders (`border: 1px solid rgba(255,255,255,0.08)`).
   - **Tactile Micro-Interactions:** Custom easing curves (`cubic-bezier(0.16, 1, 0.3, 1)`), hover magnetic feels, sound effects on key buttons, keyboard shortcuts (`⌘K`), and live real-world telemetry data.

### Part B: Eliminating the "AI Look" in Generated Images
1. **BANNED Image AI-Clichés:**
   - 🚫 No plastic waxy skin, no hyper-smooth reflective surfaces on everything.
   - 🚫 No generic "rainbow neon glow" without clear light sources.
   - 🚫 No centered objects floating in abstract bokeh vacuums.
2. **MANDATORY Analog & Film De-Artificialization Tokens:**
   - **Physical Imperfections:** Add `"35mm film grain, subtle analog color science (Kodak Portra 400), micro-scratches, dust particles, realistic surface patina, matte finish"`.
   - **Realistic Optics & Lenses:** Specify concrete focal lengths and lenses: `"Shot on Arri Alexa Mini LF, 50mm f/2.8 anamorphic lens, realistic depth of field (no fake blurry bokeh), subtle chromatic aberration at frame edges"`.
   - **Single-Source Directional Lighting:** Replace multi-colored ambient glows with `"Harsh single-source key light, natural shadows, soft atmospheric falloff, overcast daylight or chiaroscuro studio lighting"`.

---

## 7. Editorial Luxury & Isolated Object Synthesis Protocol (High-Design Benchmark)

### 1. Isolated 3D Objects & Props (Cutouts / Transparent PNGs)
When generating props, furniture, icons, or standalone products:
- **Prompt Formula:** `"Editorial studio product photograph of a <OBJECT (e.g. minimalist mid-century walnut lounge chair, brutalist concrete sculptural lamp, matte ceramic vase)>, isolated on pure solid white background [or pure chroma key green #00ff00], soft studio softbox overhead lighting, soft realistic contact ground shadow, neutral studio catalog, Hasselblad 100MP, ultra-crisp edges"`
- **AspectRatio:** `"1:1"` (Square) or `"3:4"` (Portrait).
- **Background Removal:** Use a fast Python PIL/OpenCV script in `scratch/remove_bg.py` (or thresholding on pure white/chroma) to output clean transparent `.png` files directly into `public/images/`.

### 2. Editorial Architectural Photography & Moodboards
To recreate the high-end architectural aesthetics (Mies van der Rohe, Architectural Digest, Kinfolk, Minimalist Warm Luxury):
- **Prompt Formula:** `"Architectural Digest editorial photograph of a <SCENE (e.g. minimalist glass and concrete pavilion nestled in a golden autumn forest / luxury twilight modern villa with warm timber slats and outdoor sunken lounge)>, warm natural sunlight streaming through tree canopy, cinematic composition, Kodak Portra 400 35mm film grain, Hasselblad medium format camera, earthy muted taupe and warm cedar color palette, ultra-high dynamic range"`
- **AspectRatio:** `"16:9"` (Hero/Wide Banners) or `"9:16"` (Editorial Vertical Layouts).

### 3. Multi-Image Editorial Layout Assembly (HTML/CSS + Google Fonts)
Never bake typography into the image. Deconstruct the layout into **code-based editorial grids**:
- **Typography Pairing (Luxury / High-End):**
  - Headings: `Cormorant Garamond` (Italic / Regular), `Cinzel`, `Playfair Display`, `Syne`, or `Instrument Serif`.
  - Body / Subheadings: `Inter`, `Geist`, `Plus Jakarta Sans`, `Neue Montreal`.
  - Heading CSS: `font-family: 'Cormorant Garamond', serif; letter-spacing: -0.02em; font-weight: 300; text-transform: uppercase;`
- **Glassmorphism Frosted Panels:**
  - `background: rgba(40, 32, 28, 0.35); backdrop-filter: blur(24px); -webkit-backdrop-filter: blur(24px); border: 1px solid rgba(255, 255, 255, 0.08);`
- **Grid Deconstruction:** Assemble multi-column moodboards (e.g., 3-column split with hero background, floating vertical glass panel, and isolated product thumbnails).

---

## 8. Liquid Glassmorphism & Luxury FinTech/Spa Blueprint (VisionOS Tier)

### 1. Liquid Frosted Pill Navbars & Sliders (VisionOS / macOS Tier)
```css
.liquid-glass-pill {
  display: flex;
  align-items: center;
  gap: 16px;
  padding: 8px 20px;
  border-radius: 9999px;
  background: linear-gradient(180deg, rgba(255, 255, 255, 0.14) 0%, rgba(255, 255, 255, 0.03) 100%);
  backdrop-filter: blur(32px) saturate(190%);
  -webkit-backdrop-filter: blur(32px) saturate(190%);
  border: 1px solid rgba(255, 255, 255, 0.16);
  box-shadow: 
    inset 0 1px 1px rgba(255, 255, 255, 0.4),
    inset 0 -1px 1px rgba(0, 0, 0, 0.3),
    0 16px 36px -8px rgba(0, 0, 0, 0.45);
  color: #f3f4f6;
  transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
}

.liquid-glass-pill:hover {
  background: linear-gradient(180deg, rgba(255, 255, 255, 0.22) 0%, rgba(255, 255, 255, 0.07) 100%);
  border-color: rgba(255, 255, 255, 0.25);
  transform: translateY(-1px);
}
```

### 2. Luxury Floating Glass Dashboards Over Architectural Landscapes
- **Fundo Arquitetural:** `generate_image` com `"Cinematic architectural photograph of a brutalist concrete villa perched on a coastal cliff above stormy ocean waves, overcast moody daylight, Kodak Portra 400 film grain, Arri Alexa cinematography, 16:9"`
- **Dashboard Flutuante:**
```css
.luxury-dashboard-panel {
  position: relative;
  background: rgba(14, 16, 20, 0.68);
  backdrop-filter: blur(48px) saturate(180%);
  -webkit-backdrop-filter: blur(48px) saturate(180%);
  border: 1px solid rgba(255, 255, 255, 0.12);
  border-radius: 24px;
  padding: 32px;
  box-shadow: 
    0 32px 64px -16px rgba(0, 0, 0, 0.6),
    inset 0 1px 1px rgba(255, 255, 255, 0.18);
}

.kanban-glass-card {
  background: rgba(255, 255, 255, 0.04);
  border: 1px solid rgba(255, 255, 255, 0.07);
  border-radius: 12px;
  padding: 16px;
  transition: background 0.2s ease, border-color 0.2s ease;
}

.kanban-glass-card:hover {
  background: rgba(255, 255, 255, 0.08);
  border-color: rgba(255, 255, 255, 0.15);
}
```

### 3. Luxury Spa & Editorial Wellness Layouts
- **Hero Image:** `generate_image` com `"Editorial luxury spa beauty photograph of a serene woman resting by dark water with glistening droplets on skin, warm golden side rim light, deep dark background, shallow depth of field, Vogue / Harper's Bazaar editorial, 35mm film grain, 16:9"`
- **Typography & Capsule CTA:**
```css
.spa-hero-title {
  font-family: 'Cormorant Garamond', serif;
  font-size: 3.5rem;
  font-weight: 300;
  color: #f7f3ee;
  line-height: 1.1;
}

.spa-hero-title em {
  font-style: italic;
  font-family: 'Playfair Display', serif;
}

.spa-capsule-btn {
  background: #C4A482;
  color: #1a1614;
  border-radius: 9999px;
  padding: 12px 28px;
  font-family: 'Inter', sans-serif;
  font-size: 0.85rem;
  font-weight: 600;
  letter-spacing: 0.05em;
  border: none;
  cursor: pointer;
  transition: transform 0.2s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.2s ease;
}

.spa-capsule-btn:hover {
  transform: scale(1.03);
  box-shadow: 0 8px 24px rgba(196, 164, 130, 0.35);
}
```

---

## 9. Creative Out-of-the-Box Interaction Patterns & Dynamic Structural Layouts

### 1. Interactive Product Hotspots (`.ui-hotspot-pin` — Lumora Pattern)
Place interactive glowing radar pins directly over rendered furniture/models to show tooltips on hover/click:
```css
.hotspot-pin {
  position: absolute;
  width: 22px;
  height: 22px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.9);
  border: 4px solid rgba(255, 255, 255, 0.3);
  box-shadow: 0 0 12px rgba(255, 255, 255, 0.8);
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: transform 0.2s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.2s ease;
}

.hotspot-pin::after {
  content: '';
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: #121212;
}

.hotspot-pin:hover {
  transform: scale(1.25);
  box-shadow: 0 0 20px rgba(255, 255, 255, 1);
}
```

### 2. Vertical Narrative Storytelling & Asymmetrical Grids (Deep Blue Pattern)
- **Continuous Depth Transition:** Layered dark gradients transitioning from light surface water (`#1a3a4b`) to deep abyss (`#05080c`).
- **Rotated Vertical Typography:**
```css
.vertical-editorial-label {
  writing-mode: vertical-rl;
  transform: rotate(180deg);
  font-family: 'Inter', sans-serif;
  font-size: 0.75rem;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: rgba(255, 255, 255, 0.4);
}
```

### 3. Monumental Surreal Hero with Magnetic Controls (Eosai Pattern)
- **Animated Scroll Indicator:**
```css
.scroll-indicator-line {
  width: 1px;
  height: 48px;
  background: linear-gradient(180deg, #d4af37 0%, transparent 100%);
  animation: scroll-pulse 2s infinite ease-in-out;
}

@keyframes scroll-pulse {
  0%, 100% { opacity: 0.3; transform: scaleY(0.6); }
  50% { opacity: 1; transform: scaleY(1); }
}
```
- **Circular Magnetic CTA:**
```css
.circular-cta-btn {
  display: inline-flex;
  align-items: center;
  gap: 12px;
  padding: 12px 24px;
  border-radius: 9999px;
  border: 1px solid rgba(255, 255, 255, 0.2);
  background: rgba(255, 255, 255, 0.05);
  backdrop-filter: blur(12px);
  color: #ffffff;
  font-size: 0.85rem;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  cursor: pointer;
  transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
}

.circular-cta-btn:hover {
  background: rgba(255, 255, 255, 0.15);
  border-color: rgba(255, 255, 255, 0.5);
  transform: translateX(4px);
}
```

### 4. Brutalist Bottom Metric Telemetry Bar (Fenêtre Pattern)
```css
.metric-telemetry-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 32px;
  border-top: 1px solid rgba(255, 255, 255, 0.15);
  padding-top: 24px;
}

.metric-item .metric-number {
  font-family: 'Neue Montreal', 'Inter', sans-serif;
  font-size: 2.5rem;
  font-weight: 400;
  color: #ffffff;
}

.metric-item .metric-caption {
  font-size: 0.8rem;
  color: rgba(255, 255, 255, 0.6);
  letter-spacing: 0.02em;
}
```





