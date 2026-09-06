param(
    [string]$Subject = "Cybernetic Executive Headquarters",
    [string]$Category = "cinematic_scene", # options: cinematic_scene, icon_logo, video_prompt, audio_spec
    [string]$OutputFile = ""
)

$rootDir = Split-Path -Parent $PSScriptRoot
$stateDir = Join-Path $rootDir ".state"
$stateScript = Join-Path $PSScriptRoot "sync_state.ps1"

Write-Host "================================================================="
Write-Host "       MATRIX REVERSE MULTI-MODAL PROMPT & ASSET ENGINE"
Write-Host "================================================================="
Write-Host "Subject:     $Subject"
Write-Host "Category:    $Category`n"

$result = @{
    subject = $Subject
    timestamp = (Get-Date).ToString("yyyy-MM-ddTHH:mm:sszzz")
    category = $Category
}

# 1. Cinema-Grade Industrial Image Prompt (Sony Venice 8K Standard - Zero Text / Zero Human)
$result.cinema_image_prompt = "Ultra-wide 8K architectural photograph of an unmanned, monolithic research facility housing $Subject at twilight, shot on Sony Venice 2 8K Full-Frame cinema camera with Cooke Anamorphic/i Full Frame Plus 50mm T2.3 prime lens, Tiffen 1/4 Black Pro-Mist filter. Dramatic low-angle perspective, dark brushed titanium monoliths, liquid-cooled optical computing nodes, subtle amber and cool teal fiber-optic ribbons, natural glass caustics and physical reflections on polished concrete floor. Realistic surface micro-textures, CNC-machined dark anodized aluminum plates, authentic 35mm Kodak Vision3 5219 film grain emulation, shallow depth of field with organic anamorphic oval bokeh, deep ambient occlusion, master DaVinci Resolve color grade. Absolutely no text, no letters, no typography, no words, no signs, no human beings, no people, no characters, no faces, no suits."

# 2. Minimalist SVG Vector System (Pure Code Directive)
$result.logo_icon_prompt = "Pure semantic SVG vector asset representing $Subject. Authored in clean XML code: viewBox='0 0 24 24', fill='none', stroke='currentColor', stroke-width='1.5', stroke-linecap='round', stroke-linejoin='round'. Bold geometric silhouette, Golden Ratio symmetry, zero raster pixels, zero diffusion hallucination, enterprise-grade SVG design system standard."

# 3. Gemini / Veo AI Video Prompt (Unmanned Kinetic Camera Motion)
$result.gemini_video_prompt = "Smooth 4K 60fps cinematic tracking shot of an unmanned $Subject installation. The camera performs a slow, continuous forward dolly-in through frosted glass architectural arches, gracefully tilting up 15 degrees. Volumetric atmospheric haze drifts across the frame as subtle amber and cyan rim lights illuminate geometric CNC metal surfaces and fiber-optic conduits. Photorealistic reflections, seamless physics-based motion, zero temporal artifacts, cinematic aspect ratio 16:9. Absolutely no humans, no characters, no text, no logos."

# 4. Audio Ingestion Manifest (YouTube Sourcing Spec)
$result.audio_ingestion_manifest = @{
    required_asset = "$Subject soundscape & interaction audio"
    sourcing_instruction = "Prompt user for high-fidelity YouTube video/audio link demonstrating authentic mechanical or environmental acoustic behavior."
    target_duration = "00:03 - 00:08 (loopable ambient / 1.5s one-shot click)"
    bitrate_standard = "48kHz / 24-bit uncompressed WAV or 320kbps MP3"
    spatial_ui_placement = "UI hover micro-haptic feedback + 3D positional background soundscape"
}

# 5. Glassmorphism CSS Tokens
$result.glassmorphism_css = @"
.glass-panel {
  background: rgba(255, 255, 255, 0.08);
  backdrop-filter: blur(24px);
  -webkit-backdrop-filter: blur(24px);
  border: 1px solid rgba(255, 255, 255, 0.18);
  box-shadow: 0 12px 40px 0 rgba(0, 0, 0, 0.45);
  border-radius: 16px;
}
"@

Write-Host "[GENERATED PROMPTS UNDER MATRIX REVERSE STANDARDS]`n" -ForegroundColor Green
Write-Host "--- 1. SONY VENICE 8K IMAGE PROMPT (ENGLISH) ---" -ForegroundColor Cyan
Write-Host $result.cinema_image_prompt -ForegroundColor White

Write-Host "`n--- 2. MINIMALIST LOGO / ICON PROMPT ---" -ForegroundColor Cyan
Write-Host $result.logo_icon_prompt -ForegroundColor White

Write-Host "`n--- 3. GOOGLE GEMINI / VEO VIDEO PROMPT ---" -ForegroundColor Cyan
Write-Host $result.gemini_video_prompt -ForegroundColor White

Write-Host "`n--- 4. REAL AUDIO SOURCING MANIFEST ---" -ForegroundColor Cyan
Write-Host "Instruction: $($result.audio_ingestion_manifest.sourcing_instruction)" -ForegroundColor Yellow
Write-Host "Placement:   $($result.audio_ingestion_manifest.spatial_ui_placement)" -ForegroundColor White

$outFile = if ($OutputFile) { $OutputFile } else { Join-Path $stateDir "matrix_reverse_latest.json" }
$result | ConvertTo-Json -Depth 6 | Set-Content -Path $outFile -Encoding UTF8
Write-Host "`n[SAVED] Manifest recorded to: $outFile" -ForegroundColor Green

# Log to ledger
& powershell -ExecutionPolicy Bypass -File $stateScript -Action log-event -Initiator "Matrix Reverse Engine" -EventType "MATRIX_REVERSE_MEDIA_GEN" -Description "Generated cinema-grade media prompts and glassmorphic UI specifications for '$Subject'." | Out-Null
