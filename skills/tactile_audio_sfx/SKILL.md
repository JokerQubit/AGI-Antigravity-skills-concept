---
name: tactile_audio_sfx
version: 5.0.0
description: "v5.0 — Universal Cognitive Parity — Áudio Acústico Físico Real & Spatial Audio HRTF. Manual técnico de engenharia de áudio físico real via gravações acústicas fatiadas (YouTube/Freesound CC0) com scripts/sfx_tool.py, Spatial Audio HRTF binaural tridimensional com PannerNode cartesiano, normalização LUFS diferencial (-16 UI / -14 Crítico), envelope anti-click sub-5ms e verificação espectral SFM. Síntese matemática por script constitui fraude de áudio e aciona [HARD HALT] sem exceção."
---

# Tactile Audio Engineering: Áudio Físico Real & Spatial Engine Playbook v5.0 — Universal Cognitive Parity

Na v5.0.0, toda interação operacional que toque componentes com feedback sonoro dispara compulsoriamente as salvaguardas desta skill — sem distinção entre "adicionar um beep simples" e "sistema de SFX completo". Não existe som que justifique síntese matemática por script: qualquer áudio gerado via AudioSynthesizer, OscillatorNode ou gerador matemático constitui fraude de áudio e aciona `[HARD HALT]`.

Manual prático para obtenção, processamento e integração de efeitos sonoros táteis capturados exclusivamente do mundo real. Veda sumariamente ruídos gerados por script (white/brown noise), ondas senoidais e síntese procedural, integrando **Spatial Audio HRTF binaural com projeção cartesiana de viewport**, **normalização LUFS diferencial (-16 UI / -14 Crítico)**, **envelopes anti-click sub-5ms** e **auditoria espectral automatizada (Spectral Flatness Measure - SFM)** via `scripts/sfx_tool.py`.

---

## 1. Diretriz Mandatória: Sons Físicos Reais & Banimento Ontológico de Sintetizadores

- **A Proibição Inviolável:** É expressamente proibido gerar ruídos matemáticos (white/brown noise), bipes, tons senoidais puros ou ondas sintetizadas via script ou Web Audio (`OscillatorNode`, `createOscillator`, `PeriodicWave`, loops com `Math.sin`). Todo som sintético gerado por fórmula viola a Lei Constitucional nº 10.
- **Fundamentação Acústica do Banimento:** Materiais sólidos reais (madeira nobre, titânio usinado, polímeros de alta densidade) possuem taxas desiguais de dispersão de energia por frequência ($Q(f)$ variável) e atrito de Coulomb microscópico. Sons matemáticos não possuem amortecimento viscoelástico, soam inorgânicos e geram fadiga coclear rápida no usuário.
- **O Padrão Exigido:** Todo clique de botão, transição de tela, confirmação ou feedback tátil deve provir de **gravações físicas acústicas reais** (madeira, vidro, metal polido, obturador mecânico de câmera analógica, papel pesado, micro-switches mecânicos).

---

## 2. Métodos Mandatórios de Extração & Processamento Físico (`scripts/sfx_tool.py`) — v5.0

> **[HARD HALT se violado]** O uso de `scripts/sfx_tool.py` é **mandatório e incondicional** para todo e qualquer áudio produzido no projeto. Não existe categoria de som ("beep simples", "clique rápido", "feedback mínimo") que isente o agente de usar este utilitário. A ausência de `sfx_tool.py` na cadeia de produção de qualquer arquivo de áudio constitui fraude operacional imediata.

O script `scripts/sfx_tool.py` fornece os métodos homologados de aquisição e processamento de áudio real:

### Método A: Fatiamento Cirúrgico de Áudio do YouTube (`slice-youtube`)
Captura trechos com precisão de milissegundos e normalização de volume padrão EBU R128 (`loudnorm`) parametrizada por perfil:
```bash
# Extração de som mecânico autêntico de interruptor com perfil de micro-feedback de interface (-16 LUFS)
python scripts/sfx_tool.py slice-youtube "https://youtube.com/watch?v=..." --start "00:01.200" --end "00:01.600" --profile interface -o public/sfx/tactile_click.wav

# Extração de confirmação fiduciária crítica (-14 LUFS)
python scripts/sfx_tool.py slice-youtube "https://youtube.com/watch?v=..." --start "00:10.500" --end "00:11.200" --profile critical -o public/sfx/fiduciary_commit.wav
```

