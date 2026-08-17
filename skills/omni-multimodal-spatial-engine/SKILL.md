---
name: omni-multimodal-spatial-engine
description: MANDATORY. Use for Multimodal Spatial Reasoning, procedural 3D math & GLSL shader generation, 3D bounding box projection, raymarching, Interior Mapping & Window Parallax shaders, audio-reactive visual synthesis, and high-frequency Flash swarm subagent execution.
---

# 🌐 Omni-Multimodal Spatial & Procedural 3D Engine

## Core Directive
The **Omni-Multimodal Spatial Engine** operationalizes native multimodal reasoning across text, code, audio, 2D visuals, and 3D spatial dimensions. It connects atomic asset generation (`generate_image` / Nano Banana), multi-source spatial/3D asset prospecting (`sketchfab-prospecting-protocol`), and acoustic intelligence (`youtube-audio-prospecting`) through high-performance procedural mathematics, GLSL/WGSL shaders, Matrix-tier Interior Parallax Mapping, 3D spatial coordinate calculations, and rapid subagent swarm execution.

---

## 1. Photorealistic 3D Foundation & Lighting Standards (Three.js / WebGL)

> 🔴 **PROHIBITION OF FLAT & UNCALIBRATED 3D LIGHTING:**
> - Strictly forbidden to use raw single `DirectionalLight` without Image-Based Lighting (IBL).
> - Strictly forbidden to use `MeshBasicMaterial` or flat zero-roughness materials with repetitive artificial bump maps.
> - **MANDATORY:** Every photorealistic 3D scene must configure IBL via HDRI (`.hdr` / `.exr`), `ACESFilmicToneMapping`, physical PBR materials (`MeshPhysicalMaterial`), and contact shadow ambient occlusion (SSAO/GTAO).

### Standard Production Setup (Scene & Renderer Rigging):
```javascript
import * as THREE from 'three';
import { RGBELoader } from 'three/examples/jsm/loaders/RGBELoader.js';
import { EffectComposer } from 'three/examples/jsm/postprocessing/EffectComposer.js';
import { RenderPass } from 'three/examples/jsm/postprocessing/RenderPass.js';
import { UnrealBloomPass } from 'three/examples/jsm/postprocessing/UnrealBloomPass.js';
import { GTAOPass } from 'three/examples/jsm/postprocessing/GTAOPass.js';

// 1. Configure High-Dynamic-Range Renderer
const renderer = new THREE.WebGLRenderer({ antialias: true, powerPreference: 'high-performance' });
renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
renderer.setSize(window.innerWidth, window.innerHeight);
renderer.toneMapping = THREE.ACESFilmicToneMapping;
renderer.toneMappingExposure = 1.0;
renderer.outputColorSpace = THREE.SRGBColorSpace;
renderer.shadowMap.enabled = true;
renderer.shadowMap.type = THREE.PCFSoftShadowMap;

// 2. Load Real Image-Based Lighting (IBL HDRI)
new RGBELoader().load('textures/studio_interior_1k.hdr', (texture) => {
  texture.mapping = THREE.EquirectangularReflectionMapping;
  scene.environment = texture;
  // Optional: scene.background = texture;
});

// 3. Post-Processing Pipeline for Film-Grade Cohesion
const composer = new EffectComposer(renderer);
composer.addPass(new RenderPass(scene, camera));

// Ambient Occlusion for realistic ground/crevice contact shadows
const gtaoPass = new GTAOPass(scene, camera, window.innerWidth, window.innerHeight);
gtaoPass.output = GTAOPass.OUTPUT.Default;
composer.addPass(gtaoPass);

// Subtle Optical Bloom (imperceptible threshold, soft diffusion)
const bloomPass = new UnrealBloomPass(
  new THREE.Vector2(window.innerWidth, window.innerHeight),
  0.15, // strength (keep subtle: 0.1 - 0.25)
  0.4,  // radius
  0.85  // threshold
);
composer.addPass(bloomPass);
```

---

## 2. Advanced Parallax & Interior Mapping Shaders (Matrix Awakens / UE5 Style)

When rendering building windows, shopfronts, or panoramic scenic vistas, **never use flat static images**. Implement real-time parallax shaders:

### A. Matrix-Style Window Interior Mapping (GLSL)
Renders fully perspective-correct 3D furnished rooms behind a 2D plane with **zero geometric vertices**:

```glsl
// Vertex Shader (Pass Tangent View Direction)
varying vec3 v_viewDirTangent;
varying vec2 v_uv;

attribute vec4 tangent;

void main() {
    v_uv = uv;
    vec3 normalW = normalize(mat3(modelMatrix) * normal);
    vec3 tangentW = normalize(mat3(modelMatrix) * tangent.xyz);
    vec3 bitangentW = normalize(cross(normalW, tangentW) * tangent.w);
    mat3 tbnMatrix = mat3(tangentW, bitangentW, normalW);

    vec3 worldPos = (modelMatrix * vec4(position, 1.0)).xyz;
    vec3 worldViewDir = normalize(worldPos - cameraPosition);
    v_viewDirTangent = worldViewDir * tbnMatrix; // Transform to tangent space

    gl_Position = projectionMatrix * viewMatrix * vec4(worldPos, 1.0);
}
```

