SUMMARY_SLIDE_LAYOUT = {
  "1": {
    "name": "Split-Screen / Bullet-to-Visual",
    "purpose": "Clear takeaway list supported by visual reinforcement",
    "structure": (
      "Layout: display:flex; flex-direction:column; padding:44px 64px; gap:14px. "
      "Header: eyebrow + H1 (36px/800) + expanding accent rule. "
      "Body (grid 1.1fr 1fr; gap:32px; flex:1): "
      "Left — icon-led takeaway list: each row flex gap:14px padding:12px 16px bg:rgba(255,255,255,0.05) border-radius:12px. "
      "  Icon (36px; border-radius:10px; bg:rgba(accent,0.15); color:accent) + "
      "  title (14px; font-weight:700) + sub-note (12px; opacity:0.6). "
      "Right — illustration panel: bg:rgba(255,255,255,0.05); border-radius:18px; padding:28px; "
      "box-shadow:0 16px 48px rgba(0,0,0,0.3); min-height:260px; flex center. "
      "Large icon (72px; accent opacity:0.85) + caption (13px; opacity:0.6)."
    )
  },
  "2": {
    "name": "Card Grid / Executive Summary",
    "purpose": "Condensed executive-style insight overview",
    "structure": (
      "Layout: display:flex; flex-direction:column; padding:40px 60px; gap:16px. "
      "Header (center): eyebrow + H1 (38px/800) + centered accent rule. "
      "Card grid (repeat(2,1fr) or repeat(3,1fr); gap:14px; flex:1): "
      "Each card: bg rgba(255,255,255,0.06); border rgba(255,255,255,0.1); border-radius:16px; padding:20px. "
      "  Icon (40px; border-radius:10px; bg:rgba(accent,0.15); color:accent). "
      "  Headline (15px; font-weight:700) + one-line insight (12px; opacity:0.65). "
      "Optional footer highlight: bg:rgba(accent,0.08); border-radius:10px; padding:10px 18px; 12px font-weight:600."
    )
  },
  "3": {
    "name": "Timeline Compression / From Start to Finish",
    "purpose": "Condensed journey recap",
    "structure": (
      "Layout: display:flex; flex-direction:column; padding:44px 72px; gap:20px. "
      "Header: eyebrow + H1 (38px/800) + accent rule. "
      "Horizontal timeline (flex; align-items:flex-start; gap:0; flex:1): "
      "Each milestone (flex:1; flex-direction:column; align-items:center): "
      "  Rail: left line (flex:1; 2px; rgba(255,255,255,0.15)) + node circle (40px; border-radius:50%; "
      "  accent for final, rgba(255,255,255,0.1) others) + right line. "
      "  Card (margin-top:14px; bg:rgba(255,255,255,0.05); border-radius:12px; padding:12px 16px; center): "
      "    icon (20px; accent) + stage label (10px uppercase; accent) + title (13px; font-weight:700). "
      "Final node: bg:rgba(accent,0.12); border:rgba(accent,0.3); accent-tinted."
    )
  },
  "4": {
    "name": "Problem-Insight-Outcome",
    "purpose": "Structured reflection from challenge to result",
    "structure": (
      "Layout: display:flex; flex-direction:column; padding:44px 64px; gap:14px. "
      "Header: H1 (36px/800; center) + centered accent rule. "
      "Body (grid 1fr 48px 1fr 48px 1fr; flex:1; align-items:stretch): "
      "Col1 Problem: bg:rgba(239,68,68,0.07); border:rgba(239,68,68,0.18); border-radius:16px; padding:22px 24px. "
      "  'PROBLEM' eyebrow (red) + problem title (16px; color:#f87171) + 1–2 supporting points. "
      "Arrow separators: '→' font-size:24px; color:accent. "
      "Col2 Insights: bg:rgba(255,255,255,0.05) neutral; accent eyebrow + 2–3 insight bullets each accent dot. "
      "Col3 Outcomes: bg:rgba(16,185,129,0.07); border:rgba(16,185,129,0.2); green eyebrow + ✓ green outcomes."
    )
  },
  "5": {
    "name": "Central Core / Takeaway Orbit",
    "purpose": "Unified central idea with supporting takeaways",
    "structure": (
      "Layout: display:flex; flex-direction:column; padding:40px 64px; gap:14px. "
      "Background: dark gradient + centered radial glow. "
      "Header: eyebrow + H1 (36px/800) + accent rule. "
      "Orbit container (position:relative; flex:1; flex center; min-height:320px): "
      "Core circle (position:absolute; top:50%; left:50%; transform:translate(-50%,-50%)): "
      "  110px; border-radius:50%; gradient accent; box-shadow 0 0 52px; 14px/800; white; center text. "
      "5–7 nodes (position:absolute distributed around): bg:rgba(255,255,255,0.07); border-radius:12px; "
      "padding:10px 16px; max-width:170px; center; 12px/600. "
      "Thin connector lines (1px rgba(255,255,255,0.12))."
    )
  },
  "6": {
    "name": "Checklist / Action-Oriented Summary",
    "purpose": "Practical, implementation-focused recap",
    "structure": (
      "Layout: display:flex; flex-direction:column; padding:48px 80px; gap:16px. "
      "Header: 'WHAT YOU SHOULD REMEMBER' eyebrow (11px; accent) + H1 (38px/800) + accent rule. "
      "Checklist (flex-direction:column; gap:10px; flex:1): "
      "Each item: flex; align-items:flex-start; gap:16px; padding:14px 20px; "
      "bg:rgba(255,255,255,0.05); border-radius:12px; border rgba(255,255,255,0.08). "
      "  ✓ circle (32px; bg:rgba(16,185,129,0.15); color:#10b981) + "
      "  takeaway text (15px/700) + implication (12px; opacity:0.65). "
      "CTA footer: bg:rgba(accent,0.09); border-radius:12px; padding:12px 20px; "
      "space-between: CTA text (13px/600) + action pill (accent bg; 12px/700; border-radius:20px; padding:6px 20px)."
    )
  },
  "7": {
    "name": "Before-After / Knowledge Shift",
    "purpose": "Highlight transformation or learning shift",
    "structure": (
      "Layout: display:flex; flex-direction:column; padding:44px 64px; gap:14px. "
      "Header: H1 (36px/800; center) + centered accent rule. "
      "Body (grid 1fr 60px 1fr; flex:1; align-items:stretch): "
      "Left (BEFORE): bg:rgba(100,100,120,0.08); border rgba(255,255,255,0.08); border-radius:16px 0 0 16px; padding:22px 28px. "
      "  'BEFORE' (11px; muted; opacity:0.5) + title (18px/700; opacity:0.75) + "
      "  items (13px; opacity:0.7; optional red ✗). "
      "Center: column flex center; '→' (28px; accent/800) + 'NOW' (10px; opacity:0.5). "
      "Right (AFTER): bg:rgba(accent,0.07); border:rgba(accent,0.2); border-radius:0 16px 16px 0; "
      "  'AFTER' (accent; opacity:0.8) + title (18px/700; color:accent) + ✓ green bullets."
    )
  },
  "8": {
    "name": "Metrics + Insights / Data-Backed Summary",
    "purpose": "Quantitative or performance-driven recap",
    "structure": (
      "Layout: display:flex; flex-direction:column; padding:40px 64px; gap:14px. "
      "Header: eyebrow + H1 (36px/800) + accent rule. "
      "Primary takeaway block: bg:rgba(accent,0.08); border:rgba(accent,0.2); border-radius:14px; padding:18px 24px. "
      "  'KEY TAKEAWAY' eyebrow (10px; accent) + insight text (16px/600). "
      "Metric cards (repeat(3,1fr) gap:12px): each bg:rgba(255,255,255,0.06); border-radius:14px; padding:16px 20px. "
      "  Value (30px/900; accent) + label (10px uppercase) + insight caption (12px; opacity:0.65). "
      "Bottom synthesis strip: border-top rgba(255,255,255,0.08); flex; space-between. "
      "  Synthesis text (13px; opacity:0.7) + action chip (accent bg; border-radius:20px; padding:6px 16px)."
    )
  },
  "9": {
    "name": "Quote-Led / Principle Summary",
    "purpose": "Reinforce key principle or philosophy",
    "structure": (
      "Layout: display:flex; flex-direction:column; justify-content:center; padding:60px 100px; gap:20px. "
      "Background: dark gradient + optional subtle texture (opacity:0.04). "
      "Quote block (center; max-width:820px): "
      "  Opening quote mark (80px; accent; opacity:0.3; line-height:0.6). "
      "  Quote text (26px/700; italic; letter-spacing:-0.5px; line-height:1.4). "
      "  Attribution (14px/300; opacity:0.6; margin-top:16px). "
      "Accent rule (2px; 80px; accent; margin:20px auto). "
      "Bullet takeaways (flex-direction:column; gap:10px; max-width:680px; margin:0 auto): "
      "Each: flex; gap:12px; font-size:14px; opacity:0.80. Accent dot (8px; border-radius:50%). "
      "Footer: 12px; opacity:0.45; letter-spacing:1.5px; uppercase."
    )
  }
}