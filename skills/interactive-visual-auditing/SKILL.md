---
name: interactive-visual-auditing
description: "MANDATORY. Use after a UI component, frontend page, or game scene is built. Enforces live visual testing via the /browser slash command and auto-rejects 'generic' or 'basic' aesthetics."
---

# 👁️ Interactive Visual & Aesthetic Auditing Protocol

> 🔴 **DEEP INTERACTIVE CRAWL MANDATE:**
> Antigravity agents are strictly forbidden from taking a single static landing page screenshot and declaring success.
> You MUST interact with the live application: click buttons, open modals, simulate gameplay controls, test inputs, and audit across multiple active states.

---

## 1. Multi-State Interactive Playtesting Workflow

### Phase A: Live Interactive Exploration & State Capture
1. Dispatch the `browser` subagent (`invoke_subagent` with `TypeName: browser`, `Role: Deep UI/UX Playtester`) or invoke Puppeteer MCP tools directly.
2. **Execute Multi-State Fullscreen Actions (1920x1080 Mandatory):**
   - **Step 1 (Resting Full HD Desktop State):** Navigate to `localhost:<port>`, set viewport to `1920x1080` and capture `state_01_desktop_fullscreen.png` (width: 1920, height: 1080).
   - **Step 2 (Interactive State):** Click navigation links, open sidebars/drawers, trigger modals, type sample text into inputs, capture `state_02_interaction.png` (width: 1920, height: 1080).
   - **Step 3 (Dynamic / Gameplay State):** For games or interactive 3D, simulate controls, collisions, audio triggers, capture `state_03_active_gameplay.png` (width: 1920, height: 1080).
   - **Step 4 (Responsive Mobile Breakpoint):** Resize viewport to mobile dimensions (`390x844`), capture `state_04_mobile.png`.
3. **Mandatory Image Inspection:** YOU MUST execute `view_file` on **all captured `.png` files**. Reading text status alone is strictly prohibited.


---

## 2. Multi-Tier Aesthetic & Functional Diagnostic

Inspect each captured state image across 4 core vectors:

1. **Material & Lighting Depth:** Check for untextured flat surfaces, missing PBR roughness/metalness, blown-out or missing bloom, harsh unsoftened shadows.
2. **Typography & Layout Hierarchy:** Ensure no default Times New Roman/Arial, check letter-spacing, line-height, text truncation, and breathing room.
3. **Micro-Interactions & Feedback:** Verify hover glow effects, active press animations, smooth transitions, and loading states.
4. **State Transition Cohesion:** Ensure modals overlay cleanly with backdrop blur (`backdrop-filter: blur(...)`), HUD elements do not overlap, and game cameras follow smoothly without jitter.

---

## 3. Mandatory Veto & Autonomous Breakthrough

- **Iteration 1 & 2 Rule:** Automatically trigger `🔴 AESTHETIC VETO TRIGGERED` on early cycles.
- Identify at least **3 critical visual/functional improvements** AND **1 transformative feature innovation**.
- **Immediate Auto-Refactor:** Refactor the codebase to implement the improvements and innovations immediately.
- Re-run Phase A to visually confirm the elevated state before exiting.

