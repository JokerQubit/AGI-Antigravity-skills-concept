---
name: autonomous_computer_use
version: 5.0.0
description: "v5.0 — Universal Cognitive Parity & Closed-Loop Motor Mutator. Playbook de Engenharia e Controle Operacional para Computer Use Autônomo de nível AGI. Governa o Ciclo OODA em malha fechada (Observe -> Orient -> Decide -> Act), a hierarquia mecânica de menor atrito motor (Arquivo/AST > CLI > DOM > GUI XY), os 5 playbooks determinísticos de auto-cura A a E (EADDRINUSE, Zumbis, Locks EBUSY/EPERM, Caches corrompidos, Stale Git Locks), o veto [HARD REJECT: MOTOR_TASK_ABANDONMENT] e a telemetria fria padronizada MOTOR_EXECUTION_RECEIPT."
---

# Autonomous Computer Use & Closed-Loop Motor Control — v5.0 (Universal Cognitive Parity & Closed-Loop Motor Mutator)

Manual de engenharia e governança de interação motora, sensorial e computacional com o sistema operacional (Windows 11, PowerShell, Node.js, compiladores, processos em background) e navegador web via `browser-mcp`. Estabelece o fim definitivo do paradigma amador "dispare e reze" (*fire-and-forget*), impondo **autonomia de malha fechada, propriocepção de ambiente, auto-cura determinística em nível de SO e o Mandato do Artífice Motor**.

> **Salvaguarda v5.0 — Ativação Compulsória Universal & Veto ao Abandono:**
> Na v5.0.0, o Ciclo OODA em Malha Fechada e os Playbooks de Auto-Cura A a E são disparados compulsoriamente em toda ação motora. É expressamente proibido ao subagente motor abandonar tarefas diante de erros ou devolver texto/código no chat para o caller: a tarefa só se encerra com `$LASTEXITCODE === 0`, sob pena de cancelamento imediato via `[HARD REJECT: MOTOR_TASK_ABANDONMENT]`.

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

### 1.1. O Mandato do Artífice Motor no Quadrante ACT & VERIFY (Leis 5, 39 e 43)

Subagentes despachados com objetivo de produção, refatoração ou correção (`[ACTION_MODE: PHYSICAL_MUTATION]`, `TypeName: "self"`) fecham o ciclo OODA compulsoriamente dentro de sua própria sessão de execução:

1. **Atuação Física Direta (Nível 1 - Arquivo):** O subagente não interrompe seu ciclo no quadrante DECIDE nem emite propostas textuais no chat. Ele dispara compulsoriamente ferramentas motoras de escrita (`replace_file_content`, `write_to_file`) para consumar a mutação física no disco.
2. **Validação Sensorial Estrita (Nível 2 - CLI & Compilação):** Imediatamente após a mutação no filesystem, o subagente executa a etapa VERIFY disparando ferramentas de execução CLI (`run_command`) para validar que `$LASTEXITCODE === 0` (ex: compilação estática `npx tsc --noEmit`, suítes de teste ou linters).
3. **Veto Inegociável ao Abandono de Tarefas em Erro (Anti-Surrender Mandate):**
   - É expressamente proibido ao subagente motor emitir mensagens declarando falhas de ambiente sem antes executar a auto-cura: *"Ocorreu erro X. Por favor libere a porta / encerre o processo / limpe o cache"*.
   - A ocorrência de qualquer erro de execução em comando ou build obriga o subagente a entrar recursivamente nos quadrantes **ORIENT $\to$ DECIDE $\to$ ACT**, executando os Playbooks Determinísticos de Auto-Cura A a E.
4. **Critério de Repouso Inegociável:**
   A tarefa física do subagente só é dada como concluída quando o comando de validação formal retornar exit code idêntico a zero:
   $$\text{TaskCompletion}(\tau) \iff (\text{DiskMutationConfirmed} \land \$LASTEXITCODE = 0 \land \text{StderrFatal} = 0)$$
5. **Trava Mecânica `[HARD REJECT: MOTOR_TASK_ABANDONMENT]`:**
   Caso um subagente encerre sua execução enviando um relatório de erro sem ter aplicado as rotinas determinísticas de auto-cura e sem ter consumido seu orçamento de 2 ciclos do Circuit Breaker, sua resposta será sumariamente invalidada com a tag `[HARD REJECT: MOTOR_TASK_ABANDONMENT]`.
