---
name: autonomous_computer_use
version: 4.0
description: "v4.0 — Universal Cognitive Parity — Autonomous Computer Use & OODA Closed-Loop. Playbook de Engenharia e Controle Operacional para Computer Use Autônomo de nível AGI. Governa o Ciclo OODA em malha fechada (Observe -> Orient -> Decide -> Act), a hierarquia mecânica de menor atrito motor (Arquivo/CLI > DOM > GUI XY), protocolos determinísticos de auto-cura (portas presas EADDRINUSE, processos órfãos, locks de arquivos EBUSY/EPERM, caches corrompidos), verificação sensorial em navegador real via browser-mcp com telemetria de zero erros e Checklist Forense Binário obrigatório (Lei 41)."
---

# Autonomous Computer Use & Closed-Loop Motor Control — v4.0 (Universal Cognitive Parity)

Manual de engenharia e governança de interação motora, sensorial e computacional com o sistema operacional (Windows 11, PowerShell, Node.js, compiladores, processos em background) e navegador web via `browser-mcp`. Estabelece o fim definitivo do paradigma amador "dispare e reze" (*fire-and-forget*), impondo **autonomia de malha fechada, propriocepção de ambiente e auto-cura determinística**.

Na v4.0.0, o Ciclo OODA em Malha Fechada e o Self-Healing Protocol são disparados compulsoriamente em toda ação motora — sem distinção entre "comando simples" e "pipeline complexo". Não existe comando CLI que dispense verificação sensorial pós-execução (`$LASTEXITCODE === 0` e ausência de stderr fatais).

---

## 1. O Ciclo Cibernético OODA em Malha Fechada

Toda ação motora sobre o computador deve executar compulsoriamente os quatro quadrantes do ciclo OODA:

```text
┌─────────────────────────────────────────────────────────────┐
│ 1. OBSERVE (Sensoriamento Multimodal & Telemetria Fria)     │
│ • Shell: $LASTEXITCODE, stdout, stderr, consumo de memória  │
│ • Rede: Get-NetTCPConnection, portas ativas e sockets       │
│ • Disco: Test-Path, integridade de bytes e file locks       │
│ • Browser: DOM estável, AXTree, network in-flight, logs     │
└─────────────────────────────┬───────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│ 2. ORIENT (Mapeamento Causal & Propriocepção de Estado)     │
│ • Confronto do estado medido vs invariante arquitetural     │
│ • Discriminação: Falha de Domínio vs Falha de Ambiente      │
│ • Modelagem de impacto de 2ª ordem sobre processos filhos   │
└─────────────────────────────┬───────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│ 3. DECIDE (Algoritmo Determinístico da Menor Ação)          │
│ • Seleção do canal de menor resistência física              │
│ • Ativação de playbook de remediação / retry com jitter     │
│ • Fixação do critério exato de validação de repouso         │
└─────────────────────────────┬───────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│ 4. ACT & VERIFY (Disparo Motor Atômico & Retorno à Malha)   │
│ • Execução da primitiva motora com timeout defensivo        │
│ • Invariante: Nunca encerra em Act; transita obrigatoriamente│
│   de volta para Observe para certificar o novo estado       │
└─────────────────────────────────────────────────────────────┘
```

---

## 2. Hierarquia Mecânica de Menor Atrito Motor

A estabilidade da execução é inversamente proporcional aos graus de liberdade estocásticos da interface:

$$\text{Confiabilidade} \propto \frac{1}{\text{Graus de Liberdade Visual} \times \text{Latência de Renderização}}$$

| Nível de Canal | Primitiva Motora | Custo de Atrito | Caso de Uso Mandatório | Veto / Restrição |
|---|---|---|---|---|
| **Nível 1 (Ótimo)** | Manipulação Direta de Arquivo/AST (`write_to_file`, `replace_file_content`) | Mínimo (<10ms, determinismo 100%) | Escrita de código, configs, refactors, documentação. | Proibido usar editores interativos em shell (`nano`, `vim`). |
| **Nível 2 (Forte)** | Shell CLI Nativo & Subprocessos (`run_command` via PowerShell) | Baixo (exit-codes estritos, pipes) | Compilação, testes unitários, linters, git, gerenciamento de PIDs. | Proibido comandos com prompts interativos sem automação de flag (`-y`, `-Force`). |
| **Nível 3 (Médio)** | APIs Locais & Sockets HTTP/TCP (`Invoke-WebRequest`, IPC) | Moderado (depende de listener) | Health-checks ativos de servidores de desenvolvimento e endpoints. | Proibido assumir que o server subiu usando `sleep` sem testar o socket. |
| **Nível 4 (Alto)** | Ações Semânticas de DOM no Navegador (`browser_click`, `browser_fill`) | Alto (sujeito a hidratação de SPA e reflow) | Testes funcionais E2E em formulários, botões, modais com seletores estáveis. | Proibido clicar sem aguardar a estabilização de rede (`browser_wait_for_network`). |
| **Nível 5 (Último Recurso)** | Interação Visual Espacial GUI (`browser_click_xy`, coordenadas ópticas) | Máximo (extremamente frágil a DPI/zoom) | Superfícies sem nós no DOM (Canvas 3D, WebGL, drag-and-drop livre). | **Veto Absoluto** em botões, links ou inputs acessíveis via DOM. |

