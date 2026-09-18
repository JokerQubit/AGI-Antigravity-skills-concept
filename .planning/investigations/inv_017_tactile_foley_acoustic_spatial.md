# Laudo Pericial Forense: Arquitetura de Áudio Acústico Físico Real v5.0
## Micro-Feedback Tátil Espacializado, Ambisonics, Normalização LUFS e Blindagem Anti-Síntese Matemática

- **ID da Investigação:** `INV-017`
- **Subagente Responsável:** `Tactile Foley & Acoustic Spatial Engine Specialist`
- **Data/Hora:** `2026-09-17T20:18:37-03:00`
- **Âncora Sináptica:** `.planning/mission_dossier.md` (Onda 1 - Subagente 8)
- **Status da Homologação:** `CONCLUÍDO - EVIDÊNCIA EMPÍRICA SATURADA`
- **Alvo Principal de Refatoração:** `skills/tactile_audio_sfx/SKILL.md` e `scripts/sfx_tool.py`

---

## 1. Sumário Executivo & Diagnóstico Causal de Primeira Ordem

O ecossistema v4.0 estabeleceu a proibição irrevogável da síntese matemática de áudio (bipes senoidais, ruídos brancos e osciladores por código), exigindo gravações físicas reais fatiadas de estúdio via YouTube ou Freesound CC0. Contudo, a análise pericial da implementação de frontend (`SoundManager` em `skills/tactile_audio_sfx/SKILL.md`) e do utilitário de aquisição (`scripts/sfx_tool.py`) revelou quatro lacunas mecânicas críticas que limitavam a imersão sensorial e a integridade acústica:

1. **Mono-Posicionamento e Ausência de Espacialização Sensorial (Spatial Audio Void):**
   O `SoundManager` v4.0 conectava o buffer diretamente a um `GainNode` e deste ao `ctx.destination`. Toda interação (botões no topo direito, drawers laterais, toggles no rodapé, modais centralizados) reproduzia som no centro geométrico estéreo idêntico. Em interfaces de alta fidelidade e telas amplas (ou monitores ultrawide), a dissonância cognitivo-perceptual entre o estímulo visual excêntrico (ex: clique no canto superior esquerdo da tela) e a resposta sonora centrada colapsa a sensação tátil de física real de materiais.
2. **Homogeneidade Indiscriminada de Loudness e Desalinhamento LUFS:**
   O script `scripts/sfx_tool.py` utilizava uma parametrização genérica de `loudnorm=I=-16:TP=-1.5:LRA=11` sem distinção do papel semântico do evento sonoro. Cliques rápidos de alta frequência, micro-feedbacks táteis contínuos e alertas críticos de encerramento de sessão ou transações financeiras irreversíveis competiam pela mesma energia sonora, gerando saturação auditiva ou perda de assertividade fiduciária.
3. **Ausência de Controle Dinâmico de Transientes de Envelope Sub-5ms:**
   A extração de áudio acústico fatiado do mundo real sem janelas matemáticas suaves de fade-in/fade-out mecânico introduz descontinuidades de corrente contínua (DC offset) e estalidos espúrios de alta frequência nos limites do buffer. Na Web Audio API, a inicialização instantânea do buffer sem envelope de ataque programado gera cliques parasitas imperceptíveis no isolamento, mas destrutivos durante navegação rápida a 120fps.
4. **Vulnerabilidade Epistêmica na Detecção de Fraude de Síntese:**
   A proibição da síntese por código dependia unicamente de auditoria humana ou inspeção textual por `grep`. Não havia validação computacional espectral determinística em `sfx_tool.py` para impedir que arquivos de áudio sintéticos (falsamente nomeados como gravações reais) fossem injetados no repositório.

---

## 2. Pipeline de Spatial Audio & Ambisonics para Micro-Feedback Tátil

### 2.1. Cinemática Espacial e Vetores Tridimensionais de Viewport
Para converter coordenadas CSS do DOM em vetores cartesianos de propagação sonora em tempo real, implementa-se o modelo espacial tridimensional baseado em `PannerNode` e `AudioListener` da Web Audio API.

