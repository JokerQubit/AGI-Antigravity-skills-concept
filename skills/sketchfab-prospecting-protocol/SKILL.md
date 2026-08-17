---
name: sketchfab-prospecting-protocol
description: >-
  Universal protocol for autonomously researching, evaluating, visually inspecting via candidate catalogs, and integrating 3D models, CAD assets, scientific meshes, and spatial environments from Sketchfab and open 3D repositories. Use whenever a project requires 3D assets, meshes, props, or spatial data.
---

# Universal 3D & Spatial Asset Intelligence Protocol

This skill dictates the rigorous procedure for researching, evaluating, downloading, and integrating high-fidelity 3D models, CAD assets, and spatial meshes across open repositories (including Sketchfab, Poly Haven, NASA 3D, Free3D, ambientCG, and open CAD/mesh repositories).

## ⛔ HARD GATES (Execute BEFORE any 3D/Spatial Code)

### Gate 1: SCENE MESH & SPATIAL INVENTORY
**Before writing rendering or simulation code**, compile a complete inventory of every visible 3D mesh and spatial object needed (Characters, Vehicles, Buildings, Props, Terrain, Robotics URDF/Meshes, Scientific Geometries) with their real-world metric dimensions (height/width/depth in meters).

### Gate 2: ZERO BLIND DOWNLOADS (Visual Candidate Catalog Mandatory)
- **STRICTLY FORBIDDEN:** Grabbing uninspected models or downloading a random asset without prior visual triage.
- **STRICTLY FORBIDDEN:** Mixing mismatched art directions (e.g., hyper-realistic photogrammetry mesh alongside low-poly stylized assets).
- **MANDATORY:** Every 3D candidate **MUST BE VISUALLY INSPECTED** via thumbnail preview grid or screenshot comparison across at least 3 candidates before downloading.

---

## 🛠️ Universal 4-Step Prospecting & Vetting Pipeline

### Step 1: Multi-Source Search & Visual Candidate Catalog
Dispatch the `browser` subagent (`invoke_subagent` with `TypeName: browser`, `Role: 3D Spatial Asset Researcher`):
- **Search Sources:** 
  - Sketchfab API / Search: `https://sketchfab.com/search?q=<QUERY>&features=downloadable&type=models`
  - Open 3D / PBR Repositories (Poly Haven, NASA 3D, ambientCG, GitHub 3D repos).
- **Candidate Catalog Extraction:** Extract metadata and high-resolution thumbnail URLs for 3–5 candidate models:
  ```json
  [
    {
      "name": "Espresso Machine Commercial V2",
      "source": "Sketchfab",
      "uid": "abc123xyz",
      "thumbnailUrl": "https://media.sketchfab.com/models/abc123xyz/thumbnails/...",
      "polyCount": 42500,
      "materials": ["Albedo", "Normal", "Roughness", "Metallic", "AO"],
      "license": "CC-BY-4.0"
    }
  ]
  ```
- **Visual Inspection:** The agent must inspect candidate thumbnails to verify topology cleanliness, material fidelity, and stylistic cohesion with the scene.

### Step 2: Aesthetic, Scale & Topology Triage
Evaluate candidates against strict production criteria:
1. **Art Direction & Cohesion:** Match scene archetype (Luxury PBR, Industrial CAD, Architectural Brutalism, Photogrammetry, Cyberpunk).
2. **Topology & Vertex Budget:** Target $< 50\text{k} - 100\text{k}$ triangles for real-time WebGL/Three.js; optimize with LODs or mesh simplification if necessary.
3. **PBR Texture Health:** Confirm embedded PBR channels (Diffuse/Albedo, Normal Map, Roughness, Metalness). Reject models with unlit diffuse-only textures or blown-out baked lighting.
4. **License Verification:** Ensure appropriate open license (CC0, CC-BY, MIT, Apache 2.0).

### Step 3: Model Ingestion & Local Conversion
Once vetted:
- Download via Python script or direct API into standard binary formats (`.glb`, `.gltf`, `.obj`, `.stl`, `.step`).
- Place assets into `public/models/` or `assets/models/`.
- Verify the downloaded file is valid, non-empty, and loadable via standard parsers.

### Step 4: Metric Scale Normalization & Spatial Calibration
Never render imported GLB models without automated pivot centering and metric dimension bounding:

```javascript
import * as THREE from 'three';

/**
 * Normalizes an imported 3D model to real-world metric dimensions
 * @param {THREE.Object3D} modelScene - The root model object
 * @param {Object} options - Metric constraints
 * @param {number} options.targetDimension - Desired dimension (in meters)
 * @param {'height'|'width'|'depth'|'max'} options.axis - Axis to constrain
 */
export function normalizeModelScale(modelScene, { targetDimension = 1.0, axis = 'max' } = {}) {
  // Compute initial bounding box
  const box = new THREE.Box3().setFromObject(modelScene);
  const size = box.getSize(new THREE.Vector3());
  const center = box.getCenter(new THREE.Vector3());

  // Center pivot at bottom-center of the object (ideal for placement on floors/surfaces)
  modelScene.position.x -= center.x;
  modelScene.position.y -= box.min.y; // Bottom sits on ground plane (y = 0)
  modelScene.position.z -= center.z;

  // Calculate scale factor based on real-world metric targets
  let currentDim;
  if (axis === 'height') currentDim = size.y;
  else if (axis === 'width') currentDim = size.x;
  else if (axis === 'depth') currentDim = size.z;
  else currentDim = Math.max(size.x, size.y, size.z);

  if (currentDim > 0) {
    const scaleFactor = targetDimension / currentDim;
    modelScene.scale.setScalar(scaleFactor);
  }

  // Ensure shadows and PBR properties are applied across all child meshes
  modelScene.traverse((child) => {
    if (child.isMesh) {
      child.castShadow = true;
      child.receiveShadow = true;
      if (child.material) {
        child.material.envMapIntensity = 1.2;
        child.material.needsUpdate = true;
      }
    }
  });

  return modelScene;
}
```

#### Standard Real-World Metric Scale References:
| Object Category | Real-World Target Dimension | Constraint Axis |
|---|---|---|
| Espresso Machine / Kitchen Appliance | $0.45\text{m} - 0.60\text{m}$ | Height |
| Coffee Cup / Glass | $0.08\text{m} - 0.12\text{m}$ | Height |
| Bar / Counter Top | $0.90\text{m} - 1.05\text{m}$ | Height |
| Dining / Work Chair | $0.45\text{m}$ (seat) / $0.85\text{m}$ (back) | Height |
| Indoor Plant (Floor Pot) | $1.20\text{m} - 1.80\text{m}$ | Height |
| Ceiling Lamp / Pendant | $0.30\text{m} - 0.60\text{m}$ | Height |
| Room Ceiling Height | $2.80\text{m} - 3.50\text{m}$ | Height |

- **In-Scene Visual Telemetry:** Start dev server, capture live render screenshot via Puppeteer MCP (`puppeteer_screenshot(width: 1920, height: 1080)`), and run `view_file` on `.png` to verify lighting, scale, and material shaders.