---

## 3. Playbooks Determinísticos de Auto-Cura e Resiliência Operacional

É terminantemente proibido ao agente congelar ou delegar ao usuário a solução de atritos operacionais triviais do ambiente de execução. Diante de falhas, execute o playbook cabível:

### A. Colisão de Sockets & Portas Presas (`EADDRINUSE`)
*Sintoma:* Um dev server falha ao subir porque a porta designada (ex: `3000`) já está em uso por processo anterior ou zumbi.
*Playbook PowerShell de Auto-Cura:*
```powershell
$TargetPort = 3000
$Connection = Get-NetTCPConnection -LocalPort $TargetPort -State Listen -ErrorAction SilentlyContinue
if ($Connection) {
    $ZombiePID = $Connection.OwningProcess
    # Encerra em cascata o processo ocupante e seus filhos
    taskkill /PID $ZombiePID /T /F | Out-Null
    # Polling determinístico de liberação de socket (máximo 3000ms)
    $Timeout = 0
    while ((Get-NetTCPConnection -LocalPort $TargetPort -State Listen -ErrorAction SilentlyContinue) -and ($Timeout -lt 15)) {
        Start-Sleep -Milliseconds 200
        $Timeout++
    }
}
```
*Fallback Determinístico:* Caso a porta permaneça bloqueada pelo kernel no estado `TIME_WAIT`, selecione a próxima porta sequencial ($N+1$) e atualize a variável de ambiente correspondente.

---

### B. Processos Órfãos & Zumbis de Compilação
*Sintoma:* Processos de empacotamento (`esbuild`, `node`, `vite`, `next-server`) travam consumindo CPU ou retendo descritores de arquivos.
*Playbook de Encerramento em Árvore:*
```powershell
# Localiza e elimina a linhagem inteira do processo órfão
taskkill /PID <PID_ALVO> /T /F
```

---

### C. Arquivos Travados por Locks do Sistema (`EBUSY`, `EPERM`)
*Sintoma:* Tentativa de reescrita de arquivo falha porque o Windows Defender, o Search Indexer ou um processo em background está inspecionando o arquivo.
*Playbook de Remediação em 2 Etapas:*
1. **Exponential Backoff com Jitter:** Tente 3 vezes com espaçamento progressivo ($200\text{ms} \to 500\text{ms} \to 1200\text{ms}$).
2. **Atomic Swap Transacional:** Grave os novos dados em arquivo sombra (`<target>.tmp.<guid>`) e execute a substituição atômica via `Move-Item -Force`.

---

### D. Caches Corrompidos de Ferramentas de Build
*Sintoma:* Erros inexplicáveis de compilação ou importação circular persistindo após edições corretas.
*Playbook de Purga de Caches:*
```powershell
# Remove deterministamente os diretórios de cache efêmeros
Remove-Item -Recurse -Force .next, dist, build, node_modules/.cache, .turbo -ErrorAction SilentlyContinue
# Re-valida estritamente a tipagem
npx tsc --noEmit
```

---

### E. Estabilização de DOM & Sincronização Assíncrona no `browser-mcp`
*Sintoma:* O subagente clica em um botão, mas a ação falha porque o React/Vue ainda estava hidratando o componente ou uma animação de mola ainda estava em curso.
*Playbook de Estabilização:*
1. Disparar `browser_wait_for_network(Timeout: 5000)` para garantir zero requisições in-flight.
2. Executar script de validação de repouso: `document.readyState === 'complete'`.
3. Selecionar o elemento via `data-testid` ou atributos semânticos estritamente estáveis, jamais por classes utilitárias voláteis (`css-1a2b3c`).

---

## 4. Protocolo de Fechamento de Malha (Closed-Loop Verification Protocol)

Nenhuma tarefa de Computer Use é considerada concluída sem a satisfação cumulativa da **Triangulação de Telemetria**:

1. **Telemetria de Shell:** O comando executado encerrou com `$LASTEXITCODE === 0`.
2. **Telemetria de Runtime:** Ausência de exceções não capturadas (`UnhandledPromiseRejection`, `Fatal error`) em `stderr`.
3. **Telemetria de Navegador (`browser_console_logs`):**
   - **ZERO** erros de JavaScript no console.
   - **ZERO** erros 404 de carregamento de mídia, imagens, áudios ou fontes.
   - **ZERO** avisos de quebra de hidratação ou chaves duplicadas no React.
