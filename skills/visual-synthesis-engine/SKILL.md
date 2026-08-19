---
name: visual-synthesis-engine
description: MANDATORY. Use for any visual asset generation, web app design, frontend UI panels, CSS styling, glassmorphism components, graphics, HTML layouts, or AAA WebGL environments (Bloom, Fog, PBR).
---

# Visual Synthesis Engine — Design System Protocol

## Core Directive
When asked to create visual assets, graphics, banners, UI designs, or WebGL environments, adapt the aesthetic to the exact domain, identity, and practical requirements of the project. **Never force a single aesthetic niche (such as luxury, dark-mode-only, or heavy glassmorphism) on every project.** A clean developer tool, high-density SaaS dashboard, playful educational app, robust industrial interface, or crisp light-mode publication each require distinct, purpose-driven design systems. Avoid generic, plain, or cluttered visual designs; always enforce clean hierarchy, intentional color theory, tactile micro-interactions, and crisp contrast.

> [!IMPORTANT]
> **MANDATORY LOCAL ASSET GENERATION (NANO BANANA ENGINE / `generate_image`):**
> - You are **STRICTLY PROHIBITED** from using external image URLs (e.g., Unsplash, Placeholders, Wikimedia, CDN links) or skipping visual creation.
> - Whenever a project requires an image, illustration, avatar, card art, hero banner, icon, or texture, you **MUST** generate it locally using the `generate_image` tool (powered by the Nano Banana Engine).
> - Generating visual mockups during planning is forbidden; invoke `generate_image` during the *implementation phase* to produce real, usable assets.

## 1. AAA Graphics & WebGL Post-Processing
If developing a 3D environment or game (e.g., Three.js, React Three Fiber, WebGL):
- **Realism & Spatial Depth:** Implement Post-Processing, subtle Bloom (EffectComposer/UnrealBloomPass), Atmospheric Fog (`THREE.FogExp2`), and Soft Shadows when appropriate for the scene's art direction.
- **PBR (Physically Based Rendering):** Always use `MeshStandardMaterial` or `MeshPhysicalMaterial` with appropriate roughness and metalness. Never use `MeshBasicMaterial` for final assets.
- **Lighting Rig:** Set up HDR environment maps (HDRI) or balanced cinematic/studio lighting rigs (Directional Key Light with cascaded shadows, Ambient Light, and colored Fill/Rim Lights).

## 2. Domain-Adaptive Aesthetics & Visual Guidelines (UI/Web)
Adapt the visual language to the project archetype:
- **Clean SaaS & Productivity (Light & Dark Mode):** Crisp functional borders (`1px solid #e2e8f0` / `rgba(255,255,255,0.08)`), multi-stop elevation shadows, high-legibility typography (`Inter`, `Geist`, `Plus Jakarta Sans`), disciplined whitespace, and purposeful accent colors.
- **Developer Tools & High-Density Telemetry:** Dark slate/charcoal or crisp light terminal backgrounds, monospace typography (`Geist Mono`, `JetBrains Mono`), compact grids, live telemetry badges, and high-contrast status indicators.
- **Modern Translucent Elevation (VisionOS / macOS Tier):** Subtle frosted glass cards (`backdrop-filter: blur(20px)`), refined hairline specular borders, and soft ambient drop-shadows.
- **Editorial & Content-Driven:** Generous editorial whitespace, sophisticated font pairing (e.g., `Syne` or `Instrument Serif` + `Inter`), asymmetric grids, and rich imagery.
- **Boutique & Luxury (When explicitly requested / brand-appropriate):** Deep espresso/charcoal or warm alabaster palettes, champagne/gold accents, serif typography (`Cormorant Garamond`, `Cinzel`, `Playfair Display`), and generous margins.

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
1. **Pillar 1: Micro-Detail Specificity (Imperfections & Real-World Context):**
   - Instead of "a robot", specify: *"Heavy bipedal industrial loader mech with exposed copper hydraulic lines, heat-discolored exhaust vents, scratched yellow hazard decals, and matte gunmetal chassis."*
2. **Pillar 2: Material & Surface Physics:**
   - Instead of "metal/glass", specify: *"Brushed anodized dark titanium with micro-machining marks, honed porous basalt stone, textured matte composite resin, or frosted borosilicate glass."*
3. **Pillar 3: Lighting Architecture & Optics:**
   - Specify real lighting setups: *"Soft directional 4500K studio softbox key light, subtle cool rim fill, realistic depth of field (f/2.8), anamorphic 35mm lens, natural optical falloff."*
4. **Pillar 4: Artistic Lineage & Domain-Appropriate Style:**
   - Anchor the style: *"Dieter Rams minimalist product design"*, *"Bauhaus functionalism"*, *"Syd Mead industrial concept art"*, *"Contemporary Swedish interior editorial"*, *"Macro studio hardware photography on Hasselblad 100MP"*.
