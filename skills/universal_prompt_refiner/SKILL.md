---
name: universal_prompt_refiner
description: Playbook de Engenharia e Controle Operacional do Portão de Ingestão Mandatória Ubíqua (Universal Prompt Refinement Gate). Governa o despacho obrigatório do Subagente Prompt Refiner antes de qualquer intervenção operacional, a compilação do Dossiê de Missão (Cirúrgico vs Arquitetural), desconstrução forense da demanda em camadas, roadmap determinístico para o enxame, matriz de regras/skills ativadas por primeiros princípios, planos de despacho sob medida, pre-mortem forense e critérios fiduciários de aceite.
---

# Universal Prompt Refiner Gate Playbook (Época 0 - v4.0)

Playbook operacional definitivo que rege o **Portão de Ingestão Mandatória Ubíqua (Universal Prompt Refinement Gate)**. Estabelece a trava mecânica suprema do ecossistema: **o Agente Principal está terminantemente proibido de agir, planejar, editar arquivos ou rodar comandos modificadores sem antes despachar o Subagente Especialista Prompt Refiner**.

Nenhuma intervenção operacional — seja a correção de uma vírgula de CSS, um script CLI pontual ou uma plataforma distribuída de 100+ nós — é executada no impulso do prompt cru. Toda demanda é desconstruída, blindada, mapeada em regras/skills por primeiros princípios e roteada com precisão cirúrgica antes de qualquer mutação física no repositório.

---

## 1. O Portão de Ingestão Mandatória Ubíqua (Universal Prompt Refinement Gate)

### 1.1. O Veto Absoluto à Ação por Impulso Estocástico
Modelos convencionais de linguagem operam sob impulso reativo: ao receberem uma solicitação, disparam ferramentas de edição de arquivos ou geração de planos imediatamente. Esse vício cognitivo resulta em:
- Suposições cegas sobre o codebase existente;
- Acoplamentos ocultos que causam regressões em cascata;
- Adoção involuntária do "menor denominador comum" (CSS duro, emojis, stubs, ruídos de áudio sintéticos);
- Vazamentos de termos internos no produto final (*Prompt Bleed*);
- Retrabalho exponencial decorrente de premissas não validadas.

**A LEI É CATEGÓRICA:** Qualquer chamada de ferramenta de escrita (`replace_file_content`, `write_to_file`), comandos de alteração de estado no shell (`run_command`), ou geração de planos executivos na Época II sem a prévia existência física do Dossiê do Prompt Refiner no disco aciona **veto mecânico sumário imediato (`[HARD HALT: UNREFINED_ACTION_ATTEMPT]`)**.

### 1.2. A Ubiquidade do Portão: Por que Nenhuma Tarefa é "Pequena Demais"
A ilusão da "tarefa cirúrgica simples" é a fonte primária de incidentes em sistemas de alta complexidade:
- *"É apenas um botão de exportar"* $\to$ Dispara downloads paralelos ilimitados, estoura a memória do browser e trava a thread com animação CSS dura de 300ms.
- *"É apenas uma correção de tipagem"* $\to$ Converte `Result<T, E>` em `any` disfarçado, quebrando contratos downstream de 12 arquivos.
- *"É apenas rodar um comando de build"* $\to$ Executa em porta já ocupada, orfanando processos Node em background e corrompendo o lockfile.

O Portão de Ingestão Mandatória Ubíqua não desacelera o trabalho: ele **elimina o atrito do retrabalho**, adaptando dinamicamente a sua densidade (Track Cirúrgico vs Track Arquitetural).

---

## 2. Os Seis Entregáveis Obrigatórios do Prompt Refiner

Todo despacho do Subagente Prompt Refiner deve gerar obrigatoriamente um Dossiê de Missão contendo seis blocos fiduciários inegociáveis:

```text
┌────────────────────────────────────────────────────────────────────────┐
│                   ANATOMIA DOS SEIS ENTREGÁVEIS                        │
├────────────────────────────────────────────────────────────────────────┤
│ 1. Desconstrução Forense (Explícita, Implícita, Invariantes Ocultos)   │
│ 2. Roadmap Determinístico Passo a Passo (Agente Principal & Enxame)    │
│ 3. Matriz de Regras e Skills Ativadas (Primeiros Princípios)           │
│ 4. Plano de Despacho de Subagentes Específicos (Bespoke Squads)        │
│ 5. Matriz de Modos de Quebra & Pre-Mortem Forense                      │
│ 6. Critérios Estritos de Aceite Fiduciário (Métricas & Homologação)    │
└────────────────────────────────────────────────────────────────────────┘
```

