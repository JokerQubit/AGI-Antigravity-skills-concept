---
trigger: model_decision
description: Layer 9 Multi-Modal Creative Synthesis, Matrix Reverse Protocol, and Cinema Optics
---
# Layer 9: Multi-Modal Creative Synthesis & Cinema Optics

Creative multi-modal production studio of OmniCognition Labs executing Matrix Reverse protocol: high-density Glassmorphism UI layouts, cinema-grade optical camera prompts, spatial acoustics, and AI video motion trajectories.

## 1. Multi-Modal Philosophy & Invariants
- Cinema-Grade Physicality Invariant: Emulate physical optical cameras, real-world lighting physics, material absorption acoustics, and industrial telemetry. Generic prompts ("futuristic 4k") are prohibited.
- Zero Device Frame Mandate: When generating UI layouts via `generate_image`, render strictly the UI canvas itself. Surrounding laptop frames, smartphone bezels, monitors, desks, and hands are strictly prohibited.

## 2. Department of Multi-Modal Synthesis (`matrix_reverse`)
Staff: `DIR-MAT-01` (Director), `DES-MAT-01` (UI/UX Architect), `OPT-MAT-02` (Cinematography Director), `AUD-MAT-03` (Spatial Acoustic Engineer).

## 3. UI/UX Glassmorphism & Industrial Dashboard Standards
Design Palette: Void Depth `#07080B`, Obsidian Canvas `#0B0D12`, Card Surface `rgba(18, 21, 30, 0.65)` with `backdrop-filter: blur(24px)`. Glass Border `1px solid rgba(255, 255, 255, 0.08)`. Accents: Cyan (`#00F0FF`), Purple (`#7000FF`), Amber (`#FFB800`), Emerald (`#00FFA3`).

```css
:root {
  --bg-void: #07080b; --bg-surface: rgba(18, 21, 30, 0.65);
  --border-glass: 1px solid rgba(255, 255, 255, 0.08); --border-glow: 1px solid rgba(0, 240, 255, 0.35);
  --backdrop-blur: blur(24px); --color-cyan: #00f0ff; --color-purple: #7000ff;
  --font-telemetry: 'JetBrains Mono', monospace; --font-executive: 'Inter', sans-serif;
}
```
Telemetry Grid: Tabular figures (`width: 8ch`, `font-variant-numeric: tabular-nums`). Microsecond Timestamps `HH:mm:ss.ffffff` in slate (`#64748B`). Scanline vignette overlays with `pointer-events: none`.

## 4. Cinema-Grade Optical Physics & Sensor Prompts
1. Sony Venice 2 8K:
   `"8K capture on Sony Venice 2 cinema camera, 36x24mm sensor, Cooke Anamorphic/i FF+ 40mm T2.3 lens, 1.8x squeeze, horizontal blue streak flares, specular highlights, ISO 3200 noise, volumetric mist in cyan light."`
2. Arri Alexa 65 Large Format:
   `"Master shot on ARRI ALEXA 65 with Hasselblad Prime DNA 65mm lens at T1.8, shallow depth of field, natural roll-off, soft halation around filaments, clean dynamic range, Kodak Vision3 texture."`

AI Video Dynamics: Physical camera trajectories ("Slow cinematic dolly-in with 15-degree orbital pan at 24fps"), explicit rack focus transitions.

Spatial Acoustic Modeling (Sabine Reverberation):
$$RT_{60} = \frac{0.161 \cdot V}{\sum_{i} S_i \alpha_i}$$
Coefficients: Concrete/Granite $\alpha = 0.02$, Panels $\alpha = 0.85$, Glass $\alpha = 0.04$. Sound delay $\Delta t = \frac{\text{Distance}}{343\,\text{m/s}}$.
Execution: `powershell -ExecutionPolicy Bypass -File .\scripts\generate_media_prompts.ps1 -VisualTheme "Cybernetic Boardroom" -Aspect "16:9"` -> `.state/matrix_reverse_latest.json`.

## 5. Layer 9 to Layer 10 Handshake Contract
- [ ] UI components satisfy Zero Device Frame mandate; optical prompts declare physical sensor, lens, $T$-stop, Kelvins.
- [ ] Monospace telemetry grid engineered with zero layout shift; spatial acoustics and speed-of-sound delays modeled.
- [ ] Manifest `.state/matrix_reverse_latest.json` verified BOM-free UTF-8; transaction `MATRIX_REVERSE_MEDIA_GEN` in ledger.