5. **Pillar 5: Composition & Negative Space Discipline:**
   - **For Icons / Avatars / Props:** *"Centered isolated subject, dramatic negative space, clean solid neutral studio background, soft ground contact shadow, zero visual clutter."*
   - **For Seamless PBR Textures:** *"Flat top-down orthographic 90-degree view, seamless tileable pattern, uniform diffuse studio lighting, zero perspective distortion, zero shadows."*

### Comparison Matrix: Generic vs Bespoke Domain-Adapted Prompts

| Asset Type | ❌ Generic / Cliché Prompt (Banned) | ✅ Bespoke Non-Generic Prompt (Mandatory) |
|---|---|---|
| **Tech Hero Background** | `"Dark space background, stars, nebula, 8k"` | `"Cinematic high-angle view of a modern quantum computing datacenter with modular server racks, fiber-optic illuminated conduit lines, atmospheric cool mist, shot on Arri Alexa Mini LF, 35mm anamorphic lens, 16:9 widescreen"` |
| **Seamless Texture** | `"Metal texture seamless"` | `"Orthographic top-down seamless texture of weathered industrial dark steel plates with recessed hexagonal bolts and subtle oil sheen, uniform diffuse lighting, tileable 1:1, PBR albedo map"` |
| **Logo / 3D Icon** | `"Cyberpunk logo icon"` | `"Minimalist 3D isometric emblem of a biometric security shield, sculpted in matte obsidian polymer with a polished cobalt core, soft studio rim lighting, isolated on solid pure white background, 1:1 square"` |
| **Product / Prop Asset** | `"Cool gadget 3D"` | `"Studio product photograph of a handheld modular synthesizer, matte cream enclosure with CNC-milled aluminum knobs and monochrome OLED display, soft overhead softbox lighting, Hasselblad 100MP macro, isolated on solid neutral white"` |
| **Character / User Avatar** | `"Cool cyber hacker portrait"` | `"Close-up editorial portrait of a senior software engineer in a modern sunlit design studio, natural lighting, genuine expression, shallow depth of field, 85mm portrait lens, Kodak Portra 400 color science"` |

## 4. Asset Lifecycle & Repository Integration
- **Storage:** Immediately copy/move generated images from artifact directory to `public/images/` or `assets/` within the target project using native shell tools (`Copy-Item`).
- **No Dummy Placeholders:** Never use placeholder image URLs or text descriptions where an actual visual asset is requested. Autonomously generate isolated visual elements via `generate_image` (Nano Banana Engine).

## 5. MANDATORY Post-Render Visual Verification (Full HD 1920x1080)
After any visual asset is generated, CSS is written, or WebGL scene is composed, you MUST:
1. **Capture Live Full HD Screenshot:** Invoke Puppeteer MCP (`puppeteer_screenshot(width: 1920, height: 1080)`) to capture the rendered result in the running dev server (`localhost:<port>`).
2. **Run `view_file` on the screenshot `.png`** — reading text output is NOT sufficient.
3. **Emit a 3-Point Red Team critique** on the screenshot: identify at minimum 3 specific flaws (color contrast, font quality, missing depth/shadows, flat textures, broken layout).
4. **Fix the 3 flaws** before declaring the visual task complete.

**FORBIDDEN:** Claiming "the UI looks great" or "the scene renders correctly" based purely on reading your own code. Evidence must be a real screenshot inspected via `view_file`.

## 6. The Anti-AI-Look Protocol (De-Artificialization Manifesto)

### Part A: Eliminating the "AI Look" in Web & UI Design
1. **BANNED UI AI-Clichés:**
   - 🚫 No purple/violet gradients on generic dark backgrounds (`#0a0a0a` + neon purple) on every project.
   - 🚫 No floating pill badges with pulsing dots (`✨ AI Powered Platform`) right above headlines.
   - 🚫 No hollow grid-line overlays (`background-image: linear-gradient(...)` fake meshes).
   - 🚫 No generic bento boxes filled with unrelated icons and empty buzzwords ("Fast", "Secure").
   - 🚫 No generic AI copy ("Empower your workflow with cutting-edge intelligence").
