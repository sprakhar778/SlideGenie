KEY_POINTS_SLIDE_LAYOUT = {
  "1": {
    "name": "Split-Screen / Bullet Emphasis",
    "purpose": "When key points need strong visual reinforcement",
    "structure": (
      "Layout: display:flex; flex-direction:column; padding:44px 64px; gap:14px. "
      "Background: deep dark gradient. "
      "Header bar (display:flex; align-items:baseline; gap:16px): "
      "  • Eyebrow — 11px uppercase, letter-spacing:3px, accent, opacity:0.65. "
      "  • H1 — font-size:36px; font-weight:800; letter-spacing:-1px. "
      "  • Thin expanding accent rule (flex:1; height:2px; bg:linear-gradient(90deg, accent, transparent)). "
      "Main body (display:grid; grid-template-columns:1.1fr 1fr; gap:32px; flex:1; align-items:center): "
      "Left column — icon-led bullet list: display:flex; flex-direction:column; gap:12px. "
      "  Each bullet row: display:flex; align-items:flex-start; gap:14px; padding:12px 16px; "
      "  background:rgba(255,255,255,0.05); border-radius:12px; border:1px solid rgba(255,255,255,0.08). "
      "  • Icon container (36px; border-radius:10px; bg:rgba(accent,0.15); color:accent; "
      "    display:flex; align-items:center; justify-content:center; font-size:16px; flex-shrink:0). "
      "  • Text block: key point title (font-size:14px; font-weight:700; line-height:1.3) "
      "    + optional sub-note (font-size:12px; opacity:0.6; margin-top:3px; line-height:1.4). "
      "Right column — supporting visual/illustration container: "
      "background:rgba(255,255,255,0.05); border:1px solid rgba(255,255,255,0.1); "
      "border-radius:18px; padding:28px; display:flex; align-items:center; justify-content:center; "
      "box-shadow:0 16px 48px rgba(0,0,0,0.3); min-height:280px. "
      "  Large thematic icon (80px; color:accent; opacity:0.85) or abstract decorative shape."
    )
  },
  "2": {
    "name": "Vertical Stack / Emphasis Blocks",
    "purpose": "Clear emphasis on each key point individually",
    "structure": (
      "Layout: display:flex; flex-direction:column; padding:40px 72px; gap:12px. "
      "Background: deep dark gradient. "
      "Header: H1 (font-size:38px; font-weight:800; letter-spacing:-1px) + subtitle (font-size:16px; font-weight:300; opacity:0.7) + accent rule. "
      "Stacked bullet cards (display:flex; flex-direction:column; gap:10px; flex:1): "
      "Each card: display:flex; align-items:center; gap:18px; padding:14px 20px; "
      "background:rgba(255,255,255,0.06); border:1px solid rgba(255,255,255,0.1); border-radius:14px. "
      "  • Left accent indicator bar (width:4px; height:36px; border-radius:2px; background:accent; flex-shrink:0). "
      "  • Card text: key point (font-size:15px; font-weight:700) + optional implication (font-size:12px; opacity:0.62; margin-top:3px). "
      "  • Right side (margin-left:auto): optional category tag — 10px uppercase, accent bg faint, border-radius:20px, padding:2px 10px. "
      "Callout/takeaway banner (margin-top:auto): "
      "background: linear-gradient(135deg, rgba(accent, 0.15), rgba(accent, 0.05)); "
      "border:1px solid rgba(accent,0.3); border-radius:12px; padding:14px 20px; "
      "display:flex; align-items:center; gap:12px; font-size:13px; font-weight:600. "
      "  Star or lightbulb icon (accent) + takeaway text."
    )
  },
  "3": {
    "name": "Chronological Timeline",
    "purpose": "Sequential or time-based key points",
    "structure": (
      "Layout: display:flex; flex-direction:column; padding:44px 64px; gap:14px. "
      "Background: deep dark gradient. "
      "Header: eyebrow + H1 (font-size:36px; font-weight:800) + accent rule. "
      "Vertical timeline (display:flex; flex-direction:column; gap:0; flex:1; margin-top:8px): "
      "For each key point: display:flex; gap:18px; align-items:flex-start; margin-bottom:0. "
      "  Marker column (display:flex; flex-direction:column; align-items:center; gap:0): "
      "    • Circle node (width:36px; height:36px; border-radius:50%; bg:accent for first/active, "
      "      rgba(255,255,255,0.1) others; display:flex; align-items:center; justify-content:center; "
      "      font-size:12px; font-weight:800; flex-shrink:0). "
      "    • Connecting line below (width:2px; flex:1; min-height:24px; bg:rgba(255,255,255,0.12); margin:2px auto). "
      "  Content block (padding-bottom:16px): "
      "    • Phase/step badge — 11px uppercase, accent, background:rgba(accent,0.12), border-radius:20px, padding:2px 10px; margin-bottom:6px. "
      "    • Key point title — font-size:15px; font-weight:700; line-height:1.3. "
      "    • Annotation/micro-description — font-size:12px; opacity:0.65; margin-top:4px; line-height:1.5. "
      "    • Optional side annotation chip (display:inline-flex; font-size:11px; opacity:0.55; margin-top:6px)."
    )
  },
  "4": {
    "name": "Grid / Feature Cards",
    "purpose": "Equal-weight, modular key ideas",
    "structure": (
      "Layout: display:flex; flex-direction:column; padding:40px 60px; gap:14px. "
      "Background: deep dark gradient. "
      "Header: eyebrow + H1 (font-size:36px; font-weight:800; letter-spacing:-1px) + accent rule. "
      "Card grid (display:grid; grid-template-columns: repeat(2,1fr) or repeat(3,1fr) based on count; gap:16px; flex:1): "
      "Each card: background:rgba(255,255,255,0.06); border:1px solid rgba(255,255,255,0.1); "
      "border-radius:16px; padding:22px 22px; display:flex; flex-direction:column; gap:12px. "
      "  • Top row: icon container (44px; border-radius:12px; bg:rgba(accent,0.15); "
      "    display:flex; align-items:center; justify-content:center; font-size:20px; color:accent) "
      "    + card number (margin-left:auto; font-size:11px; font-weight:700; opacity:0.35). "
      "  • Card title — font-size:15px; font-weight:700; line-height:1.3. "
      "  • Short description — font-size:12px; font-weight:300; opacity:0.7; line-height:1.5. "
      "  • Bottom accent strip (position:absolute; bottom:0; left:0; right:0; height:3px; bg:accent; "
      "    border-radius:0 0 16px 16px; use position:relative on card)."
    )
  },
  "5": {
    "name": "Problem-Solution Split",
    "purpose": "When content contrasts challenges with resolutions",
    "structure": (
      "Layout: display:flex; flex-direction:column; padding:44px 64px; gap:14px. "
      "Background: deep dark gradient. "
      "Header: H1 (font-size:36px; font-weight:800; text-align:center) + thin centered accent rule. "
      "Main body (display:grid; grid-template-columns:1fr 56px 1fr; gap:0; flex:1; align-items:stretch): "
      "Left panel (Problem): background:rgba(239,68,68,0.07); border:1px solid rgba(239,68,68,0.18); "
      "border-radius:16px; padding:22px 26px; display:flex; flex-direction:column; gap:10px. "
      "  • 'CHALLENGES' eyebrow — 10px uppercase, red-tinted, opacity:0.75. "
      "  • Problem parent title — font-size:17px; font-weight:700; color:#f87171; margin-top:6px. "
      "  • Bullet items: display:flex; gap:10px; align-items:flex-start; font-size:13px; opacity:0.82; line-height:1.5. "
      "    ✗ red dot (8px; border-radius:50%; bg:#ef4444; flex-shrink:0; margin-top:6px). "
      "Center directional divider: display:flex; flex-direction:column; align-items:center; justify-content:center; gap:8px. "
      "  • '→' — font-size:28px; color:accent; font-weight:800. "
      "Right panel (Solutions): background:rgba(16,185,129,0.07); border:1px solid rgba(16,185,129,0.2); "
      "border-radius:16px; padding:22px 26px; display:flex; flex-direction:column; gap:10px. "
      "  • 'RESOLUTIONS' eyebrow — 10px uppercase, green, opacity:0.75. "
      "  • Solution parent title — font-size:17px; font-weight:700; color:#10b981; margin-top:6px. "
      "  • Solution bullets with ✓ green circles."
    )
  },
  "6": {
    "name": "Central Core / Orbiting Points",
    "purpose": "Multiple ideas connected to one central concept",
    "structure": (
      "Layout: display:flex; flex-direction:column; padding:40px 64px; gap:14px. "
      "Background: deep dark gradient with large radial glow at center. "
      "Header row: eyebrow + H1 (font-size:36px; font-weight:800) + accent rule. "
      "Diagram container (position:relative; flex:1; display:flex; align-items:center; justify-content:center; min-height:320px): "
      "Center core node (position:absolute; top:50%; left:50%; transform:translate(-50%,-50%)): "
      "  width:110px; height:110px; border-radius:50%; background:linear-gradient(135deg, accent-light, accent); "
      "  box-shadow:0 0 48px rgba(accent,0.45); display:flex; align-items:center; justify-content:center; "
      "  font-size:14px; font-weight:800; color:white; text-align:center; padding:12px. "
      "Surrounding bullet point nodes (position absolute, distributed around center): "
      "  Each node: background:rgba(255,255,255,0.07); border:1px solid rgba(255,255,255,0.12); "
      "  border-radius:12px; padding:10px 16px; max-width:160px; text-align:center; font-size:12px; font-weight:600; line-height:1.3. "
      "Connecting lines from nodes to center: thin (1px; rgba(255,255,255,0.15); "
      "can be done with CSS transform + position:absolute lines or borders)."
    )
  },
  "7": {
    "name": "Numbered Priority Stack",
    "purpose": "Ranked or prioritized key messages",
    "structure": (
      "Layout: display:flex; flex-direction:column; padding:44px 80px; gap:14px. "
      "Background: deep dark gradient. "
      "Header: eyebrow + H1 (font-size:38px; font-weight:800; letter-spacing:-1px) + accent rule. "
      "Numbered bullet list (display:flex; flex-direction:column; gap:10px; flex:1): "
      "Each item row: display:flex; align-items:center; gap:20px; padding:14px 20px; "
      "background:rgba(255,255,255,0.05); border-radius:12px; border:1px solid rgba(255,255,255,0.08). "
      "Progressive emphasis: first item — accent bg stronger (rgba(accent,0.12)); border:rgba(accent,0.3); "
      "second item — slightly less emphasis; rest — standard. "
      "  • Large number — font-size:32px; font-weight:900; color:accent (first), reducing opacity for lower ranks; "
      "    letter-spacing:-1px; min-width:44px; line-height:1. "
      "  • Vertical separator — width:1px; height:32px; bg:rgba(255,255,255,0.15); flex-shrink:0. "
      "  • Text block: key message (font-size:15px; font-weight:700; line-height:1.3) "
      "    + sub-note (font-size:12px; opacity:0.6; margin-top:3px). "
      "  • Right priority badge (margin-left:auto): 'TOP', '2ND', '3RD' or ranking label — "
      "    10px uppercase, accent (top), fading for lower; border-radius:20px; padding:3px 10px; "
      "    bg:rgba(accent,0.12)."
    )
  },
  "8": {
    "name": "Side-by-Side Comparison",
    "purpose": "Direct comparison between two approaches or options",
    "structure": (
      "Layout: display:flex; flex-direction:column; padding:44px 64px; gap:14px. "
      "Background: deep dark gradient. "
      "Header: H1 (font-size:36px; font-weight:800; text-align:center or left) + accent rule. "
      "Column header row (display:grid; grid-template-columns:1fr 2px 1fr; padding:8px 16px; gap:0; margin-bottom:4px): "
      "  • Left label — 12px uppercase, letter-spacing:2px, accent-A, font-weight:700. "
      "  • Divider line (width:2px; bg:rgba(255,255,255,0.15); align-self:stretch). "
      "  • Right label — 12px uppercase, letter-spacing:2px, accent-B, font-weight:700; text-align:right. "
      "Comparison body (display:grid; grid-template-columns:1fr 2px 1fr; gap:0; flex:1; align-items:start): "
      "Left column (Approach A bullets): display:flex; flex-direction:column; gap:8px; padding:0 16px 0 0. "
      "  Each: display:flex; align-items:flex-start; gap:10px; font-size:13px; line-height:1.5; opacity:0.85. "
      "  Bullet: accent-A dot (8px; border-radius:50%; flex-shrink:0; margin-top:6px). "
      "Center divider: width:2px; bg:linear-gradient(180deg, transparent, rgba(255,255,255,0.2), transparent); align-self:stretch. "
      "Right column (Approach B bullets): mirrors left with accent-B dots. "
      "Verdict/Summary row (margin-top:auto; padding-top:12px; border-top:1px solid rgba(255,255,255,0.08); "
      "display:flex; justify-content:center; gap:24px; font-size:13px; font-weight:600): "
      "  Verdict chip — accent bg, border-radius:20px, padding:6px 18px."
    )
  },
  "9": {
    "name": "Key Points with Metrics",
    "purpose": "Data-supported key insights",
    "structure": (
      "Layout: display:flex; flex-direction:column; padding:44px 72px; gap:14px. "
      "Background: deep dark gradient. "
      "Header: eyebrow + H1 (font-size:36px; font-weight:800; letter-spacing:-1px) + accent rule. "
      "Primary bullet list (display:flex; flex-direction:column; gap:10px; flex:1): "
      "Each bullet row: display:flex; align-items:flex-start; gap:14px; padding:12px 18px; "
      "background:rgba(255,255,255,0.05); border-radius:12px; border:1px solid rgba(255,255,255,0.08). "
      "  • Icon/number circle (32px; border-radius:50%; bg:accent; display:flex; align:center; justify:center; "
      "    font-size:13px; font-weight:800; color:white; flex-shrink:0). "
      "  • Key insight text — font-size:14px; font-weight:600; line-height:1.4; flex:1. "
      "  • Supporting stat (margin-left:auto; font-size:18px; font-weight:900; color:accent; "
      "    letter-spacing:-0.5px; white-space:nowrap) + unit label below it (10px; opacity:0.55). "
      "Bottom metrics/KPI strip (display:grid; grid-template-columns: repeat(3,1fr) or repeat(4,1fr); gap:12px; margin-top:8px): "
      "Each metric tile: background:rgba(255,255,255,0.06); border:1px solid rgba(255,255,255,0.1); "
      "border-radius:12px; padding:14px 18px; display:flex; flex-direction:column; gap:4px. "
      "  • KPI value — font-size:26px; font-weight:900; color:accent; letter-spacing:-1px. "
      "  • KPI label — font-size:10px; uppercase; letter-spacing:2px; opacity:0.55."
    )
  }
}
