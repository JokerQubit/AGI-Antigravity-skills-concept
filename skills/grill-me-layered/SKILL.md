---
name: grill-me-layered
description: MANDATORY. Protocolo de entrevista profunda em 12 tópicos organizados em 4 camadas progressivas (Escopo → Arquitetura → Debate → Contratos). Ativado pelo comando /grill-me ou quando o projeto exige alinhamento profundo antes de planejamento.
---

# 🔥 GRILL-ME LAYERED — Entrevista de Alinhamento em 12 Tópicos / 4 Camadas

> 🔴 **MANDATO:** Toda entrevista `/grill-me` para projetos complexos DEVE seguir este protocolo de 4 camadas. Cada camada só começa APÓS a camada anterior estar 100% resolvida. Proibido saltar camadas. Proibido fazer múltiplas perguntas de uma só vez. Uma pergunta por vez, com recomendação explícita da resposta preferida pelo agente.

---

## GATILHO DE ATIVAÇÃO

- Usuário digita `/grill-me` explicitamente
- Projeto com 5+ arquivos de implementação ou múltiplos sistemas integrados
- Agente detecta ambiguidades críticas que impossibilitam planejamento seguro
- Requisição muito vaga onde qualquer implementação poderia estar "correta"

---

## PROTOCOLO DE CONDUÇÃO

**Regras de Ouro:**
1. **Uma pergunta por vez** — nunca agrupar múltiplos tópicos
2. **Sempre fornecer recomendação** — apresentar a resposta que o agente acredita ser melhor, com justificativa técnica
3. **Usar `ask_question` com opções** — nunca fazer perguntas abertas sem opções
4. **Registrar todas as respostas** — ao final, gerar `GRILL_RESULTS.md` com decisões
5. **Desafiar respostas quando necessário** — se a resposta parece superficial ou contradiz uma resposta anterior, aprofundar antes de avançar

---

## CAMADA 1 — ESCOPO & INTENÇÃO (Tópicos 1-3)

> **Objetivo:** Entender o que o usuário realmente quer, não o que ele disse. Resolver ambiguidades de escopo antes de qualquer análise técnica.

### T1: Intenção Real
**Pergunta-raiz:** "O que você está tentando realmente alcançar com este projeto?"
- Identificar o problema de negócio subjacente, não apenas o feature solicitado
- Distinguir entre "o que foi pedido" e "o que resolve o problema"
- Verificar se existe uma solução mais simples que o usuário não considerou

**Checklist de resolução:**
- [ ] Problema de negócio claramente articulado
- [ ] Definição de sucesso mensurável
- [ ] Validação de que a solução proposta realmente resolve o problema

### T2: Escopo de Sucesso
**Pergunta-raiz:** "O que define que este projeto foi entregue com excelência?"
- Critérios objetivos e mensuráveis de sucesso
- O que o usuário vai testar primeiro ao ver o resultado
- Qual a métrica mais importante: performance? Estética? Funcionalidade? Escalabilidade?

**Checklist de resolução:**
- [ ] Definição de "DONE" é mensurável (não "parece bom")
- [ ] Critérios de qualidade por dimensão (funcional, visual, técnico)
- [ ] Teste de aceite claro que o usuário pode executar

### T3: Anti-Scope (O que NÃO fazer)
**Pergunta-raiz:** "O que está FORA do escopo e absolutamente não deve ser implementado?"
- Prevenir feature creep e gold-plating
- Identificar dependências externas que não serão construídas agora
- Estabelecer o que é MVP vs o que é "nice-to-have"

**Checklist de resolução:**
- [ ] Lista explícita do que está fora do escopo
- [ ] MVP claramente separado de extensões futuras
- [ ] Dependências externas mapeadas (o que existe, o que precisa ser criado)

---

## CAMADA 2 — ARQUITETURA & ANTI-ALUCINAÇÃO (Tópicos 4-6)

> **Objetivo:** Eliminar suposições perigosas e garantir que a arquitetura proposta está baseada em fatos verificáveis, não em chutes.

### T4: Restrições Técnicas Reais
**Pergunta-raiz:** "Quais são as restrições técnicas que o agente deve respeitar absolutamente?"
- Stack tecnológica (linguagem, framework, banco — com versões exatas)
- Ambiente de execução (OS, recursos de hardware, cloud provider)
- Integrações existentes que não podem ser alteradas
- Restrições de licença ou compliance

