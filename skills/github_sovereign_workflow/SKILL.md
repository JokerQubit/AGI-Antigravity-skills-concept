---
name: github_sovereign_workflow
version: 6.0.0
description: "Use when starting risky refactors, schema or rule overhauls, destructive git operations, or multi-agent swarm waves (mandatory pre-flight snapshot commit), or when staging (git add .), committing (conventional commits), pushing, verifying remotes/upstreams, checking .gitignore/secrets/large binaries, or recovering branches safely on Git/GitHub."
---

# GitHub Sovereign Backup & Safe Delivery Workflow — v6.0

Protocolo operacional de blindagem Git/GitHub do Hyper-Cortex v6.0. Garante que **nenhuma mutação arriscada comece sem ponto de restauração versionado** e que **toda entrega concluída seja persistida com segurança** (`git add .` → `git commit` → `git push`), com higiene estrita contra vazamento de segredos, binários gigantes ou histórico corrompido.

> **Fronteira de Responsabilidade (SSOT):**
> Reparos de travas do sistema de arquivos (`.git/index.lock`, `HEAD.lock`) e integridade física de disco são tratados pelo Playbook E de [`autonomous_computer_use`](../autonomous_computer_use/SKILL.md). Esta skill governa o ciclo completo de **snapshot pré-voo, higiene pré-commit, entrega convencional, push seguro e recuperação**.

---

## 1. Gatilhos Obrigatórios de Backup Pré-Voo (Pre-Flight Snapshots)

Antes de executar qualquer operação de alto risco sobre o repositório, execute um **Pre-Flight Snapshot** se houver modificações locais não commitadas ou se o estado base precisar de âncora recuperável:

| Gatilho Pré-Voo | Exemplos Concretos | Ação Obrigatória Antes de Prosseguir |
|---|---|---|
| **Refatoração Estrutural** | Renomeação em massa, quebra de módulos, mudança de contratos/APIs centrais | Commit de checkpoint ou tag/branch de salvaguarda com working tree limpa |
| **Overhaul de Schema / Regras** | Alteração em migrações de DB, `.agents/rules/`, `rules/`, `plugin.json` | Snapshot commit antes da edição + registro do SHA em `.planning/ledger/` |
| **Operação Git Destrutiva** | `git rebase`, `git merge` complexo, `git reset`, limpeza de histórico | Criar branch/tag temporária (`backup/pre-<op>-<ts>`) apontando para `HEAD` |
| **Onda Paralela de Enxame** | Despacho de múltiplos agentes com `workspace: "share"` ou edições concorrentes | Garantir working tree limpa e `HEAD` estável antes de abrir os workspaces |

### Procedimento Rápido de Pre-Flight Snapshot
```powershell
# 1. Verificar estado atual
git status -sb

# 2. Se houver alterações válidas pendentes (após passar pelo Gate de Higiene da Seção 2):
git add .
git commit -m "chore(checkpoint): pre-flight snapshot before <operation>"

# 3. Opcional em operações destrutivas (rebase/reset): marcar âncora de recuperação
git branch "backup/pre-<op>-$(Get-Date -Format 'yyyyMMdd-HHmmss')"
```
Se o working tree tiver alterações experimentais que não devem entrar no histórico principal ainda, crie um commit em branch temporária de backup ou registre o hash via `git stash push -u -m "pre-flight-<op>"` antes de prosseguir.

---

## 2. Portão de Higiene Pré-Commit (Segredos, `.gitignore` e Binários)

**NUNCA** execute `git add .` ou `git commit` às cegas. Antes de empacotar arquivos, valide os 3 vetores abaixo:

### 2.1. Auditoria de `.gitignore`
Confirme que `.gitignore` existe na raiz do repositório e bloqueia artefatos transitórios e sensíveis:
- Segredos e ambiente: `.env`, `.env.*` (exceto `.env.example`), `*.pem`, `*.key`, `credentials*.json`, `*secret*`.
- Dependências e builds: `node_modules/`, `dist/`, `build/`, `.next/`, `target/`, `__pycache__/`, `.venv/`.
- Temporários do Hyper-Cortex / SO: `.tmp/`, `*.tmp.*`, `.DS_Store`, `Thumbs.db`.

### 2.2. Varredura Anti-Vazamento de Segredos (`[HARD HALT: SECRET_EXPOSURE_RISK]`)
Inspecione os arquivos a serem adicionados (`git status --porcelain` e `git diff --cached`):
- Bloqueie imediatamente se detectar chaves privadas, tokens (`ghp_`, `github_pat_`, `AIza`, `AKIA`, `sk-`, strings `Bearer ` hardcoded) ou arquivos `.env` reais.
- Caso um segredo já tenha sido stageado: remova com `git restore --staged <arquivo>`, adicione o padrão ao `.gitignore` e só então retome.

