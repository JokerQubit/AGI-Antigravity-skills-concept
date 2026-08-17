---
name: puppeteer-browser-automation
description: MANDATORY. Protocol for autonomous browser automation, web scraping, live UI testing, form interaction, and multi-state visual verification using the bundled Puppeteer MCP server.
---

# 🌐 Puppeteer Browser Automation & Telemetry Engine (MCP)

## Core Directive
When assigned tasks involving live web applications, frontend verification, web scraping, synthetic user flows, or automated UI audits, the agent must leverage the **bundled Puppeteer MCP Server** (`@modelcontextprotocol/server-puppeteer`).

> 🔴 **ANTI-BLIND EXECUTION MANDATE:**
> The agent is strictly forbidden from claiming that a web application, frontend UI, or web scraping pipeline functions correctly without driving the real browser session via Puppeteer tools and visually inspecting the resulting state.

---

## 1. Puppeteer MCP Tool Suite

The bundled Puppeteer MCP server exposes the following high-precision tools:

| Tool Name | Parameters | Purpose |
|---|---|---|
| `puppeteer_navigate` | `url` | Navigate the headless browser to any local (`http://localhost:<port>`) or remote URL. |
| `puppeteer_screenshot` | `name`, `width`, `height`, `selector` | Capture a high-resolution viewport or element screenshot directly into artifacts. |
| `puppeteer_click` | `selector` | Simulate user click on any CSS selector (buttons, tabs, links, toggles). |
| `puppeteer_fill` | `selector`, `value` | Fill input fields, textareas, or search boxes with test data. |
| `puppeteer_select` | `selector`, `value` | Select options from HTML dropdown menus. |
| `puppeteer_hover` | `selector` | Hover over elements to trigger CSS `:hover` states, tooltips, or dropdown menus. |
| `puppeteer_evaluate` | `script` | Execute arbitrary JavaScript in the page context and extract DOM data or telemetry. |

---

## 2. High-Resolution & Fullscreen Viewport Standard (MANDATORY)

> 🔴 **PROIBIÇÃO DE RESOLUÇÃO 800x600 (LOW-RES BAN):**
> É estritamente proibido chamar `puppeteer_screenshot` sem especificar dimensões ou usar a resolução padrão de 800x600.
> Toda captura DEVE usar resolução **Full HD (1920x1080)** ou superior em tela cheia para garantir fidelidade visual, renderização de layouts responsivos e nitidez de tipografia.

### Tabela de Resoluções Padrão:
| Modo | Largura (`width`) | Altura (`height`) | Uso |
|---|---|---|---|
| **🖥️ Full HD Desktop (Padrão Obrigatório)** | `1920` | `1080` | Dashboards, websites, landing pages, jogos WebGL em tela cheia |
| **🖥️ 2K / Widescreen Ultra-HD** | `2560` | `1440` | Interfaces de alta densidade, editores gráficos, simuladores |
| **📱 Mobile Full Breakpoint** | `390` | `844` | Validação mobile responsiva (iPhone 14/15 viewport) |
| **📱 Tablet Breakpoint** | `820` | `1180` | Layouts para iPad / tablets |

---

## 3. Mandatory Workflows

### Protocol A: Multi-State High-Res Playtesting & Visual Auditing
For any web application or frontend interface built or refactored:

1. **Launch Dev Server:** Start the local development server (e.g. `npx serve .`, `npm run dev`, `python -m http.server 8080`) via `run_command`.
2. **Navigate & Set Viewport:**
   - Call `puppeteer_navigate(url: "http://localhost:<port>")`.
   - Call `puppeteer_evaluate(script: "window.innerWidth = 1920; window.innerHeight = 1080; window.dispatchEvent(new Event('resize'));")`.
3. **Full HD Initial Capture (1920x1080):**
   - Call `puppeteer_screenshot(name: "state_01_desktop_fullscreen", width: 1920, height: 1080)`.
4. **Interactive State Transitions:**
   - Simulate user clicks (`puppeteer_click(selector: "#open-modal")` or `puppeteer_hover(selector: ".nav-dropdown")`).
   - Call `puppeteer_screenshot(name: "state_02_interaction", width: 1920, height: 1080)`.
5. **Form Submission & Dynamic Telemetry:**
   - Fill inputs (`puppeteer_fill(selector: "#search-input", value: "test query")`).
   - Trigger submission and capture `puppeteer_screenshot(name: "state_03_submitted", width: 1920, height: 1080)`.
6. **Mobile Breakpoint:**
   - Capture `puppeteer_screenshot(name: "state_04_mobile", width: 390, height: 844)`.
7. **Visual Inspection:** Run `view_file` on all captured `.png` screenshot artifacts to confirm typography, contrast, and layout integrity.


---

### Protocol B: Autonomous Web Scraping & Data Extraction
When gathering real-world data, benchmarks, or API documentation from websites:

1. **Page Load:** `puppeteer_navigate(url: "<target_url>")`.
2. **Dynamic Script Evaluation:**
   ```javascript
   // Pass script string to puppeteer_evaluate:
   () => {
     const items = Array.from(document.querySelectorAll('.item-card')).map(el => ({
       title: el.querySelector('.title')?.innerText?.trim(),
       price: el.querySelector('.price')?.innerText?.trim(),
       rating: el.querySelector('.rating')?.innerText?.trim(),
       link: el.querySelector('a')?.href
     }));
     return JSON.stringify(items, null, 2);
   }
   ```
3. **Pagination / Infinite Scroll:**
   - Execute scroll script via `puppeteer_evaluate(script: "window.scrollTo(0, document.body.scrollHeight);")` or click next page (`puppeteer_click(selector: ".pagination-next")`).
4. **Output Synthesis:** Format extracted data into structured JSON or Markdown reports.

---

### Protocol C: Runtime Telemetry & Console Error Diagnostic
To detect silent JavaScript errors, network drops, or performance regressions:

1. **Console & Error Inspection Script:**
   ```javascript
   () => {
     return {
       url: window.location.href,
       title: document.title,
       bodyLength: document.body.innerHTML.length,
       totalImages: document.images.length,
       brokenImages: Array.from(document.images).filter(img => !img.complete || img.naturalWidth === 0).map(img => img.src),
       fps: window.__fps_counter || 'N/A'
     };
   }
   ```
2. **Execute Diagnostic:** Call `puppeteer_evaluate` with the diagnostic script and verify `brokenImages.length === 0`.

---

## 3. Output Mandate

When executing Puppeteer browser automation, log the operational block:
```markdown
> 🌐 **PUPPETEER MCP AUTOMATION ACTIVE**
> **Target URL:** [http://localhost:PORT or URL]
> **Action Sequence:** [Navigate -> Click -> Fill -> Screenshot]
> **Captured Artifacts:** [state_01.png, state_02.png]
> **Telemetry Verdict:** [PASSED / FAILED with specific UI fixes applied]
```
