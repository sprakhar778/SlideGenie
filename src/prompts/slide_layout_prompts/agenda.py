AGENDA_SLIDE_LAYOUT = {
  "1": {
    "name": "Split-Screen / Timeline",
    "purpose": "Chronological, step-based, workshop or process-driven content.",
    "structure": (
      "Layout: display:flex; flex-direction:column; padding:48px 72px; gap:20px. "
      "Background: deep dark gradient (e.g. linear-gradient(135deg, #0f0c29, #302b63, #24243e)). "
      "Top header row (display:flex; align-items:center; justify-content:space-between): "
      "  • Eyebrow label 'AGENDA' — 11px uppercase, letter-spacing:4px, accent color, opacity:0.7. "
      "  • H1 slide title — font-size:38px; font-weight:800; letter-spacing:-1px; flex:1; margin-left:24px. "
      "  • Optional step count badge (e.g. '4 Topics') — pill shape, accent bg, 12px, font-weight:600. "
      "Thin full-width accent rule — height:2px; background:linear-gradient(90deg, accent, transparent); margin:4px 0. "
      "Main body (display:grid; grid-template-columns:220px 1fr; gap:40px; flex:1; align-items:start; margin-top:8px): "
      "Left column — vertical timeline rail: display:flex; flex-direction:column; gap:0; position:relative. "
      "  For each step render: "
      "  • Circle node — width:36px; height:36px; border-radius:50%; background: accent (active first) or rgba(255,255,255,0.1); "
      "    display:flex; align-items:center; justify-content:center; font-size:13px; font-weight:700; z-index:1. "
      "  • Vertical connecting line below node — width:2px; flex:1; min-height:28px; background:rgba(255,255,255,0.12); "
      "    margin:0 auto. "
      "  • Step label beside node — font-size:12px; opacity:0.55; letter-spacing:0.5px; margin-left:12px (use flex row). "
      "Right column — description cards: display:flex; flex-direction:column; gap:14px. "
      "  Each card: background:rgba(255,255,255,0.05); border:1px solid rgba(255,255,255,0.1); "
      "  border-radius:14px; padding:16px 22px; display:flex; align-items:flex-start; gap:16px. "
      "  Inside each card: left accent bar (width:3px; border-radius:2px; background: accent; align-self:stretch) + "
      "  content block (section title 15px font-weight:700 + subpoints 13px opacity:0.65 line-height:1.5)."
    )
  },
  "2": {
    "name": "Two-Column / Minimal Outline",
    "purpose": "Professional, structured, executive presentations.",
    "structure": (
      "Layout: display:flex; flex-direction:column; padding:56px 90px; gap:28px. "
      "Background: clean light gradient (linear-gradient(160deg, #f8faff, #eef2ff)) or very dark muted tone. "
      "Header (text-align:center or left): "
      "  • Eyebrow label — 11px uppercase, letter-spacing:4px, accent, opacity:0.6. "
      "  • H1 title — font-size:44px; font-weight:800; letter-spacing:-1.5px; line-height:1.1; margin-top:8px. "
      "  • Thin centered accent rule — height:2px; width:70px; background: accent; margin:18px auto (or left if left-aligned). "
      "Main body — two-column outline grid (display:grid; grid-template-columns:1fr 1fr; gap:32px; flex:1; align-content:start): "
      "Each agenda item row (spans full grid as a sub-grid or individual row): "
      "  Background: transparent or rgba(0,0,0,0.03); border-bottom:1px solid rgba(0,0,0,0.07) (light) or rgba(255,255,255,0.08) (dark). "
      "  padding:14px 0; display:grid; grid-template-columns:1fr 1fr; align-items:center; gap:24px. "
      "  Left cell: section number or index (accent color, font-size:11px, font-weight:700, letter-spacing:2px, opacity:0.7) "
      "    + section heading (font-size:15px; font-weight:700; margin-top:4px). "
      "  Right cell: short description — font-size:13px; font-weight:300; opacity:0.7; line-height:1.55. "
      "Footer bar (margin-top:auto; display:flex; justify-content:space-between; align-items:center): "
      "  • Presenter name or date — 11px, opacity:0.45, letter-spacing:1px. "
      "  • Topic count badge — accent colored pill, 11px."
    )
  },
  "3": {
    "name": "Single-Column / Numbered Stack",
    "purpose": "Linear talks, keynotes, simple progressive flow.",
    "structure": (
      "Layout: display:flex; flex-direction:column; padding:52px 100px; gap:16px. "
      "Background: bold full-bleed dark gradient. "
      "Header: "
      "  • H1 title — font-size:40px; font-weight:800; letter-spacing:-1px; margin-bottom:4px. "
      "  • Subtitle or session name — font-size:16px; font-weight:300; opacity:0.65; letter-spacing:0.5px. "
      "  • Accent rule — height:2px; width:60px; background: accent; border-radius:2px; margin:16px 0. "
      "Stacked agenda item list (display:flex; flex-direction:column; gap:12px; flex:1): "
      "Each item row: display:flex; align-items:center; gap:24px; padding:14px 20px; "
      "background:rgba(255,255,255,0.05); border-radius:12px; border:1px solid rgba(255,255,255,0.08). "
      "  • Large number — font-size:32px; font-weight:900; color: accent; letter-spacing:-1px; min-width:40px; line-height:1. "
      "  • Vertical separator — width:1px; height:36px; background:rgba(255,255,255,0.15). "
      "  • Text block: section title (font-size:16px; font-weight:700) + optional sub-label (font-size:12px; opacity:0.55; margin-top:3px). "
      "  • Right side (margin-left:auto): duration or phase label — 11px uppercase, letter-spacing:2px, accent, opacity:0.7. "
      "Bottom progress bar (display:flex; gap:6px; margin-top:auto; padding-top:12px): "
      "  Render one small pill segment per agenda item — height:4px; border-radius:4px; flex:1; "
      "  First item: background: accent; rest: background:rgba(255,255,255,0.15)."
    )
  },
  "4": {
    "name": "Split-Screen / Feature-Focus",
    "purpose": "Product demos, feature breakdowns, thematic storytelling.",
    "structure": (
      "Layout: display:flex; flex-direction:column; padding:48px 72px; gap:20px. "
      "Background: deep rich dark gradient. "
      "Header row (display:flex; align-items:baseline; gap:20px): "
      "  • H1 title — font-size:40px; font-weight:800; letter-spacing:-1px. "
      "  • Eyebrow sub-tag — 11px uppercase, letter-spacing:3px, accent, opacity:0.65. "
      "  • Thin accent rule — height:2px; flex:1; background:linear-gradient(90deg, accent, transparent). "
      "Main body (display:grid; grid-template-columns:1.1fr 1fr; gap:36px; flex:1): "
      "Left column — feature card list (display:flex; flex-direction:column; gap:14px): "
      "  Each feature card: background:rgba(255,255,255,0.06); border:1px solid rgba(255,255,255,0.1); "
      "  border-radius:14px; padding:18px 22px; display:flex; align-items:center; gap:16px; "
      "  transition:background 0.2s (first/active card can have stronger accent bg). "
      "  • Icon or number circle — width:36px; height:36px; border-radius:10px; background: accent; "
      "    display:flex; align-items:center; justify-content:center; font-size:15px; font-weight:700; color:white. "
      "  • Text block: feature title (font-size:15px; font-weight:700) + micro-description (font-size:12px; opacity:0.6; margin-top:3px). "
      "Right column — central theme visual panel: "
      "  background:rgba(255,255,255,0.04); border:1px solid rgba(255,255,255,0.1); border-radius:20px; "
      "  display:flex; flex-direction:column; align-items:center; justify-content:center; gap:20px; padding:32px. "
      "  • Large central icon or abstract shape — 80px, accent-tinted. "
      "  • Core theme label — font-size:20px; font-weight:700; text-align:center. "
      "  • 2–3 callout chips (display:flex; flex-wrap:wrap; gap:8px; justify-content:center): "
      "    each chip: background:rgba(accent,0.12); color:accent; border-radius:20px; padding:4px 14px; font-size:12px."
    )
  },
  "5": {
    "name": "Horizontal Roadmap",
    "purpose": "Strategic plans, phases, milestones.",
    "structure": (
      "Layout: display:flex; flex-direction:column; padding:52px 80px; gap:24px. "
      "Background: dark premium gradient. "
      "Header (display:flex; align-items:center; justify-content:space-between): "
      "  • H1 title — font-size:42px; font-weight:800; letter-spacing:-1px. "
      "  • Total phases badge — accent pill, 12px font-weight:600. "
      "Thin full-width rule — height:1px; background:rgba(255,255,255,0.12); margin:4px 0. "
      "Horizontal milestone container (display:flex; align-items:flex-start; gap:0; flex:1; margin-top:16px): "
      "For each milestone: "
      "  Wrapper — display:flex; flex-direction:column; align-items:center; flex:1; gap:0. "
      "  Top row (display:flex; align-items:center; width:100%): "
      "    • Left connecting line (flex:1; height:2px; background:rgba(255,255,255,0.15)) — omit for first node. "
      "    • Node circle — width:44px; height:44px; border-radius:50%; "
      "      background: accent (active) or rgba(255,255,255,0.1); "
      "      border:2px solid accent (active) or rgba(255,255,255,0.2); "
      "      display:flex; align-items:center; justify-content:center; font-size:14px; font-weight:800. "
      "    • Right connecting line (flex:1; height:2px; background:rgba(255,255,255,0.15)) — omit for last node. "
      "  Description card below node (margin-top:16px; width:90%; max-width:200px; text-align:center): "
      "    background:rgba(255,255,255,0.05); border:1px solid rgba(255,255,255,0.1); border-radius:12px; padding:14px 16px. "
      "    • Phase label — font-size:11px; uppercase; letter-spacing:2px; accent; opacity:0.7. "
      "    • Phase title — font-size:14px; font-weight:700; margin-top:6px; line-height:1.35. "
      "    • 1–2 bullet sub-items — font-size:11px; opacity:0.55; margin-top:6px; line-height:1.5."
    )
  },
  "6": {
    "name": "Grid / Modular Cards",
    "purpose": "Equal-weight, non-linear agenda sections.",
    "structure": (
      "Layout: display:flex; flex-direction:column; padding:48px 72px; gap:24px. "
      "Background: deep dark gradient or bold gradient. "
      "Header (text-align:center or left): "
      "  • Eyebrow — 11px uppercase, letter-spacing:4px, accent, opacity:0.65. "
      "  • H1 title — font-size:40px; font-weight:800; letter-spacing:-1px; margin-top:8px. "
      "  • Short accent rule — height:2px; width:60px; background: accent; margin:14px auto (or left). "
      "Card grid (display:grid; grid-template-columns: repeat(3, 1fr) or repeat(2, 1fr) depending on item count; gap:18px; flex:1): "
      "Each card: background:rgba(255,255,255,0.06); border:1px solid rgba(255,255,255,0.1); "
      "border-radius:16px; padding:22px 24px; display:flex; flex-direction:column; gap:12px; "
      "transition:background 0.2s; position:relative; overflow:hidden. "
      "Inside each card: "
      "  • Top row: icon container (width:40px; height:40px; border-radius:10px; background:rgba(accent,0.15); "
      "    display:flex; align-items:center; justify-content:center; font-size:18px; color:accent) "
      "    + section number (margin-left:auto; font-size:11px; opacity:0.4; font-weight:700). "
      "  • Section title — font-size:15px; font-weight:700; line-height:1.3. "
      "  • Optional micro-description — font-size:12px; opacity:0.6; line-height:1.5. "
      "  • Bottom accent strip (position:absolute; bottom:0; left:0; right:0; height:3px; background: accent; "
      "    border-radius:0 0 16px 16px; opacity:0 → 1 for active card)."
    )
  },
  "7": {
    "name": "Central Core Diagram",
    "purpose": "All agenda items connect to one core theme.",
    "structure": (
      "Layout: display:flex; flex-direction:column; padding:44px 72px; gap:20px. "
      "Background: dark deep gradient with a large radial glow centered on the canvas (position:absolute, pointer-events:none). "
      "Header row: "
      "  • H1 title — font-size:38px; font-weight:800; letter-spacing:-1px. "
      "  • Eyebrow 'AGENDA' — 11px uppercase, letter-spacing:4px, accent, opacity:0.65; margin-left:16px. "
      "Main diagram area (position:relative; flex:1; display:flex; align-items:center; justify-content:center): "
      "Center core node (position:absolute; top:50%; left:50%; transform:translate(-50%,-50%)): "
      "  width:120px; height:120px; border-radius:50%; "
      "  background:linear-gradient(135deg, accent-light, accent); "
      "  box-shadow:0 0 48px rgba(accent,0.5); "
      "  display:flex; align-items:center; justify-content:center; text-align:center; "
      "  font-size:15px; font-weight:800; color:white; padding:12px. "
      "Surrounding agenda item nodes — position each absolutely around the center using calc-based offsets "
      "(e.g. top:10% left:10%, top:10% right:10%, bottom:10% left:10%, bottom:10% right:10%, top:50% left:5%, top:50% right:5%): "
      "Each node: background:rgba(255,255,255,0.07); border:1px solid rgba(255,255,255,0.12); "
      "border-radius:14px; padding:14px 18px; max-width:170px; text-align:center; "
      "display:flex; flex-direction:column; align-items:center; gap:8px. "
      "  • Icon circle — width:30px; height:30px; border-radius:50%; background:rgba(accent,0.15); "
      "    display:flex; align-items:center; justify-content:center; font-size:14px; color:accent. "
      "  • Section title — font-size:13px; font-weight:700; line-height:1.3. "
      "Connector lines between center and nodes: use thin border/box-shadow trick or simply omit — "
      "rely on visual proximity if exact SVG lines are not feasible in pure HTML/CSS."
    )
  },
  "8": {
    "name": "Executive Summary / Outline",
    "purpose": "Leadership briefings, high-level overviews.",
    "structure": (
      "Layout: display:grid; grid-template-columns:320px 1fr; height:720px; overflow:hidden. "
      "Background: dark premium gradient on the right panel; left panel has a distinct deeper or accent-tinted bg. "
      "Left panel (padding:56px 40px; display:flex; flex-direction:column; gap:20px; "
      "background:rgba(accent,0.08); border-right:1px solid rgba(255,255,255,0.1)): "
      "  • Eyebrow label — 10px uppercase, letter-spacing:4px, accent, opacity:0.7. "
      "  • H1 title — font-size:38px; font-weight:800; letter-spacing:-1.5px; line-height:1.15; margin-top:8px. "
      "  • Thin accent rule — height:3px; width:50px; background: accent; border-radius:2px; margin:20px 0. "
      "  • Presenter or date info — font-size:13px; font-weight:300; opacity:0.55. "
      "  • Goal/objective block (margin-top:auto): small 'KEY OBJECTIVE' eyebrow + 2-3 line outcome statement "
      "    (font-size:14px; font-weight:400; opacity:0.75; line-height:1.6). "
      "Right panel (padding:52px 56px; display:flex; flex-direction:column; gap:16px): "
      "  Agenda item list (display:flex; flex-direction:column; gap:12px; flex:1): "
      "  Each item row: display:flex; align-items:center; gap:20px; padding:16px 20px; "
      "  background:rgba(255,255,255,0.05); border-radius:12px; border:1px solid rgba(255,255,255,0.08). "
      "    • Number/index — font-size:11px; font-weight:700; letter-spacing:2px; color:accent; min-width:24px. "
      "    • Section heading — font-size:16px; font-weight:700; flex:1. "
      "    • Outcome tag (pill) — font-size:11px; background:rgba(accent,0.12); color:accent; "
      "      border-radius:20px; padding:3px 12px; white-space:nowrap. "
      "  Footer row (margin-top:auto; display:flex; align-items:center; justify-content:space-between; "
      "  border-top:1px solid rgba(255,255,255,0.08); padding-top:16px): "
      "    • Total items label — 12px opacity:0.45. "
      "    • Accent bar progress strip (display:flex; gap:4px): one small rect per item, accent for first, muted rest."
    )
  }
}