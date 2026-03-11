FLOW_SLIDE_LAYOUT = {
  "1": {
    "name": "Linear Timeline",
    "purpose": "Best for clearly sequential, start-to-finish processes.",
    "structure": (
      "Layout: display:flex; flex-direction:column; padding:48px 72px; gap:20px. "
      "Background: deep dark gradient. "
      "Header: eyebrow + H1 (font-size:38px; font-weight:800; letter-spacing:-1px) + accent rule. "
      "Horizontal timeline (display:flex; align-items:flex-start; gap:0; flex:1; margin-top:12px): "
      "For each step (flex:1; display:flex; flex-direction:column; align-items:center): "
      "  Top rail (display:flex; align-items:center; width:100%): "
      "    • Left line (flex:1; height:2px; bg:rgba(255,255,255,0.15)) — omit for first. "
      "    • Node circle (width:44px; height:44px; border-radius:50%; bg:accent for first/active, "
      "      rgba(255,255,255,0.1) for rest; border:2px solid accent or rgba(255,255,255,0.2); "
      "      display:flex; align-items:center; justify-content:center; font-size:14px; font-weight:800). "
      "    • Right line (flex:1; height:2px; bg:rgba(255,255,255,0.15)) — omit for last. "
      "  Content card (margin-top:14px; width:90%; max-width:200px; text-align:center; "
      "  background:rgba(255,255,255,0.05); border:1px solid rgba(255,255,255,0.1); border-radius:12px; padding:14px 16px): "
      "    • Icon (font-size:20px; color:accent; margin-bottom:6px). "
      "    • Step label — 10px uppercase, letter-spacing:2px, accent, opacity:0.7. "
      "    • Step title — font-size:13px; font-weight:700; margin-top:4px; line-height:1.3. "
      "    • Description — font-size:11px; opacity:0.55; margin-top:4px; line-height:1.4. "
      "Footer notes/CTA bar: margin-top:auto; padding-top:12px; border-top:1px solid rgba(255,255,255,0.08); "
      "display:flex; justify-content:space-between; font-size:11px; opacity:0.5."
    )
  },
  "2": {
    "name": "Vertical Stepper",
    "purpose": "Best for guided walkthroughs or instructional processes.",
    "structure": (
      "Layout: display:flex; flex-direction:column; padding:44px 64px; gap:14px. "
      "Background: deep dark gradient. "
      "Header: eyebrow + H1 (font-size:36px; font-weight:800; letter-spacing:-1px) + accent rule. "
      "Main body (display:grid; grid-template-columns:280px 1fr; gap:36px; flex:1; align-items:start): "
      "Left column — vertical stepper: display:flex; flex-direction:column; gap:0. "
      "  For each step: display:flex; gap:14px; align-items:flex-start; margin-bottom:0. "
      "  • Marker column (display:flex; flex-direction:column; align-items:center): "
      "    - Circle node (width:36px; height:36px; border-radius:50%; bg:accent (active) or rgba(255,255,255,0.1); "
      "      display:flex; align-items:center; justify-content:center; font-size:13px; font-weight:800; flex-shrink:0). "
      "    - Connecting line below (width:2px; flex:1; min-height:20px; bg:rgba(255,255,255,0.12); margin:2px auto) — omit for last. "
      "  • Step content (display:flex; flex-direction:column; gap:2px; padding-bottom:16px): "
      "    - Step label — 10px uppercase, accent, letter-spacing:2px, opacity:0.7; margin-top:2px. "
      "    - Step title — font-size:14px; font-weight:700; margin-top:4px. "
      "Right column (supporting visual panel): "
      "background:rgba(255,255,255,0.05); border:1px solid rgba(255,255,255,0.1); "
      "border-radius:18px; padding:28px; display:flex; flex-direction:column; align-items:center; justify-content:center; gap:16px. "
      "  • Visual icon or diagram — font-size:80px; color:accent; opacity:0.85. "
      "  • Visual caption — font-size:13px; opacity:0.6; text-align:center; max-width:240px; line-height:1.5."
    )
  },
  "3": {
    "name": "Split-Screen Chronological",
    "purpose": "Best for historical progression or staged evolution.",
    "structure": (
      "Layout: display:flex; flex-direction:column; padding:44px 64px; gap:14px. "
      "Background: deep dark gradient. "
      "Header bar (display:flex; align-items:baseline; gap:16px): "
      "  • Eyebrow — 11px uppercase, accent, letter-spacing:3px, opacity:0.65. "
      "  • H1 — font-size:36px; font-weight:800; letter-spacing:-1px. "
      "  • Expanding accent rule (flex:1; height:2px). "
      "Main body (display:grid; grid-template-columns:1fr 1fr; gap:32px; flex:1; align-items:start): "
      "Left column (chronological list with icons/badges): display:flex; flex-direction:column; gap:14px. "
      "  For each entry: display:flex; gap:14px; align-items:flex-start. "
      "  • Icon or phase mark (width:36px; height:36px; border-radius:10px; bg:rgba(accent,0.15); "
      "    display:flex; align-items:center; justify-content:center; font-size:16px; color:accent; flex-shrink:0). "
      "  • Content: year/stage badge (11px accent pill) + title (14px; font-weight:700; margin-top:4px) "
      "    + short note (12px; opacity:0.65; margin-top:2px; line-height:1.4). "
      "  Thin connecting rule between entries (height:1px; bg:rgba(255,255,255,0.07); margin:-4px 0 0 18px). "
      "Right column (visual container): "
      "background:rgba(255,255,255,0.05); border:1px solid rgba(255,255,255,0.1); "
      "border-radius:18px; box-shadow:0 16px 48px rgba(0,0,0,0.3); padding:28px; "
      "display:flex; align-items:center; justify-content:center; min-height:320px. "
      "  Large visual icon or abstract diagram (80–100px; accent-tinted) + optional caption below."
    )
  },
  "4": {
    "name": "Split-Screen Feature Flow",
    "purpose": "Best for explaining feature-driven workflows or product flows.",
    "structure": (
      "Layout: display:flex; flex-direction:column; padding:44px 64px; gap:14px. "
      "Background: deep dark gradient. "
      "Header: eyebrow + H1 (font-size:36px; font-weight:800) + accent rule. "
      "Main body (display:grid; grid-template-columns:1fr 1fr; gap:32px; flex:1; align-items:start): "
      "Left column (process explanation blocks + feature cards): display:flex; flex-direction:column; gap:12px. "
      "  Process intro — font-size:16px; font-weight:300; opacity:0.75; line-height:1.65; margin-bottom:4px. "
      "  Feature flow cards (display:flex; flex-direction:column; gap:10px): "
      "    Each card: background:rgba(255,255,255,0.05); border:1px solid rgba(255,255,255,0.1); "
      "    border-radius:12px; padding:14px 18px; display:flex; align-items:center; gap:14px. "
      "    • Step number (accent; font-size:20px; font-weight:900; min-width:28px). "
      "    • Feature title (font-size:14px; font-weight:700) + micro-description (font-size:11px; opacity:0.6; margin-top:2px). "
      "Right column (central flow diagram + metrics): display:flex; flex-direction:column; gap:14px; align-items:center. "
      "  Flow diagram panel: background:rgba(255,255,255,0.04); border:1px solid rgba(255,255,255,0.1); "
      "  border-radius:18px; padding:24px; display:flex; flex-direction:column; align-items:center; gap:12px; flex:1. "
      "  Nodes connected by downward arrows: each node circle/rect with icon + label. "
      "  Key metrics/outcomes bar (display:flex; gap:16px; margin-top:8px; justify-content:center): "
      "    Metric chip: accent bg faint, border-radius:10px, padding:10px 16px; metric value (18px; font-weight:800; accent) + label (11px; opacity:0.6)."
    )
  },
  "5": {
    "name": "Circular Process Loop",
    "purpose": "Best for iterative cycles, feedback systems, or continuous improvement.",
    "structure": (
      "Layout: display:flex; flex-direction:column; padding:44px 64px; gap:16px; align-items:center. "
      "Background: deep dark gradient with large radial glow centered on canvas. "
      "Header (full-width, text-align:center): eyebrow + H1 (font-size:38px; font-weight:800) + accent rule (centered). "
      "Circular diagram container (position:relative; width:480px; height:340px; flex-shrink:0): "
      "  Center label circle (position:absolute; top:50%; left:50%; transform:translate(-50%,-50%); "
      "  width:100px; height:100px; border-radius:50%; bg:linear-gradient(135deg, accent-light, accent); "
      "  box-shadow:0 0 48px rgba(accent,0.4); display:flex; align-items:center; justify-content:center; "
      "  font-size:13px; font-weight:800; text-align:center; padding:10px; color:white). "
      "  Step nodes positioned absolutely in a circle (top, top-right, bottom-right, bottom, bottom-left, top-left etc.): "
      "  Each node: background:rgba(255,255,255,0.07); border:1px solid rgba(255,255,255,0.12); "
      "  border-radius:12px; padding:10px 16px; max-width:140px; text-align:center; font-size:12px; font-weight:600. "
      "  Curved connector arcs (use border-radius on pseudo-elements or thin lines between nodes). "
      "Legend/key (display:flex; gap:20px; justify-content:center; margin-top:8px; flex-wrap:wrap): "
      "  Each legend item: accent dot (8px; border-radius:50%) + label (12px; opacity:0.65)."
    )
  },
  "6": {
    "name": "Swimlane Flow",
    "purpose": "Best for cross-functional processes involving multiple roles or systems.",
    "structure": (
      "Layout: display:flex; flex-direction:column; padding:40px 60px; gap:12px. "
      "Background: deep dark gradient. "
      "Header: H1 (font-size:34px; font-weight:800) + accent rule. "
      "Swimlane container (display:flex; flex-direction:column; gap:0; flex:1; border:1px solid rgba(255,255,255,0.1); border-radius:14px; overflow:hidden): "
      "For each lane: display:flex; align-items:center; gap:0; min-height:90px; border-bottom:1px solid rgba(255,255,255,0.08). "
      "  Lane header (width:120px; flex-shrink:0; padding:12px 14px; bg:rgba(accent,0.08); border-right:1px solid rgba(255,255,255,0.1); "
      "  display:flex; align-items:center; justify-content:center): "
      "  • Role/system label — 11px uppercase, letter-spacing:2px, accent, text-align:center, line-height:1.3. "
      "  Lane steps (display:flex; align-items:center; gap:0; flex:1; padding:12px 20px): "
      "  For each step in lane: display:flex; align-items:center; gap:0; flex:1. "
      "    • Step card (background:rgba(255,255,255,0.06); border:1px solid rgba(255,255,255,0.1); "
      "      border-radius:10px; padding:10px 14px; text-align:center; font-size:12px; font-weight:600; max-width:140px). "
      "    • Connecting arrow '→' (font-size:16px; color:accent; opacity:0.6; flex-shrink:0; margin:0 6px). "
      "Footer assumptions bar: background:rgba(255,255,255,0.04); border-top:1px solid rgba(255,255,255,0.08); "
      "padding:10px 20px; font-size:11px; opacity:0.5; letter-spacing:0.5px."
    )
  },
  "7": {
    "name": "Card-Based Flow",
    "purpose": "Best for modular step-based flows with equal emphasis.",
    "structure": (
      "Layout: display:flex; flex-direction:column; padding:44px 64px; gap:16px. "
      "Background: deep dark gradient. "
      "Header: eyebrow + H1 (font-size:38px; font-weight:800; letter-spacing:-1px) + accent rule. "
      "Card flow (display:grid; grid-template-columns: repeat(3,1fr) or repeat(4,1fr); gap:16px; flex:1; align-items:start; position:relative): "
      "Each step card: background:rgba(255,255,255,0.06); border:1px solid rgba(255,255,255,0.1); "
      "border-radius:16px; padding:22px 20px; display:flex; flex-direction:column; gap:10px; position:relative. "
      "  Active/current card: background:rgba(accent,0.1); border:1px solid rgba(accent,0.3). "
      "  • Top row: icon container (40px; border-radius:10px; bg:rgba(accent,0.15); color:accent; display:flex; align:center; justify:center; font-size:18px) "
      "    + step number (margin-left:auto; font-size:11px; opacity:0.4; font-weight:700). "
      "  • Step title — font-size:15px; font-weight:700; line-height:1.3. "
      "  • Short description — font-size:12px; opacity:0.65; line-height:1.5. "
      "Directional arrows between cards: position:absolute; right:-14px; top:50%; transform:translateY(-50%); "
      "font-size:18px; color:accent; opacity:0.6; z-index:2."
    )
  },
  "8": {
    "name": "Problem-to-Outcome Flow",
    "purpose": "Best for storytelling from challenge to result.",
    "structure": (
      "Layout: display:flex; flex-direction:column; padding:44px 64px; gap:14px. "
      "Background: deep dark gradient. "
      "Header: H1 (font-size:36px; font-weight:800; letter-spacing:-1px) + accent rule. "
      "Main body (display:grid; grid-template-columns:1fr 48px 1fr 48px 1fr; gap:0; flex:1; align-items:stretch): "
      "Problem section: background:rgba(239,68,68,0.07); border:1px solid rgba(239,68,68,0.18); "
      "border-radius:16px; padding:22px 24px; display:flex; flex-direction:column; gap:10px. "
      "  • 'PROBLEM' eyebrow — 10px uppercase, red-tinted, opacity:0.75. "
      "  • Problem statement — font-size:16px; font-weight:700; color:#f87171; margin-top:6px; line-height:1.4. "
      "  • 2–3 challenge points — font-size:12px; opacity:0.72; line-height:1.5. "
      "Left arrow separator: display:flex; align-items:center; justify-content:center. "
      "'→' font-size:24px; color:accent; font-weight:800. "
      "Process stages section: background:rgba(255,255,255,0.05); border:1px solid rgba(255,255,255,0.1); "
      "border-radius:16px; padding:22px 24px; display:flex; flex-direction:column; gap:10px. "
      "  • 'PROCESS' eyebrow — 10px uppercase, accent, opacity:0.7. "
      "  • Process stages list: display:flex; flex-direction:column; gap:8px. "
      "    Each stage: display:flex; align-items:center; gap:10px; font-size:13px. "
      "    Numbered circle (24px; bg:rgba(accent,0.15); color:accent; border-radius:50%; font-size:11px; font-weight:700). "
      "Right arrow separator: same '→' style. "
      "Outcomes section: background:rgba(16,185,129,0.07); border:1px solid rgba(16,185,129,0.2); "
      "border-radius:16px; padding:22px 24px; display:flex; flex-direction:column; gap:10px. "
      "  • 'OUTCOMES' eyebrow — 10px uppercase, green, opacity:0.75. "
      "  • 2–3 outcome/benefit items with ✓ green circles."
    )
  },
  "9": {
    "name": "Data-Driven Process",
    "purpose": "Best for analytics-heavy workflows or KPI-based processes.",
    "structure": (
      "Layout: display:flex; flex-direction:column; padding:44px 64px; gap:14px. "
      "Background: deep dark gradient. "
      "Header: eyebrow + H1 (font-size:36px; font-weight:800) + accent rule. "
      "Main body (display:grid; grid-template-columns:220px 1fr; gap:28px; flex:1; align-items:start): "
      "Left column (process steps list): display:flex; flex-direction:column; gap:10px. "
      "  Each step: display:flex; gap:12px; align-items:flex-start. "
      "  • Marker (circle 32px; bg:accent for active; rgba(255,255,255,0.1) others; "
      "    border-radius:50%; font-size:12px; font-weight:800; display:flex; align:center; justify:center; flex-shrink:0). "
      "  • Step text (font-size:13px; font-weight:600; line-height:1.4; margin-top:6px). "
      "  Connecting line between markers (width:2px; min-height:14px; bg:rgba(255,255,255,0.1); margin:0 auto). "
      "Right column (charts + metrics per step): display:flex; flex-direction:column; gap:12px. "
      "  Each step metric card: background:rgba(255,255,255,0.05); border:1px solid rgba(255,255,255,0.1); "
      "  border-radius:12px; padding:14px 18px; display:grid; grid-template-columns:1fr auto; gap:16px; align-items:center. "
      "  • Left: inline annotation (font-size:12px; opacity:0.65; line-height:1.5) + "
      "    mini bar chart (height:8px; border-radius:4px; bg:rgba(255,255,255,0.1); inner fill:accent; width:60%). "
      "  • Right: key metric value (font-size:22px; font-weight:800; color:accent; letter-spacing:-1px). "
      "Bottom KPI summary strip: display:flex; gap:24px; padding-top:10px; border-top:1px solid rgba(255,255,255,0.08). "
      "Each KPI: metric value (18px; font-weight:800; accent) + label (10px; opacity:0.5)."
    )
  }
}