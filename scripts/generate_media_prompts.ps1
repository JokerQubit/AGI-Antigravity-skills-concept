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

# 1. Cinema-Grade Image Prompt (Sony Venice 8K Standard)
$result.cinema_image_prompt = "Cinematic 8K wide architectural photograph of $Subject, shot on Sony Venice 2 8K Full-Frame cinema camera with Cooke Anamorphic/i Full Frame Plus 50mm T2.3 prime lens, Tiffen 1/4 Black Pro-Mist filter. Dramatic low-angle perspective, volumetric god rays streaming through floor-to-ceiling frosted glass panels, ambient dusk lighting with balanced teal and tungsten tones. Realistic surface micro-textures, subtle brushed titanium reflections, translucent glass refraction with 1px luminous edge highlights. 35mm Kodak Vision3 5219 film grain emulation, shallow depth of field with organic anamorphic oval bokeh, deep ambient occlusion, zero digital oversharpening, master DaVinci Resolve color grade."

# 2. Minimalist Logo / Icon Prompt
$result.logo_icon_prompt = "Modern minimalist vector logo representing $Subject, clean geometric silhouette, Golden Ratio proportions, monochrome dark charcoal on frosted translucent glass backdrop, extreme optical balance, negative space symmetry, high-end Swiss corporate aesthetic, scalable SVG vector quality, zero clutter, iconic prestige design."

# 3. Gemini / Veo AI Video Prompt
$result.gemini_video_prompt = "Smooth 4K 60fps cinematic tracking shot of $Subject. The camera performs a slow, continuous forward dolly-in through frosted glass architectural arches, gracefully tilting up 15 degrees. Volumetric atmospheric haze drifts across the frame as subtle amber and cyan rim lights illuminate geometric surfaces. Photorealistic reflections, seamless physics-based motion, zero temporal artifacts, cinematic aspect ratio 16:9."

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
