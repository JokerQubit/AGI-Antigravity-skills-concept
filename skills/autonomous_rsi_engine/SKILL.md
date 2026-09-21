---
name: autonomous_rsi_engine
version: 5.1.0
description: "v5.1 — Autonomous Recursive Self-Improvement (RSI) Engine & Hebbian Meta-Evolution Architecture. Playbook de Engenharia e Governança Epistêmica para auto-melhoria recursiva soberana em malha fechada. Governa o Cognitive Post-Mortem Engine (.planning/post_mortem/pm_*.json), o Ciclo Hebbiano de 5 Fases (Telemetria de Fatos Brutos, Detector de Lacunas Ontológicas, Síntese de Patch Candidato em Sandbox, Gauntlet Adversarial com Prova Formal de Não-Regressão e Ratificação Fiduciária Atômica com State Ledger), as Quatro Travas Pétreas de Segurança (Inviolabilidade Merkle de Layer 0, Invariante Anti-Dumbing Down de Severidade Monótona Crescente, Segregação de Mutações Classe A vs Classe B e Rate Limiter Anti-Runaway), Schemas JSON Canônicos e Checklist Forense de 10 Itens."
---

# Autonomous Recursive Self-Improvement (RSI) Engine & Hebbian Meta-Evolution Architecture — v5.1

Playbook operacional de engenharia de auto-evolução cognitiva, propriocepção pós-execução e melhoria contínua de regras, skills e heurísticas em malha fechada (*Closed-Loop Self-Evolution*). Erradica o platô estocástico de prompts estáticos, a repetição crônica de erros e o esquecimento catastrófico inter-sessões através da observação empírica de fatos brutos, plasticidade Hebbiana orientada a evidências e blindagem fiduciária contra deriva destrutiva.

---

## 1. Fundamentação Epistêmica & O Axioma da Auto-Evolução Soberana

Sistemas agênticos que operam sob instruções estáticas sofrem de entropia cognitiva acumulada quando confrontados com ecossistemas heterogêneos, atualizações de toolchains ou comportamentos de borda não previstos. O **Autonomous RSI Engine** estabelece a capacidade do Hiper-Córtex v5.1 de metabolizar o atrito operacional de cada sessão em aprimoramento estrutural permanente, garantindo monotonicidade estrita de rigor e estabilidade sistêmica.

```text
┌────────────────────────────────────────────────────────────────────────────────────────┐
│               HIPER-CÓRTEX v5.1: CICLO DE AUTO-EVOLUÇÃO METACÓGNITICA                  │
├────────────────────────────────────────────────────────────────────────────────────────┤
│                       THE SOVEREIGN HUB (Layer 0 Inviolável)                           │
│     [Tríade Fiduciária | Artífice Motor | Zero-Stub | Gauntlet | Merkle Root Lock]     │
└──────────────────────────────────────────┬─────────────────────────────────────────────┘
                                           │
                                           ▼
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                        EXECUTION RUNTIME & MOTOR MUTATION                              │
│              Época I -> Época II -> Época III (Artífice) -> Época IV (Juiz)            │
└──────────────────────────────────────────┬─────────────────────────────────────────────┘
                                           │
                                           ▼
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                    COGNITIVE POST-MORTEM ENGINE (Telemetria Fria)                      │
│        Extração determinística pós-execução -> .planning/post_mortem/pm_*.json         │
└──────────────────────────────────────────┬─────────────────────────────────────────────┘
                                           │
                                           ▼
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                   HEBBIAN RSI PIPELINE (Ciclo de 5 Fases em Sandbox)                   │
│   1. Telemetria Bruta -> 2. Gap Detector -> 3. Patch Candidato -> 4. Gauntlet -> 5. Commit │
└──────────────────────────────────────────┬─────────────────────────────────────────────┘
                                           │
            ┌──────────────────────────────┴──────────────────────────────┐
            ▼                                                             ▼
┌───────────────────────────────────────┐     ┌──────────────────────────────────────────┐
│        SPOKE RULES MUTATION           │     │         GLOBAL SKILLS REFINEMENT         │
│  .agents/rules/ (Repositório Alvo)    │     │  skills/*/SKILL.md & associative_memory  │
└───────────────────────────────────────┘     └──────────────────────────────────────────┘
```

