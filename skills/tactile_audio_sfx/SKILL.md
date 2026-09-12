---
name: tactile_audio_sfx
description: Manual técnico de engenharia de áudio físico real via gravações acústicas do YouTube (slice-youtube) e Freesound CC0 com scripts/sfx_tool.py, e integração de micro-áudio responsivo em aplicações web.
---

# Tactile Audio Engineering: Áudio Físico Real Playbook

Manual prático para obtenção e integração de efeitos sonoros táteis capturados exclusivamente do mundo real. Veda sumariamente o uso de ruídos gerados por script (white/brown noise), ondas matemáticas senoidais e síntese procedural, exigindo amostras acústicas físicas reais (Foley CC0 e recortes cirúrgicos de estúdio via YouTube) através do utilitário `scripts/sfx_tool.py`.

---

## 1. Diretriz Mandatória: Sons Físicos Reais (Veto a Sons Sintéticos e Ruídos de Script)

- **A Proibição Inviolável:** É expressamente proibido gerar ruídos matemáticos (white/brown noise), bipes, tons senoidais puros ou ondas sintetizadas via script ou Web Audio. Todo som sintético gerado por fórmula soa artificial, amador e viola a Lei Constitucional nº 6.
- **O Padrão Exigido:** Todo clique de botão, transição de tela, confirmação ou feedback tátil deve provir de **gravações físicas acústicas reais** (madeira, vidro, metal polido, obturador mecânico de câmera analógica, papel pesado, veludo, acústica automotiva premium de luxo).


---

## 2. Métodos Primários de Extração de Áudio Real (`scripts/sfx_tool.py`)

O script `scripts/sfx_tool.py` fornece métodos de alta fidelidade para aquisição de áudio real:

### Método A: Fatiamento Cirúrgico de Áudio do YouTube (`slice-youtube`)
Captura trechos com precisão de milissegundos e normalização de volume padrão EBU R128 (`loudnorm`):
```bash
# Extração de som mecânico autêntico de obturador de câmera ou clique tátil
python scripts/sfx_tool.py slice-youtube "https://youtube.com/watch?v=..." --start "00:01.200" --end "00:01.600" -o public/sfx/tactile_click.wav

# Extração de transição suave e atmosférica
python scripts/sfx_tool.py slice-youtube "https://youtube.com/watch?v=..." --start "00:10.500" --end "00:11.200" -o public/sfx/whoosh.wav
```

### Método B: Amostras Acústicas de Estúdio no Freesound (CC0)
Busca e download direto de gravações profissionais de Foley:
```bash
# Busca de gravações reais de cliques mecânicos
python scripts/sfx_tool.py search "mechanical switch click" --max-duration 1.0 --provider freesound

# Download direto pelo ID oficial da amostra
python scripts/sfx_tool.py download <SOUND_ID> --output public/sfx/click_real.mp3
```

### Método C: Varredura de Biblioteca Local de Assets (`scan-local`)
Utilização de arquivos WAV/MP3 reais gravados ou importados para `assets/sfx/`:
```bash
python scripts/sfx_tool.py scan-local --dir public/sfx/ --json
```

---

## 4. Integração Resiliente no Frontend (Web Audio API Sound Manager)

O áudio na web nunca deve bloquear a renderização nem quebrar silenciosamente por restrições de autoplay dos navegadores:

```typescript
// src/lib/audioManager.ts
class SoundManager {
  private static instance: SoundManager;
  private ctx: AudioContext | null = null;
  private buffers: Map<string, AudioBuffer> = new Map();
  private isMuted: boolean = false;

  private constructor() {}

  public static getInstance(): SoundManager {
    if (!SoundManager.instance) {
      SoundManager.instance = new SoundManager();
    }
    return SoundManager.instance;
  }

  private initContext(): void {
    if (!this.ctx && typeof window !== 'undefined') {
      const AudioCtx = window.AudioContext || (window as unknown as { webkitAudioContext: typeof AudioContext }).webkitAudioContext;
      if (AudioCtx) {
        this.ctx = new AudioCtx();
      }
    }
    if (this.ctx && this.ctx.state === 'suspended') {
      this.ctx.resume();
    }
  }

  public async loadSound(name: string, url: string): Promise<void> {
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
      // Fallback silencioso: se falhar o carregamento, a UI continua funcionando normalmente
    }
  }

  public play(name: string, volume: number = 0.5): void {
    if (this.isMuted) return;
    this.initContext();
    if (!this.ctx) return;

    const buffer = this.buffers.get(name);
    if (!buffer) return;

    try {
      const source = this.ctx.createBufferSource();
      const gainNode = this.ctx.createGain();
      source.buffer = buffer;
      gainNode.gain.value = Math.max(0, Math.min(1, volume));
      source.connect(gainNode);
      gainNode.connect(this.ctx.destination);
      source.start(0);
    } catch {
      // Falha graciosa sem interromper o fluxo de interação
    }
  }

  public toggleMute(): boolean {
    this.isMuted = !this.isMuted;
    return this.isMuted;
  }
}

export const sfx = SoundManager.getInstance();
```

### Regras de Convivência Acústica:
1. **Discreto & Baixo Volume:** O volume de feedback tátil deve ser sutil (`0.2` a `0.4`), nunca estridente.
2. **Respeito ao Mute:** Sempre forneça controle de volume ou mute na interface quando sons forem reproduzidos.
3. **Desbloqueio no Primeiro Gesto:** Inicialize o contexto de áudio a partir do primeiro clique ou toque do usuário para atender às políticas de segurança dos navegadores.