6. **Telemetria de Malha Fechada & Recibo Fiduciário Motor:** Somente após a mutação física persistida e a validação sensorial executada, o subagente emite o `send_message` contendo o recibo estruturado `[MOTOR_EXECUTION_RECEIPT]`. Devolver blocos de código em markdown no chat sem ter atuado fisicamente nas ferramentas motoras constitui colapso consultivo e aciona `[HARD REJECT: ADVISORY_CODE_DUMP]`.

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

## 3. Playbooks Determinísticos de Auto-Cura e Resiliência Operacional no Sistema Operacional

É terminantemente proibido ao agente congelar ou delegar ao usuário a solução de atritos operacionais triviais do ambiente de execução (Windows 11 / PowerShell). Diante de qualquer falha mecânica, execute de forma autônoma o playbook determinístico cabível:

```text
                                [INCIDENTE OPERACIONAL]
                                           │
         ┌───────────────────┬─────────────┴───────┬───────────────────┬───────────────────┐
         ▼                   ▼                     ▼                   ▼                   ▼
    [EADDRINUSE]       [ZOMBIE PIDS]         [FILE LOCKS]        [CACHE ROT]         [GIT LOCKS]
   Socket Ocupado     Processos Órfãos      EBUSY / EPERM      Build Corrompido    .git/index.lock
         │                   │                     │                   │                   │
         ▼                   ▼                     ▼                   ▼                   ▼
    Get-NetTCP           Get-CimInstance        Exponential         Purga Atômica       Remoção de Lock
    taskkill /T /F     Stop-Process -Force   Backoff + Jitter    .next, dist, cache      git fsck / reset
         │                   │                     │                   │                   │
         ▼                   ▼                     ▼                   ▼                   ▼
  Polling 3000ms       Limpeza de Handles    Atomic Swap TMP      Re-verificação       Working Tree
    ou Port N+1        Verificação PIDs      Move-Item -Force      tsc --noEmit            Clean
```

---

### Playbook A: Colisão de Sockets & Portas Presas (`EADDRINUSE`)
*Sintoma:* Um servidor local falha ao iniciar porque a porta designada (ex: `3000`) já está em uso por processo anterior ou zumbi retido em `TIME_WAIT`.
*Procedimento Autônomo Obrigatório em PowerShell:*
```powershell
$TargetPort = 3000
$MaxRetries = 2
$Attempt = 0
$PortCleared = $false

while (-not $PortCleared -and $Attempt -lt $MaxRetries) {
    $Attempt++
    $Connection = Get-NetTCPConnection -LocalPort $TargetPort -State Listen -ErrorAction SilentlyContinue

    if ($null -ne $Connection) {
        $ZombiePID = $Connection.OwningProcess
        # Encerramento forçado do processo pai e de toda a árvore de subprocessos
        taskkill /PID $ZombiePID /T /F 2>&1 | Out-Null
        
        # Polling determinístico com timeout de 3000ms para liberação do socket no kernel
        $WaitTimeout = 0
        while ((Get-NetTCPConnection -LocalPort $TargetPort -State Listen -ErrorAction SilentlyContinue) -and ($WaitTimeout -lt 15)) {
            Start-Sleep -Milliseconds 200
            $WaitTimeout++
        }
    }

    # Verificação pós-atuação
    $CheckActive = Get-NetTCPConnection -LocalPort $TargetPort -State Listen -ErrorAction SilentlyContinue
    if ($null -eq $CheckActive) {
        $PortCleared = $true
    }
}

# Fallback Determinístico Se o Socket Estiver Preso no Kernel (TIME_WAIT):
if (-not $PortCleared) {
    $AlternativePort = $TargetPort + 1
    # Registra o desvio na variável de ambiente local para disparo do processo
    $env:PORT = "$AlternativePort"
}
```

---

### Playbook B: Processos Órfãos, Vazamento de Memória & Zumbis de Compilação
*Sintoma:* Processos de empacotamento (`esbuild`, `node`, `vite`, `next-server`) travam consumindo CPU, retendo memória ou bloqueando descritores de arquivos do projeto.
*Procedimento Autônomo Obrigatório em PowerShell:*
```powershell
$TargetProcessNames = @("node", "esbuild", "vite", "next-server")

foreach ($ProcName in $TargetProcessNames) {
    # Localiza processos cuja linha de comando esteja associada ao diretório do workspace atual
    $Processes = Get-CimInstance Win32_Process -Filter "Name LIKE '$ProcName%.exe'" -ErrorAction SilentlyContinue |
                 Where-Object { $_.CommandLine -like "*$((Get-Location).Path.Replace('\', '\\'))*" }

    foreach ($Proc in $Processes) {
        if ($Proc.ProcessId -ne $PID) {
            taskkill /PID $Proc.ProcessId /T /F 2>&1 | Out-Null
        }
    }
}

# Pausa mecânica de 300ms para liberação de handles no subsistema de arquivos Win32
Start-Sleep -Milliseconds 300
```