### Método B: Amostras Acústicas de Estúdio no Freesound (CC0)
Busca e download direto de gravações profissionais de Foley:
```bash
# Busca de gravações reais de cliques mecânicos
python scripts/sfx_tool.py search "mechanical switch click" --max-duration 1.0 --provider freesound

# Download direto pelo ID oficial da amostra
python scripts/sfx_tool.py download <SOUND_ID> --output public/sfx/click_real.wav
```

### Método C: Normalização LUFS Diferencial em Lote (`normalize-lufs`)
Aplica normalização estrita EBU R128 / ITU-R BS.1770-4 e envelope suave anti-click sub-5ms:
```bash
# Perfil 1: Micro-Feedback Tátil de Interface (-16.0 LUFS, True Peak -1.5 dBTP, LRA 4.0 LU)
python scripts/sfx_tool.py normalize-lufs --input input_raw.wav --output public/sfx/button_click.wav --profile interface

# Perfil 2: Confirmação Crítica / Fiduciária (-14.0 LUFS, True Peak -1.0 dBTP, LRA 6.0 LU)
python scripts/sfx_tool.py normalize-lufs --input input_raw.wav --output public/sfx/deploy_success.wav --profile critical
```

### Método D: Verificação Espectral Forense Anti-Fraude (`verify-acoustic`)
Analisa a densidade espectral e o Spectral Flatness Measure (SFM) via FFT para detectar e barrar sons sintéticos:
$$\text{SFM} = \frac{\exp\left(\frac{1}{N} \sum_{k=0}^{N-1} \ln |X[k]|^2\right)}{\frac{1}{N} \sum_{k=0}^{N-1} |X[k]|^2}$$
- $\text{SFM} > 0.85$: Ruído branco sintético gerado por script $\to$ **REJEIÇÃO SUMÁRIA**.
- $\text{SFM} < 0.001$: Tom senoidal puro ou oscilador $\to$ **REJEIÇÃO SUMÁRIA**.
```bash
python scripts/sfx_tool.py verify-acoustic public/sfx/tactile_click.wav
```

### Método E: Varredura de Biblioteca Local de Assets (`scan-local`)
```bash
python scripts/sfx_tool.py scan-local --dir public/sfx/ --json
```

---

## 3. Arquitetura de Spatial Audio HRTF Binaural & Projeção Cartesiana de Viewport

Para converter coordenadas CSS do DOM em vetores cartesianos de propagação sonora tridimensional em tempo real, implementa-se o modelo espacial baseado em `PannerNode` e `AudioListener` da Web Audio API.

### 3.1. Modelo de Projeção Cartesiana Normalizada
Dado o elemento de interface $E$ com retângulo delimitador $\text{Rect}(E) = (x_{\text{min}}, y_{\text{min}}, w, h)$ na viewport de dimensões $W \times H$:
1. Coordenadas do centroide do elemento na viewport:
   $$c_x = x_{\text{min}} + \frac{w}{2}, \quad c_y = y_{\text{min}} + \frac{h}{2}$$
2. Normalização no espaço de escuta acústico tridimensional:
   $$P_x = \frac{c_x - \frac{W}{2}}{\frac{W}{2}} \in [-1.0, 1.0]$$
   $$P_y = -\left(\frac{c_y - \frac{H}{2}}{\frac{H}{2}}\right) \in [-1.0, 1.0]$$
   $$P_z = -0.5 \quad (\text{plano frontal ligeiramente recuado do ouvinte})$$

### 3.2. Configuração do Ouvinte (`AudioListener`)
O ponto focal do usuário é modelado no ponto neutro $(0, 0, 0)$ voltado para o plano da tela (vetor de orientação $(0, 0, -1)$, vetor ascendente $(0, 1, 0)$):
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