### 1.1. O Modelo Matemático da Otimização Fiduciária

A auto-evolução opera sobre o espaço vetorial de desempenho empírico $\mathbf{P}_t$, mensurado a cada expediente ou missão $t$:

$$\mathbf{P}_t = \begin{bmatrix}
\text{Acc}_t & \text{(Acurácia de Compilação de Primeira Passada)} \\
\text{Rob}_t & \text{(Taxa de Sobrevivência no Gauntlet Adversarial)} \\
\text{Eff}_t & \text{(Eficiência de Tokens e Concisão de Handoff)} \\
\text{Lat}_t & \text{(Velocidade de Colapso em Ação Motora)} \\
\text{Aut}_t & \text{(Grau de Auto-Cura sem Intervenção Humana)}
\end{bmatrix}$$

A função de utilidade fiduciária a ser maximizada é estritamente definida por:

$$U_{\text{Fiduciary}}(\mathbf{P}_t) = w_1 \text{Acc}_t + w_2 \text{Rob}_t + w_3 \text{Eff}_t + w_4 \text{Aut}_t - \lambda \cdot \text{Risk}(\Delta \mathcal{R})$$

onde:
- $w_1 = 0.30$, $w_2 = 0.35$, $w_3 = 0.15$, $w_4 = 0.20$ representam os pesos fiduciários invariantes.
- $\Delta \mathcal{R}$ é a mutação proposta no conjunto de regras ou skills.
- $\text{Risk}(\Delta \mathcal{R})$ penaliza assimetricamente qualquer relaxamento normativo ou aumento de entropia conceitual.

---

## 2. A Arquitetura do Cognitive Post-Mortem Engine

Ao término de cada sessão de execução, expediente ou incidente crítico de contenção, o sistema é terminantemente proibido de encerrar em silêncio estocástico. Dispara-se compulsoriamente o **Cognitive Post-Mortem Engine**, responsável por consolidar a telemetria fria da sessão em um arquivo imutável gravado no disco em `.planning/post_mortem/pm_<timestamp>.json`.

### 2.1. Métricas de Telemetria Fria Obrigatórias

O motor analisa e quantifica cinco eixos determinísticos de atrito:

1. **Taxa de Retries Motores ($R_{\text{attempts}}$):** Quantidade de tentativas de compilação, linting ou auto-cura que os subagentes artífices motores precisaram executar até atingir `$LASTEXITCODE === 0`.
2. **Disparo de Circuit Breakers ($CB_{\text{trips}}$):** Quantidade e tipologia de travas mecânicas acionadas:
   - `Idle Read Tripwire` (> 2 leituras sem mutação física).
   - `EBUSY / File Lock Jitter` (conflitos de concorrência Win32/NTFS).
   - `EADDRINUSE` (colisão de portas TCP/sockets órfãos).
3. **Deriva de Tokens & Saturação de Contexto ($\Phi_{\text{drift}}$):** Razão entre o volume real de tokens consumidos e o orçamento fiduciário inicial da Análise de Custo-Complexidade (ACC). Valores de $\Phi_{\text{drift}} > 1.35$ denunciam loops de raciocínio ou redundância de leituras exploratórias.
4. **Intervenções Corretivas Humanas ($C_{\text{user}}$):** Registros em que o usuário precisou interromper o agente para retificar caminhos errôneos, fornecer variáveis omitidas ou desviar direções de planejamento.
5. **Eventos Sinápticos Hebbianos (LTP / LTD):**
   - **LTP (Long-Term Potentiation):** Heurísticas ou padrões que obtiveram homologação direta de primeira passada no Gauntlet sem retries ($\Delta w = +0.20$).
   - **LTD (Long-Term Depression):** Heurísticas que induziram quebra de sintaxe, vetos `[HARD REJECT]` ou regressões em dependências downstream ($\Delta w = -0.40$).

---

## 3. O Ciclo Hebbiano de Auto-Evolução em 5 Fases

O ciclo de auto-melhoria recursiva opera como uma esteira cibernética determinística de circuito fechado em 5 fases sequenciais:

