---
name: meta-skill-synthesis
description: Protocolo AGI/ASI de Autoaprendizado de Máquina. Define como o agente deve extrair insights técnicos duradouros de uma sessão e sintetizá-los em novas skills definitivas no próprio disco.
---
# 🧠 META-SKILL SYNTHESIS (Dual-Scope Machine Self-Learning)

**DOGMA CENTRAL:** A inteligência AGI/ASI não repete o mesmo esforço arquitetural duas vezes. Ao conquistar uma nova fronteira de complexidade ou resolver problemas específicos de um domínio/projeto, o sistema sintetiza novas skills no escopo apropriado (Global vs Local).

---

## 🧭 Bifurcação de Escopo de Síntese

Antes de escrever a nova skill, classifique o destino:

### Destino A: Skill Global (ASI/AGI Neural Matrix)
- **Critério:** Capacidade transversal, protocolo epistemológico, motor de raciocínio, ferramenta universal ou método aplicável a qualquer software/ciência.
- **Caminho:** `c:\Users\pichau\.gemini\config\plugins\AGI-Antigravity-skills-concept\skills/<nome-da-skill>/SKILL.md`
- **Registro:** Adicionar à Matriz Universal em `rules/AGI_CORE.md`.

### Destino B: Skill Nichada / Local (Workspace & Projeto)
- **Critério:** Procedimentos operacionais do repositório, pipelines de build específicos, scripts de migração, geradores de boilerplate do projeto, regras de domínio do cliente ou stack local.
- **Caminho:** `<workspace_root>/.agent/skills/<nome-da-skill-nichada>/SKILL.md` (ou `.agents/skills/`, `.gemini/skills/`)
- **Registro:** Registrar no `GEMINI.md` ou `AGENTS.md` da raiz do projeto.

---

## 🛠️ Processo de Síntese de Nova Skill

1. **Reconhecimento de Avanço:** Quando uma barreira técnica for quebrada, um novo workflow for estabelecido ou uma rotina repetitiva for identificada.
2. **Criação do Diretório e Arquivo:**
   - Crie a pasta da skill no destino apropriado (Global ou Workspace Local).
   - Crie o `SKILL.md` com frontmatter YAML (`name`, `description`).
3. **Linguagem de Reforço Estrito & Invariantes:**
   - Utilize comandos imperativos claros, pre-condições, post-condições e invariantes formais.
   - Proibido usar linguagem vaga ou passiva ("você pode querer...", "talvez").
   - Detalhe a cadeia de ferramentas necessárias, argumentos e tratamento de exceções.
4. **Registro de Invocação:**
   - Para Global: Registre em `rules/AGI_CORE.md`.
   - Para Local: Registre no `GEMINI.md` ou `.agent/rules/` do workspace para que o agente saiba quando ativá-la no projeto.
