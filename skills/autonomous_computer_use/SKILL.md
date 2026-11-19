---
name: autonomous_computer_use
version: 6.0.0
description: "Use when executing OS commands, managing local dev servers, resolving port collisions (EADDRINUSE), zombie processes, Windows file locks (EBUSY/EPERM), corrupted build caches, .git/index.lock stale locks, browser DOM/E2E stabilization, or enforcing closed-loop verification and <=10% quota checkpoint safety."
---

# Autonomous Computer Use & Closed-Loop Motor Control — v6.0

Manual operacional de interação motora e sensorial com o sistema operacional (Windows 11, PowerShell, Node.js, compiladores, processos em background) e navegador via `browser-mcp`. Impõe execução em **malha fechada (OODA)**, auto-cura determinística de ambiente, **controle de cota (`<= 10%`)** e entrega física validada no disco.

> **Fronteiras & Delegação (SSOT):**
> - **Git/GitHub (`git add .`, `commit`, `push`, backup pré-voo, `.gitignore`, segredos):** delegado integralmente à skill [`github_sovereign_workflow`](../github_sovereign_workflow/SKILL.md). Esta skill mantém apenas o **Playbook E** para reparo de travas físicas do SO (`.git/*.lock`).
> - **Roteamento de Modelos:** Workers motores padrão operam em **Hydrogen 4 High** (`gemini-4-hydrogen-high`) ou **Hydrogen 4 XHigh** (`gemini-4-hydrogen-xhigh`) para codificação paralela pesada.

---

## 1. Ciclo OODA em Malha Fechada & Trava de Abandono

Toda ação sobre o computador fecha obrigatoriamente os quatro quadrantes:

```text
1. OBSERVE  ──► Telemetria fria ($LASTEXITCODE, stderr, Get-NetTCPConnection, locks, DOM/console)
      │
      ▼
2. ORIENT   ──► Diagnóstico causal: erro de código/domínio vs. atrito de ambiente (porta/lock/cache)
      │
      ▼
3. DECIDE   ──► Menor canal de atrito + Playbook de auto-cura aplicável (A–G)
      │
      ▼
4. ACT & VERIFY ──► Mutação física no disco + validação CLI ($LASTEXITCODE === 0) ──► volta a OBSERVE
```

### Regras Invioláveis do Artífice Motor
1. **Mutação Física Obrigatória:** Subagentes motores aplicam edições diretamente no disco (`edit_file` / `write_file`). Devolver blocos de código ou diffs no chat sem persistir no disco aciona `[HARD REJECT: ADVISORY_CODE_DUMP]`.
2. **Anti-Surrender Mandate (`[HARD REJECT: MOTOR_TASK_ABANDONMENT]`):** É proibido parar e pedir ao usuário para matar portas, liberar locks ou limpar cache. O agente executa os Playbooks A–E autonomamente dentro do teto de 2 ciclos do Circuit Breaker.
3. **Critério de Conclusão:** `DiskMutationConfirmed && $LASTEXITCODE === 0 && StderrFatal === 0`.

---

## 2. Segurança de Cota (`<= 10%`) & Checkpoint de Retomada

Antes de iniciar servidores persistentes, suítes longas ou ondas motoras paralelas:
1. Verifique o orçamento/cota restante via `swarm{action:"models"}` ou alertas `[quota]` do sistema.
2. **Trava Obrigatória em `<= 10%`:** Se a cota Gemini restante atingir **`<= 10%`**:
   - **PARE** imediatamente de disparar novos processos pesados ou novas ondas de subagentes (evitando travar o modelo no meio de um build/refactor).
   - Garanta que nenhum servidor zumbi ou `.git/*.lock` fique órfão no SO.
   - Persista o checkpoint exato do estado atual, arquivos modificados e próximo comando de retomada em `.planning/ledger/` (e crie snapshot commit seguro via `github_sovereign_workflow` se houver edições validadas).
   - Agende a retomada automática via ferramenta `schedule` para o horário informado em `quota_resets`.

---

## 3. Hierarquia Mecânica de Menor Atrito Motor

Sempre escolha o canal mais determinístico e de menor atrito disponível:

| Nível | Canal / Ferramenta | Uso Obrigatório | Restrição |
|---|---|---|---|
| **1 (Ótimo)** | Arquivo/AST direto (`read_file`, `edit_file`, `write_file`) | Edição de código, configs, docs | Proibido usar editores interativos em shell (`vim`, `nano`). |
| **2 (Forte)** | Shell CLI nativo (`run_command` em PowerShell) | Build, testes, linters, PIDs, Git | Proibido comandos interativos sem flags não-interativas (`-y`, `-Force`). |
| **3 (Médio)** | HTTP/TCP local (`Invoke-WebRequest`, sockets) | Health-check ativo de servidores | Proibido usar `sleep` cego para assumir que um server subiu. |
| **4 (Alto)** | DOM semântico (`browser_click`, `browser_fill`) | Testes E2E em elementos com `data-testid`/ARIA | Aguardar `browser_wait_for_network` antes de interagir. |
| **5 (Último Recurso)** | Coordenadas XY (`browser_click_xy`) | Apenas Canvas/WebGL/drag livre sem nós DOM | **Veto absoluto** em botões, links ou inputs acessíveis via DOM. |

---

## 4. Playbooks Determinísticos de Auto-Cura (A a G)

### Playbook A: Colisão de Sockets & Portas Presas (`EADDRINUSE`)
```powershell
$TargetPort = 3000
$MaxRetries = 2; $Attempt = 0; $PortCleared = $false

while (-not $PortCleared -and $Attempt -lt $MaxRetries) {
    $Attempt++
    $Conn = Get-NetTCPConnection -LocalPort $TargetPort -State Listen -ErrorAction SilentlyContinue
    if ($null -ne $Conn) {
        taskkill /PID $Conn.OwningProcess /T /F 2>&1 | Out-Null
        $Wait = 0
        while ((Get-NetTCPConnection -LocalPort $TargetPort -State Listen -ErrorAction SilentlyContinue) -and ($Wait -lt 15)) {
            Start-Sleep -Milliseconds 200; $Wait++
        }
    }
    if ($null -eq (Get-NetTCPConnection -LocalPort $TargetPort -State Listen -ErrorAction SilentlyContinue)) {
        $PortCleared = $true
    }
}
if (-not $PortCleared) { $env:PORT = "$($TargetPort + 1)" }
```

### Playbook B: Processos Órfãos & Zumbis de Build
```powershell
$TargetNames = @("node", "esbuild", "vite", "next-server")
$WorkspaceEscaped = (Get-Location).Path.Replace('\', '\\')
foreach ($ProcName in $TargetNames) {
    $Procs = Get-CimInstance Win32_Process -Filter "Name LIKE '$ProcName%.exe'" -ErrorAction SilentlyContinue |
             Where-Object { $_.CommandLine -like "*$WorkspaceEscaped*" }
    foreach ($P in $Procs) {
        if ($P.ProcessId -ne $PID) { taskkill /PID $P.ProcessId /T /F 2>&1 | Out-Null }
    }
}
Start-Sleep -Milliseconds 300
```

### Playbook C: Locks de Arquivos Win32/NTFS (`EBUSY`, `EPERM`)
```powershell
function Mutate-FileWithLockResilience {
    param([Parameter(Mandatory=$true)][string]$FilePath, [Parameter(Mandatory=$true)][string]$Content)
    foreach ($Delay in @(200, 500, 1200)) {
        try {
            [System.IO.File]::WriteAllText($FilePath, $Content, [System.Text.Encoding]::UTF8)
            return
        } catch [System.IO.IOException], [System.UnauthorizedAccessException] {
            Start-Sleep -Milliseconds ($Delay + (Get-Random -Minimum 10 -Maximum 50))
        }
    }
    $TempPath = "$FilePath.tmp.$([System.Guid]::NewGuid().ToString('N'))"
    try {
        [System.IO.File]::WriteAllText($TempPath, $Content, [System.Text.Encoding]::UTF8)
        Move-Item -Path $TempPath -Destination $FilePath -Force -ErrorAction Stop
    } catch {
        if (Test-Path $TempPath) { Remove-Item -Force $TempPath -ErrorAction SilentlyContinue }
        throw "FALHA_FATAL_FILE_LOCK: $FilePath"
    }
}
```

