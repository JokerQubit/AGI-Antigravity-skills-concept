---
name: matrix_reverse
description: The Matrix Reverse Multi-Modal Production Skill. Activates when generating UI designs, visual layouts, sound integration plans, hyper-realistic image prompts (Sony Venice 8K), and AI video motion prompts for Gemini/Veo.
---

# The "Matrix Reverse" Multi-Modal Production Engine (`matrix_reverse`)

## 1. Executive Purpose
The **Matrix Reverse Skill** enforces modern, senior-grade multimedia production standards. It eliminates generic, low-effort defaults across four specialized multi-modal domains:
1. **Glassmorphism UI & Visual Design**: Dynamic fluid layouts, luminous translucent surfaces, and parallax depth planes.
2. **Acoustic Engineering (48kHz / 24-bit)**: Real-world acoustic recordings, precise sound manifests, and binaural spatial placement.
3. **Cinema-Grade Image Prompting**: Sony Venice 2 8K sensor profiles, master prime anamorphic optics, volumetric lighting, and DaVinci Resolve color science.
4. **AI Video Motion Control**: Kinetic camera motion prompting for Google Gemini / Veo (dolly, crane, pan, temporal coherence).

---

## 2. Operational Production Pillars

### Pillar 1: UI & Visual Design (Glassmorphism Standard)
- **User Reference Ingestion**: Ingest user reference images or mood boards prior to generating layouts to anchor visual tokens.
- **Glassmorphism Design Tokens**:
  - Surface blur: `backdrop-filter: blur(24px); -webkit-backdrop-filter: blur(24px);`
  - Background surface: semi-transparent white/dark base (`rgba(255, 255, 255, 0.08)` or `rgba(15, 23, 42, 0.65)`).
  - Luminous stroke: 1px continuous perimeter border (`rgba(255, 255, 255, 0.18)`).
  - Elevation & Depth: Multi-plane ambient drop shadows (`0 8px 32px 0 rgba(0, 0, 0, 0.37)`).
- **Dynamic Layout Architecture**: Fluid responsive CSS Grid / Flexbox layouts, parallax scroll depth planes, and smooth cubic-bezier transitions.

### Pillar 2: Acoustic Architecture & YouTube Ingestion (48kHz Standard)
- **Zero Synthetic Bleeps**: Pure synthesized robotic beeps and generic MIDI sounds are prohibited.
- **Real Acoustic Sourcing**: Prompt user for YouTube links to real-world acoustic sources (field recordings, mechanical switches, physical impacts).
- **Sound Manifest Specification**:
  - *Source URI*: YouTube URL or raw lossless audio capture pointer.
  - *Timestamp Segment*: Explicit start/end range (e.g., `00:42.100 - 00:44.850`).
  - *Acoustic Quality*: Uncompressed 48kHz / 24-bit PCM standard.
  - *Destination & Spatial Mapping*: UI micro-haptic feedback, environmental ambient bed, or binaural raytraced acoustic impulse response.

### Pillar 3: Cinema-Grade 8K Photorealism Prompt Authoring
- **Hardware & Sensor Specification**: Ultra-dense English-only prompts specifying *Sony Venice 2 8K*, *ARRI Alexa 35*, or *Hasselblad H6D-100c*.
- **Optics & Glass**: *Cooke Anamorphic/i Full Frame Plus 50mm T2.3*, *Zeiss Supreme Prime*, *1/4 Black Pro-Mist filter*, natural elliptical bokeh, shallow depth of field (f/1.8).
- **Lighting Dynamics**: Volumetric God rays, Rembrandt key illumination, sub-surface skin scattering, natural optical flares, zero plastic skin artifacts.
- **Micro-Texture & Color Science**: Micro-pores, natural fabric weave, organic dust motes, DaVinci Resolve 35mm film emulation (*Kodak Vision3 5219*), neutral contrast curve.
- **Vector Assets**: Minimalist 24px pixel-aligned SVG vector icons and sharp geometric SVG logos.

### Pillar 4: Google Gemini / Veo AI Video Motion Control
- **Dynamic Camera Kinematics**: Author motion-controlled prompts specifying camera velocity and direction:
  - *Tracking Dolly*: Slow forward tracking push-in at eye level, parallax separation between foreground and background.
  - *Crane Elevation*: Smooth mechanical crane rise from ground-level perspective to high-angle 45-degree vantage.
  - *Sweeping Arc/Pan*: Dynamic 60-degree rotational arc maintaining continuous focal lock on central subject.
- **Pacing & Lighting Coherence**: Strict temporal consistency across frames, continuous 60fps motion blur, and coherent atmospheric illumination.

---

## 3. Runbooks & Automation
- Glassmorphism Design System: [glassmorphism_ui_design_system.md](./references/glassmorphism_ui_design_system.md)
- Cinema Image Prompting Guide: [image_prompt_engineering_guide.md](./references/image_prompt_engineering_guide.md)
- Media Prompt Generator: [`scripts/generate_media_prompts.ps1`](../../scripts/generate_media_prompts.ps1)

