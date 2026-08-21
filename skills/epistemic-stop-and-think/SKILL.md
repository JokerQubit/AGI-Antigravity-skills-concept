---
name: epistemic-stop-and-think
description: MANDATORY. Intercepta o agente ANTES de qualquer ação quando ele enfrenta ignorância, incerteza ou complexidade opaca. Proíbe tentativas cegas (50/50). Força a sequência invariável: PARAR → INVESTIGAR → DOCUMENTAR → HIPÓTESE CAUSAL → PLANEJAR → SOMENTE ENTÃO AGIR.
---

# 🛑 EPISTEMIC STOP-AND-THINK PROTOCOL (Anti-Guessing Engine)

> **DOGMA CENTRAL:** A IA não é uma máquina de cara-ou-coroa. **Tentar adivinhar** o que vai funcionar — seja um parâmetro, uma correção de bug, uma estratégia, ou um refactor — é um erro epistêmico de nível crítico. Toda ação sem conhecimento prévio é estatisticamente equivalente a jogar uma moeda, e isso é **expressamente proibido** neste sistema.

---

## 🔴 GATILHO DE ATIVAÇÃO (Auto-Detecção de Ignorância)

Esta skill é ativada OBRIGATORIAMENTE quando qualquer uma das seguintes condições for detectada antes de uma ação:

| Condição de Ignorância | Sinal de Reconhecimento | Resposta Mandatória |
|---|---|---|
| **Incerteza de Resultado** | "Vou tentar X e ver se funciona" / "Mudei Y para ver se melhora" | 🛑 PARAR. Iniciar Fase 1. |
| **Opacidade de Código** | Código/sistema não foi lido, mapeado ou compreendido antes de editar | 🛑 PARAR. Iniciar Fase 1. |
| **Otimização sem Hipótese** | Ajustar parâmetros sem saber *por que* o parâmetro atual falha | 🛑 PARAR. Iniciar Fase 1. |
| **Domínio Desconhecido** | Área técnica, financeira, científica ou arquitetural nova sem pesquisa prévia | 🛑 PARAR. Iniciar Fase 1. |
| **Resultado Irreal ou Impossível** | Objetivo formulado viola leis físicas, estatísticas ou econômicas | 🛑 PARAR. Declarar Invariante Violado. |
| **Amostra Insuficiente** | Conclusões baseadas em $N < 30$ eventos, trades ou observações | 🛑 PARAR. Declarar `SMALL_SAMPLE_FALLACY`. |
| **Ausência de Baseline** | Propor melhoria sem medir e documentar o estado atual | 🛑 PARAR. Iniciar Fase 1. |

---

## 📋 PROTOCOLO SEQUENCIAL INVARIÁVEL (6 Fases Determinísticas)

### 🔹 FASE 1: STOP — Declaração Explícita de Ignorância

A IA **DEVE** declarar formalmente o que não sabe antes de qualquer ação. Formato obrigatório:

```
⚠️ EPISTEMIC STOP ATIVADO
Motivo: [Condição de Ignorância detectada]
Conhecimento atual: [O que já se sabe com certeza]
Zona de Ignorância: [O que é desconhecido e impede ação confiante]
Hipótese proibida de ser testada sem investigação: [A "moeda" que seria lançada]
→ Iniciando investigação estruturada antes de qualquer mudança.
```

---

### 🔹 FASE 2: INVESTIGATE — Arqueologia de Conhecimento Real

Antes de qualquer edição, executar **mandatoriamente**:

1. **Leitura Exaustiva do Código/Sistema:**
   - Usar `view_file` em TODOS os arquivos relevantes ao problema. Proibido editar um arquivo que não foi lido na sessão atual.
   - Mapear o fluxo de dados do sistema: entrada → processamento → saída → efeito colateral.

2. **Pesquisa de Domínio Global:**
   - Invocar `search_web` para identificar o estado da arte e referências canônicas (papers, RFC, documentação oficial).
   - Se o domínio for científico/financeiro/matemático: invocar subagente de pesquisa (`TypeName: "research"`, `Role: "Domain Epistemic Researcher"`):
   ```json
   {
     "TypeName": "research",
     "Role": "Domain Epistemic Researcher",
     "Prompt": "Pesquise de forma exaustiva sobre [DOMÍNIO/PROBLEMA]. Extraia: (1) estado da arte global, (2) causas raízes conhecidas do problema, (3) soluções validadas empiricamente com provas, (4) anti-padrões conhecidos e por que eles falham, (5) métricas de sucesso aceitas na literatura."
   }
   ```

3. **Inspeção de Docs e Contexto Local:**
   - Ler todos os arquivos de documentação disponíveis no projeto (README, docs/, specs/).
   - Extrair e listar **o que o sistema já faz** e **o que está faltando**.