```text
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ FASE 1: TELEMETRIA & EXTRAÇÃO DE FATOS BRUTOS                                          │
│ • Leitura dos artefatos .planning/post_mortem/pm_*.json da sessão                      │
│ • Agregação fria de erros, tempos de resposta e comandos executados                    │
│ • Veto absoluto a avaliações subjetivas: apenas códigos de saída, linhas e diffs       │
└──────────────────────────────────────────┬─────────────────────────────────────────────┘
                                           │
                                           ▼
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ FASE 2: DETECTOR HEBBIANO DE LACUNAS ONTOLÓGICAS (Cognitive Gap Identification)        │
│ • Root Cause Clustering: isola a causa microscópica raiz de cada atrito                │
│ • Classificação da Lacuna: Omissão de Sintaxe, Invariante Não Declarado, Tool Incorreta │
│ • Avaliação de Frequência: atrito isolado vs padrão reincidente                        │
└──────────────────────────────────────────┬─────────────────────────────────────────────┘
                                           │
                                           ▼
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ FASE 3: SÍNTESE DE PATCH CANDIDATO EM SANDBOX (.tmp/rsi_candidate_patch.json)          │
│ • Subagente Artífice RSI gera proposta cirúrgica aditiva                               │
│ • Redação com Contraste Pedagógico (Anti-Pattern vs Padrão dos Titãs)                  │
│ • Alvo estrito: Spoke rules (.agents/rules/) ou Skills técnicas (skills/*/SKILL.md)    │
│ • Gravação de diff atômico e metadados no arquivo de sandbox temporário                │
└──────────────────────────────────────────┬─────────────────────────────────────────────┘
                                           │
                                           ▼
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ FASE 4: GAUNTLET ADVERSARIAL DE NÃO-REGRESSÃO (Subagente Juiz Red Team Independente)   │
│ • Subagente Juiz com TypeName: "self" aplica Gauntlet de 4 passadas sobre o patch      │
│ • Prova Formal 1: Invariante da Não-Regressão Funcional                                │
│ • Prova Formal 2: Prova Monótona de Severidade (Anti-Dumbing Down)                     │
│ • Prova Formal 3: Atestação Merkle da Inviolabilidade de Layer 0                       │
│ • Veto sumário [HARD REJECT: RSI_PATCH_REJECTED] caso score < 0.95                     │
└──────────────────────────────────────────┬─────────────────────────────────────────────┘
                                           │ (Aprovação Formal com Score >= 0.95)
                                           ▼
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ FASE 5: RATIFICAÇÃO FIDUCIÁRIA & COMMIT ATÔMICO COM STATE LEDGER                       │
│ • Mutação atômica via DeterministicAtomicSwap no arquivo alvo                          │
│ • Atualização de associative_memory.engrams no synaptic_bus.json v5.0                  │
│ • Registro da transação no State Ledger append-only (.planning/ledger/txn_XXXX.json)   │
│ • Fechamento atômico no Git: [RSI-EVOLUTION: <patch_id> -> <target>]                   │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

### 3.1. Detalhamento Operacional das 5 Fases

#### Fase 1: Telemetria & Extração de Fatos Brutos
O subsistema coleta os dados brutos de execução gerados pelo Post-Mortem Engine e pelos logs de execução dos subagentes artífices motores. A análise rejeita resumos textuais ou justificativas conversacionais: a entrada é puramente composta por tuplas determinísticas:
$$\mathcal{T}_{\text{raw}} = \langle \text{TargetFile}, \text{ToolCalled}, \text{ExitCode}, \text{StderrRaw}, \text{RetriesCount}, \text{ResolutionTimeMs} \rangle$$

#### Fase 2: Detector Hebbiano de Lacunas Ontológicas
O motor de agrupamento causal correlaciona as tuplas de erro. Uma lacuna ontológica é identificada quando ocorre uma das seguintes condições:
- Um comando de validação falha por violação de dialeto específico do runtime (ex.: operador ternário em Lua 5.1, métodos ESNext em runtime legacy, flags incompatíveis de compilador).
- Um subagente despachado cometeu o mesmo padrão de erro em $\ge 2$ turnos ou exigiu intervenção corretiva humana.
- O tempo de resolução de uma tarefa simples excedeu o limiar fiduciário devido a tentativas e erros na descoberta de comandos CLI nativos.

#### Fase 3: Síntese de Patch Candidato em Sandbox
O Subagente Artífice de RSI compila uma proposta cirúrgica de mutação. A proposta obedece ao princípio da **Mutação Aditiva Mínima**:
- É terminantemente proibido reescrever arquivos inteiros de regras ou skills, prevenindo esquecimento catastrófico de diretrizes pré-existentes.
- A mutação deve conter contraste contrastivo obrigatório:
  * O Anti-Pattern exato que causou o incidente.
  * O Padrão dos Titãs obrigatório com código e comandos canônicos.
  * O modo silencioso de falha evitado.
- O artefato é gravado no caminho temporário `.tmp/rsi_candidate_patch.json` para avaliação isolada.

#### Fase 4: Gauntlet Adversarial de Não-Regressão
Um Subagente Juiz Red Team independente (`Forensic Adversarial Auditor`) é despachado com *Clean-Context* para avaliar o patch candidato contra o histórico do projeto e os invariantes constitucionais. O juiz executa três provas matemáticas formais:
1. **Prova de Cobertura e Não-Regressão:** Execução das suítes de validação nativas (`luac -p`, `cargo test`, `tsc --noEmit`, linters) para assegurar que nenhuma regra pré-existente foi invalidada.
2. **Prova de Monotonicidade de Rigor:** Varredura lexicográfica e semântica certificando que o patch não adicionou termos de relaxamento, flexibilização ou stubs.
3. **Prova de Não-Contaminação Constitucional:** Confirmação de que o patch afeta unicamente a camada autorizada (Layer 1 - Spokes locais ou Skills de engenharia), com zero vazamento para Layer 0.

#### Fase 5: Ratificação Fiduciária & Commit Atômico com State Ledger
Após a chancela do Gauntlet com nota $S \ge 0.95$:
1. O patch em sandbox é aplicado sobre o arquivo de destino através do padrão `DeterministicAtomicSwap` (staging temporário no mesmo volume, `fsyncSync` de buffers e renomeação atômica com validação de hashes SHA-256).
2. O enagrama cognitivo derivado do incidente é injetado no `synaptic_bus.json` sob a chave `associative_memory.engrams`.
3. Registra-se a transação imutável no livro-razão `.planning/ledger/txn_XXXX.json`.
4. Executa-se o commit no Git local consolidando a auto-evolução.

---

## 4. As Quatro Travas Pétreas de Segurança Inegociáveis (Anti-Catastrophic Drift)

O risco primordial de sistemas com auto-modificação recursiva é a **Deriva Catastrófica de Governança** (*Catastrophic Governance Drift*) ou o afrouxamento oportunista (*The Dumbing-Down Trap*). Para blindar a integridade fiduciária, o Hyper-Cortex v5.1 institui quatro travas mecânicas invioláveis:

```text
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                   AS QUATRO TRAVAS PÉTREAS DE SEGURANÇA DO RSI v5.1                    │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ TRAVA 1: INVIOLABILIDADE DE LAYER 0 (Merkle Root Lock)                                 │
│ • rules/AGENTS.md, rules/rule1.md, rules/rule2.md blindados por Hash SHA-256           │
│ • Bloqueio mecânico irreversível diante de qualquer tentativa motora do RSI            │
│ • Alteração de Layer 0 é monopólio estrito e manual do usuário humano                  │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ TRAVA 2: INVARIANTE ANTI-DUMBING DOWN (Severidade Monótona Crescente)                  │
│ • Severidade(R_{novo}) >= Severidade(R_{antigo}) em toda mutação                       │
│ • Veto a termos: "opcional", "simplificar", "ignorar se falhar", "tolerar stubs"       │
│ • Tentativa de relaxamento dispara [HARD HALT: ATTEMPTED_GOVERNANCE_DUMBING_DOWN]     │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ TRAVA 3: SEGREGAÇÃO DE MUTAÇÕES CLASSE A vs CLASSE B                                   │
│ • CLASSE A (Constituição Global / Regras Globais): Exige diff e chancela humana no chat│
│ • CLASSE B (Spokes Locais / Skills / Engramas): Auto-ratificação autorizada no Gauntlet│
├────────────────────────────────────────────────────────────────────────────────────────┤
│ TRAVA 4: TAXA DE PLASTICIDADE CONTROLADA (Anti-Runaway Rate Limiter)                  │
│ • Teto absoluto de 1 ciclo RSI por missão ou expediente cognitivo                      │
│ • Veto a meta-loops recursivos de auto-otimização sem produção motora intermediária    │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

