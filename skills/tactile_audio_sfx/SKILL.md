---
name: tactile_audio_sfx
version: 6.0.0
description: "Use when adding sound effects, tactile click/hover/confirmation audio, Web Audio API managers, or spatial UI audio to any web app or game. Bans synthesized oscillator/math audio (OscillatorNode, Math.sin), mandates real acoustic Foley via scripts/sfx_tool.py (YouTube surgical slicing & Freesound CC0), differential EBU R128 LUFS normalization (-16 UI / -14 critical), SFM spectral anti-fraud verification, sub-5ms anti-click envelopes, 20Hz DC blocker, and 3D viewport HRTF PannerNode spatialization."
---

# Tactile Audio Engineering: Real Acoustic Foley & Spatial HRTF — Hyper-Cortex v6.0

Playbook para aquisição, processamento espectral e reprodução espacial de efeitos sonoros táteis capturados do mundo físico. Proíbe integralmente síntese matemática por script e impõe **Spatial Audio HRTF binaural com projeção cartesiana de viewport**, **normalização LUFS diferencial (-16 UI / -14 Crítico)**, **envelopes anti-click sub-5ms** e **verificação espectral via Spectral Flatness Measure (SFM)** com `scripts/sfx_tool.py`.

> **Escopo Universal & Roteamento v6.0:** Aplicável a qualquer adição de feedback sonoro — inclusive um único clique de botão. Para verificação final sem erros de console no Chrome real, acione `browser_visual_reasoning` e `forensic_adversarial_auditor`.
> - **Implementação de Assets & Manager TS:** **Hydrogen 4 High** (`gemini-4-hydrogen-high`) ou **Hydrogen 4 XHigh** (`gemini-4-hydrogen-xhigh`)
> - **Auditoria Acústica/Espectral & Console:** **Gemini 4 Neon High** (`gemini-4-neon-high`)

---

## 1. Diretriz Mandatória: Sons Físicos Reais & Banimento de Sintetizadores

- **Proibição Absoluta de Síntese:** É proibido gerar ruído branco/marrom, bipes ou ondas via `OscillatorNode`, `createOscillator`, `PeriodicWave` ou loops com `Math.sin`.
- **Fundamentação Acústica:** Materiais sólidos reais (madeira, titânio usinado, vidro, micro-switches mecânicos, obturadores analógicos) possuem dispersão desigual de energia por frequência ($Q(f)$ variável) e atrito de Coulomb microscópico. Ondas matemáticas puras carecem de amortecimento viscoelástico natural e causam fadiga auditiva.
- **Padrão Exigido:** Todo clique, transição ou confirmação tátil provém exclusivamente de gravações acústicas reais fatiadas e verificadas por `scripts/sfx_tool.py`.

---

## 2. Extração, Normalização & Verificação via `scripts/sfx_tool.py`

> O uso de `scripts/sfx_tool.py` é obrigatório na cadeia de produção de qualquer asset sonoro.

### Método A: Fatiamento Cirúrgico do YouTube (`slice-youtube`)
Captura trechos com precisão de milissegundos e normalização EBU R128 (`loudnorm`):
```bash
# Micro-feedback tátil de interface (-16 LUFS)
python scripts/sfx_tool.py slice-youtube "https://youtube.com/watch?v=..." --start "00:01.200" --end "00:01.600" --profile interface -o public/sfx/tactile_click.wav

# Confirmação crítica / transacional (-14 LUFS)
python scripts/sfx_tool.py slice-youtube "https://youtube.com/watch?v=..." --start "00:10.500" --end "00:11.200" --profile critical -o public/sfx/fiduciary_commit.wav
```

### Método B: Amostras Acústicas CC0 no Freesound
```bash
python scripts/sfx_tool.py search "mechanical switch click" --max-duration 1.0 --provider freesound
python scripts/sfx_tool.py download <SOUND_ID> --output public/sfx/click_real.wav
```

### Método C: Normalização LUFS Diferencial (`normalize-lufs`)
Aplica EBU R128 / ITU-R BS.1770-4 com envelope anti-click sub-5ms:
```bash
# Perfil 1: Interface (-16.0 LUFS, True Peak -1.5 dBTP, LRA 4.0 LU)
python scripts/sfx_tool.py normalize-lufs --input input_raw.wav --output public/sfx/button_click.wav --profile interface

# Perfil 2: Crítico (-14.0 LUFS, True Peak -1.0 dBTP, LRA 6.0 LU)
python scripts/sfx_tool.py normalize-lufs --input input_raw.wav --output public/sfx/deploy_success.wav --profile critical
```