#### Modelo de Projeção Cartesiana Normalizada:
Dado o elemento de interface $E$ com retângulo delimitador $\text{Rect}(E) = (x_{\text{min}}, y_{\text{min}}, w, h)$ na viewport de dimensões $W \times H$:
1. Coordenadas do centroide do elemento na viewport:
   $$c_x = x_{\text{min}} + \frac{w}{2}, \quad c_y = y_{\text{min}} + \frac{h}{2}$$
2. Normalização no espaço de escuta acústico tridimensional:
   $$P_x = \frac{c_x - \frac{W}{2}}{\frac{W}{2}} \in [-1.0, 1.0]$$
   $$P_y = -\left(\frac{c_y - \frac{H}{2}}{\frac{H}{2}}\right) \in [-1.0, 1.0]$$
   $$P_z = -0.5 \quad (\text{plano frontal ligeiramente recuado do ouvinte})$$

#### Configuração do Ouvinte (`AudioListener`):
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

### 2.2. Algoritmo de Atenuação e Panorâmica HRTF (Head-Related Transfer Function)
Para micro-feedback tátil, reflexões tardias e reverbs excessivos criam poluição espectral e turvam a percepção do usuário. A espacialização v5.0 utiliza modelagem anecóica com HRTF pura:
- **`panningModel`:** `'HRTF'` (simulação binaural real de atraso inter-aural ITD e diferença de nível ILD com base na morfologia da orelha humana). Fallback para `'equalpower'` em dispositivos de baixo consumo.
- **`distanceModel`:** `'inverse'`
- **`refDistance`:** $1.0$ metro
- **`maxDistance`:** $10.0$ metros
- **`rolloffFactor`:** $0.8$ (atenuação natural sutil de altas frequências à medida que o elemento se afasta do centro da tela).

### 2.3. Resposta ao Impulso Acústico Real (Acoustic Impulse Response Convolver)
É terminantemente proibido simular espaço acústico por recirculação de delay ou algoritmos matemáticos como Schroeder/Freeverb. O `SpatialSoundManager` v5.0 integra suporte nativo a `ConvolverNode` abastecido exclusivamente com matrizes acústicas reais fatiadas de estúdio (.wav IR):
- Amostras de convolução de salas secas de mixagem (Foley room impulse response);
- Matrizes de reflexão primária de materiais sólidos (superfícies de madeira nobre, cabines acústicas de isolamento absoluto);
- Coeficiente *wet/dry* estritamente limitado: $0.05 \le \alpha_{\text{wet}} \le 0.15$ para preservar a nitidez e o impacto mecânico sub-16ms do clique físico.

---

## 3. Algoritmos de Normalização LUFS e Envelopes de Ataque/Release Sub-5ms

### 3.1. Matriz Fiduciária de Normalização de Loudness (EBU R128 & ITU-R BS.1770-4)
O gerenciamento acústico de UI divide-se em duas categorias sonoras mutuamente exclusivas e matematicamente parametrizadas:

| Categoria Perceptual | Target Integrado ($I$) | True Peak Máximo ($TP$) | Loudness Range ($LRA$) | Caso de Uso Estrito |
|---|---|---|---|---|
| **Micro-Feedback Tátil de Interface** | **$-16.0\text{ LUFS}$** | **$-1.5\text{ dBTP}$** | **$\le 4.0\text{ LU}$** | Hover de alta precisão, toggles, digitação tátil, scrolls elásticos, micro-switches mecânicos. Preserva clareza sem fadiga sensorial em uso prolongado. |
| **Confirmações Críticas & Alertas Fiduciários** | **$-14.0\text{ LUFS}$** | **$-1.0\text{ dBTP}$** | **$\le 6.0\text{ LU}$** | Confirmação de checkout, deploy concluído com sucesso, assinatura digital, transações irreversíveis, autorização de credenciais. Máxima densidade sem clipping. |

#### Parametrização Determinística no `sfx_tool.py` (FFmpeg loudnorm):
```bash
# Perfil Micro-Feedback de Interface:
ffmpeg -i input_raw.wav -af "loudnorm=I=-16.0:TP=-1.5:LRA=4.0:print_format=json" -ar 48000 -ac 2 output_interface.wav

# Perfil Confirmação Crítica:
ffmpeg -i input_raw.wav -af "loudnorm=I=-14.0:TP=-1.0:LRA=6.0:print_format=json" -ar 48000 -ac 2 output_critical.wav
```