---

### Playbook C: Locks de Arquivos pelo Sistema Operacional (`EBUSY`, `EPERM`, Sharing Violation)
*Sintoma:* Tentativa de reescrita de arquivo falha porque o Windows Defender, o Search Indexer ou outro processo retém descritor aberto sem compartilhamento.
*Procedimento Autônomo Obrigatório em PowerShell:*
```powershell
function Mutate-FileWithLockResilience {
    param (
        [Parameter(Mandatory=$true)] [string]$FilePath,
        [Parameter(Mandatory=$true)] [string]$Content
    )

    $Delays = @(200, 500, 1200) # Milissegundos progressivos
    $Success = $false

    # Tentativa 1: Escrita direta com backoff
    foreach ($Delay in $Delays) {
        try {
            [System.IO.File]::WriteAllText($FilePath, $Content, [System.Text.Encoding]::UTF8)
            $Success = $true
            break
        } catch [System.IO.IOException], [System.UnauthorizedAccessException] {
            $Jitter = Get-Random -Minimum 10 -Maximum 50
            Start-Sleep -Milliseconds ($Delay + $Jitter)
        }
    }

    # Tentativa 2: Atomic Swap Transacional se a escrita direta for bloqueada
    if (-not $Success) {
        $Guid = [System.Guid]::NewGuid().ToString("N")
        $TempPath = "$FilePath.tmp.$Guid"
        
        try {
            [System.IO.File]::WriteAllText($TempPath, $Content, [System.Text.Encoding]::UTF8)
            Move-Item -Path $TempPath -Destination $FilePath -Force -ErrorAction Stop
            $Success = $true
        } catch {
            if (Test-Path $TempPath) { Remove-Item -Force $TempPath -ErrorAction SilentlyContinue }
            throw "FALHA_FATAL_FILE_LOCK: Impossível liberar descritor para o arquivo $FilePath"
        }
    }
}
```

---

### Playbook D: Purga Determinística de Caches de Build Corrompidos
*Sintoma:* Erros inexplicáveis de compilação, importação fantasma ou resolução circular persistindo após edições corretas de código.
*Procedimento Autônomo Obrigatório em PowerShell:*
```powershell
$CachePaths = @(
    ".next",
    "dist",
    "build",
    ".turbo",
    "node_modules/.cache",
    "tsconfig.tsbuildinfo",
    ".eslintcache"
)

foreach ($CachePath in $CachePaths) {
    if (Test-Path $CachePath) {
        Remove-Item -Recurse -Force $CachePath -ErrorAction SilentlyContinue
    }
}

# Verificação imediata em malha fechada da higienização
Start-Sleep -Milliseconds 200
```

---

### Playbook E: Reparação de Travas Órfãs e Corrupção de Índice Git
*Sintoma:* Quedas de processos, falhas de desligamento ou concorrência deixam travas residuais no diretório `.git` (`.git/index.lock`), impedindo checagens de integridade ou transições de estado.
*Procedimento Autônomo Obrigatório em PowerShell:*
```powershell
$GitLockFiles = @(
    ".git/index.lock",
    ".git/HEAD.lock",
    ".git/refs/heads/*.lock",
    ".git/shallow.lock",
    ".git/config.lock"
)

foreach ($LockPattern in $GitLockFiles) {
    $Locks = Get-ChildItem -Path $LockPattern -ErrorAction SilentlyContinue
    foreach ($Lock in $Locks) {
        Remove-Item -Force $Lock.FullName -ErrorAction SilentlyContinue
    }
}

# Verificação de integridade da árvore git sem destruição de dados do usuário
git fsck --no-full --no-dangling 2>&1 | Out-Null
if ($LASTEXITCODE -ne 0) {
    # Reparar índice sem perder modificações na working tree
    git read-tree HEAD 2>&1 | Out-Null
}

# Confirmação de status funcional
$GitStatus = git status --porcelain 2>&1
if ($LASTEXITCODE -ne 0) {
    throw "FALHA_CRÍTICA_GIT: Repositório com metadados irrecuperáveis"
}
```

---

### Playbook F: Estabilização de DOM & Sincronização Assíncrona no `browser-mcp`
*Sintoma:* Ações visuais falham por hidratação assíncrona ou animações em andamento no frontend.
*Playbook de Estabilização:*
1. Disparar `browser_wait_for_network(Timeout: 5000)` para certificar zero requisições in-flight.
2. Executar script de repouso: `document.readyState === 'complete'`.
3. Selecionar elementos por `data-testid` ou atributos semânticos estritamente estáveis, jamais por classes CSS utilitárias voláteis (`css-1a2b3c`).