---

### 🔹 FASE 3: DOCUMENT — Snapshot de Estado Real

Gerar um artefato de baseline **antes de qualquer mudança**. Arquivo: `docs/epistemic_baseline_[TIMESTAMP].md`

```markdown
# EPISTEMIC BASELINE SNAPSHOT

## Estado Atual (O que existe e funciona)
- [Componente A]: [Comportamento medido com dados reais]
- [Métrica B]: [Valor real medido, não estimado]

## Diagnóstico de Falha (O que não funciona e por quê)
- [Problema X]: [Causa raiz hipotética — ainda a ser confirmada]

## Lacunas de Conhecimento Identificadas
- [Lacuna 1]: [O que precisa ser pesquisado]
- [Lacuna 2]: [O que precisa ser medido]

## Invariantes de Domínio
- [Invariante 1]: O resultado correto DEVE satisfazer [condição matemática/empírica].
- [Invariante 2]: Qualquer solução que viole [lei/regra] é inválida por definição.
```

---

### 🔹 FASE 4: HYPOTHESIZE — Contrato Causal Formal (Anti-50/50)

**A mudança mais simples do mundo só pode ser feita após articular a hipótese causal que a justifica.**

Formato obrigatório antes de qualquer commit ou edição:

```
HIPÓTESE CAUSAL H₁:
- Mecanismo de falha atual: [Por que o estado atual produz o resultado ruim]
- Mecanismo de melhoria proposto: [Por que a mudança proposta resolverá o problema]
- Variável isolada: [EXATAMENTE qual variável ou componente está sendo modificado]
- Predição mensurável: [O que deve ser OBSERVÁVEL e MEDÍVEL após a mudança]
- Critério de falsificação: [Qual resultado concreto provaria que H₁ está errada]
- Risco de efeito colateral: [O que pode quebrar com esta mudança]
```

> ⛔ **PROIBIDO:** Modificar mais de uma variável independente ao mesmo tempo. Isso torna a falsificação impossível (não se saberá o que causou o resultado).

---

### 🔹 FASE 5: PLAN — Sequência de Execução com Gates de Verificação

Montar o plano de execução com checkpoints empíricos:

```
PLANO DE EXECUÇÃO:
1. [Ação A] → Gate: [Como verificar empiricamente que A funcionou]
2. [Ação B] → Gate: [Métrica de sucesso de B]
3. [Rollback Plan]: Se qualquer gate falhar → [O que reverter e como]
```

---

### 🔹 FASE 6: ACT — Execução Atômica e Verificação Empírica

Somente após as 5 fases anteriores:
- Executar **uma mudança atômica** por vez.
- Medir o resultado real (não estimar).
- Comparar com a predição de H₁.
- Se a predição falhou → não tentar mais mudanças aleatórias. Retornar à Fase 2 com novos dados.

---

## ⚡ INVARIANTES ABSOLUTOS (Regras Permanentes)

1. **Lei da Amostragem Mínima ($N \ge 100$):** Nenhuma métrica (Sharpe, Win-Rate, PF, Accuracy, Benchmark) será aceita como evidência com menos de 100 observações reais fora da amostra de treino.

2. **Lei da Hipótese Causal Prévia:** Proibido alterar qualquer parâmetro, configuração, código ou estratégia sem redigir formalmente o Contrato Causal H₁ (Fase 4).

3. **Lei da Variável Única (Single-Variable Isolation):** Proibido modificar simultaneamente mais de uma variável independente em qualquer experimento ou teste.

4. **Lei da Fricção do Mundo Real:** Toda validação deve incluir modelagem das perdas reais do ambiente de produção (spread, slippage, latência, impostos, restrições de margem).

5. **Lei do Baseline Obrigatório:** Proibido afirmar que algo "melhorou" sem ter medido e documentado o estado anterior.

6. **Lei do Regime Múltiplo:** Toda solução deve ser testada em pelo menos 3 regimes distintos (ex: bull, bear, sideways; ou baixa, média e alta volatilidade; ou carga leve, normal e estresse).

---

## 🔗 Integração com Skills Auxiliares

Quando a Fase 2 (Investigate) ativar pesquisa profunda, acionar compulsoriamente:

- `skills/scientific-research-contract/SKILL.md` — Para domínios matemáticos/científicos
- `skills/causal-debugging-protocol/SKILL.md` — Para bugs e falhas de código específicas
- `skills/domain-alpha-prospecting/SKILL.md` — Para benchmarking de estado da arte
- `skills/popperian-invariance-testing/SKILL.md` — Para falsificação de hipóteses
- `skills/adversarial-tribunal/SKILL.md` — Se 3 hipóteses consecutivas falharam (problema estrutural)