**Checklist de resolução:**
- [ ] Stack definida com versões exatas
- [ ] Ambiente de deploy especificado
- [ ] Integrações legadas mapeadas
- [ ] Restrições de recursos (CPU, memória, latência máxima)

### T5: Anti-Alucinação — Validação de Suposições
**Pergunta-raiz:** "Quais suposições o agente está fazendo que PODEM estar erradas?"
- O agente declara explicitamente suas suposições sobre o projeto
- O usuário valida ou corrige cada uma
- Eliminar `DEC::SPECULATIVE` antes de arquitetar

**Formato:**
```
O agente está assumindo:
1. [suposição A] — correto?
2. [suposição B] — correto?
3. [suposição C] — correto?
```

**Checklist de resolução:**
- [ ] Todas as suposições do agente foram listadas explicitamente
- [ ] Usuário validou cada suposição (confirmar ou corrigir)
- [ ] Zero `DEC::SPECULATIVE` restantes nas decisões críticas

### T6: Dados e Fontes Reais
**Pergunta-raiz:** "Quais dados o sistema vai consumir e de onde eles vêm?"
- APIs reais disponíveis (com credenciais ou plano de obtenção)
- Datasets existentes vs a serem criados
- Volumes esperados (quantos registros, quantas requisições/segundo)
- Dados mock aceitáveis somente em qual fase (nunca em produção)

**Checklist de resolução:**
- [ ] Fontes de dados reais identificadas com detalhes de acesso
- [ ] Volume de dados estimado (não "alguns registros")
- [ ] Estratégia para ausência de dados reais em desenvolvimento

---

## CAMADA 3 — DEBATE & FALSIFICAÇÃO (Tópicos 7-9)

> **Objetivo:** Forçar a máquina a pensar criticamente, se contradizer e identificar pontos de falha antes de qualquer implementação. Esta camada é o coração do grill-me.

### T7: Debate de Alternativas
**Pergunta-raiz:** "Quais são as 3 abordagens possíveis para este problema? Por que escolher esta e não as outras?"
- O agente apresenta 3 alternativas reais com prós/contras
- Justifica qual é a escolha recomendada com argumentos técnicos
- Usuário valida ou escolhe alternativa diferente (com entendimento dos trade-offs)

**Formato:**
```markdown
Alternativa A: [nome]
✅ Prós: [lista]
❌ Contras: [lista]
📊 Quando usar: [contexto ideal]

Alternativa B: [nome]
✅ Prós: [lista]
❌ Contras: [lista]

Alternativa C: [nome]
...

🏆 Recomendação: A porque [argumento técnico preciso].
```

**Checklist de resolução:**
- [ ] 3 alternativas genuínas avaliadas (não straw men)
- [ ] Trade-offs documentados sem viés para a recomendação
- [ ] Usuário entendeu os trade-offs antes de escolher

### T8: Mapeamento de Pontos de Falha
**Pergunta-raiz:** "O que pode dar terrivelmente errado? Quais são os 3 riscos críticos?"
- Análise adversarial da proposta escolhida
- Identificar: gargalos de performance, pontos únicos de falha, edge cases perigosos
- Definir plano de mitigação concreto para cada risco

**Formato:**
```markdown
RISCO-01: [descrição concreta]
- Probabilidade: Alta/Média/Baixa
- Impacto: Crítico/Alto/Médio
- Mitigação: [ação concreta]
- Plano B: [se a mitigação falhar]
```

**Checklist de resolução:**
- [ ] Top-3 riscos identificados com probabilidade e impacto reais
- [ ] Mitigação concreta (não "monitorar" sem ação)
- [ ] Plano B documentado para o risco mais crítico

### T9: Critério de Falsificação
**Pergunta-raiz:** "Como saberemos com CERTEZA que a solução falhou? Qual é o critério empírico de falsificação?"
- Definir métricas concretas que indicam falha (não "parece lento")
- Estabelecer thresholds: latência máxima aceitável, taxa de erro máxima, etc.
- Definir como e quando a solução será testada empiricamente

**Formato:**
```markdown
A solução é declarada FALHA se:
- [ ] Latência P99 > [X]ms em condições normais
- [ ] Taxa de erro > [Y]% em 24h de operação
- [ ] [métrica] exceder [threshold] por mais de [duração]

Protocolo de teste:
- Quando: [fase do projeto]
- Como: [ferramenta/método de teste]
- Por quem: [QA Worker / Red Team]
```