### Método D: Verificação Espectral Anti-Fraude (`verify-acoustic`)
Calcula o *Spectral Flatness Measure* (SFM) via FFT para barrar áudio sintético:
$$\text{SFM} = \frac{\exp\left(\frac{1}{N} \sum_{k=0}^{N-1} \ln |X[k]|^2\right)}{\frac{1}{N} \sum_{k=0}^{N-1} |X[k]|^2}$$
- $\text{SFM} > 0.85$: Ruído branco sintético $\to$ **REJEIÇÃO**.
- $\text{SFM} < 0.001$: Tom senoidal puro / oscilador $\to$ **REJEIÇÃO**.
```bash
python scripts/sfx_tool.py verify-acoustic public/sfx/tactile_click.wav
```

### Método E: Varredura Local de Biblioteca (`scan-local`)
```bash
python scripts/sfx_tool.py scan-local --dir public/sfx/ --json
```

---

## 3. Arquitetura de Spatial Audio HRTF Binaural & Projeção Cartesiana

### 3.1. Projeção Cartesiana Normalizada de Viewport
Dado um elemento de interface $E$ com retângulo $\text{Rect}(E) = (x_{\text{min}}, y_{\text{min}}, w, h)$ em uma viewport $W \times H$:
$$c_x = x_{\text{min}} + \frac{w}{2}, \quad c_y = y_{\text{min}} + \frac{h}{2}$$
$$P_x = \frac{c_x - \frac{W}{2}}{\frac{W}{2}} \in [-1.0, 1.0], \quad P_y = -\left(\frac{c_y - \frac{H}{2}}{\frac{H}{2}}\right) \in [-1.0, 1.0], \quad P_z = -0.5$$

### 3.2. Configuração do Ouvinte (`AudioListener`)
Ouvinte posicionado na origem $(0, 0, 0)$, voltado para o plano da tela $(0, 0, -1)$ com vetor vertical $(0, 1, 0)$:
```typescript
const listener = ctx.listener;
if (listener.positionX) {
  listener.positionX.setValueAtTime(0, ctx.currentTime);
  listener.positionY.setValueAtTime(0, ctx.currentTime);
  listener.positionZ.setValueAtTime(0, ctx.currentTime);
  listener.forwardX.setValueAtTime(0, ctx.currentTime);
  listener.forwardY.setValueAtTime(0, ctx.currentTime);
  listener.forwardZ.setValueAtTime(-1, ctx.currentTime);
  listener.upX.setValueAtTime(0, ctx.currentTime);
  listener.upY.setValueAtTime(1, ctx.currentTime);
  listener.upZ.setValueAtTime(0, ctx.currentTime);
}
```

### 3.3. Parâmetros de Atenuação e Panorâmica HRTF
- **`panningModel`:** `'HRTF'` (modelagem binaural ITD/ILD)
- **`distanceModel`:** `'inverse'`
- **`refDistance`:** $1.0\text{ m}$
- **`maxDistance`:** $10.0\text{ m}$
- **`rolloffFactor`:** $0.8$

### 3.4. Envelope Anti-Click Sub-5ms & Filtro DC Blocker
- Rampa programada em `AudioParam`: $\tau_{\text{attack}} = 2.0\text{ms}$ ($\le 5\text{ms}$), $\tau_{\text{release}} = 3.0\text{ms}$ ($\le 5\text{ms}$).
- Filtro passa-altas Butterworth de 2ª ordem em linha ($20\text{ Hz}$, $Q = 0.7071$) para eliminar offsets DC subsônicos.

---

## 4. Integração no Frontend: `SpatialSoundManager` (TypeScript)