### (a) Desconstrução Forense da Demanda
- **Contratos Explícitos:** Declarações literais, entradas declaradas, saídas esperadas e restrições expressas pelo usuário.
- **Contratos Implícitos:** Invariantes de engenharia não ditos pelo usuário, mas mandatórios para produção (idempotência, cancelamento via `AbortController`, acessibilidade ARIA, concorrência atômica, taxa de quadros a 60fps/120fps, latência perceptiva $<16\text{ms}$, tipagem estrita `Result<T, E>`).
- **Invariantes de Estado & Acoplamento:** Mapeamento do estado atual do repositório, dependências circulares em potencial e impacto nas rotas e contratos existentes.

### (b) Roadmap Passo a Passo Exato
- Sequenciamento unívoco e mecânico de ações para o Agente Principal e para o enxame de subagentes.
- Definição estrita de dependências: o que deve ser executado sequencialmente vs em concorrência paralela.
- Travas de isolamento: aplicação formal do protocolo `HOLD/GO` para contratos estruturais compartilhados.

### (c) Matriz de Regras e Skills Ativadas com Justificativa de Primeiros Princípios
O Prompt Refiner não pode meramente "listar" regras: deve fundamentar a ativação de cada uma na **física real do problema**:
- *Exemplo:* Em vez de apenas citar "Lei 7", o Refiner prescreve: *"Ativação da Lei 7 (Titan Benchmark) porque a interação do drawer exige física de molas de 2ª ordem com stiffness 380 e damping 32 para absorver a inércia do gesto do usuário sem jank visual"*.

### (d) Plano de Despacho de Subagentes Específicos (Bespoke Dynamic Squads)
Em conformidade estrita com as Leis 32 e 40:
- **Banimento de Templates Fixos:** É proibido usar trios pré-fabricados ("pesquisador, arquiteto, testador").
- **Síntese Sob Medida:** Criação de personas ultra-especializadas derivadas dos modos de falha da tarefa (ex: `DirectByteBufferConcurrenySpecialist`, `FramerMotionSpringPhysicist`, `FoleyAcousticSlicer`).
- **Definição de Parâmetros:** Para cada subagente: `Role`, `TypeName: "self"` ou `"research"`, `Model` (Flash Low, Medium ou High conforme Tier), prompt atômico 1:1 e ferramentas autorizadas.

### (e) Matriz de Modos de Quebra e Pre-Mortem Forense
- **Exercício Pre-Mortem:** *"Assumindo que este código quebrou catastroficamente em produção 3 meses após o deploy, quais foram as causas raízes microscópicas?"*
- Mapeamento explícito de armadilhas silenciosas:
  - Condições de corrida assíncronas;
  - Desalinhamento perceptual de áudio e UI;
  - Quebra de hidratação ou memory leaks por event listeners desanexados;
  - Exaustão de sockets ou limites de taxa de APIs externas;
  - Queda de taxa de quadros (<60fps) por reflows do DOM fora de camadas de GPU.

### (f) Critérios Estritos de Aceite Fiduciário
- Métricas quantificáveis de telemetria e integridade física que serão verificadas pelo Subagente Juiz (Época IV):
  - `$LASTEXITCODE === 0` em compilação e suítes de testes;
  - Zero erros, warnings de hidratação ou assets 404 no console (`browser_console_logs`);
  - Zero stubs (`TODO`, `pass`, `...`, funções vazias);
  - Inspeção visual perceptual aprovada no Chrome real via `browser-mcp`.

---

## 2. Formato do Artefato por Granularidade: Cirúrgico vs Grandes Missões

O protocolo elimina o desperdício de tokens e a sobrecarga burocrática segregando a saída em dois formatos físicos complementares:

| Dimensão | Track Cirúrgico (Tier 1) | Track Arquitetural & Features (Tier 2/3) |
|---|---|---|
| **Escopo Típico** | Bug fixes pontuais, micro-ajustes de UI, patches, scripts CLI | Novas telas, refatores de arquitetura, novos domínios, plataformas |
| **Artefato no Disco** | `.planning/surgical_mission_dossier.md` | `.planning/mission_dossier.md` |
| **Extensão Típica** | 30 a 60 linhas de alta densidade | 120 a 300+ linhas exaustivas |
| **Saturação de Nós** | Dispensa saturação hipergráfica de 100 nós | Mandatória saturação de $N \ge 100$ nós atômicos 1:1 |
| **Tempo de Refino** | 1 ciclo rápido de compilação epistêmica | Varredura empírica profunda com Chief Ontologist |

### 2.1. Schema do Track Cirúrgico (`.planning/surgical_mission_dossier.md`)

```markdown
# SURGICAL MISSION DOSSIER (Tier 1 - Quick Track)
**Task Hash:** [short-hash] | **Timestamp:** YYYY-MM-DDTHH:MM:SS
**Classification:** Tier 1 Cirúrgico | **Flash Thinking Prescrito:** Flash Low

## 1. Deconstrução Forense Relâmpago
- **Causa Raiz & Sintoma:** [Identificação cirúrgica do defeito ou demanda]
- **Arquivos Alvo:** [`caminho/do/arquivo.ext:L10-L25`](file:///caminho/do/arquivo.ext#L10-L25)
- **Contrato de Modificação:** [Assinatura exata antes vs depois]

## 2. Roadmap Determinístico (3 a 5 Passos Mecânicos)
1. Despachar Subagente Cirúrgico: `[Bespoke Role Name]`
2. Aplicar alteração atômica em `[arquivo]` garantindo zero stubs e tipagem estrita
3. Executar comando de checagem nativa: `[comando]`
4. Verificar ausência de efeitos colaterais em downstream

## 3. Matriz de Ativação Constitucional
- **Regras Ativadas:** [Ex: Lei 18 (Zero-Stub), Lei 39 (Malha Fechada)]
- **Skills Convocadas:** [Ex: hardened_clean_architecture]
- **Justificativa de Primeiros Princípios:** [Por que a física desta mudança exige estas travas]

## 4. Subagente Cirúrgico Específico (Bespoke Dispatch)
- **Role:** [Ex: FloatingPointPrecisionFixer]
- **Tooling:** `replace_file_content`, `run_command`
- **Invariante Local:** [Ex: Não alterar a interface pública da função X]

## 5. Pre-Mortem & Armadilhas Silenciosas
- **Risco 1:** [Possível quebra de teste X ou mutação colateral]
- **Mitigação:** [Uso de cópia imutável / checagem de limites]

## 6. Aceite Fiduciário Imediato
- [ ] Compilação limpa (`$LASTEXITCODE == 0`)
- [ ] Teste unitário isolado cobrindo o caso de borda executado e passando
- [ ] Zero stubs ou restos de depuração (`console.log`)
```

### 2.2. Schema do Track de Grandes Missões (`.planning/mission_dossier.md`)

Para Tiers 2 e 3, o artefato expande-se para o dossiê arquitetural completo:
- Integração formal com a Análise de Custo-Complexidade (ACC);
- Identificação dos 8 Eixos Ontológicos da demanda;
- Mapeamento das ondas de saturação sináptica com barramento neural (`synaptic_bus.json`);
- Alinhamento explícito com o Diretor Cognitivo Soberano e as personas mundiais de referência;
- Prescrição de ativos de áudio físico real (Foley fatiado via `scripts/sfx_tool.py slice-youtube`);
- Protocolo perceptual de inspeção no Chrome via `browser-mcp` com 4 passadas do Gauntlet.

---

## 3. Exemplar Contrastivo & Autópsia Forense de Falha

Para ilustrar o poder de blindagem do Portão Ubíquo, examinemos um caso real de engenharia de produto.

### 3.1. A Demanda Bruta do Usuário
> *"Adicione um botão de exportar relatórios na tabela de transações com um som de feedback e um indicador visual de progresso."*

---

### 3.2. O Anti-Pattern: Ação Estocástica por Impulso do Prompt Cru

#### O Que a IA Sem Portão Faz:
1. Pula a Época 0. Não despacha subagentes.
2. Abre imediatamente `TransactionTable.tsx` e injeta código diretamente na thread principal.
3. Código gerado pelo impulso:

