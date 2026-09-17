---
name: universal_prompt_refiner
description: Playbook de Engenharia e Controle Operacional do Portão de Ingestão Mandatória Ubíqua (Universal Prompt Refinement Gate) v4.1. Governa o despacho obrigatório do Subagente Prompt Refiner antes de qualquer intervenção operacional, a classificação mandatória de modo (Arquitetural vs. Direto), o gatilho de ativação imediata do esquadrão ([HARD HALT: SQUAD_DISPATCH_BYPASSED]), a compilação do Dossiê Universal (.planning/mission_dossier.md), desconstrução forense em 4 camadas, roadmap determinístico, matriz de regras/skills por primeiros princípios e critérios fiduciários de aceite.
---

# Universal Prompt Refiner Gate Playbook (Época 0 - v4.1)

Playbook operacional definitivo que rege o **Portão de Ingestão Mandatória Ubíqua (Universal Prompt Refinement Gate)**. Estabelece as duas travas mecânicas supremas do ecossistema:
1. **Trava de Refinamento:** O Agente Principal está terminantemente proibido de agir, planejar, editar arquivos ou rodar comandos modificadores sem antes despachar o Subagente Especialista Prompt Refiner (`[HARD HALT: PROMPT_REFINER_GATE_BYPASSED]`).
2. **Trava de Ativação do Esquadrão:** O Agente Principal está terminantemente proibido de mutacionar código sem antes despachar os subagentes do blueprint do Dossiê (`[HARD HALT: SQUAD_DISPATCH_BYPASSED]`).

Nenhuma intervenção operacional — seja a correção de uma vírgula de CSS, um script CLI pontual ou uma plataforma distribuída — é executada no impulso do prompt cru. Toda demanda é desconstruída, classificada em modo arquitetural ou direto, blindada por subagentes especializados e roteada com precisão cirúrgica antes de qualquer mutação física no repositório.

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

### 1.2. A Ubiquidade do Portão & A Bifurcação de Modo de Missão
A ilusão da "tarefa negligenciável" é a fonte primária de incidentes em sistemas de alta complexidade. Na v4.1, toda demanda passa pelo Portão do Prompt Refiner, mas a execução subsequente é calibrada por dois modos mutuamente exclusivos:

1. **MODO ARQUITETURAL / PLATAFORMA:**
   - Para criação de novas plataformas, módulos estruturais complexos ou refatorações profundas de arquitetura.
   - Dispara compulsoriamente a saturação exaustiva de **$N \ge 100$ nós atômicos** em `.planning/nodes/`.
2. **MODO DIRETO / OPERACIONAL / INVESTIGATIVO:**
   - Para correções de bugs, investigações de falhas, alterações diretas em arquivos existentes ou pequenas melhorias.
   - **Zero nós em disco (`nodes_floor: 0`)**. É terminantemente proibido poluir o disco com arquivos `.planning/nodes/`.
   - O plano é sintetizado diretamente em `implementation_plan.md` e 100% dos tokens são canalizados para os subagentes que investigam e codificam de fato.

---

## 2. Os Seis Entregáveis Obrigatórios do Dossiê Universal (`.planning/mission_dossier.md`)

Todo despacho do Subagente Prompt Refiner deve gerar compulsoriamente o Dossiê Universal contendo seis blocos fiduciários inegociáveis:

```text
┌────────────────────────────────────────────────────────────────────────┐
│                   ANATOMIA DOS SEIS ENTREGÁVEIS                        │
├────────────────────────────────────────────────────────────────────────┤
│ 1. Classificação de Modo & Desconstrução Forense (4 Camadas - Lei 38) │
│ 2. Roadmap Determinístico Passo a Passo (arquivo a arquivo)            │
│ 3. Matriz de Regras e Skills Ativadas (Primeiros Princípios)           │
│ 4. Bespoke Dynamic Squad Blueprint (Ordem Executiva de Despacho)       │
│ 5. Matriz de Modos de Quebra & Pre-Mortem Forense                      │
│ 6. Matriz de Checklists Forenses Extensivos & Aceite Fiduciário        │
└────────────────────────────────────────────────────────────────────────┘
```

### (a) Classificação de Modo & Desconstrução Forense da Demanda
- **Classificação:** `mission_type: "ARCHITECTURAL"` ($N \ge 100$ nós) ou `"DIRECT_OPERATIONAL"` (Zero nós em disco).
- **Contratos Explícitos (CE):** Declarações literais, entradas, saídas esperadas e restrições expressas pelo usuário.
- **Contratos Implícitos (CI):** Invariantes não ditos, mas mandatórios (idempotência, `AbortController`, ARIA, concorrência atômica, 60fps, latência $<16\text{ms}$, `Result<T, E>`).
- **Invariantes de Estado & Acoplamento:** Mapeamento do estado atual, dependências circulares e impacto em rotas/contratos existentes.