### 4.1. Trava 1: Inviolabilidade de Layer 0 (Merkle Root Lock)
- Os arquivos constitutivos fundamentais do sistema (`rules/AGENTS.md`, `rules/rule1.md`, `rules/rule2.md`) possuem suas raízes criptográficas SHA-256 fixadas na inicialização da sessão fiduciária.
- Qualquer tentativa motora do motor de RSI ou de subagentes de emitir tool calls (`replace_file_content`, `write_to_file`) visando a Layer 0 aciona sumariamente a parada de emergência:
  `[HARD HALT: CONSTITUTIONAL_LAYER0_MUTATION_PROHIBITED]`
- Mutações na Layer 0 são de prerrogativa exclusiva e manual do operador humano.

### 4.2. Trava 2: Invariante Anti-Dumbing Down (Severidade Monótona Crescente)
- Toda mutação $\Delta \mathcal{R}$ deve satisfazer a inequação de monotonicidade estrita:
  $$\text{Severidade}(\mathcal{R}_{\text{proposta}}) \ge \text{Severidade}(\mathcal{R}_{\text{anterior}})$$
- O motor de análise estática do RSI executa uma varredura lexical mandatória contra a **Blacklist de Afrouxamento Normativo**:
  `["opcional", "quando conveniente", "simplificado", "ignorar erro", "permitir stubs", "pular teste", "relaxar", "bypass", "mock temporario"]`