```glsl
// Fragment Shader (Ray-Box Intersection inside Virtual Room Cube)
uniform samplerCube u_roomCubemap;
uniform vec3 u_roomDepthScale; // e.g. vec3(1.0, 1.0, 1.0)
varying vec3 v_viewDirTangent;
varying vec2 v_uv;

void main() {
    vec3 rayDir = normalize(v_viewDirTangent);
    
    // Scale UVs to room grid (e.g. 1 window = 1 room)
    vec2 roomUv = fract(v_uv);
    vec3 pos = vec3(roomUv * 2.0 - 1.0, 0.0); // Point on window pane in [-1, 1]

    // Compute intersection with unit box walls: x = +-1, y = +-1, z = -1 (back wall)
    vec3 invRay = 1.0 / rayDir;
    vec3 planes = (sign(rayDir) * u_roomDepthScale - pos) * invRay;
    
    // Nearest wall intersection in ray direction
    float dist = min(min(planes.x, planes.y), planes.z);
    vec3 hitPoint = pos + rayDir * dist;

    // Sample interior room cubemap at virtual hit location
    vec4 roomColor = textureCube(u_roomCubemap, hitPoint);
    
    // Add glass surface reflection
    float fresnel = pow(1.0 - abs(dot(vec3(0.0, 0.0, 1.0), -rayDir)), 3.0);
    vec3 glassTint = vec3(0.05, 0.08, 0.12);
    
    gl_FragColor = vec4(mix(roomColor.rgb, glassTint, fresnel * 0.4), 1.0);
}
```

### B. Depth-Map 2.5D Panoramic Parallax Shader (Window Scenic Vistas)
For mountain ranges, forests, or city horizons visible through panoramic windows:

```glsl
uniform sampler2D u_albedoTexture;
uniform sampler2D u_depthTexture; // Greyscale depth map: 1.0 = near, 0.0 = infinity
uniform vec2 u_cameraOffset;
uniform float u_parallaxIntensity;
varying vec2 v_uv;

void main() {
    float depth = texture2D(u_depthTexture, v_uv).r;
    vec2 offset = u_cameraOffset * (depth * u_parallaxIntensity);
    vec4 sceneColor = texture2D(u_albedoTexture, v_uv + offset);
    gl_FragColor = sceneColor;
}
```

### C. Parallax Occlusion Mapping (POM) for Tactile Surfaces
For physical displacement on floors (stone, travertine, weathered wood, cobblestone):
- Performs raymarching through heightmap layers in the fragment shader.
- Computes self-shadowing and depth displacement without increasing vertex counts.

---

## 3. Procedural Shaders & Spatial Raymarching

When scenes require dynamic, volumetric, or mathematical phenomena:

### A. Raymarching & Signed Distance Fields (SDF)
- Generate optimized fragment shaders (`THREE.ShaderMaterial` / WebGL2 / WebGPU) for mathematical surfaces, fractals, black holes, nebulas, volumetric clouds, and organic morphing geometries.
- Enforce analytical normal calculation $\mathbf{N} = \text{normalize}(\nabla f(\mathbf{p}))$ and sphere-tracing step bounds to maintain $60+$ FPS.

### B. Audio-Reactive Vertex & Fragment Modulations
- Couple Web Audio FFT analysis (Fast Fourier Transform frequency bins) directly to GLSL shader uniforms:
  - `u_time`: continuous frame delta.
  - `u_bass`, `u_mid`, `u_treble`: normalized spectral energy.
  - `u_resolution`: viewport dimensional vector.

---

## 4. Ultra-Fast Subagent Swarm Execution (`Model: "flash"`)

When deploying programmatic subagents via `invoke_subagent`:
- **Model Selection Strategy:**
  - `Model: "flash"`: Mandatory for high-frequency parallel subagents conducting live DOM auditing, visual screenshot verification, fast web scraping, and unit test execution.
  - `Model: "pro"` or `"inherit"`: Reserved for top-level architectural synthesis, master refactoring, and multi-branch Graph-of-Thought reasoning.
- **Latency Optimization:** Flash subagents process multi-file inspections and visual telemetry with sub-second token turnaround, enabling real-time feedback loops without stalling the orchestrator.

---

## 5. Unified Production Pipeline Integration

| Asset / Layer | Responsible Engine / Tool | Output Format |
|---|---|---|
| **Polygonal 3D Meshes & CAD** | Spatial Prospecting Subagent (`sketchfab-prospecting-protocol`) | `.glb` / `.gltf` / `.obj` with candidate catalog triage & metric scaling |
| **2D Art, UI & Seamless Textures** | Nano Banana Engine (`generate_image`) | `.png` 1:1 seamless tileable PBR maps |
| **Window & Vista Shaders** | Omni Spatial Shaders (`omni-multimodal-spatial-engine`) | GLSL Interior Mapping & Depth Parallax Shaders |
| **Acoustic Streams & SFX** | Acoustic Prospecting Subagent (`youtube-audio-prospecting` + `yt-dlp`) | `.mp3` / `.ogg` / `.wav` audio streams |
| **Lighting & Post-Processing** | Omni Multimodal Core (`omni-multimodal-spatial-engine`) | IBL HDRI + ACES Filmic + SSAO/Bloom Composer |
| **Scene Composition & UX** | Ultra-Loop Engine (`one-shot-ultra-loop-engine`) | Production application ($Q \ge 9.0$) |