### 3.2. Equações e Mecânica do Envelope Anti-Click Sub-5ms
Para anular descontinuidades de fase e transientes DC em transições rápidas na Web Audio API, todo buffer disparado passa por uma rampa de ganho programada diretamente no `AudioParam`:

$$G(t) = \begin{cases} 
0, & t < t_{\text{start}} \\
\frac{t - t_{\text{start}}}{\tau_{\text{attack}}} \cdot G_{\text{target}}, & t_{\text{start}} \le t < t_{\text{start}} + \tau_{\text{attack}} \\
G_{\text{target}}, & t_{\text{start}} + \tau_{\text{attack}} \le t < t_{\text{end}} - \tau_{\text{release}} \\
G_{\text{target}} \cdot \left(1 - \frac{t - (t_{\text{end}} - \tau_{\text{release}})}{\tau_{\text{release}}}\right), & t_{\text{end}} - \tau_{\text{release}} \le t < t_{\text{end}} \\
0, & t \ge t_{\text{end}}
\end{cases}$$

Onde:
- $\tau_{\text{attack}} = 2.0\text{ms}$ ($0.002\text{s} \le 5\text{ms}$)
- $\tau_{\text{release}} = 3.0\text{ms}$ ($0.003\text{s} \le 5\text{ms}$)
- $t_{\text{end}} = t_{\text{start}} + \text{duration}$

#### Implementação de Rampa em Web Audio:
```typescript
const gainNode = ctx.createGain();
const now = ctx.currentTime;
const duration = buffer.duration;
const attackTime = 0.002;
const releaseTime = 0.003;

gainNode.gain.setValueAtTime(0.0001, now);
gainNode.gain.exponentialRampToValueAtTime(targetGain, now + attackTime);
gainNode.gain.setValueAtTime(targetGain, Math.max(now + attackTime, now + duration - releaseTime));
gainNode.gain.exponentialRampToValueAtTime(0.0001, now + duration);
```

#### Filtro High-Pass DC Blocker (IIR Butterworth de 2ª Ordem em 20Hz):
Para impedir que ruído subsônico inframagnético desloque a bobina de alto-falantes ou distorça fones de ouvido:
```typescript
const dcBlocker = ctx.createBiquadFilter();
dcBlocker.type = 'highpass';
dcBlocker.frequency.setValueAtTime(20, ctx.currentTime);
dcBlocker.Q.setValueAtTime(0.7071, ctx.currentTime);
```

---

## 4. Reforço Absoluto da Proibição de Sintetizadores Senoidais & Osciladores

### 4.1. Fundamentação Física e Acústica do Banimento Ontológico
Qualquer gerador algorítmico baseado em fórmulas matemáticas puras ($s(t) = A \sin(\omega t)$ ou ruído gaussiano) exibe características inorgânicas detectáveis pelo córtex auditivo humano:
1. **Ausência de Amortecimento Viscoelástico:** Materiais sólidos reais (madeira de bétula, liga de titânio, polímeros de alta densidade) dispersam energia cinética em taxas desiguais em função da frequência ($Q(f)$ variável). Fórmulas matemáticas geram decaimentos exponenciais uniformes homogêneos.
2. **Ausência de Não-Linearidades e Ruído Browniano Microscópico:** O contato mecânico de um interruptor ou obturador envolve atrito estático de Coulomb, micro-ressonâncias de aspereza e imperfeições físicas aleatórias.
3. **Fadiga Auditiva:** Tons puros senoidais ativam zonas ultra-localizadas na membrana basilar da cóclea, gerando irritabilidade e fadiga neural rápida no usuário.

### 4.2. Algoritmo Determinístico de Verificação Espectral em `sfx_tool.py` (`verify-acoustic`)
Para impedir que gravações sintéticas sejam mascaradas como reais, o `sfx_tool.py` v5.0 introduz uma ferramenta forense de análise de densidade espectral e desvio harmônico baseada na Transformada Rápida de Fourier (FFT):