**Checklist de resolução:**
- [ ] Critérios de falha são mensuráveis e objetivos
- [ ] Thresholds numéricos definidos (não qualitativos)
- [ ] Protocolo de teste documentado

---

## CAMADA 4 — CONTRATOS & RELEASE (Tópicos 10-12)

> **Objetivo:** Formalizar os contratos de entrega, definir o que Q ≥ 9.0 significa para este projeto específico, e planejar o ciclo de vida pós-entrega.

### T10: Outputs Esperados (Entregáveis Formais)
**Pergunta-raiz:** "Liste EXATAMENTE o que deve ser entregue ao final deste projeto."
- Lista exata de arquivos, sistemas, documentos, APIs, interfaces
- Formato de cada entregável
- Onde cada entregável será deployado/armazenado

**Formato:**
```markdown
ENTREGÁVEIS OBRIGATÓRIOS:
- [ ] `src/core/engine.py` — Motor principal implementado e testado
- [ ] `docs/API.md` — Documentação completa de endpoints
- [ ] `tests/` — Suite com ≥ 90% de cobertura
- [ ] `docker-compose.yml` — Deploy one-command
- [ ] `PROJECT_BRAIN.md` — Mapa neural completo do projeto
```

**Checklist de resolução:**
- [ ] Lista de entregáveis é exaustiva e sem ambiguidade
- [ ] Formato de cada entregável especificado
- [ ] Localização de deploy/storage definida

### T11: Critérios de Aceite (Q ≥ 9.0 específico)
**Pergunta-raiz:** "O que define Q ≥ 9.0 para ESTE projeto específico?"
- Critérios de qualidade customizados ao domínio
- Gates de qualidade por fase do projeto
- Quem tem autoridade de declarar o projeto DONE

**Formato:**
```markdown
Q = 9.0 para [nome do projeto] exige:
- Funcional: [critérios específicos]
- Performance: [benchmarks numéricos]
- Visual/UX: [se aplicável]
- Segurança: [se aplicável]
- Documentação: [nível mínimo exigido]
- Testes: [cobertura mínima]
```

**Checklist de resolução:**
- [ ] Critérios de Q ≥ 9.0 são específicos ao projeto (não genéricos)
- [ ] Gates por fase definidos (não apenas gate final)
- [ ] Responsável pela aprovação final definido

### T12: Pós-Entrega & Sustentabilidade
**Pergunta-raiz:** "O que acontece depois da entrega? Quem vai usar, manter e evoluir este sistema?"
- Usuários finais e como serão onboardados
- Responsável pela manutenção
- Estratégia de evolução e extensão
- Documentação necessária para handoff

**Checklist de resolução:**
- [ ] Usuários finais identificados
- [ ] Estratégia de manutenção definida
- [ ] Documentação de handoff planejada

---

## OUTPUT FINAL: GRILL_RESULTS.md

Ao concluir os 12 tópicos, o agente gera automaticamente:

```markdown
# GRILL_RESULTS.md — [Nome do Projeto]
> Sessão: [timestamp] | Duração: [X] minutos | Tópicos resolvidos: 12/12

## CAMADA 1 — Escopo
- Intenção real: [resposta validada]
- Definição de sucesso: [critérios mensuráveis]
- Anti-scope: [lista do que está fora]

## CAMADA 2 — Arquitetura
- Stack: [especificação completa]
- Suposições validadas: [lista]
- Fontes de dados: [detalhes]

## CAMADA 3 — Debate
- Alternativa escolhida: [nome + justificativa]
- Top-3 riscos: [com mitigações]
- Critérios de falsificação: [métricas numéricas]

## CAMADA 4 — Contratos
- Entregáveis: [lista exaustiva]
- Q ≥ 9.0 significa: [critérios específicos]
- Pós-entrega: [plano]

## PRÓXIMOS PASSOS
→ Ativar `deep-planning-protocol` (5 documentos obrigatórios)
→ Ativar `project-neural-map` (criar PROJECT_BRAIN.md)
→ Ativar `corporate-swarm-os` (instanciar hierarquia de times)
```

Este arquivo é gerado em `.planning/GRILL_RESULTS.md` e referenciado no `PROJECT_BRAIN.md`.