```typescript
// src/lib/spatialSoundManager.ts
/**
 * SpatialSoundManager — Hyper-Cortex v6.0
 * Real Acoustic Foley + 3D HRTF Spatial Audio Engine.
 * Proibição estrita de OscillatorNode e síntese procedural.
 */

export interface SpatialAudioOptions {
  element?: HTMLElement | null;
  coords?: { x: number; y: number };
  volume?: number;                     // 0.0 a 1.0 (default: 0.3 UI / 0.6 critical)
  category?: 'interface' | 'critical'; // -16 LUFS vs -14 LUFS
}

export class SpatialSoundManager {
  private static instance: SpatialSoundManager;
  private ctx: AudioContext | null = null;
  private buffers: Map<string, AudioBuffer> = new Map();
  private dcBlocker: BiquadFilterNode | null = null;
  private masterGain: GainNode | null = null;
  private isMuted: boolean = false;

  private constructor() {}

  public static getInstance(): SpatialSoundManager {
    if (!SpatialSoundManager.instance) {
      SpatialSoundManager.instance = new SpatialSoundManager();
    }
    return SpatialSoundManager.instance;
  }

  private initContext(): void {
    if (typeof window === 'undefined') return;

    if (!this.ctx) {
      const AudioCtx =
        window.AudioContext ||
        (window as unknown as { webkitAudioContext: typeof AudioContext }).webkitAudioContext;
      if (AudioCtx) {
        this.ctx = new AudioCtx({ latencyHint: 'interactive' });
      }
    }

    if (this.ctx && !this.masterGain) {
      this.masterGain = this.ctx.createGain();
      this.masterGain.gain.setValueAtTime(this.isMuted ? 0 : 1.0, this.ctx.currentTime);

      // DC Blocker Butterworth 20Hz
      this.dcBlocker = this.ctx.createBiquadFilter();
      this.dcBlocker.type = 'highpass';
      this.dcBlocker.frequency.setValueAtTime(20, this.ctx.currentTime);
      this.dcBlocker.Q.setValueAtTime(0.7071, this.ctx.currentTime);

      this.dcBlocker.connect(this.masterGain);
      this.masterGain.connect(this.ctx.destination);

      const listener = this.ctx.listener;
      if (listener.positionX) {
        listener.positionX.setValueAtTime(0, this.ctx.currentTime);
        listener.positionY.setValueAtTime(0, this.ctx.currentTime);
        listener.positionZ.setValueAtTime(0, this.ctx.currentTime);
        listener.forwardX.setValueAtTime(0, this.ctx.currentTime);
        listener.forwardY.setValueAtTime(0, this.ctx.currentTime);
        listener.forwardZ.setValueAtTime(-1, this.ctx.currentTime);
        listener.upX.setValueAtTime(0, this.ctx.currentTime);
        listener.upY.setValueAtTime(1, this.ctx.currentTime);
        listener.upZ.setValueAtTime(0, this.ctx.currentTime);
      }
    }

    if (this.ctx && this.ctx.state === 'suspended') {
      this.ctx.resume().catch(() => {});
    }
  }

  public async preload(name: string, url: string): Promise<void> {
    if (typeof window === 'undefined' || this.buffers.has(name)) return;
    try {
      this.initContext();
      if (!this.ctx) return;
      const res = await fetch(url);
      if (!res.ok) return;
      const arrayBuffer = await res.arrayBuffer();
      const audioBuffer = await this.ctx.decodeAudioData(arrayBuffer);
      this.buffers.set(name, audioBuffer);
    } catch {
      // Fallback gracioso: falha de áudio nunca bloqueia a UI
    }
  }

  public play(name: string, options: SpatialAudioOptions = {}): void {
    if (this.isMuted) return;
    this.initContext();
    if (!this.ctx || !this.dcBlocker) return;

    const buffer = this.buffers.get(name);
    if (!buffer) return;

    try {
      const now = this.ctx.currentTime;
      const source = this.ctx.createBufferSource();
      source.buffer = buffer;

      // 1. Envelope Dinâmico Anti-Click Sub-5ms
      const gainNode = this.ctx.createGain();
      const baseVol =
        options.volume !== undefined ? options.volume : options.category === 'critical' ? 0.6 : 0.3;
      const targetGain = Math.max(0.0001, Math.min(1.0, baseVol));
      const attack = 0.002; // 2ms
      const release = 0.003; // 3ms
      const duration = buffer.duration;

      gainNode.gain.setValueAtTime(0.0001, now);
      gainNode.gain.exponentialRampToValueAtTime(targetGain, now + attack);
      const sustainEnd = Math.max(now + attack, now + duration - release);
      gainNode.gain.setValueAtTime(targetGain, sustainEnd);
      gainNode.gain.exponentialRampToValueAtTime(0.0001, now + duration);

      // 2. Projeção Cartesiana & Nó HRTF
      let posX = 0;
      let posY = 0;
      const winW = window.innerWidth || 1920;
      const winH = window.innerHeight || 1080;

      if (options.element) {
        const rect = options.element.getBoundingClientRect();
        const cx = rect.left + rect.width / 2;
        const cy = rect.top + rect.height / 2;
        posX = (cx - winW / 2) / (winW / 2);
        posY = -((cy - winH / 2) / (winH / 2));
      } else if (options.coords) {
        posX = (options.coords.x - winW / 2) / (winW / 2);
        posY = -((options.coords.y - winH / 2) / (winH / 2));
      }

      const panner = this.ctx.createPanner();
      panner.panningModel = 'HRTF';
      panner.distanceModel = 'inverse';
      panner.refDistance = 1.0;
      panner.maxDistance = 10.0;
      panner.rolloffFactor = 0.8;
      panner.coneInnerAngle = 360;

      if (panner.positionX) {
        panner.positionX.setValueAtTime(Math.max(-1.0, Math.min(1.0, posX)), now);
        panner.positionY.setValueAtTime(Math.max(-1.0, Math.min(1.0, posY)), now);
        panner.positionZ.setValueAtTime(-0.5, now);
      }

      source.connect(gainNode);
      gainNode.connect(panner);
      panner.connect(this.dcBlocker);

      source.start(now);
    } catch {
      // Falha graciosa sem interromper o ciclo de renderização
    }
  }

  public toggleMute(): boolean {
    this.isMuted = !this.isMuted;
    if (this.masterGain && this.ctx) {
      this.masterGain.gain.setValueAtTime(this.isMuted ? 0 : 1.0, this.ctx.currentTime);
    }
    return this.isMuted;
  }
}

export const spatialSfx = SpatialSoundManager.getInstance();
```