4. **Health-Check Ativo:** Serviços locais só são considerados operacionais após resposta HTTP 200 via pooling de socket, banindo sleeps cegos.

---

## 5. Exemplar Contrastivo de Computer Use (Lei 36)

### Cenário:
> **Demanda:** *"Suba o servidor de desenvolvimento local, abra a aplicação no navegador e valide a tela inicial."*

---

### ❌ WRONG (Anti-Pattern: Dispare e Reze da Média da Web):
```powershell
npm run dev
Start-Sleep -Seconds 4
# Chamada cega: browser_navigate("http://localhost:3000")
# Chamada frágil: browser_click_xy(380, 210)
```

#### 🔬 Autópsia de Falha Post-Mortem:
1. **Colisão Silenciosa de Porta:** Se a porta 3000 já estava aberta, o Vite sobe na 3001. O agente navega para a 3000 e interage com uma aplicação morta ou irrelevante.
2. **Suposição Temporal Cega:** O `sleep 4` falha se o bundling demorar 4.2 segundos (gera `ERR_CONNECTION_REFUSED`), e desperdiça 3.5 segundos se o cache estiver quente.
3. **Coordenadas Espaciais Frágeis:** `browser_click_xy(380, 210)` quebra se a resolução da janela mudar ou se houver uma barra de aviso que desloque os elementos 10 pixels para baixo.
4. **Abandono Fiduciário:** Se o terminal emitir um erro, o agente para e pede ajuda ao usuário: *"A porta 3000 está ocupada, por favor encerre o processo"*.
5. **Cegueira a Erros de Console:** A aplicação pode estar renderizando uma tela cinza com erro de import circular, mas o agente declara vitória sem inspecionar os logs do Chrome.

---

### ✅ CORRECT (Padrão Titã: Computer Use Autônomo em Malha Fechada AGI):
```powershell
# 1. OBSERVE & AUTO-CURA: Limpeza profilática de portas
$Port = 3000
$Zombie = Get-NetTCPConnection -LocalPort $Port -State Listen -ErrorAction SilentlyContinue
if ($Zombie) {
    taskkill /PID $Zombie.OwningProcess /T /F | Out-Null
    Start-Sleep -Milliseconds 400
}

# 2. DECIDE & ACT: Inicialização de processo em segundo plano monitorado
# Executa npm run dev mantendo controle de processo

# 3. CLOSED-LOOP HEALTH-CHECK: Polling ativo com timeout determinístico
$Ready = $false; $Attempts = 0
while (-not $Ready -and $Attempts -lt 30) {
    try {
        $Response = Invoke-WebRequest -Uri "http://127.0.0.1:$Port" -UseBasicParsing -TimeoutSec 1
        if ($Response.StatusCode -eq 200) { $Ready = $true }
    } catch {
        $Attempts++
        Start-Sleep -Milliseconds 250
    }
}
if (-not $Ready) { throw "Falha na inicialização do servidor local na porta $Port" }

# 4. BROWSER CLOSED-LOOP: Navegação semântica via browser-mcp
# - browser_navigate("http://127.0.0.1:3000")
# - browser_wait_for_network(Timeout: 5000)
# - browser_click(Selector: "[data-testid='primary-action-button']")
# - browser_console_logs() -> validação de ZERO erros e warnings
# - browser_screenshot() -> persistência da prova visual de alta definição no disco
```

---

## Checklist Forense de Autonomous Computer Use (Binário — Lei 41)

> Auditado pelo Agente Principal após cada ação motora e confirmado pelo Red Team na Época IV. Um único item reprovado sem evidência física dispara `[HARD REJECT: FRAUDULENT_CHECKLIST_SIGNOFF]`.

- [ ] **$LASTEXITCODE === 0:** todo comando shell retornou exit code 0; zero execuções "fire-and-forget" sem verificação pós-execução.
- [ ] **Zero stderr Fatal:** ausência de exceções fatais, stack traces não capturadas ou mensagens `ERROR` em stderr.
- [ ] **Hierarquia de Menor Atrito Respeitada:** Arquivo/AST > CLI > API Local > DOM > XY — XY usado apenas em Canvas/WebGL sem representação DOM acessível.
- [ ] **Self-Healing Ativo:** colisões de porta (`EADDRINUSE`), locks (`EBUSY`/`EPERM`) e caches corrompidos tratados autonomamente sem delegar ao usuário.
- [ ] **Working Tree Clean:** `git status` confirma zero arquivos untracked ou modificados sem commit ao final de cada expediente.
- [ ] **Commit Semântico Verificado:** `git log -n 1` confirma commit com mensagem semântica e hash válido após cada expediente.
- [ ] **Zero Processos Órfãos:** confirmação de zero processos de compilação ou servidor abandonados em background após cada turno.