2. **MANDATORY Human-Crafted Aesthetic Principles (Domain-Adapted Craft):**
   - **Restrained Color Palettes:** Curate deliberate palettes matching brand tone (e.g., crisp slate/zinc and electric blue for developer tooling; warm stone/charcoal and terracotta for editorial; clean alabaster/navy for enterprise).
   - **High-Density Typography:** Use premium font pairings (`Inter Display`, `Syne`, `Geist`, `Neue Montreal`, `Plus Jakarta Sans`, `Space Grotesk`) with tight negative tracking (`letter-spacing: -0.03em`) on large headings and strict line-height hierarchy.
   - **Subtle Layered Elevation:** Multi-stop subtle box shadows (`0 1px 2px rgba(0,0,0,0.06), 0 8px 24px rgba(0,0,0,0.12)`) and translucent hairline borders (`border: 1px solid rgba(0,0,0,0.08)` in light mode, `rgba(255,255,255,0.08)` in dark mode).
   - **Tactile Micro-Interactions:** Custom easing curves (`cubic-bezier(0.16, 1, 0.3, 1)`), hover feedback, sound effects on key interactions where appropriate, keyboard shortcuts (`⌘K`), and live real-world telemetry data.

### Part B: Eliminating the "AI Look" in Generated Images
1. **BANNED Image AI-Clichés:**
   - 🚫 No plastic waxy skin, no hyper-smooth reflective surfaces on everything.
   - 🚫 No generic "rainbow neon glow" without clear light sources.
   - 🚫 No centered objects floating in abstract bokeh vacuums.
2. **MANDATORY Analog & Optical De-Artificialization Tokens:**
   - **Physical Imperfections & Authentic Materials:** Add `"35mm film grain, subtle analog color science (Kodak Portra 400), micro-scratches, dust particles, realistic surface patina, matte finish"`.
   - **Realistic Optics & Lenses:** Specify concrete focal lengths and lenses: `"Shot on Arri Alexa Mini LF, 50mm f/2.8 anamorphic lens, realistic depth of field (no fake blurry bokeh), subtle chromatic aberration at frame edges"`.
   - **Purposeful Directional Lighting:** Replace multi-colored ambient glows with `"Directional studio softbox key light, natural shadows, soft atmospheric falloff, overcast daylight or chiaroscuro lighting"`.

## 7. Domain-Adaptive Visual Asset Synthesis & Isolated Object Protocol

### 1. Isolated 3D Objects & Props (Cutouts / Transparent PNGs)
When generating standalone props, hardware, tools, icons, or products:
- **Prompt Formula:** `"Studio product photograph of a <OBJECT (e.g. ergonomic wireless trackball in matte graphite resin / precision laboratory micropipette / mid-century walnut task stool)>, isolated on pure solid white background [or pure chroma green #00ff00], soft studio softbox overhead lighting, soft realistic contact ground shadow, neutral studio catalog, Hasselblad 100MP, ultra-crisp edges"`
- **AspectRatio:** `"1:1"` (Square) or `"3:4"` (Portrait).
- **Background Removal:** Use a fast Python PIL/OpenCV script in `scratch/remove_bg.py` (or thresholding on pure white/chroma) to output clean transparent `.png` files directly into `public/images/`.

### 2. Multi-Domain Hero Environments & Backgrounds
Tailor background generation to the project domain:
- **SaaS / Tech / Modern Workspace:** `"Architectural photograph of an open-plan modern industrial design studio, floor-to-ceiling windows with diffused morning light, minimalist standing desks with aluminum displays, indoor ficus plant, Kodak Portra 400 35mm film grain, 16:9"`
- **Hardware / Industrial / Engineering:** `"Cinematic photograph of a precision CNC milling machine working on an aerospace aluminum bracket, coolant fluid mist, crisp directional work light, shallow depth of field, 16:9"`
- **Editorial / Culture / Architecture:** `"Editorial architectural photograph of a minimalist concrete and timber pavilion surrounded by pines, overcast Nordic daylight, Hasselblad medium format, muted earthy palette, 16:9"`
- **Science / Biotech / Data:** `"High-resolution macro photograph of optical crystal lasers aligning on an optical breadboard, subtle chromatic refraction, clean dark scientific laboratory, 16:9"`

### 3. Typographic Pairings by Domain
Assemble code-based typography suited to context:
- **Modern SaaS & App UI:** Headings `Inter Display` / `Plus Jakarta Sans` | Body `Inter` / `Geist`
- **Developer Platforms & Data Dashboards:** Headings `Geist Sans` | Body `Inter` | Telemetry/Code `Geist Mono` / `JetBrains Mono`
- **Editorial & Culture:** Headings `Instrument Serif` / `Syne` / `Newsreader` | Body `Plus Jakarta Sans`
- **Boutique & Luxury (When appropriate):** Headings `Cormorant Garamond` / `Cinzel` | Body `Inter` / `Neue Montreal`

## 8. Adaptive UI Component Blueprints