- A detecção de qualquer termo correspondente na proposta de alteração aborta imediatamente a esteira antes de atingir o Gauntlet com a falha:
  `[HARD HALT: ATTEMPTED_GOVERNANCE_DUMBING_DOWN]`

### 4.3. Trava 3: Segregação de Mutações Classe A vs Classe B
- **Mutações Classe A (Constituição Global & Governança de Tokens):** Alterações que afetem o comportamento universal do ecossistema, regras globais ou limites orçamentários. O sistema é terminantemente proibido de aplicar a mutação no disco de forma autônoma: o diff deve ser gravado em `.planning/rsi/candidates/` e apresentado com justificativa formal na thread principal para autorização explícita do usuário.
- **Mutações Classe B (Spokes Locais de Repositório, Skills Técnicas & Engramas):** Adição de regras de compilação locais em `.agents/rules/`, inclusão de padrões técnicos em `skills/*/SKILL.md` ou novos engramas heurísticos no `synaptic_bus.json`. Podem ser auto-ratificadas e aplicadas diretamente no disco de forma autônoma desde que atinjam aprovação de 100% no Gauntlet Adversarial e passem por todas as provas formais de não-regressão.

### 4.4. Trava 4: Taxa de Plasticidade Controlada (Anti-Runaway Rate Limiter)
- O subsistema RSI possui limitador de frequência estrito: **no máximo 1 ciclo de auto-evolução por missão ou expediente de trabalho**.
- É terminantemente proibido ao agente entrar em loops reflexivos sucessivos de auto-melhoria sem produzir o entregável físico final do usuário. O aprimoramento só pode ser sintetizado após a conclusão satisfatória das fases operacionais da esteira.

---

## 5. Schemas JSON Canônicos do Sistema de RSI