1. **Spectral Flatness Measure (SFM):**
   Relação entre média geométrica e média aritmética do espectro de potência:
   $$\text{SFM} = \frac{\exp\left(\frac{1}{N} \sum_{k=0}^{N-1} \ln |X[k]|^2\right)}{\frac{1}{N} \sum_{k=0}^{N-1} |X[k]|^2}$$
   - Se $\text{SFM} > 0.85$: Som é ruído branco sintetizado por script $\to$ **REJEIÇÃO SUMÁRIA**.
   - Se $\text{SFM} < 0.001$: Som é tom senoidal puro isolado $\to$ **REJEIÇÃO SUMÁRIA**.
2. **Entropia Espectral Harmônica:**
   Calcula a distribuição de energia entre harmônicos superiores. Sons reais possuem ressonâncias modais complexas não-inteiras. Senoides e ondas quadradas possuem apenas harmônicos perfeitos ou um pico isolado.
3. **Ação:** O comando `python scripts/sfx_tool.py verify-acoustic <arquivo.wav>` analisa os primeiros 200ms do arquivo e aborta com código de saída $1$ caso detecte síntese procedural.

---

## 5. Especificação Técnica Completa: `SpatialSoundManager` v5.0 (TypeScript)

Abaixo é especificada a arquitetura da classe `SpatialSoundManager` que deve substituir a versão simplificada de `skills/tactile_audio_sfx/SKILL.md`:

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

## 6. Evolução Necessária no `scripts/sfx_tool.py` para a v5.0

Para sustentar a arquitetura v5.0, o utilitário físico `scripts/sfx_tool.py` deve receber as seguintes implementações mecânicas:

1. **Subcomando `normalize-lufs`:**
   Adicionar processamento em dois passos com `ffmpeg-python` ou chamadas `ffmpeg` diretas para normalizar com exatidão conforme os perfis:
   - `--profile interface`: `-16.0 LUFS`, `-1.5 dBTP`, `LRA 4.0`.
   - `--profile critical`: `-14.0 LUFS`, `-1.0 dBTP`, `LRA 6.0`.
   - Aplicação de fade-in e fade-out sub-5ms em lote: `afade=t=in:ss=0:d=0.002,afade=t=out:st=<dur-0.003>:d=0.003`.
2. **Subcomando `verify-acoustic`:**
   Módulo de análise espectral via `numpy` e `scipy.fft` ou análise estatística de amostras WAV brutas que rejeita arquivos com achatamento espectral ($\text{SFM} > 0.85$) ou frequências senoidais puras isoladas ($\text{SFM} < 0.001$), retornando erro fiduciário explícito caso detecte áudio procedural.
3. **Ajuste no Subcomando `slice-youtube`:**
   Substituir a flag fixa de loudnorm por escolha de perfil (`--profile interface` padrão), garantindo que todo áudio extraído do YouTube já saia no padrão exato com transiente de ataque limpo.

---

## 7. Novo Checklist Forense de Áudio Acústico Real v5.0 (10 Critérios Binários)

> Integrado à Época IV e auditado compulsoriamente pelo Red Team Juiz.

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

---

## 8. Sinapses Feedforward & Injeção de Contratos para a Onda 2

- **Subagente Motor Downstream:** Subagente de Implementação da Onda 2 responsável pelo módulo de áudio e assets táteis (`Tactile Foley & Acoustic Engine Artificer`).
- **Arquivos-Alvo Disjuntos para Mutação Física:**
  1. `skills/tactile_audio_sfx/SKILL.md` (Atualizar para versão 5.0.0 com o playbook de Spatial Audio, normalização LUFS diferencial e novo checklist);
  2. `scripts/sfx_tool.py` (Adicionar perfis de normalização EBU R128 e subcomandos de verificação espectral);
- **Contrato Sináptico Feedforward (`[SYNAPTIC_OUTPUTS]`):**
  - `SPATIAL_SFX_INTERFACE`: Exporta interface `SpatialAudioOptions`, classe `SpatialSoundManager` e instância `spatialSfx`.
  - `LUFS_TARGET_PROFILES`: Interface = `-16 LUFS / -1.5 dBTP / LRA 4`, Critical = `-14 LUFS / -1.0 dBTP / LRA 6`.
  - `ENVELOPE_ATTACK_RELEASE`: $\tau_{\text{attack}} = 2\text{ms}$, $\tau_{\text{release}} = 3\text{ms}$.