### 1. Modern Translucent Navigation Pill (VisionOS / Clean UI Tier)
```css
.liquid-glass-pill {
  display: inline-flex;
  align-items: center;
  gap: 16px;
  padding: 8px 20px;
  border-radius: 9999px;
  background: rgba(255, 255, 255, 0.08);
  backdrop-filter: blur(24px) saturate(180%);
  -webkit-backdrop-filter: blur(24px) saturate(180%);
  border: 1px solid rgba(255, 255, 255, 0.12);
  box-shadow: 0 12px 28px -6px rgba(0, 0, 0, 0.25);
  color: #f3f4f6;
  transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
}

.liquid-glass-pill:hover {
  background: rgba(255, 255, 255, 0.14);
  border-color: rgba(255, 255, 255, 0.22);
  transform: translateY(-1px);
}
```

### 2. High-Density Dashboard / Kanban Panel (SaaS & Enterprise Tier)
```css
.dashboard-panel {
  position: relative;
  background: var(--surface-bg, #ffffff);
  border: 1px solid var(--surface-border, #e2e8f0);
  border-radius: 16px;
  padding: 24px;
  box-shadow: 0 4px 16px -2px rgba(0, 0, 0, 0.05);
}

/* Dark mode override */
@media (prefers-color-scheme: dark) {
  .dashboard-panel {
    background: #111827;
    border-color: rgba(255, 255, 255, 0.08);
    box-shadow: 0 16px 36px -8px rgba(0, 0, 0, 0.4);
  }
}

.kanban-task-card {
  background: var(--card-bg, #f8fafc);
  border: 1px solid var(--card-border, #e2e8f0);
  border-radius: 10px;
  padding: 14px;
  transition: transform 0.2s ease, border-color 0.2s ease, box-shadow 0.2s ease;
}

.kanban-task-card:hover {
  transform: translateY(-2px);
  border-color: var(--primary-accent, #3b82f6);
  box-shadow: 0 6px 16px -2px rgba(0, 0, 0, 0.08);
}
```

### 3. Clean Responsive CTA & Hero Actions
```css
.primary-action-btn {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  background: var(--primary-accent, #18181b);
  color: #ffffff;
  border-radius: 10px;
  padding: 10px 22px;
  font-family: var(--font-sans, 'Inter', sans-serif);
  font-size: 0.875rem;
  font-weight: 500;
  border: 1px solid transparent;
  cursor: pointer;
  transition: transform 0.2s cubic-bezier(0.16, 1, 0.3, 1), background 0.2s ease;
}

.primary-action-btn:hover {
  transform: translateY(-1px);
  background: var(--primary-accent-hover, #27272a);
}
```

## 9. Creative Out-of-the-Box Interaction Patterns & Dynamic Structural Layouts

### 1. Interactive Product Hotspots (`.ui-hotspot-pin`)
Place interactive glowing radar pins directly over rendered objects/models to show tooltips on hover/click:
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

### 2. Vertical Narrative Storytelling & Asymmetrical Grids
```css
.vertical-editorial-label {
  writing-mode: vertical-rl;
  transform: rotate(180deg);
  font-family: var(--font-sans, 'Inter', sans-serif);
  font-size: 0.75rem;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--muted-text, rgba(255, 255, 255, 0.4));
}
```

### 3. Monumental Hero with Magnetic Controls
```css
.scroll-indicator-line {
  width: 1px;
  height: 48px;
  background: linear-gradient(180deg, var(--accent-color, #3b82f6) 0%, transparent 100%);
  animation: scroll-pulse 2s infinite ease-in-out;
}

@keyframes scroll-pulse {
  0%, 100% { opacity: 0.3; transform: scaleY(0.6); }
  50% { opacity: 1; transform: scaleY(1); }
}

.circular-cta-btn {
  display: inline-flex;
  align-items: center;
  gap: 12px;
  padding: 12px 24px;
  border-radius: 9999px;
  border: 1px solid var(--border-color, rgba(255, 255, 255, 0.2));
  background: var(--btn-surface, rgba(255, 255, 255, 0.05));
  backdrop-filter: blur(12px);
  color: var(--text-color, #ffffff);
  font-size: 0.85rem;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  cursor: pointer;
  transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
}

.circular-cta-btn:hover {
  background: var(--btn-surface-hover, rgba(255, 255, 255, 0.15));
  border-color: var(--border-color-hover, rgba(255, 255, 255, 0.5));
  transform: translateX(4px);
}
```

### 4. Technical Telemetry & Metric Bar
```css
.metric-telemetry-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 32px;
  border-top: 1px solid var(--border-color, rgba(255, 255, 255, 0.15));
  padding-top: 24px;
}

.metric-item .metric-number {
  font-family: var(--font-display, 'Geist Sans', 'Neue Montreal', 'Inter', sans-serif);
  font-size: 2.5rem;
  font-weight: 400;
  color: var(--text-color, #ffffff);
}

.metric-item .metric-caption {
  font-size: 0.8rem;
  color: var(--muted-text, rgba(255, 255, 255, 0.6));
  letter-spacing: 0.02em;
}
```