---

## 5. Regras de Convivência Acústica

1. **Latência Sub-16ms:** Decodifique todas as amostras em `AudioBuffer` previamente (nunca instanciar `new Audio()` no evento de clique).
2. **Volume Sutil:** Feedback tátil de UI em `0.2`–`0.4` para evitar fadiga sensorial.
3. **Respeito ao Mute Global:** Toggle acessível silencia o `masterGain` imediatamente.
4. **Desbloqueio no Primeiro Gesto:** Inicialize/retome o `AudioContext` na primeira interação do usuário.
5. **Fallback Silencioso:** Políticas de autoplay ou falhas de rede não podem gerar exceções nem erros no console.

---

## 6. Checklist Forense de Áudio Acústico Real (10 Critérios Binários)

- [ ] **Origem Física Autêntica:** Todo asset vem de `scripts/sfx_tool.py slice-youtube` ou Freesound CC0 verificado com `verify-acoustic` ($0.001 \le \text{SFM} \le 0.85$).
- [ ] **Zero Síntese por Código:** 0 ocorrências de `OscillatorNode`, `createOscillator`, `PeriodicWave` ou `Math.sin(` em buffers de áudio no repositório.
- [ ] **Normalização UI (-16 LUFS):** Micro-interações em $-16.0\text{ LUFS} \pm 0.5$ e True Peak $\le -1.5\text{ dBTP}$.
- [ ] **Normalização Crítica (-14 LUFS):** Confirmações críticas em $-14.0\text{ LUFS} \pm 0.5$ e True Peak $\le -1.0\text{ dBTP}$.
- [ ] **Envelope Sub-5ms:** Ataque $\le 2\text{ms}$ e release $\le 3\text{ms}$ sem estalidos.
- [ ] **DC Blocker em Linha:** Filtro passa-altas Butterworth 20Hz antes do destino.
- [ ] **Espacialização HRTF:** Coordenadas normalizadas mapeadas em `PannerNode` com `panningModel = 'HRTF'`.
- [ ] **Buffer Pré-Decodificado:** `AudioBuffer` carregado em memória antes do clique (latência sub-16ms).
- [ ] **Mute Global Efetivo:** Toggle silencia todos os canais instantaneamente.
- [ ] **Console Limpo:** Zero uncaught promises ou erros DevTools em `browser_console_logs` (skill `browser_visual_reasoning`).