### 3.3. Algoritmo de Atenuação e Panorâmica HRTF
A espacialização v5.0 utiliza modelagem anecóica com HRTF pura:
- **`panningModel`:** `'HRTF'` (simulação binaural de atraso inter-aural ITD e diferença de nível ILD baseada na morfologia da orelha humana).
- **`distanceModel`:** `'inverse'`
- **`refDistance`:** $1.0\text{ m}$
- **`maxDistance`:** $10.0\text{ m}$
- **`rolloffFactor`:** $0.8$ (atenuação natural sutil de altas frequências à medida que o elemento se afasta do centro da tela).

### 3.4. Envelope Dinâmico Anti-Click Sub-5ms e Filtro DC Blocker
Para anular descontinuidades de fase e transientes DC em transições rápidas na Web Audio API, todo buffer disparado passa por rampa de ganho programada diretamente no `AudioParam`:
- $\tau_{\text{attack}} = 2.0\text{ms}$ ($0.002\text{s} \le 5\text{ms}$)
- $\tau_{\text{release}} = 3.0\text{ms}$ ($0.003\text{s} \le 5\text{ms}$)

E filtro passa-altas de 2ª ordem (Butterworth 20Hz, $Q = 0.7071$) em linha para barrar offsets subsônicos.

---

## 4. Integração Resiliente no Frontend: `SpatialSoundManager` v5.0 (TypeScript)

