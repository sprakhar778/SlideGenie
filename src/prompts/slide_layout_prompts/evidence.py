EVIDENCE_SLIDE_LAYOUT = {
  "1": {
    "name": "Chronological Evidence Split",
    "purpose": "Split-Screen / Timeline Focus",
    "structure": (
      "Layout: display:flex; flex-direction:column; padding:44px 64px; gap:14px. "
      "Background: deep dark gradient. "
      "Header (display:flex; align-items:baseline; gap:16px): "
      "  • Eyebrow — 11px uppercase, letter-spacing:3px, accent, opacity:0.65. "
      "  • H1 — font-size:36px; font-weight:800; letter-spacing:-1px. "
      "  • Thin expanding accent rule (flex:1; height:2px). "
      "Main body (display:grid; grid-template-columns:200px 1fr; gap:32px; flex:1; align-items:start): "
      "Left column — vertical timeline rail: display:flex; flex-direction:column; gap:0. "
      "  For each evidence entry: display:flex; gap:12px; align-items:flex-start; margin-bottom:16px. "
      "  • Timeline marker: circle (28px; border-radius:50%; accent bg for key entry, rgba(255,255,255,0.1) others) + "
      "    connecting line below (width:2px; flex:1; min-height:24px; bg:rgba(255,255,255,0.12); margin:0 auto). "
      "  • Year/phase badge — 11px; font-weight:700; color:accent; background:rgba(accent,0.12); "
      "    border-radius:20px; padding:2px 10px; white-space:nowrap. "
      "Right column — evidence detail cards: display:flex; flex-direction:column; gap:12px. "
      "  Each card: background:rgba(255,255,255,0.05); border:1px solid rgba(255,255,255,0.1); "
      "  border-radius:14px; padding:16px 20px; display:flex; gap:16px; align-items:flex-start. "
      "  • Left accent bar (width:3px; border-radius:2px; background:accent; align-self:stretch). "
      "  • Content: evidence title (font-size:14px; font-weight:700) + description (font-size:12px; opacity:0.65; line-height:1.5) "
      "    + optional supporting visual placeholder (right side, 60px × 60px, accent-tinted border-radius:8px)."
    )
  },
  "2": {
    "name": "Metric-Driven Comparison",
    "purpose": "Two-Column / Quantitative Comparison",
    "structure": (
      "Layout: display:flex; flex-direction:column; padding:44px 64px; gap:16px. "
      "Background: deep dark gradient. "
      "Header: eyebrow + H1 (font-size:36px; font-weight:800) + accent rule. "
      "Main body (display:grid; grid-template-columns:1fr 1.2fr; gap:32px; flex:1; align-items:start): "
      "Left column (key metric list): display:flex; flex-direction:column; gap:12px. "
      "  Each metric row: display:flex; align-items:center; gap:16px; padding:12px 16px; "
      "  background:rgba(255,255,255,0.05); border-radius:10px; border:1px solid rgba(255,255,255,0.08). "
      "  • Icon box (32px; border-radius:8px; bg:rgba(accent,0.15); display:flex; align:center; justify:center; color:accent). "
      "  • Metric label — font-size:13px; font-weight:600; flex:1. "
      "  • Benchmark value — font-size:18px; font-weight:800; color:accent; letter-spacing:-0.5px. "
      "Right column (chart area): background:rgba(255,255,255,0.04); border:1px solid rgba(255,255,255,0.1); "
      "border-radius:18px; padding:24px; display:flex; flex-direction:column; gap:12px. "
      "  • Chart title — font-size:14px; font-weight:700; opacity:0.8. "
      "  • Bar chart placeholder: display:flex; flex-direction:column; gap:10px; flex:1. "
      "    For each bar: label (12px; opacity:0.6) + bar track (height:10px; border-radius:5px; bg:rgba(255,255,255,0.1)) "
      "    with filled bar (bg:accent; border-radius:5px; width:% of max). "
      "Insight callout box (below main body): background:rgba(accent,0.08); border:1px solid rgba(accent,0.2); "
      "border-radius:10px; padding:12px 20px; display:flex; align-items:center; gap:12px; font-size:13px. "
      "  • Light bulb icon (accent) + insight text."
    )
  },
  "3": {
    "name": "Before-After Proof",
    "purpose": "Split-Screen / Before-After",
    "structure": (
      "Layout: display:flex; flex-direction:column; padding:44px 64px; gap:14px. "
      "Background: dark gradient; optionally tint left half slightly cooler/darker, right half with accent warmth. "
      "Header: H1 (font-size:36px; font-weight:800) + accent rule. "
      "Main body (display:grid; grid-template-columns:1fr 60px 1fr; gap:0; flex:1; align-items:stretch): "
      "Left panel (Before / Baseline): background:rgba(100,100,120,0.08); border:1px solid rgba(255,255,255,0.08); "
      "border-radius:16px 0 0 16px; padding:22px 26px. "
      "  • 'BEFORE' eyebrow — 10px uppercase, muted gray, opacity:0.55. "
      "  • Baseline state title — font-size:18px; font-weight:700; opacity:0.8; margin-top:8px. "
      "  • Baseline metrics (display:flex; flex-direction:column; gap:10px; margin-top:12px): "
      "    Each metric: display:flex; justify-content:space-between; align-items:center; "
      "    font-size:13px; border-bottom:1px solid rgba(255,255,255,0.06); padding-bottom:8px. "
      "    Metric label (opacity:0.65) + baseline value in muted/red tone. "
      "Center improvement indicator: display:flex; flex-direction:column; align-items:center; justify-content:center; gap:8px. "
      "  • Arrow icon '→' — font-size:26px; color:accent; font-weight:800. "
      "  • Delta label (e.g. '+40%') — font-size:14px; font-weight:900; color:accent. "
      "Right panel (After / Result): background:rgba(accent,0.07); border:1px solid rgba(accent,0.2); "
      "border-radius:0 16px 16px 0; padding:22px 26px. "
      "  • 'AFTER' eyebrow — 10px uppercase, accent, opacity:0.8. "
      "  • Result title — font-size:18px; font-weight:700; color:accent; margin-top:8px. "
      "  • Improved metrics mirroring left — result values in accent/green tone, improvement badges."
    )
  },
  "4": {
    "name": "Evidence Card Grid",
    "purpose": "Grid-Based / Evidence Tiles",
    "structure": (
      "Layout: display:flex; flex-direction:column; padding:40px 60px; gap:14px. "
      "Background: deep dark gradient. "
      "Header (display:flex; align-items:center; justify-content:space-between): "
      "  • H1 — font-size:34px; font-weight:800; letter-spacing:-1px. "
      "  • Evidence count badge — accent pill, 12px font-weight:600. "
      "Evidence card grid (display:grid; grid-template-columns: repeat(2,1fr) or repeat(3,1fr); gap:14px; flex:1): "
      "Each evidence card: background:rgba(255,255,255,0.06); border:1px solid rgba(255,255,255,0.1); "
      "border-radius:16px; padding:20px 22px; display:flex; flex-direction:column; gap:10px. "
      "  • Top row: icon/chart mini (width:36px; height:36px; border-radius:8px; bg:rgba(accent,0.15); color:accent) "
      "    + metric value (margin-left:auto; font-size:22px; font-weight:800; color:accent; letter-spacing:-1px). "
      "  • Metric label — font-size:11px; uppercase; letter-spacing:2px; opacity:0.6. "
      "  • Short explanation — font-size:12px; opacity:0.7; line-height:1.5; margin-top:4px. "
      "  • Optional micro-chart bar (height:4px; border-radius:4px; bg:rgba(accent,0.2); "
      "    inner fill:bg:accent; width:60–90%; margin-top:auto). "
      "Footer summary insight strip: background:rgba(accent,0.08); border:1px solid rgba(accent,0.2); "
      "border-radius:10px; padding:12px 20px; font-size:13px; font-weight:600; "
      "display:flex; align-items:center; gap:12px. Icon + insight text."
    )
  },
  "5": {
    "name": "Claim-to-Evidence Mapping",
    "purpose": "Split-Screen / Argument Mapping",
    "structure": (
      "Layout: display:flex; flex-direction:column; padding:44px 64px; gap:14px. "
      "Background: deep dark gradient. "
      "Header: H1 (font-size:36px; font-weight:800) + accent rule. "
      "Main body (display:grid; grid-template-columns:240px 1fr; gap:28px; flex:1; align-items:start): "
      "Left column (Claims/Hypotheses): display:flex; flex-direction:column; gap:10px. "
      "  Each claim badge: background:rgba(accent,0.1); border:1px solid rgba(accent,0.25); "
      "  border-radius:12px; padding:12px 16px; cursor-pointer look. "
      "  • 'CLAIM' eyebrow — 10px uppercase, accent, opacity:0.7. "
      "  • Claim text — font-size:14px; font-weight:700; margin-top:4px; line-height:1.4. "
      "  • Confidence pill (bottom-right of card): 'High / Medium / Low' — 10px; border-radius:20px; "
      "    bg green/yellow/red tinted; padding:2px 8px. "
      "Right column (Evidence blocks): display:flex; flex-direction:column; gap:12px. "
      "  Each evidence block (mapped to a claim with matching accent-tint left border): "
      "  background:rgba(255,255,255,0.05); border:1px solid rgba(255,255,255,0.1); border-left:3px solid accent; "
      "  border-radius:10px; padding:14px 18px; display:flex; flex-direction:column; gap:6px. "
      "  • Evidence type label — 10px uppercase, letter-spacing:2px, opacity:0.55. "
      "  • Evidence detail — font-size:13px; line-height:1.55; opacity:0.85. "
      "  • Strength indicator dot row: 3–5 dots, filled = strength level (accent filled, muted empty)."
    )
  },
  "6": {
    "name": "Data Story Flow",
    "purpose": "Vertical Flow / Narrative Data",
    "structure": (
      "Layout: display:flex; flex-direction:column; padding:44px 64px; gap:14px. "
      "Background: deep dark gradient. "
      "Header: eyebrow + H1 (font-size:36px; font-weight:800) + accent rule. "
      "Sequential data sections (display:flex; flex-direction:column; gap:0; flex:1): "
      "For each section (display:grid; grid-template-columns:1fr 2px 1fr; gap:24px; align-items:center; padding:14px 0): "
      "  Left: chart/data block (background:rgba(255,255,255,0.05); border-radius:12px; padding:16px 20px; "
      "    chart title 13px font-weight:700 + mini bar/line chart placeholder (height:60px; display:flex; align-items:flex-end; gap:6px) "
      "    with bars of varying heights accent-colored). "
      "  Center progress indicator: vertical line (width:2px; bg:rgba(255,255,255,0.12); align-self:stretch) "
      "    with a small circle node at the junction (width:12px; height:12px; border-radius:50%; bg:accent; margin:0 auto). "
      "  Right: explanation panel (font-size:13px; line-height:1.6; opacity:0.82) "
      "    + optional key stat chip (accent color, font-size:18px; font-weight:800; display:block; margin-top:8px). "
      "Section divider: height:1px; bg:rgba(255,255,255,0.07); margin:4px 0. "
      "Conclusion insight panel (margin-top:auto): background:rgba(accent,0.09); border:1px solid rgba(accent,0.25); "
      "border-radius:12px; padding:14px 20px; font-size:14px; font-weight:600. "
      "  'KEY INSIGHT' eyebrow + conclusion text."
    )
  },
  "7": {
    "name": "Visual-First Evidence",
    "purpose": "Split-Screen / Visual Emphasis",
    "structure": (
      "Layout: display:flex; flex-direction:column; padding:44px 64px; gap:14px. "
      "Background: dark clean gradient. "
      "Header (display:flex; align-items:center; justify-content:space-between): "
      "  • H1 — font-size:34px; font-weight:800; letter-spacing:-1px. "
      "  • Eyebrow category chip — accent pill, 11px uppercase. "
      "Main body (display:grid; grid-template-columns:1fr 1.5fr; gap:32px; flex:1; align-items:start): "
      "Left column (text evidence summary + highlights): display:flex; flex-direction:column; gap:14px. "
      "  • Section eyebrow — 11px uppercase, accent, opacity:0.65. "
      "  • Summary paragraph — font-size:14px; line-height:1.65; opacity:0.8. "
      "  • Key takeaway highlights (display:flex; flex-direction:column; gap:10px; margin-top:8px): "
      "    Each: display:flex; align-items:center; gap:12px; font-size:13px; font-weight:600; "
      "    accent dot (8px; border-radius:50%; bg:accent; flex-shrink:0) + takeaway text. "
      "Right column (primary chart/visualization container): "
      "background:rgba(255,255,255,0.04); border:1px solid rgba(255,255,255,0.1); "
      "border-radius:18px; padding:24px; display:flex; flex-direction:column; gap:12px. "
      "  • Chart title — 13px; font-weight:700; opacity:0.8. "
      "  • Large chart area placeholder (flex:1; min-height:220px; display:flex; align-items:flex-end; gap:8px; padding-top:16px): "
      "    Bars of varying heights with accent gradients; base line 1px rgba(255,255,255,0.15). "
      "  • Annotation overlays: small floating labels with accent bg, border-radius:6px, padding:3px 8px, font-size:10px."
    )
  },
  "8": {
    "name": "Source & Validation Layout",
    "purpose": "Two-Column / Credibility Focus",
    "structure": (
      "Layout: display:flex; flex-direction:column; padding:44px 64px; gap:14px. "
      "Background: deep dark gradient. "
      "Header: eyebrow + H1 (font-size:36px; font-weight:800) + accent rule. "
      "Main body (display:grid; grid-template-columns:1.2fr 1fr; gap:32px; flex:1; align-items:start): "
      "Left column (Findings + Key Statistics): display:flex; flex-direction:column; gap:12px. "
      "  Stat spotlight row (display:flex; gap:20px; margin-bottom:8px): "
      "    Each stat card: background:rgba(255,255,255,0.06); border:1px solid rgba(255,255,255,0.1); "
      "    border-radius:12px; padding:16px 20px; flex:1. "
      "    • Stat value — font-size:28px; font-weight:900; color:accent; letter-spacing:-1px. "
      "    • Stat label — font-size:11px; uppercase; letter-spacing:1px; opacity:0.6; margin-top:4px. "
      "  Finding items (display:flex; flex-direction:column; gap:10px): "
      "    Each: border-left:3px solid accent; padding-left:14px; font-size:13px; line-height:1.55; opacity:0.82. "
      "Right column (Sources + Methodology): display:flex; flex-direction:column; gap:12px. "
      "  • 'SOURCES' eyebrow — 11px uppercase, letter-spacing:3px, accent, opacity:0.65. "
      "  Source list items (display:flex; flex-direction:column; gap:8px): "
      "    Each: display:flex; align-items:flex-start; gap:10px; font-size:12px; opacity:0.7; line-height:1.45. "
      "    Citation number (accent color, font-weight:700, min-width:18px). "
      "  Methodology block (margin-top:12px): background:rgba(255,255,255,0.04); border-radius:10px; padding:14px 16px. "
      "    'METHODOLOGY' eyebrow + method description (font-size:12px; opacity:0.65; line-height:1.5)."
    )
  },
  "9": {
    "name": "Evidence Dashboard Snapshot",
    "purpose": "Dashboard / KPI Snapshot",
    "structure": (
      "Layout: display:flex; flex-direction:column; padding:36px 56px; gap:12px. "
      "Background: deep dark gradient. "
      "Header (display:flex; align-items:center; justify-content:space-between): "
      "  • H1 — font-size:32px; font-weight:800; letter-spacing:-1px. "
      "  • Timestamp/source label — 11px; opacity:0.45; letter-spacing:1px. "
      "KPI stat cards row (display:grid; grid-template-columns: repeat(3,1fr) or repeat(4,1fr); gap:12px): "
      "Each KPI card: background:rgba(255,255,255,0.06); border:1px solid rgba(255,255,255,0.1); "
      "border-radius:14px; padding:16px 20px; display:flex; flex-direction:column; gap:6px. "
      "  • KPI label — 10px uppercase, letter-spacing:2px, opacity:0.55. "
      "  • KPI value — font-size:30px; font-weight:900; color:accent; letter-spacing:-1px; line-height:1. "
      "  • Delta chip (e.g. '↑ 12%') — 11px; font-weight:700; "
      "    bg:rgba(16,185,129,0.12); color:#10b981 (green up) or red (down); border-radius:20px; padding:2px 8px. "
      "Primary chart block (display:grid; grid-template-columns:1.5fr 1fr; gap:12px; flex:1): "
      "  Main chart: background:rgba(255,255,255,0.04); border:1px solid rgba(255,255,255,0.1); "
      "  border-radius:14px; padding:18px; display:flex; flex-direction:column; gap:10px. "
      "  Chart title (13px; font-weight:700) + chart area (flex:1; display:flex; align-items:flex-end; gap:6px; min-height:120px). "
      "  Secondary panel: display:flex; flex-direction:column; gap:10px. "
      "  2 smaller info cards (background:rgba(255,255,255,0.05); border-radius:12px; padding:14px 16px). "
      "Insight/recommendation strip: background:rgba(accent,0.08); border-radius:10px; padding:10px 18px; "
      "font-size:13px; font-weight:600; display:flex; align-items:center; gap:10px. Icon + text."
    )
  }
}