COMPARISON_SLIDE_LAYOUT = {
  "1": {
    "name": "Split-Screen / Two-Column Classic",
    "purpose": "Direct side-by-side comparison of two entities",
    "structure": (
      "Layout: display:flex; flex-direction:column; padding:44px 64px; gap:16px. "
      "Background: deep dark gradient. "
      "Header row: H1 title — font-size:36px; font-weight:800; letter-spacing:-1px. "
      "Accent rule — height:2px; width:60px; background: accent; margin:10px 0. "
      "Main comparison body (display:grid; grid-template-columns:1fr 4px 1fr; gap:0; flex:1; align-items:start): "
      "Left column (Entity A): background:rgba(255,255,255,0.04); border-radius:16px 0 0 16px; padding:24px 28px. "
      "  • Entity A label — 11px uppercase, letter-spacing:3px, accent-A color, opacity:0.8. "
      "  • Entity title — font-size:20px; font-weight:700; margin-top:8px. "
      "  • Bullet list (display:flex; flex-direction:column; gap:10px; margin-top:14px): "
      "    Each item — display:flex; gap:10px; font-size:14px; line-height:1.5. "
      "    Bullet dot: width:8px; height:8px; border-radius:50%; background:accent-A; margin-top:6px; flex-shrink:0. "
      "Center divider: width:4px; background:linear-gradient(180deg, transparent, accent, transparent); border-radius:2px; align-self:stretch. "
      "Right column (Entity B): background:rgba(255,255,255,0.04); border-radius:0 16px 16px 0; padding:24px 28px. "
      "  • Mirrors left column structure with accent-B color variant. "
      "  • Each mirrored bullet aligns visually with the corresponding left bullet."
    )
  },
  "2": {
    "name": "Split-Screen / Feature-by-Feature",
    "purpose": "Structured comparison across shared features",
    "structure": (
      "Layout: display:flex; flex-direction:column; padding:44px 64px; gap:12px. "
      "Background: deep premium dark gradient. "
      "Header row (display:flex; align-items:center; justify-content:space-between): "
      "  • H1 title — font-size:34px; font-weight:800; letter-spacing:-1px. "
      "  • Two entity badge pills (display:flex; gap:12px) — each: accent/contrast bg, 12px font-weight:700, border-radius:20px, padding:4px 16px. "
      "Column header row (display:grid; grid-template-columns:1fr 1fr 1fr; padding:10px 16px; "
      "background:rgba(255,255,255,0.06); border-radius:10px; margin-bottom:4px): "
      "  • Feature label — 11px uppercase, letter-spacing:2px, opacity:0.5. "
      "  • Entity A header — 12px font-weight:700, accent-A color. "
      "  • Entity B header — 12px font-weight:700, accent-B color. "
      "Feature rows (display:flex; flex-direction:column; gap:6px; flex:1): "
      "Each row: display:grid; grid-template-columns:1fr 1fr 1fr; align-items:center; "
      "padding:12px 16px; border-radius:10px; border-bottom:1px solid rgba(255,255,255,0.06). "
      "  • Feature label — font-size:13px; font-weight:600; opacity:0.8. "
      "  • Entity A value — font-size:13px; color:accent-A. "
      "  • Entity B value — font-size:13px; color:accent-B. "
      "Difference highlight badge — small pill beside differing values: background:rgba(accent,0.15); border-radius:20px; padding:2px 10px; font-size:11px."
    )
  },
  "3": {
    "name": "Split-Screen / Timeline Contrast",
    "purpose": "Historical or phase-based comparison",
    "structure": (
      "Layout: display:flex; flex-direction:column; padding:44px 64px; gap:14px. "
      "Background: deep dark gradient. "
      "Header: H1 — font-size:36px; font-weight:800; letter-spacing:-1px. Accent rule below. "
      "Main body (display:grid; grid-template-columns:1fr 2px 1fr; gap:0; flex:1; align-items:start): "
      "Left column (Entity A timeline): display:flex; flex-direction:column; gap:0; padding:16px 24px. "
      "  • Column label — 11px uppercase, letter-spacing:3px, accent-A, opacity:0.7; margin-bottom:14px. "
      "  • For each milestone: display:flex; gap:14px; align-items:flex-start; margin-bottom:14px. "
      "    - Year/phase badge — font-size:11px; font-weight:700; color:accent-A; "
      "      background:rgba(accent-A,0.12); border-radius:20px; padding:2px 10px; white-space:nowrap. "
      "    - Milestone text — font-size:13px; line-height:1.5; opacity:0.85. "
      "    - Icon marker dot — width:10px; height:10px; border-radius:50%; background:accent-A; margin-top:5px; flex-shrink:0. "
      "Center divider: width:2px; background:linear-gradient(180deg, transparent, accent, transparent); align-self:stretch. "
      "Right column (Entity B timeline): mirrors left column with accent-B color scheme."
    )
  },
  "4": {
    "name": "Split-Screen / Problem–Solution Contrast",
    "purpose": "One entity presents problems, the other presents solutions",
    "structure": (
      "Layout: display:flex; flex-direction:column; padding:44px 64px; gap:16px. "
      "Background: deep dual-tone gradient. "
      "Header: H1 — font-size:36px; font-weight:800. Thin accent rule. "
      "Main body (display:grid; grid-template-columns:1fr auto 1fr; gap:20px; flex:1; align-items:stretch): "
      "Left column (Problems panel): background:rgba(239,68,68,0.07); border:1px solid rgba(239,68,68,0.2); "
      "border-radius:16px; padding:24px 28px. "
      "  • Eyebrow 'THE PROBLEM' — 10px uppercase, red-tinted, opacity:0.75. "
      "  • Panel title — font-size:18px; font-weight:700; color:#ef4444 or red-accent; margin-top:8px. "
      "  • Bullet items (display:flex; flex-direction:column; gap:10px; margin-top:14px): "
      "    each: display:flex; gap:10px; align-items:flex-start; font-size:14px; opacity:0.85; line-height:1.5. "
      "    Bullet icon: ✗ or × symbol, red accent color, font-weight:700. "
      "  • Callout highlight strip (margin-top:auto): background:rgba(239,68,68,0.1); border-radius:8px; padding:10px 14px; font-size:12px; opacity:0.8. "
      "Center separator: display:flex; align-items:center; justify-content:center. "
      "  Arrow icon '→' — font-size:28px; color:accent; opacity:0.8. "
      "Right column (Solutions panel): background:rgba(16,185,129,0.07); border:1px solid rgba(16,185,129,0.2); "
      "border-radius:16px; padding:24px 28px; mirrors left with green/accent-B tones. "
      "  • Eyebrow 'THE SOLUTION', green bullet ✓ icons, highlight strip."
    )
  },
  "5": {
    "name": "Central Axis / Pros vs Cons",
    "purpose": "Evaluating strengths and weaknesses of one concept",
    "structure": (
      "Layout: display:flex; flex-direction:column; padding:44px 72px; gap:14px. "
      "Background: deep dark gradient. "
      "Header (text-align:center): "
      "  • Eyebrow — 11px uppercase, letter-spacing:4px, accent, opacity:0.65. "
      "  • H1 concept title — font-size:38px; font-weight:800; letter-spacing:-1px; margin-top:8px. "
      "  • Thin accent rule — height:2px; width:60px; background: accent; margin:14px auto. "
      "Main body (display:grid; grid-template-columns:1fr 3px 1fr; gap:0; flex:1; align-items:start): "
      "Left column (Pros/Advantages): padding:16px 28px. "
      "  • Column header — display:flex; align-items:center; gap:10px; margin-bottom:16px. "
      "    Green check circle (24px, border-radius:50%, background:rgba(16,185,129,0.15)) + label 'ADVANTAGES' 11px uppercase green. "
      "  • Bullet items (display:flex; flex-direction:column; gap:12px): "
      "    Each: display:flex; gap:12px; align-items:flex-start; font-size:14px; line-height:1.55. "
      "    Icon: ✓ in green circle (20px). "
      "Center axis: width:3px; background:linear-gradient(180deg, transparent, rgba(255,255,255,0.2), transparent); "
      "border-radius:2px; align-self:stretch. "
      "Right column (Cons/Disadvantages): mirrors left with red/warning tones. "
      "  • Column header with ✗ icons, 'DISADVANTAGES' label. "
      "  • Each con bullet with red ✗ circle icon."
    )
  },
  "6": {
    "name": "Card Grid / Comparison Matrix",
    "purpose": "Multi-criteria evaluation across multiple dimensions",
    "structure": (
      "Layout: display:flex; flex-direction:column; padding:40px 60px; gap:14px. "
      "Background: deep dark gradient. "
      "Header (display:flex; align-items:center; justify-content:space-between): "
      "  • H1 — font-size:34px; font-weight:800; letter-spacing:-1px. "
      "  • Entity badge pills — two accent-colored pills naming the entities being compared. "
      "Criteria header row (display:grid per column count; gap:12px; padding:8px 12px; "
      "background:rgba(255,255,255,0.05); border-radius:10px): "
      "  • Feature/criteria labels — 11px uppercase, letter-spacing:2px, opacity:0.55. "
      "Card grid body (display:grid; grid-template-columns:1fr 1fr; gap:12px; flex:1): "
      "Each comparison card: background:rgba(255,255,255,0.06); border:1px solid rgba(255,255,255,0.1); "
      "border-radius:14px; padding:18px 22px; display:flex; flex-direction:column; gap:8px. "
      "  • Criterion label — 11px uppercase, letter-spacing:2px, opacity:0.55. "
      "  • Entity A value — font-size:16px; font-weight:700; color:accent-A. "
      "  • Entity B value — font-size:16px; font-weight:700; color:accent-B. "
      "  • Delta or comparison indicator — small pill: 'Better', '2×', '+40%' in matching accent. "
      "Best-in-class emphasis: top-left accent bar (width:3px; height:full; background:accent; border-radius:2px) "
      "on the winning entity card."
    )
  },
  "7": {
    "name": "Visual vs Visual",
    "purpose": "Primarily visual comparison with minimal text",
    "structure": (
      "Layout: display:flex; flex-direction:column; padding:44px 64px; gap:14px. "
      "Background: deep dark neutral gradient. "
      "Header (display:flex; align-items:center; gap:20px): "
      "  • H1 — font-size:36px; font-weight:800; letter-spacing:-1px. "
      "  • Thin expanding accent rule. "
      "Main visual body (display:grid; grid-template-columns:1fr 48px 1fr; gap:0; flex:1; align-items:center): "
      "Left visual panel (Entity A): border-radius:16px; overflow:hidden; "
      "background:rgba(255,255,255,0.06); border:1px solid rgba(255,255,255,0.12); "
      "display:flex; flex-direction:column; align-items:center; justify-content:center; min-height:320px; gap:16px; padding:20px. "
      "  • Entity A label pill — accent-A colored, 12px uppercase, border-radius:20px, padding:4px 14px. "
      "  • Large visual/icon representation — 120px × 120px, accent-A tinted. "
      "  • Minimal caption — font-size:13px; opacity:0.7; text-align:center; max-width:220px; line-height:1.5. "
      "  • Optional overlay tag (position:absolute top-right): small badge with key differentiator. "
      "Center VS divider: display:flex; flex-direction:column; align-items:center; justify-content:center. "
      "  • 'VS' label — font-size:18px; font-weight:900; opacity:0.4; letter-spacing:2px. "
      "  • Vertical line above and below — height:80px; width:1px; background:rgba(255,255,255,0.15). "
      "Right visual panel (Entity B): mirrors left with accent-B."
    )
  },
  "8": {
    "name": "Feature Focus / Core Diagram",
    "purpose": "Comparison anchored around a central conceptual model",
    "structure": (
      "Layout: display:flex; flex-direction:column; padding:44px 64px; gap:14px. "
      "Background: deep dark gradient with subtle radial glow on the right half. "
      "Header: H1 — font-size:36px; font-weight:800. Thin accent rule. "
      "Main body (display:grid; grid-template-columns:1fr 1.2fr; gap:36px; flex:1; align-items:center): "
      "Left column (Feature list): display:flex; flex-direction:column; gap:12px. "
      "  • Section eyebrow — 11px uppercase, letter-spacing:3px, accent, opacity:0.65. "
      "  • Feature items (display:flex; flex-direction:column; gap:10px; margin-top:8px): "
      "    Each: display:flex; align-items:center; gap:14px; padding:12px 16px; "
      "    background:rgba(255,255,255,0.05); border-radius:10px; border:1px solid rgba(255,255,255,0.08). "
      "    • Accent icon box (32px; border-radius:8px; background:rgba(accent,0.15)) + feature label (14px; font-weight:600) "
      "      + value/metric (margin-left:auto; font-size:13px; color:accent; font-weight:700). "
      "Right column (Core diagram): display:flex; align-items:center; justify-content:center; "
      "background:rgba(255,255,255,0.04); border:1px solid rgba(255,255,255,0.1); border-radius:20px; padding:28px. "
      "  • Central circle — width:110px; height:110px; border-radius:50%; background:linear-gradient(135deg, accent-light, accent); "
      "    display:flex; align-items:center; justify-content:center; font-size:14px; font-weight:800; text-align:center; padding:12px. "
      "  • Surrounding callout labels connected to center with thin lines. "
      "Footer summary strip: display:flex; gap:24px; margin-top:8px; font-size:12px; opacity:0.55."
    )
  },
  "9": {
    "name": "Before vs After",
    "purpose": "Transformation-based comparison",
    "structure": (
      "Layout: display:flex; flex-direction:column; padding:44px 64px; gap:14px. "
      "Background: dark gradient; optionally split left half slightly darker than right to reinforce before/after feel. "
      "Header: H1 — font-size:36px; font-weight:800; letter-spacing:-1px. Accent rule below. "
      "Main body (display:grid; grid-template-columns:1fr 60px 1fr; gap:0; flex:1; align-items:stretch): "
      "Left panel (Before): background:rgba(100,100,120,0.08); border:1px solid rgba(255,255,255,0.08); "
      "border-radius:16px 0 0 16px; padding:24px 28px. "
      "  • State label 'BEFORE' — 10px uppercase, letter-spacing:3px, muted gray, opacity:0.6. "
      "  • State title — font-size:18px; font-weight:700; opacity:0.85; margin-top:8px. "
      "  • Baseline metrics/items (display:flex; flex-direction:column; gap:10px; margin-top:14px): "
      "    font-size:13px; opacity:0.75; line-height:1.5; "
      "    optional red-tinted metric chips (e.g. '-40% speed'). "
      "Center arrow block: display:flex; flex-direction:column; align-items:center; justify-content:center; gap:8px. "
      "  • Arrow '→' or '⟶' — font-size:32px; color:accent; font-weight:700. "
      "  • Change delta label — font-size:11px; uppercase; letter-spacing:2px; color:accent; opacity:0.8. "
      "Right panel (After): background:rgba(accent,0.07); border:1px solid rgba(accent,0.2); "
      "border-radius:0 16px 16px 0; padding:24px 28px. "
      "  • State label 'AFTER' — 10px uppercase, accent color, opacity:0.8. "
      "  • State title — font-size:18px; font-weight:700; color:accent; margin-top:8px. "
      "  • Improvement items with green/accent-led metric chips. "
      "Footer outcome summary bar: background:rgba(accent,0.08); border-radius:10px; padding:12px 20px; "
      "display:flex; align-items:center; gap:16px; font-size:13px; margin-top:8px."
    )
  }
}