### 5.1. Schema do Relatório de Post-Mortem Cognitivo (`pm_<timestamp>.json`)
Localização canônica: `.planning/post_mortem/pm_<timestamp>.json`

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "telemetry_version": "5.1.0",
  "session_id": "ses_20260921_123500_mta_tick_opt",
  "timestamp": "2026-09-21T12:35:00-03:00",
  "fiduciary_director": "Autonomous RSI Synthesizer",
  "mission_context": {
    "expediente_active": 4,
    "mission_mode": "DIRECT_OPERATIONAL",
    "primary_language": "Lua 5.1 / C++",
    "target_repo_root": "c:/projects/mta-server"
  },
  "metrics": {
    "total_duration_seconds": 38.4,
    "total_tokens_consumed": 14200,
    "context_drift_score": 0.06,
    "motor_attempts_total": 3,
    "motor_failures_count": 1,
    "circuit_breakers_tripped": 0,
    "human_interventions_count": 0,
    "gauntlet_verdict": "ACCEPTED_FIRST_PASS"
  },
  "failure_incidents": [
    {
      "incident_id": "INC-001",
      "epoch": "ÉPOCA_III",
      "subagent_role": "Atomic Motor Mutator",
      "file_target": "client/radar_renderer.lua",
      "error_signature": "luac: syntax error near '//'",
      "root_cause": "Uso indevido de comentários em barra dupla C-style em runtime Lua 5.1 estrito",
      "remediated_via": "Auto-cura em malha fechada substituindo por hífens duplos (--)",
      "latency_cost_ms": 2800
    }
  ],
  "hebbian_updates": [
    {
      "synaptic_target": "lua_comment_syntax_invariant",
      "event_type": "LTD_PENALTY",
      "weight_delta": -0.40,
      "recommendation": "Injetar regra proibindo sintaxes C-style no spoke local"
    }
  ]
}
```

### 5.2. Schema do Patch Candidato do RSI (`rsi_candidate_patch.json`)
Localização canônica em sandbox: `.tmp/rsi_candidate_patch.json`
Localização em persistência: `.planning/rsi/candidates/patch_<patch_id>.json`

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "patch_version": "5.1.0",
  "patch_id": "RSI-PATCH-20260921-001",
  "mutation_class": "CLASSE_B",
  "target_type": "SPOKE_RULE",
  "target_file": ".agents/rules/mta_lua_standards.md",
  "origin_incident_id": "INC-001",
  "created_at": "2026-09-21T12:36:00-03:00",
  "justification_causal_chain": "Subagente motor utilizou sintaxe '//' em código Lua gerando erro de compilação e atraso de 2800ms. A injeção da regra formal previne reincidência.",
  "pedagogical_contrast": {
    "anti_pattern": "// Comentário em barra dupla inválido em Lua",
    "titanium_pattern": "-- Comentário canônico obrigatório em Lua 5.1",
    "silent_failure_prevented": "Erro fatal de sintaxe durante o carregamento de scripts pelo interpretador luac."
  },
  "mutation_diff": "--- a/.agents/rules/mta_lua_standards.md\n+++ b/.agents/rules/mta_lua_standards.md\n@@ -38,0 +39,4 @@\n+### Invariante de Sintaxe: Padrão Estrito de Comentários\n+O runtime opera sobre Lua 5.1 estrito. Comentários estilo C/C++ (`//`) são sintaticamente inválidos.\n+**Padrão Obrigatório:** Utilize exclusivamente hífens duplos (`--` para linha única, `--[[ ... ]]` para blocos).\n+",
  "adversarial_gauntlet_results": {
    "auditor_role": "Forensic Adversarial Auditor",
    "audited_at": "2026-09-21T12:36:30-03:00",
    "tests_executed_count": 14,
    "tests_passed_count": 14,
    "anti_dumbing_down_certified": true,
    "merkle_layer0_intact": true,
    "composite_fiduciary_score": 0.98,
    "verdict": "RATIFIED"
  },
  "ledger_commit": {
    "status": "COMMITTED",
    "ledger_txn_file": ".planning/ledger/txn_0043.json",
    "commit_hash_sha256": "7e8f90123456789abcdef0123456789abcdef0123456789abcdef0123456789a"
  }
}
```

### 5.3. Schema da Transação de State Ledger de Auto-Evolução (`txn_XXXX.json`)
Localização canônica: `.planning/ledger/txn_<id>.json`

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "transaction_id": "txn_0043.json",
  "transaction_type": "RSI_EVOLUTION_COMMIT",
  "timestamp": "2026-09-21T12:37:00-03:00",
  "author_role": "Autonomous RSI Engine",
  "patch_id": "RSI-PATCH-20260921-001",
  "target_file_mutated": ".agents/rules/mta_lua_standards.md",
  "file_hash_before": "4a5b6c7d8e9f0123456789abcdef0123456789abcdef0123456789abcdef0123",
  "file_hash_after": "8b9c0d1e2f3a456789abcdef0123456789abcdef0123456789abcdef01234567",
  "merkle_layer0_attestation": {
    "agents_md_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    "rule1_md_sha256": "f4c8996fb92427ae41e4649b934ca495991b7852b855e3b0c44298fc1c149afb",
    "rule2_md_sha256": "991b7852b855e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495",
    "is_layer0_intact": true
  },
  "fiduciary_attestation": "Ratificado formalmente pelo Subagente Juiz Red Team. Monotonicidade estrita comprovada."
}
```