### (b) Roadmap Passo a Passo Exato
- Sequenciamento unívoco e mecânico de ações para o Agente Principal e para o enxame de subagentes.
- Definição estrita de dependências: sequencial vs concorrência paralela.
- Travas de isolamento: protocolo `HOLD/GO` no `synaptic_bus.json` para interfaces compartilhadas.

### (c) Matriz de Regras e Skills Ativadas com Justificativa de Primeiros Princípios
O Prompt Refiner fundamenta a ativação de cada regra e skill na **física real do problema** (ex: atrito de GPU, inércia de gesto, concorrência de arquivos).

### (d) Bespoke Dynamic Squad Blueprint (Ordem Executiva Compulsória de Despacho)
Em conformidade estrita com as Leis 32 e 40:
- **Ordem de Execução Mandatória:** A Seção D NÃO é decorativa; é uma ordem de despacho executiva imediata para o Agente Principal. Mutacionar código sem despachar os subagentes mapeados aciona `[HARD HALT: SQUAD_DISPATCH_BYPASSED]`.
- **Dupla Investigativa Obrigatória (Two-Mind Minimum):** Para qualquer tarefa investigativa ou alteração de arquivo existente, o esquadrão DEVE conter no mínimo:
  * **Subagente Alfa (Causal Root Cause):** Especialista na mecânica microscópica interna da falha ou alteração.
  * **Subagente Beta (Downstream Blast Radius):** Especialista no raio de impacto colateral, interfaces externas e contratos.
- **Parametrização Estrita:** Para cada subagente: `Role`, `TypeName: "self"` ou `"research"`, `Model: "flash"`, prompt cirúrgico Clean-Context e ferramentas autorizadas.

### (e) Matriz de Modos de Quebra e Pre-Mortem Forense
- Exercício Pre-Mortem: *"Assumindo que este código quebrou catastroficamente em produção 3 meses após o deploy, quais foram as causas raízes microscópicas?"*
- Mapeamento explícito de condições de corrida, memory leaks, quebra de contratos e degradação de frame-rate.

### (f) Matriz de Checklists Forenses & Critérios Estritos de Aceite Fiduciário
- Checklists binários de verificação [0 ou 1] por nó/arquivo (Lei 41).
- Métricas quantificáveis para o Subagente Juiz (Época IV): `$LASTEXITCODE === 0`, zero erros no console (`browser_console_logs`), zero stubs e inspeção visual perceptual aprovada no Chrome real via `browser-mcp`.

