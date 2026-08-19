---
name: youtube-audio-prospecting
description: >-
  Universal protocol for researching, identifying, extracting, and synthesizing authentic audio assets, acoustic telemetry, and soundscapes from open multimedia sources (YouTube, Freesound, OpenAudio, NASA Audio). Use when a project requires real sound effects, ambient audio, telemetry sonification, or music.
---

# Universal Audio & Acoustic Intelligence Protocol

This skill outlines the process for researching, vetting, extracting, and integrating authentic audio assets, acoustic telemetry, and sound design into software systems, simulations, multimedia apps, and games.

## Workflow

### 1. Acoustic Reference Search & Grounding
- Determine the acoustic requirements (e.g., "Turbofan jet engine thrust harmonics", "Martian atmospheric wind recordings", "Relational database transaction chime", "Subtle UI tactile clicks").
- Use the `research` subagent (`invoke_subagent` with `TypeName: "research"`, `Role: "Acoustic Intelligence Researcher"`) or `search_web` to prospect authentic reference sources across open multimedia databases (YouTube, Freesound, OpenAudio, NASA Open Audio):
  ```json
  {
    "TypeName": "research",
    "Role": "Acoustic Intelligence Researcher",
    "Prompt": "AUDIO PROSPECTING: Pesquise vídeos autênticos de alta fidelidade no YouTube para [CONCEITO ACÚSTICO]. Extraia IDs e URLs para processamento via yt-dlp e ffmpeg."
  }
  ```

### 2. Multi-Source Extraction & Signal Processing
- Use Python scripts utilizing `yt-dlp`, `ffmpeg`, `pydub`, or `librosa` to extract and process the audio stream.
- Convert and optimize to web-compatible standards (`.ogg` for seamless looping, `.mp3` for compressed playback, `.wav` for uncompressed low-latency cues).
- Apply normalization, DC offset removal, and trim silence/noise if needed.

### 3. Anti-Synthetic Mandate (Authenticity First - Dual Classification)
- **Micro-interações de UI / Feedback Háptico (< 50ms):** Permitido WebAudio API (`AudioContext`) para cliques mecânicos instantâneos e beeps táteis.
- **Ambientação, SFX de Produção e Telemetria de Domínio:** Expressamente PROIBIDO o uso de osciladores sintéticos rudimentares. Todos os efeitos sonoros realistas, motores, vozes, música e ambientação DEVEM ser prospectados e extraídos de gravações autênticas via `yt-dlp` e `ffmpeg`.

### 4. Integration & Spatial Audio Rigging
- Place finalized audio assets into `public/audio/` or `assets/audio/`.
- Wire into the application's audio engine (e.g., HTML5 Audio, Web Audio API `AudioBufferSourceNode`, `THREE.AudioListener` with 3D positional panning and distance attenuation).

### 5. Verification & Telemetry
- Verify volume leveling, clean loop transitions (zero popping at loop boundaries), and correct spatial trigger responsiveness.

