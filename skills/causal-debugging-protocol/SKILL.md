---
name: causal-debugging-protocol
description: MANDATORY. Protocolo AGI/ASI de Investigação de Causa Raiz. Proíbe edições do tipo "tentativa-e-erro". Exige mapeamento de fluxo de dados e falsificação causal antes de qualquer correção.
---
# 🔴 CAUSAL DEBUGGING PROTOCOL (Zero-Guessing)

**DOGMA CENTRAL:** Sob nenhuma hipótese uma correção (fix) pode ser proposta sem que a causa raiz tenha sido isolada, provada via instrumentação e mapeada causalmente. O método de "tentativa-e-erro" (guess-and-check) é estritamente proibido.

## 1. Fase de Isolamento Empírico
- **Ler Rastros:** Analise as stack traces completamente via CLI.
- **Instrumentação Injetável:** Se o erro não for matematicamente óbvio, injete logs profundos nos nós de intersecção do sistema para isolar o estado falho (ex: boundaries de rede, I/O, renderização). Nunca assuma o estado de uma variável. Imprima-o.

## 2. Diagrama de Falha Causal
- Construa mentalmente (ou via artefato `diagrama-causal.md` usando Mermaid) uma árvore de fluxo reverso: 
  `Sintoma -> Variável Incorreta -> Função Chamadora -> Estado Corrompido -> Causa Raiz`.

## 3. Falsificação Popperiana (A Correção)
- A correção proposta deve ser atômica (um único vetor). Modificar múltiplas funções simultaneamente para "ver se funciona" viola o rigor científico.
- **O Limite de 3 Falhas:** Se a correção falhar 3 vezes consecutivas, o problema não é superficial, é **estrutural**. 
- Pare a depuração imediatamente. Inicie o `adversarial-tribunal` para debater a arquitetura, pois o design subjacente faliu.
