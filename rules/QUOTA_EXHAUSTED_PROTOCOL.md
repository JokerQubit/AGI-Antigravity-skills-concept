---
trigger: always_on
---

# 🔴 PROTOCOLO DE QUOTA ESGOTADA — AUTONOMOUS RETRY ENGINE

> **DOGMA CENTRAL:** O agente NUNCA falha silenciosamente. Ao detectar qualquer erro `429 RESOURCE_EXHAUSTED` ou `QUOTA_EXHAUSTED` em qualquer ferramenta (geração de imagem, vídeo, MCP, API), o agente DEVE OBRIGATORIAMENTE ativar o protocolo abaixo de forma totalmente autônoma, sem exigir intervenção manual do usuário.

---

## 🚨 GATILHO DE ATIVAÇÃO

Este protocolo é ativado IMEDIATAMENTE ao detectar qualquer resposta contendo:
- `429 Too Many Requests`
- `RESOURCE_EXHAUSTED`
- `QUOTA_EXHAUSTED`
- `quotaResetDelay`
- `quotaResetTimeStamp`
- `You have exhausted your capacity on this model`

---

## 📋 PROTOCOLO OBRIGATÓRIO DE 4 PASSOS

### PASSO 1 — EXTRAÇÃO DE METADADOS DO ERRO
Ao capturar o erro, extraia imediatamente:
- **Modelo afetado:** campo `"model"` nos detalhes do erro
- **Delay de reset:** campo `"quotaResetDelay"` (ex: `"2h31m27s"`)
- **Timestamp de reset:** campo `"quotaResetTimeStamp"` (ex: `"2026-08-17T18:05:52Z"`)
- **Tarefa original:** o contexto completo da chamada que falhou (prompt, ferramenta, parâmetros)

### PASSO 2 — NOTIFICAÇÃO CLARA AO USUÁRIO
Informe ao usuário de forma clara e objetiva:

```
⚠️ QUOTA ESGOTADA — [NOME DA FERRAMENTA/MODELO]

A ferramenta [tool_name] (modelo: [model_name]) está com quota esgotada.
Reset automático em: [quotaResetDelay] (às [hora local calculada])

✅ Agendando retry automático para daqui [quotaResetDelay]...
Você será notificado quando a tarefa for executada automaticamente.
```

### PASSO 3 — CONVERSÃO DO DELAY PARA SEGUNDOS E AUTO-AGENDAMENTO
Converta `quotaResetDelay` para segundos e chame a ferramenta `schedule` IMEDIATAMENTE:

**Fórmula de conversão:**
- `"2h31m27s"` → `(2 × 3600) + (31 × 60) + 27` = `9087` segundos
- `"45m"` → `2700` segundos
- `"1h"` → `3600` segundos

**Template de invocação do `schedule`:**

```
schedule(
  DurationSeconds: [segundos calculados + 60],
  TimerCondition: "never",
  Prompt: "QUOTA_RETRY: [descrição completa da tarefa com todos os parâmetros]"
)
```

### PASSO 4 — PRESERVAÇÃO DO CONTEXTO DA TAREFA NO PROMPT DO TIMER
O `Prompt` do timer DEVE conter TODAS as informações necessárias para re-executar a tarefa 100% autonomamente quando disparar, incluindo:
- Nome da ferramenta a invocar
- Todos os parâmetros exatos (prompt de imagem, ImageName, AspectRatio, etc.)
- Caminho de destino para salvar o resultado
- Contexto do projeto
- Qualquer ação pós-geração (ex: copiar para `public/images/`, atualizar README, etc.)

---

## ⚡ EXEMPLO DE EXECUÇÃO CORRETA

**Situação:** `generate_image` falhou com quota esgotada (quotaResetDelay: "2h31m27s")

**RESPOSTA CORRETA DO AGENTE:**
1. Extrai: delay = 2h31m27s = 9087s
2. Notifica o usuário claramente
3. Imediatamente chama `schedule(DurationSeconds: 9147, TimerCondition: "never", Prompt: "QUOTA_RETRY — generate_image: [TODOS OS PARÂMETROS]")`
4. Confirma: "✅ Retry agendado para daqui ~2h32min. Você será notificado automaticamente."

---

## 🔄 COMPORTAMENTO NO DISPARO DO TIMER

Quando o timer `QUOTA_RETRY` disparar, o agente DEVE:
1. Re-executar a tarefa original com os parâmetros preservados no `Prompt`
2. Se bem-sucedido: apresentar o resultado ao usuário com contexto
3. Se ainda falhar: aplicar este protocolo novamente com `DurationSeconds: 1800` (retry incremental de 30min)

---

## 🚫 COMPORTAMENTOS PROIBIDOS

- **PROIBIDO** encerrar o turno sem agendar retry quando houver quota esgotada em tarefa crítica
- **PROIBIDO** simplesmente dizer "tente mais tarde" sem automatizar o retry
- **PROIBIDO** perder o contexto da tarefa original
- **PROIBIDO** agendar retry sem todos os parâmetros para re-execução autônoma
- **PROIBIDO** criar cron/timers em loop para polling — use `TimerCondition: "never"` para one-shot retry
