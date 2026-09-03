# Reference Guide: Glassmorphism UI & Modern Graphic Design System (`UI-GLASS-01`)

## 1. The Glassmorphism Design Tokens

Modern senior-level UI designs must utilize frosted glass dynamics, luminous borders, and spatial depth:

```css
:root {
  /* Glass Surface Backgrounds */
  --glass-bg-subtle: rgba(255, 255, 255, 0.04);
  --glass-bg-card: rgba(255, 255, 255, 0.08);
  --glass-bg-active: rgba(255, 255, 255, 0.14);
  
  /* Luminous Translucent Borders */
  --glass-border-hairline: 1px solid rgba(255, 255, 255, 0.16);
  --glass-border-highlight: 1px solid rgba(255, 255, 255, 0.32);
  
  /* Optical Blurs */
  --glass-blur-card: blur(24px);
  --glass-blur-modal: blur(40px);
  
  /* Spatial Ambient Shadows */
  --glass-shadow-card: 0 12px 40px 0 rgba(0, 0, 0, 0.45);
  --glass-shadow-glow: 0 0 24px 0 rgba(255, 255, 255, 0.12);
}

.glass-panel {
  background: var(--glass-bg-card);
  backdrop-filter: var(--glass-blur-card);
  -webkit-backdrop-filter: var(--glass-blur-card);
  border: var(--glass-border-hairline);
  box-shadow: var(--glass-shadow-card);
  border-radius: 16px;
  transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
}

.glass-panel:hover {
  background: var(--glass-bg-active);
  border: var(--glass-border-highlight);
  box-shadow: var(--glass-shadow-card), var(--glass-shadow-glow);
  transform: translateY(-2px);
}
```

---

## 2. Dynamic Layouts & Parallax Spatial Composition

1. **Multi-Plane Parallax**:
   - Background Layer (z-index 0): Ambient looping video or deep particle canvas moving at 0.2x scroll velocity.
   - Middle Layer (z-index 10): Glassmorphic cards and dynamic data widgets moving at 1.0x scroll velocity.
   - Foreground Layer (z-index 20): Floating HUD elements, interactive micro-actions, and navigation docks moving at 1.2x velocity.
2. **Typography & Hierarchy**:
   - Modern grotesque sans-serifs (Inter, Geist, SF Pro Display).
   - High-contrast letter-spacing on sub-headers (`letter-spacing: 0.12em; text-transform: uppercase; font-size: 0.75rem;`).
   - Clean negative space: minimum 24px inner padding on glass cards.