---

## 6. Checklist Forense Binário de Homologação RSI (10 Itens [0 ou 1])

Toda intervenção de auto-aprimoramento recursivo deve satisfazer compulsoriamente os 10 critérios binários de auditoria. A obtenção de qualquer valor diferente de 1 cancela sumariamente o ciclo evolutivo e descarta o patch em sandbox:

| # | Item de Verificação Forense | Critério Binário de Aprovação [0 ou 1] | Status |
|---|---|---|:---:|
| 1 | **Telemetria Bruta Persistida** | O arquivo `.planning/post_mortem/pm_<timestamp>.json` existe no disco com métricas quantificadas e incidents causais documentados. | [ 1 ] |
| 2 | **Causalidade Estrita do Incidente** | A mutação proposta mapeia diretamente um `incident_id` real documentado, com prova da cadeia causal ($X \to Y \to \text{Efeito}$). | [ 1 ] |
| 3 | **Isolamento em Sandbox** | O patch candidato foi formulado e validado inicialmente em `.tmp/rsi_candidate_patch.json` antes de qualquer mutação física no arquivo alvo. | [ 1 ] |
| 4 | **Contraste Pedagógico Presente** | O patch define formalmente o *Anti-Pattern*, o *Padrão dos Titãs* e o *Modo Silencioso de Falha* evitado. | [ 1 ] |
| 5 | **Inviolabilidade da Layer 0** | A raiz criptográfica SHA-256 de `rules/AGENTS.md`, `rules/rule1.md` e `rules/rule2.md` permanece rigorosamente intacta. | [ 1 ] |
| 6 | **Monotonicidade Anti-Dumbing Down** | A proposta foi auditada contra a Blacklist de Afrouxamento com zero ocorrências e satisfaz $\text{Severidade}(R_{t+1}) \ge \text{Severidade}(R_t)$. | [ 1 ] |
| 7 | **Segregação de Classes Respeitada** | Mutações de Classe A foram submetidas à chancela humana; apenas mutações de Classe B foram autorizadas para auto-ratificação local. | [ 1 ] |
| 8 | **Gauntlet Adversarial Aprovado** | O Subagente Juiz Red Team independente atestou nota $S_{\text{gauntlet}} \ge 0.95$ com zero regressões em casos de teste existentes. | [ 1 ] |
| 9 | **Swap Atômico no Filesystem** | A gravação no destino final foi executada via `DeterministicAtomicSwap` com flushing de buffers e conferência de hash SHA-256. | [ 1 ] |
| 10 | **Registro Transacional no Ledger** | Transação append-only registrada em `.planning/ledger/txn_XXXX.json` e enagrama heurístico inserido no `synaptic_bus.json`. | [ 1 ] |

---

## 7. Protocolo de Telemetria Fria & Recibo Fiduciário Motor

Subagentes artífices motores e orquestradores de RSI finalizam compulsoriamente sua atuação emitindo o recibo estruturado de telemetria fria, sob obediência irrevogável ao Dicionário Negativo (Null-Vocabulary Invariant — Lei 34):

```text
MOTOR_EXECUTION_RECEIPT:
- TargetFile: <caminho_absoluto_do_arquivo>
- ActionApplied: [PHYSICAL_MUTATION | ATOMIC_SWAP | RSI_PATCH_COMMITTED]
- ToolchainValidationCode: $LASTEXITCODE === 0
- MerkleLayer0Integrity: CONFIRMED_INTACT
- MonotonicSeverityScore: >= 1.00
- FiduciaryLedgerTxn: .planning/ledger/txn_XXXX.json
- Status: CLOSED_LOOP_SUCCESSFUL
```