O artefato físico único de ingestão é `.planning/mission_dossier.md`. Qualquer tentativa de ignorar este artefato aciona `[HARD HALT]`.



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
      Gravação de .planning/mission_dossier.md
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
      "Prompt": "Você é o compilador epistêmico do Portão de Ingestão Mandatória Ubíqua (Universal Prompt Refinement Gate). Sua missão é congelar qualquer impulso de ação e compilar o Dossiê Executivo de Missão e o Selo Estigmérgico de Despacho antes de qualquer modificação física. Analise a demanda crua do usuário: [INSERIR_DEMANDA_CRUA]. 1. Execute a Análise de Custo-Complexidade (ACC) e classifique a missão compulsoriamente em mission_type: 'ARCHITECTURAL' (nova plataforma/módulo estrutural -> piso inegociável de 100 nós atômicos) ou 'DIRECT_OPERATIONAL' (bug fix/ajuste direto/investigação -> ZERO nós em disco, nodes_floor: 0, 100% tokens para execução real); 2. Grave o artefato físico .planning/mission_dossier.md (Dossiê Universal — único artefato permitido); 3. O dossiê deve conter com rigor absoluto: (a) Desconstrução Forense em 4 Camadas (Lei 38); (b) Roadmap Mecânico Passo a Passo determinístico; (c) Matriz de Regras e Skills Ativadas com justificativa de Primeiros Princípios; (d) Bespoke Dynamic Squad Blueprint (Seção D: ordem executiva mandatória de despacho de subagentes especializados 1:1, incluindo Dupla Investigativa Two-Mind Minimum para investigações); (e) Matriz de Modos de Quebra e Pre-Mortem Forense; (f) Critérios Estritos de Aceite Fiduciário para o Red Team na Época IV. 4. Emita compulsoriamente no disco o Selo Estigmérgico de Despacho (.planning/refiner_seal.json) com o hash criptográfico da demanda crua, status 'SEALED_VALID', session_mode: 'Universal v4.1 — Sovereign Session', mission_type ('ARCHITECTURAL' ou 'DIRECT_OPERATIONAL'), nodes_floor (100 ou 0), modo Flash prescrito e lista estrita de operações autorizadas. Aplique o Null-Vocabulary estrito. Grave os arquivos no disco e notifique o Agente Principal para proceder."
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
  "session_mode": "Universal v4.1 — Sovereign Session",
  "mission_type": "DIRECT_OPERATIONAL",
  "nodes_floor": 0,
  "recommended_flash_mode": "Flash Low",
  "mandatory_keywords_injected": [
    "Água no Deserto",
    "Cinemática de Molas dos Titãs",
    "Micro-ativos táteis reais",
    "Foley real",
    "Auditoria no Chrome Real",
    "1:1 Subagente por Nó / Arquivo",
    "Two-Mind Minimum"
  ],
  "forensic_signoff": {
    "layer1_explicit_contracts": true,
    "layer2_implicit_contracts": true,
    "layer3_pre_mortem": true,
    "layer4_two_man_rule": true
  },
  "seal_status": "SEALED_VALID",
  "authorized_operations": [
    "DISPATCH_SQUAD",
    "ATOMIC_CODE",
    "RUN_TESTS"
  ]
}
```

### 4.2. As Travas Mecânicas: `[HARD HALT]`

O ecossistema opera sob duas travas mecânicas intransponíveis:

1. **Portão do Refiner Bypassed (`[HARD HALT: PROMPT_REFINER_GATE_BYPASSED]`):**
   Tentativa de ação motora, comandos shell (`run_command`), ferramentas de escrita (`write_to_file`, `replace_file_content`) ou despacho a jusante sem a presença ativa de `.planning/refiner_seal.json` com status `SEALED_VALID`.
2. **Esquadrão Bypassed (`[HARD HALT: SQUAD_DISPATCH_BYPASSED]`):**
   Tentativa do Agente Principal de mutacionar código diretamente sem antes ter despachado o esquadrão de subagentes especializados definido na Seção D do `mission_dossier.md`.

```text
⛔ [HARD HALT: SQUAD_DISPATCH_BYPASSED]
═════════════════════════════════════════════════════════════════
VIOLAÇÃO CONSTITUCIONAL DETECTADA: Tentativa de mutação de código
sem o prévio despacho do Esquadrão Especializado mapeado na Seção D
do Dossiê Universal (.planning/mission_dossier.md).
Causa: Agente Principal agiu sozinho sem ativar as mentes do squad.
Ação Corretiva Compulsória: Disparo imediato dos subagentes do squad.
═════════════════════════════════════════════════════════════════
```

### 4.3. O Ciclo Vital de Fechamento (Teardown Transacional)
Ao término do turno (Lei 37), o Agente Principal invalida transacionalmente o selo ativo (`"seal_status": "TURN_CONSUMED"`). Isso garante que o próximo turno desperte em estado limpo, forçando compulsoriamente um novo despacho do Prompt Refiner durante o Cold Boot Handshake.

---

## 5. Geração da Matriz de Checklists Forenses da Cadeia Neural (Lei 41)

O Prompt Refiner deve compilar, dentro do `mission_dossier.md` (Seção E — Matriz de Checklists), a lista completa de critérios binários que cada subagente da Época III e o Red Team da Época IV devem verificar. Para cada arquivo ou nó a ser produzido, o dossiê lista:

| Critério | Descrição | Verificável em |
|---|---|---|
| Tipagem Estrita `Result<T,E>` | Zero `any`, `unknown` ou casts inseguros | TypeScript/source |
| Zero-Stub | Zero `TODO`, `pass`, `return null`, `{}` vazio | Grep no repositório |
| Física de Molas dos Titãs | `framer-motion` com stiffness/damping/mass reais; zero `transition-all duration-300` | Inspeção de código |
| Isolamento de Thread/GPU | Zero bloqueio de main thread; apenas `transform`/`opacity` | DevTools Performance |
| Áudio Físico Real | Gravações acústicas via `sfx_tool.py`; zero síntese por script | Grep por `AudioSynthesizer`/`oscillator` |
| Fotografia Óptica Real | `generate_image` com 6 variáveis ópticas; zero SVG genérico/emoji | Inspeção visual |
| Concorrência Atômica | Mutex sináptico (HOLD/GO); Atomic Swap na escrita; idempotência | Review de contrato |
| Telemetria Zero Erros | `$LASTEXITCODE === 0`; zero erros/warnings/404s no console | browser-mcp console |
| Pre-Mortem Blindado | Falha T+6 meses modelada e neutralizada em nó atômico | node_XXX_premortem.md |
| Null-Vocabulary | Zero preâmbulos, bajulação ou fórmulas de encerramento | Review de output |

O Red Team (Época IV) audita cada linha desta matriz com evidência física no disco ou no navegador. Qualquer item marcado como concluído sem evidência dispara `[HARD REJECT: FRAUDULENT_CHECKLIST_SIGNOFF]`.