### Playbook D: Purga Determinística de Caches Corrompidos
```powershell
foreach ($CachePath in @(".next", "dist", "build", ".turbo", "node_modules/.cache", "tsconfig.tsbuildinfo", ".eslintcache")) {
    if (Test-Path $CachePath) { Remove-Item -Recurse -Force $CachePath -ErrorAction SilentlyContinue }
}
Start-Sleep -Milliseconds 200
```

### Playbook E: Reparação de Travas Órfãs de Índice Git no SO
*Quando comandos Git falharem por `.git/*.lock` residual após queda de processo (para commits, pushes, backups e higiene de segredos, use `github_sovereign_workflow`):*
```powershell
foreach ($Pattern in @(".git/index.lock", ".git/HEAD.lock", ".git/refs/heads/*.lock", ".git/shallow.lock", ".git/config.lock")) {
    Get-ChildItem -Path $Pattern -ErrorAction SilentlyContinue | ForEach-Object {
        Remove-Item -Force $_.FullName -ErrorAction SilentlyContinue
    }
}
git fsck --no-full --no-dangling 2>&1 | Out-Null
if ($LASTEXITCODE -ne 0) { git read-tree HEAD 2>&1 | Out-Null }
git status --porcelain 2>&1 | Out-Null
if ($LASTEXITCODE -ne 0) { throw "FALHA_CRITICA_GIT_METADATA" }
```

### Playbook F: Estabilização de DOM no `browser-mcp`
1. `browser_wait_for_network(Timeout: 5000)` antes de clicar/ler.
2. Confirmar `document.readyState === 'complete'`.
3. Usar seletores `data-testid` ou atributos semânticos estáveis; nunca classes CSS geradas.

### Playbook G: Circuit Breaker (Anti-Loop)
- Máximo de **2 ciclos consecutivos** de auto-cura para o mesmo incidente.
- Persistindo a falha após 2 tentativas, suspender mutação e emitir `[EPISTEMIC_HALT: CIRCUIT_BREAKER_TRIPPED]` com `stderr` bruto para diagnóstico.

---

## 5. Triangulação de Verificação & Recibo Motor

Uma tarefa só fecha com as 4 evidências válidas:
1. **Shell:** `$LASTEXITCODE === 0`.
2. **Runtime:** Zero exceções fatais não capturadas em `stderr`.
3. **Browser (`browser_console_logs`, quando aplicável):** Zero erros JS, zero 404, zero hydration warnings.
4. **Health-Check Ativo:** Polling HTTP 200 real (ex.: loop de 250ms com `Invoke-WebRequest`), sem `Start-Sleep` cego.

### Formato Padrão (`MOTOR_EXECUTION_RECEIPT`)
```markdown
[MOTOR_EXECUTION_RECEIPT]
- Role: <SWARM_ROLE>
- Action Mode: PHYSICAL_MUTATION
- Mutated Files (On Disk):
  * <Caminho Absoluto> [Status: PERSISTED]
- Verification Command: <comando exato>
- Exit Code: 0 ($LASTEXITCODE === 0)
- Self-Healing Applied: <Nenhum | Playbook A..F>
- Circuit Breaker: <0|1|2>/2 Retries
- Quota Status: <healthy | <=10% checkpointed>
```

---

## 6. Checklist Binário de Computer Use (8 Itens)

- [ ] **1.** Edições aplicadas fisicamente no disco (zero advisory code dumps).
- [ ] **2.** Validador CLI nativo executado com `$LASTEXITCODE === 0`.
- [ ] **3.** Zero stack traces ou erros fatais em `stderr`.
- [ ] **4.** Atritos de SO/porta/lock/cache resolvidos via Playbooks A–E (<= 2 retries).
- [ ] **5.** Zero `.git/*.lock` órfãos ou processos zumbis remanescentes.
- [ ] **6.** Se houve entrega Git/GitHub, fluxo executado via `github_sovereign_workflow`.
- [ ] **7.** Se cota Gemini `<= 10%`, novas ondas freadas + checkpoint salvo + `schedule` agendado.
- [ ] **8.** `MOTOR_EXECUTION_RECEIPT` emitido com telemetria real observada.