```typescript
// src/lib/spatialSoundManager.ts
/**
 * SpatialSoundManager v5.0 — Real Acoustic Tactile Audio Engine.
 * Conforme Lei Constitucional nº 10 e Invariantes da Skill tactile_audio_sfx v5.0.
 * Proibição absoluta de OscillatorNode e síntese por script.
 */

export interface SpatialAudioOptions {
  element?: HTMLElement | null;
  coords?: { x: number; y: number }; // Coordenadas em pixels na tela
  volume?: number;                    // 0.0 a 1.0 (default: 0.3)
  category?: 'interface' | 'critical'; // -16 LUFS vs -14 LUFS calibrado
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
      const AudioCtx = window.AudioContext || (window as unknown as { webkitAudioContext: typeof AudioContext }).webkitAudioContext;
      if (AudioCtx) {
        this.ctx = new AudioCtx({ latencyHint: 'interactive' });
      }
    }

    if (this.ctx && !this.masterGain) {
      // 1. Master Gain
      this.masterGain = this.ctx.createGain();
      this.masterGain.gain.setValueAtTime(1.0, this.ctx.currentTime);

      // 2. DC Blocker Butterworth 20Hz
      this.dcBlocker = this.ctx.createBiquadFilter();
      this.dcBlocker.type = 'highpass';
      this.dcBlocker.frequency.setValueAtTime(20, this.ctx.currentTime);
      this.dcBlocker.Q.setValueAtTime(0.7071, this.ctx.currentTime);

      this.dcBlocker.connect(this.masterGain);
      this.masterGain.connect(this.ctx.destination);

      // 3. Configurar Ouvinte Neutro (Centro da Viewport)
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
      // Fallback gracioso: a aplicação nunca trava se o áudio não carregar
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
      const baseVol = options.volume !== undefined ? options.volume : (options.category === 'critical' ? 0.6 : 0.3);
      const targetGain = Math.max(0.0001, Math.min(1.0, baseVol));
      const attack = 0.002;  // 2ms
      const release = 0.003; // 3ms
      const duration = buffer.duration;

      gainNode.gain.setValueAtTime(0.0001, now);
      gainNode.gain.exponentialRampToValueAtTime(targetGain, now + attack);
      const sustainEnd = Math.max(now + attack, now + duration - release);
      gainNode.gain.setValueAtTime(targetGain, sustainEnd);
      gainNode.gain.exponentialRampToValueAtTime(0.0001, now + duration);

      // 2. Nó de Espacialização Tridimensional HRTF
      let panner: PannerNode | null = null;
      let posX = 0;
      let posY = 0;

      if (options.element) {
        const rect = options.element.getBoundingClientRect();
        const winW = window.innerWidth || 1920;
        const winH = window.innerHeight || 1080;
        const cx = rect.left + rect.width / 2;
        const cy = rect.top + rect.height / 2;
        posX = (cx - winW / 2) / (winW / 2);
        posY = -((cy - winH / 2) / (winH / 2));
      } else if (options.coords) {
        const winW = window.innerWidth || 1920;
        const winH = window.innerHeight || 1080;
        posX = (options.coords.x - winW / 2) / (winW / 2);
        posY = -((options.coords.y - winH / 2) / (winH / 2));
      }

      // Conexão do grafo de áudio com Panner
      panner = this.ctx.createPanner();
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

      // Grafo: Source -> Gain (Envelope) -> Panner (HRTF) -> DC Blocker -> Master -> Destination
      source.connect(gainNode);
      gainNode.connect(panner);
      panner.connect(this.dcBlocker);

      source.start(now);
    } catch {
      // Falha graciosa sem interromper ciclo de renderização
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

## 5. Regras de Convivência Acústica v5.0

1. **Latência de Disparo Sub-16ms:** Amostras de áudio completamente decodificadas em `AudioBuffer` na memória antes da interação física do usuário (zero `new Audio()` instanciado em tempo de clique).
2. **Discreto & Baixo Volume:** O volume de feedback tátil deve ser sutil (`0.2` a `0.4`), preservando a inteligibilidade sem fadiga sensorial.
3. **Respeito Mandatório ao Mute:** O sistema possui toggle global de áudio acessível e silencia instantaneamente todos os nós sem atraso perceptível.
4. **Desbloqueio no Primeiro Gesto:** Inicialize o contexto de áudio a partir do primeiro clique ou toque do usuário para atender às políticas de segurança dos navegadores.
5. **Fallback Silencioso Gracioso:** Se o áudio falhar ou for bloqueado pelo navegador, a UI continua funcional sem erros ou exceções no console.

---

## 6. Checklist Forense de Áudio Acústico Real v5.0 (10 Critérios Binários — Leis 10 & 41)
> Integrado à Época IV e auditado compulsoriamente pelo Red Team Juiz. Um único item fraudado dispara `[HARD REJECT: FRAUDULENT_CHECKLIST_SIGNOFF]`.

- [ ] **1. Origem Física Autêntica:** Todo asset provém de fatiamento cirúrgico de áudio real via `scripts/sfx_tool.py slice-youtube` ou gravação CC0 do Freesound; zero sons gerados por software sintetizador.
- [ ] **2. Zero Síntese por Código (Veto Absoluto):** Grep em todo o repositório por `OscillatorNode`, `createOscillator`, `PeriodicWave`, `Math.sin(` em loops de buffers de áudio — exatamente 0 ocorrências.
- [ ] **3. Normalização EBU R128 (-16 LUFS):** Sons táteis de micro-interação calibrados estritamente em $-16.0\text{ LUFS} \pm 0.5$ e True Peak $\le -1.5\text{ dBTP}$.
- [ ] **4. Normalização de Alertas Críticos (-14 LUFS):** Sons de confirmação fiduciária/transacional calibrados em $-14.0\text{ LUFS} \pm 0.5$ e True Peak $\le -1.0\text{ dBTP}$.
- [ ] **5. Envelope de Transiente Sub-5ms:** Todo disparo de som aplica rampa de ataque $\le 2\text{ms}$ e release $\le 3\text{ms}$; zero descontinuidades de amplitude ou estalidos parasitas.
- [ ] **6. DC Blocker em Linha:** Presença obrigatória de filtro passa-altas de 20Hz (Butterworth de 2ª ordem) no grafo de mixagem antes do destino final.
- [ ] **7. Espacialização HRTF Ativa:** Interações de elementos na tela utilizam coordenadas normalizadas da viewport mapeadas em nó `PannerNode` com modelo `'HRTF'`.
- [ ] **8. Latência de Disparo Sub-16ms:** Amostras de áudio completamente decodificadas em `AudioBuffer` na memória antes da interação física do usuário (zero `new Audio()` instanciado em tempo de clique).
- [ ] **9. Respeito Mandatório ao Mute:** O sistema possui toggle global de áudio acessível e silencia instantaneamente todos os nós sem atraso perceptível.
- [ ] **10. Fallback Gracioso sem Erros de Console:** Navegadores que bloqueiam autoplay ou falhas de fetch não geram uncaught promises nem erros no console DevTools (`browser_console_logs`).