---

### Playbook G: Circuit Breaker de Remediação Autônoma (Anti-Loop Invariant)
*Invariante:* A auto-cura autônoma opera sob salvaguarda determinística, nunca sob repetição cega infinita.
- **Teto Rígido de 2 Ciclos:** Todo procedimento de auto-cura tem limite absoluto de **2 tentativas consecutivas** para o mesmo incidente.
- **Disparo de Trava Epistêmica:** Se após 2 ciclos de remediação o erro persistir, o subagente DEVE suspender a execução motora e disparar `[EPISTEMIC_HALT: CIRCUIT_BREAKER_TRIPPED]`, reportando a telemetria fria do estado terminal para arbitragem do Chief Architect.

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

### 4.1. Erradicação do Dump Textual no `send_message` & Recibo Fiduciário Motor (`MOTOR_EXECUTION_RECEIPT`)

O envio de blocos de código em markdown dentro do `send_message` por subagentes de produção é tipificado como Fraude de Transcrição Fiduciária (*Advisory Dump*). Subagentes motores (`TypeName: "self"`) transmitem exclusivamente telemetria fria padronizada através do formato abaixo:

```markdown
[MOTOR_EXECUTION_RECEIPT]
- Subagent Role: <MY_SWARM_ROLE>
- Synaptic Anchor: <MY_SYNAPTIC_ANCHOR>
- Action Mode: PHYSICAL_MUTATION
- Tool Invocations Confirmed:
  * replace_file_content: <Count>
  * write_to_file: <Count>
  * run_command: <Count>
- Mutated Files (On Disk):
  * <Caminho Absoluto 1> [Delta: +X / -Y linhas | Status: PERSISTED]
  * <Caminho Absoluto 2> [Delta: +X / -Y linhas | Status: PERSISTED]
- Closed-Loop Verification Telemetry:
  * Command Executed: <Comando exato, ex: npx tsc --noEmit>
  * Exit Code: 0 ($LASTEXITCODE === 0)
  * Stderr Stream: CLEAN (Zero fatal exceptions)
- Self-Healing Events Triggered:
  * <Nenhum / Playbook A / Playbook E>
- Circuit Breaker Status: <0|1>/2 Retries Consumed
- Forensic Checklist Binary State: ALL_CRITERIA_SATISFIED [1]
- Synaptic Outputs Emitted:
  * <Chave de Contrato>: <Valor ou Referência Persistida no Disco>
```

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

## 6. Checklist Forense de Autonomous Computer Use v5.0 (Binário — Lei 41)

> Auditado pelo Agente Principal após cada ação motora e confirmado pelo Red Team na Época IV. A reprovação de um único item anula a homologação do entregável.

- [ ] **1. Mutação Física 100% Persistida no Disco:** O código foi alterado via `replace_file_content` ou `write_to_file`; zero sugestões ou diffs textuais no `send_message`.
- [ ] **2. Fechamento de Malha Comprovado ($LASTEXITCODE === 0):** O subagente executou comando formal de verificação CLI (`tsc`, `vitest`, `npm test`, linter ou validação sintática) e obteve exit code 0.
- [ ] **3. Zero Erros Fatais em Stderr:** O fluxo de stderr do comando de verificação não contém stack traces, exceções não tratadas ou mensagens críticas de falha.
- [ ] **4. Veto ao Abandono de Erro Respeitado:** O subagente não transferiu atritos de ambiente (portas, locks, caches, git) para o caller; auto-cura executada com sucesso.
- [ ] **5. Circuit Breaker Respeitado:** Em caso de re-tentativa, o número de ciclos de remediação não ultrapassou o teto rígido de 2 iterações.
- [ ] **6. Stale Git Locks Purgados:** O diretório `.git` não contém arquivos `.lock` órfãos após a execução do subagente.
- [ ] **7. Working Tree Íntegro:** `git status` comprova que o repositório permanece em estado consistente, com zero arquivos temporários abandonados.
- [ ] **8. Zero Processos Zumbis Remanescentes:** Confirmação de ausência de processos orquestrados em background pendentes sem controle de vida.
- [ ] **9. Recibo Fiduciário Motor Emitido:** O retorno via `send_message` adotou rigorosamente o schema estruturado de telemetria fria `[MOTOR_EXECUTION_RECEIPT]`.