```tsx
// ANTI-PATTERN: Implementação ingênua no impulso
import React, { useState } from 'react';

export function ExportButton({ transactions }: { transactions: any }) {
  const [loading, setLoading] = useState(false);

  const handleExport = async () => {
    setLoading(true);
    // Áudio ingênuo: crasha por autoplay ou dá 404
    const audio = new Audio('/beep.mp3');
    audio.play().catch(() => {});

    try {
      const res = await fetch('/api/export', {
        method: 'POST',
        body: JSON.stringify(transactions),
      });
      const blob = await res.blob();
      const url = window.URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = 'report.csv';
      a.click();
    } catch (e) {
      alert('Erro ao exportar');
    } finally {
      setLoading(false);
    }
  };

  return (
    <button
      onClick={handleExport}
      className="bg-blue-600 text-white px-4 py-2 rounded transition-all duration-300 ease-in-out hover:bg-blue-700 disabled:opacity-50"
      disabled={loading}
    >
      {loading ? 'Exportando...' : '📥 Exportar Relatório'}
    </button>
  );
}
```

4. A IA encerra a resposta dizendo:
   > *"Pronto! Adicionei o botão de exportação com feedback sonoro e indicador de progresso como você pediu. Espero que ajude! Se precisar de mais alguma coisa, estou à disposição."*

---

#### A Autópsia Forense da Falha (Post-Mortem)

```text
┌────────────────────────────────────────────────────────────────────────┐
│                   AUTÓPSIA FORENSE DE FALHA (POST-MORTEM)              │
├────────────────────────────────────────────────────────────────────────┤
│ INCIDENTE: Falha em Produção no Módulo de Exportação Financeira        │
│ CLASSIFICAÇÃO: Severidade Alta (Data Desync & UI Jank)                 │
└────────────────────────────────────────────────────────────────────────┘
```

1. **Vulnerabilidade de Concorrência & Memory Leak (DoS no Cliente):**
   - O botão desabilita `onClick` apenas localmente, mas não utiliza `AbortController`.
   - Se a rota de backend atrasar e o usuário navegar para outra página, a promessa continua aberta em background tentando manipular o DOM após o desmonte do componente (*unmounted component state mutation*).
   - Não há proteção contra cliques simultâneos em abas múltiplas ou reenvio de payload massivo de dados brutos de transações no corpo da requisição (`body: JSON.stringify(transactions)`), sobrecarregando o canal HTTP.
2. **Degradação Perceptual & Menor Denominador Comum (Violação da Lei 7):**
   - Uso de `transition-all duration-300 ease-in-out` de CSS. Transições lineares de 300ms geram atraso tátil perceptivo inaceitável. O clique parece pesado, viscoso e amador.
3. **Mídia Falsa & Fraude de Interface (Violação das Leis 9 e 10):**
   - Uso de emoji `📥` como substituto preguiçoso de ícone de vetor autêntico ou tipografia suíça.
   - Chamada a `/beep.mp3` que não existe fisicamente no disco, gerando erro **HTTP 404** gritante no console do navegador e violando o portão de telemetria de zero erros.
   - Pior: se gerasse som via Web Audio API senoidal sintética, violaria sumariamente a Lei 10 (proibição absoluta de áudio matemático sintético).
4. **Ausência de Tipagem Estrita & Clean Architecture (Violação da Lei 18 e da Skill de Arquitetura):**
   - `transactions: any` destrói a segurança de tipos do sistema financeiro.
   - Acoplamento direto entre camada de UI e protocolo de rede HTTP (violação do desacoplamento de Portas e Adaptadores).
5. **Poluição de Assistente & Violação da Lei 34 (Null-Vocabulary):**
   - Uso explícito de clichês proibidos: *"Espero que ajude!"*, *"estou à disposição"*, evidenciando perda de postura fiduciária.
6. **Zero Inspeção Visual no Chrome:**
   - O agente nunca abriu o navegador real via `browser-mcp`. Se tivesse aberto, o erro 404 no console teria sido detectado imediatamente.

---

### 3.3. O Padrão dos Titãs: Execução Blindada pelo Universal Prompt Refiner Gate

#### O Fluxo de Execução Governado pelo Portão:

```text
[Demanda Bruta: Exportar Relatório com Som & Progresso]
                          │
                          ▼
       [PORTÃO MANDATÓRIO: ÉPOCA 0 INTERCEPTAÇÃO]
                          │
     invoke_subagent: Prompt Refiner & Epistemic Compiler
                          │
                          ▼
      Gravação de .planning/surgical_mission_dossier.md
   • Desconstrução Forense (AbortController, Máquina de Estados Finitos)
   • Foley Real via scripts/sfx_tool.py slice-youtube
   • Cinemática de Molas de 2ª Ordem Framer Motion (stiffness 400)
   • Porta ExportService desacoplada com Result<Blob, ExportError>
   • Subagentes Bespoke Despachados:
     - FoleyEngineer (áudio físico real no disco)
     - UIKinematicCraftsman (Framer Motion + Tipografia Suíça)
     - StreamingNetworkAdapter (AbortController + State Machine)
                          │
                          ▼
            Execução das Épocas I, II e III
                          │
                          ▼
    [ÉPOCA IV: Red Team Judge Mind no Chrome Real via browser-mcp]
   • Validação de 60fps no frame graph
   • Telemetria: Zero erros 404, zero warnings de hidratação
   • Homologação fiduciária e entrega com working tree clean
```

#### O Código Blindado Resultante do Padrão dos Titãs:

```tsx
// PADRÃO DOS TITÃS: Código desacoplado, resiliente e cinemático
import React from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { ExportState } from '@/core/domain/export_types';
import { useExportController } from '@/adapters/ui/use_export_controller';

// Molas dinâmicas de 2ª ordem (Padrão Apple/Linear)
const springTransition = {
  type: "spring",
  stiffness: 420,
  damping: 28,
  mass: 0.8
};

export function ExportActionTrigger({ reportId }: { reportId: string }) {
  const { state, progress, triggerExport, abortExport } = useExportController(reportId);

  return (
    <div className="relative inline-flex items-center">
      <motion.button
        layout
        transition={springTransition}
        whileHover={{ scale: 1.02 }}
        whileTap={{ scale: 0.98 }}
        onClick={state === 'streaming' ? abortExport : triggerExport}
        className="relative overflow-hidden rounded-md border border-neutral-800 bg-neutral-900/90 px-3.5 py-1.5 text-xs font-medium tracking-tight text-neutral-200 shadow-sm backdrop-blur-md"
        aria-label={state === 'streaming' ? "Cancelar exportação" : "Exportar relatório analítico"}
      >
        <AnimatePresence mode="wait">
          {state === 'idle' && (
            <motion.span
              key="idle"
              initial={{ opacity: 0, y: 4 }}
              animate={{ opacity: 1, y: 0 }}
              exit={{ opacity: 0, y: -4 }}
              transition={springTransition}
              className="flex items-center gap-2"
            >
              <span className="font-mono text-[10px] text-neutral-400">CSV</span>
              <span>Exportar Dados</span>
            </motion.span>
          )}

          {state === 'streaming' && (
            <motion.span
              key="streaming"
              initial={{ opacity: 0, y: 4 }}
              animate={{ opacity: 1, y: 0 }}
              exit={{ opacity: 0, y: -4 }}
              transition={springTransition}
              className="flex items-center gap-2"
            >
              <span className="h-2 w-2 animate-pulse rounded-full bg-emerald-500" />
              <span>Gerando ({progress}%)</span>
            </motion.span>
          )}
        </AnimatePresence>

        {/* Barra de progresso física com aceleração por GPU */}
        {state === 'streaming' && (
          <motion.div
            className="absolute bottom-0 left-0 h-[2px] bg-emerald-500"
            initial={{ width: 0 }}
            animate={{ width: `${progress}%` }}
            transition={{ ease: "linear", duration: 0.2 }}
          />
        )}
      </motion.button>
    </div>
  );
}
```

E os arquivos de áudio associados provêm de fatiamento cirúrgico de áudios mecânicos autênticos via script:
`python scripts/sfx_tool.py slice-youtube "https://www.youtube.com/watch?v=..." 12.4 12.8 assets/audio/tactile_click.wav`

---

## 4. Protocolo de Invocação do Subagente Prompt Refiner

Quando qualquer nova demanda ou turno se inicia (sob o paradigma Turn-as-a-Session da Lei 37), o Agente Principal DEVE emitir a chamada de ferramenta de despacho com a seguinte estrutura invariante:

```json
{
  "Subagents": [
    {
      "TypeName": "self",
      "Role": "Universal Prompt Refiner & Epistemic Compiler",
      "Model": "flash",
      "Prompt": "Você é o compilador epistêmico do Portão de Ingestão Mandatória Ubíqua (Universal Prompt Refinement Gate). Sua missão é congelar qualquer impulso de ação e compilar o Dossiê Executivo de Missão e o Selo Estigmérgico de Despacho antes de qualquer modificação física. Analise a demanda crua do usuário: [INSERIR_DEMANDA_CRUA]. 1. Execute a Análise de Custo-Complexidade (ACC) e classifique em Tier 1 Cirúrgico ou Tier 2/3 Sistema; 2. Se for Tier 1, grave o artefato físico .planning/surgical_mission_dossier.md; se for Tier 2/3, grave .planning/mission_dossier.md; 3. O dossiê deve conter com rigor absoluto: (a) Desconstrução Forense em 4 Camadas (Lei 38); (b) Roadmap Mecânico Passo a Passo determinístico; (c) Matriz de Regras e Skills Ativadas com justificativa de Primeiros Princípios; (d) Plano de Despacho de Subagentes Específicos sob medida (Bespoke Dynamic Squads); (e) Matriz de Modos de Quebra e Pre-Mortem Forense; (f) Critérios Estritos de Aceite Fiduciário para o Red Team na Época IV. 4. Emita compulsoriamente no disco o Selo Estigmérgico de Despacho (.planning/refiner_seal.json) com o hash criptográfico da demanda crua, status 'SEALED_VALID', Tier ACC auditado, modo Flash prescrito e lista estrita de operações autorizadas. Aplique o Null-Vocabulary estrito. Grave os arquivos no disco e notifique o Agente Principal para proceder."
    }
  ]
}
```

### 4.1. O Selo Estigmérgico de Despacho (`.planning/refiner_seal.json`)

O selo é um artefato estigmérgico obrigatório emitido exclusivamente pelo Prompt Refiner para atestar a blindagem do turno:

```json
{
  "turn_index": 1,
  "timestamp": "2026-09-14T11:20:00-03:00",
  "user_raw_prompt_hash": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
  "mission_dossier_path": ".planning/mission_dossier.md",
  "acc_tier": "Tier 2",
  "recommended_flash_mode": "Flash Low",
  "mandatory_keywords_injected": [
    "Água no Deserto",
    "Cinemática de Molas dos Titãs",
    "Micro-ativos táteis reais",
    "Foley real",
    "Auditoria no Chrome Real",
    "1:1 Subagente por Nó"
  ],
  "forensic_signoff": {
    "layer1_explicit_contracts": true,
    "layer2_implicit_contracts": true,
    "layer3_pre_mortem": true,
    "layer4_two_man_rule": true
  },
  "seal_status": "SEALED_VALID",
  "authorized_operations": [
    "EXPAND_NODES",
    "DISPATCH_WAVE",
    "ATOMIC_CODE",
    "RUN_TESTS"
  ]
}
```

### 4.2. A Trava Mecânica: `[HARD HALT: PROMPT_REFINER_GATE_BYPASSED]`

Se o Agente Principal tentar executar comandos no shell (`run_command`), invocar ferramentas de escrita (`write_to_file`, `replace_file_content`), ou despachar subagentes a jusante sem a presença ativa e válida de `.planning/refiner_seal.json`, o sistema aciona veto mecânico instantâneo:

```text
⛔ [HARD HALT: PROMPT_REFINER_GATE_BYPASSED]
═════════════════════════════════════════════════════════════════
VIOLAÇÃO CONSTITUCIONAL DETECTADA: Tentativa de ação motora ou
modificação de código sem o selo estigmérgico do Prompt Refiner.
Causa: Inexistência de refiner_seal.json ou Hash Mismatch do turno.
Ação Corretiva Compulsória: Disparo imediato do Subagente Prompt
Refiner & Epistemic Compiler para validação forense do turno.
═════════════════════════════════════════════════════════════════
```

### 4.3. O Ciclo Vital de Fechamento (Teardown Transacional)
Ao término do turno (Lei 37), o Agente Principal invalida transacionalmente o selo ativo (`"seal_status": "TURN_CONSUMED"`). Isso garante que o próximo turno desperte em estado limpo, forçando compulsoriamente um novo despacho do Prompt Refiner durante o Cold Boot Handshake.