### 2.3. Controle de Binários Grandes e Bloat
Verifique arquivos não-rastreados ou modificados com tamanho elevado antes do commit:
```powershell
# Lista arquivos modificados/untracked acima de 10 MB
git status --porcelain | ForEach-Object {
    $path = $_.Substring(3).Trim('"')
    if (Test-Path $path -PathType Leaf) {
        $item = Get-Item $path
        if ($item.Length -gt 10MB) {
            Write-Warning "LARGE_FILE_DETECTED: $($item.FullName) ($([math]::Round($item.Length / 1MB, 2)) MB)"
        }
    }
}
```
- **Limite rígido:** GitHub rejeita arquivos `>= 100 MB` e alerta a partir de `50 MB`. Arquivos `> 10 MB` (modelos, vídeos, dumps SQL, arquivos compactados) devem ir para `.gitignore` ou Git LFS (`git lfs track`), salvo ativos visuais/áudio explicitamente pertencentes ao projeto e abaixo do teto.

---

## 3. Fluxo Seguro de Entrega (`git add .` → `git commit` → `git push`)

Execute esta sequência determinística após validar testes/linters da entrega (`$LASTEXITCODE === 0`):

```powershell
# Passo 1: Se existir .git/index.lock órfão, aplicar Playbook E (autonomous_computer_use)
# Passo 2: Auditar escopo e higiene (Seção 2)
git status -sb

# Passo 3: Stage completo após higiene confirmada
git add .
git diff --cached --stat

# Passo 4: Commit Semântico (Conventional Commits)
# Tipos: feat | fix | refactor | docs | test | chore | build | ci | perf
git commit -m "<type>(<scope>): <resumo conciso no imperativo>" -m "<motivação técnica e arquivos-chave>"
if ($LASTEXITCODE -ne 0) { throw "GIT_COMMIT_FAILED" }

# Passo 5: Verificar remoto e upstream da branch atual
$Branch = git branch --show-current
git remote -v
$Upstream = git rev-parse --abbrev-ref --symbolic-full-name "@{u}" 2>$null

# Passo 6: Push seguro (com definição de upstream se ausente)
if ($LASTEXITCODE -ne 0 -or [string]::IsNullOrWhiteSpace($Upstream)) {
    git push -u origin $Branch
} else {
    git push
}
```

### Regras Invioláveis de Commit & Push
1. **Proibido `--no-verify`:** Nunca contorne hooks de pré-commit/pré-push para mascarar falhas de lint, testes ou segredos. Corrija a causa raiz.
2. **Proibido `git push --force` em branches compartilhadas (`main`, `master`, `develop`):** Caso precise reescrever branch pessoal isolada após autorização explícita, use apenas `--force-with-lease`.
3. **Tratamento de Push Rejeitado (Non-Fast-Forward):**
   - Se o remoto estiver à frente, execute `git pull --rebase origin $Branch`.
   - Resolva conflitos cirurgicamente e valide os testes/compilador novamente antes de `git rebase --continue` e `git push`.
   - Em caso de conflito complexo durante rebase, execute `git rebase --abort` imediatamente para restaurar o estado seguro e avaliar estratégia de merge/coordenação.
4. **Cota Baixa (`<= 10%`) ou Interrupção:** Antes de pausar uma sessão com trabalho validado no disco, garanta ao menos um commit local limpo (e push se aprovado/configurado) + registro do SHA no `.planning/ledger/` para retomada sem perda.

---

## 4. Playbook de Recuperação & Rollback Seguro

| Cenário de Incidente | Comando Seguro de Recuperação | Observação Crítica |
|---|---|---|
| **Commit local errado (não enviado)** | `git reset --soft HEAD~1` | Preserva todas as edições na staging area para correção |
| **Commit já enviado (`push`) com regressão** | `git revert <commit_sha>` | Cria commit inverso sem reescrever histórico remoto |
| **Commit/branch deletado acidentalmente** | `git reflog` → `git checkout -b rescue <sha>` | O reflog retém ponteiros locais por padrão |
| **Arquivo único corrompido na working tree** | `git restore --source=HEAD -- <path>` | Restaura apenas o arquivo especificado sem tocar outros |
| **Segredo commitado localmente (antes do push)** | `git reset --soft HEAD~1` → remover segredo → `.gitignore` → novo commit | Se já foi feito `push`, **rotacione o segredo imediatamente** e alerte o usuário |

---

## 5. Checklist Binário de Aceitação (GitHub Sovereign Workflow)

- [ ] **1. Pre-Flight Snapshot Aplicado:** Operações de risco tiveram commit/branch âncora antes da mutação.
- [ ] **2. Higiene de `.gitignore` e Segredos:** Zero `.env`, chaves privadas, tokens ou credenciais no staging.
- [ ] **3. Controle de Tamanho:** Nenhum binário inadvertido `> 10 MB` adicionado ao histórico Git.
- [ ] **4. Conventional Commit Limpo:** Mensagem clara descrevendo escopo e intenção, sem `--no-verify`.
- [ ] **5. Push & Remoto Verificados:** `git push` concluído com `$LASTEXITCODE === 0`, upstream configurado e `git status` limpo.
