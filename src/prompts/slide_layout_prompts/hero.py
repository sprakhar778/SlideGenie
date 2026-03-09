HERO_SLIDE_LAYOUT = {
  "1": {
    "name": "Centered Hero",
    "purpose": "Bold, high-impact opening with strong emotional or visual presence",
    "structure": (
      "Layout: display:flex; flex-direction:column; justify-content:center; align-items:center; text-align:center; padding:80px 120px. "
      "Background: full-bleed rich gradient (e.g. linear-gradient(135deg, #0f0c29, #302b63, #24243e)) covering the full 1280x720 slide. "
      "Elements (top to bottom): "
      "(1) Optional eyebrow pill badge above the title — uppercase text, 11px, letter-spacing:3px, semi-transparent accent background, border-radius:20px, padding:4px 16px. "
      "(2) H1 main title — font-size:64px; font-weight:800; letter-spacing:-2px; line-height:1.1; max-width:800px. "
      "(3) Subtitle or tagline — font-size:22px; font-weight:300; opacity:0.75; margin-top:20px; max-width:600px. "
      "(4) Decorative horizontal accent rule — height:3px; width:80px; border-radius:2px; background: accent color; margin:28px auto. "
      "(5) Optional CTA button — padding:14px 36px; border-radius:30px; background: accent; font-size:15px; font-weight:600; letter-spacing:0.5px. "
      "Optionally add a large semi-transparent radial glow circle (position:absolute, pointer-events:none) behind the title for depth."
    )
  },
  "2": {
    "name": "Split-Screen Text-Visual",
    "purpose": "Balanced introduction combining explanation and imagery",
    "structure": (
      "Layout: display:grid; grid-template-columns:1.4fr 1fr; align-items:center; padding:60px 80px; gap:52px. "
      "Background: deep gradient (e.g. linear-gradient(135deg, #0d1b2a, #1b263b, #415a77)). "
      "Left column (text block): "
      "(1) Small eyebrow label — 11px uppercase, letter-spacing:3px, accent color, opacity:0.8. "
      "(2) H1 title — font-size:52px; font-weight:800; letter-spacing:-1.5px; line-height:1.15; margin-top:10px. "
      "(3) Value proposition paragraph — font-size:17px; font-weight:300; line-height:1.7; opacity:0.8; margin-top:16px; max-width:480px. "
      "(4) Left vertical accent bar beside the paragraph — width:4px; border-radius:2px; background: accent; align-self:stretch. "
      "Right column (visual block): "
      "Rounded accent card or illustration container — border-radius:20px; padding:36px; "
      "background:rgba(255,255,255,0.06); border:1px solid rgba(255,255,255,0.12); "
      "box-shadow:0 20px 60px rgba(0,0,0,0.3); display:flex; align-items:center; justify-content:center; min-height:320px. "
      "Inside: large icon (80px), short descriptive label, or abstract geometric decoration."
    )
  },
  "3": {
    "name": "Minimal Title-Only",
    "purpose": "Formal, clean, restrained opening",
    "structure": (
      "Layout: display:flex; flex-direction:column; justify-content:center; padding:80px 120px. "
      "Background: clean neutral gradient (e.g. linear-gradient(160deg, #f8faff, #eef2ff)) or very dark muted tone. "
      "Elements (left-aligned, vertically centered): "
      "(1) Small uppercase category or date label — font-size:11px; letter-spacing:4px; opacity:0.5; margin-bottom:20px. "
      "(2) H1 main title — font-size:68px; font-weight:800; letter-spacing:-2.5px; line-height:1.05; max-width:700px. "
      "(3) Thin horizontal divider — height:2px; width:60px; background: linear-gradient(90deg, accent, transparent); margin:28px 0. "
      "(4) Subtitle or presenter name — font-size:18px; font-weight:300; opacity:0.65; letter-spacing:0.5px. "
      "Overall: maximum whitespace, nothing below the subtitle. Slide should feel architectural and restrained. "
      "Optional: subtle corner decoration (large circle, low-opacity, position:absolute bottom-right)."
    )
  },
  "4": {
    "name": "Banner with Supporting Points",
    "purpose": "Mission-driven or theme-led introductions",
    "structure": (
      "Layout: display:flex; flex-direction:column; justify-content:center; padding:60px 90px; gap:40px. "
      "Background: bold full-bleed gradient. "
      "Top banner section (flex row, align-items:center, gap:32px): "
      "(1) H1 primary title — font-size:56px; font-weight:800; letter-spacing:-1.5px; flex:1. "
      "(2) Mission statement or subtitle — font-size:18px; font-weight:300; opacity:0.75; max-width:400px; line-height:1.6. "
      "Thin full-width horizontal rule — height:1px; background:rgba(255,255,255,0.15); margin:8px 0. "
      "Bottom supporting row (display:flex; gap:32px; align-items:stretch): "
      "2–3 keyword cards — each: background:rgba(255,255,255,0.07); border:1px solid rgba(255,255,255,0.12); "
      "border-radius:14px; padding:18px 24px; flex:1; display:flex; align-items:center; gap:14px. "
      "Each card: accent-colored icon placeholder (32px circle) + bold keyword label (16px) + optional micro-caption (12px, opacity:0.6)."
    )
  },
  "5": {
    "name": "Problem-Solution Hero",
    "purpose": "Framing a challenge and positioning a solution",
    "structure": (
      "Layout: display:flex; flex-direction:column; padding:60px 80px; gap:24px. "
      "Background: deep dual-tone dark gradient; optionally split the lower half with a subtle secondary tint. "
      "Top title bar: H1 at font-size:42px; font-weight:800; letter-spacing:-1px; text-align:center; margin-bottom:8px. "
      "Optional thin centered accent rule below the title (height:2px; width:80px; background: accent). "
      "Main body row (display:grid; grid-template-columns:1fr auto 1fr; align-items:center; gap:0; flex:1): "
      "Left panel (Problem column): background:rgba(255,80,80,0.07); border:1px solid rgba(255,100,100,0.15); "
      "border-radius:16px; padding:28px 32px. "
      "  • Eyebrow: 'THE CHALLENGE' — 10px uppercase, red-tinted accent, opacity:0.7. "
      "  • Problem headline — font-size:22px; font-weight:700; margin-top:10px; line-height:1.4. "
      "  • 1–2 supporting bullet lines — font-size:14px; opacity:0.75; margin-top:12px; line-height:1.6. "
      "Center visual separator: a vertical pill/arrow accent — width:3px; height:80px; background: accent; "
      "border-radius:4px; margin:0 auto; align-self:center. Or use a '→' arrow icon in accent color, font-size:32px. "
      "Right panel (Solution column): background:rgba(accent,0.08); border:1px solid rgba(accent,0.2); "
      "border-radius:16px; padding:28px 32px. "
      "  • Eyebrow: 'THE SOLUTION' — 10px uppercase, accent color, opacity:0.7. "
      "  • Solution headline — font-size:22px; font-weight:700; margin-top:10px; line-height:1.4. "
      "  • 1–2 supporting benefit lines — font-size:14px; opacity:0.75; margin-top:12px; line-height:1.6."
    )
  },
  "6": {
    "name": "Icon-Centric Hero",
    "purpose": "Symbolic, brand-focused, or conceptual introduction",
    "structure": (
      "Layout: display:flex; flex-direction:column; justify-content:center; align-items:center; text-align:center; padding:70px 120px. "
      "Background: deep gradient with a soft radial glow (radial-gradient ellipse) centered behind the icon — "
      "adds depth and draws the eye to the symbol. "
      "Elements (top-to-bottom, all centered): "
      "(1) Large icon or symbol container — width:100px; height:100px; border-radius:24px; "
      "background: linear-gradient(135deg, accent-light, accent); display:flex; align-items:center; justify-content:center; "
      "box-shadow:0 12px 40px rgba(accent,0.4); margin-bottom:28px. "
      "Inside: SVG icon or bold symbolic text character at 48px font-size in white. "
      "(2) H1 title — font-size:56px; font-weight:800; letter-spacing:-1.5px; line-height:1.1; max-width:720px. "
      "(3) Horizontal accent bar — height:3px; width:60px; background: accent; border-radius:2px; margin:22px auto. "
      "(4) Subtitle — font-size:19px; font-weight:300; opacity:0.72; max-width:560px; line-height:1.65. "
      "Optional: 2–3 small supporting badges (inline-flex, border-radius:20px, semi-transparent background) below the subtitle."
    )
  },
  "7": {
    "name": "Metric-Driven Hero",
    "purpose": "Data-first or impact-focused presentations",
    "structure": (
      "Layout: display:flex; flex-direction:column; justify-content:center; padding:60px 100px; gap:32px. "
      "Background: dark premium gradient. "
      "Top section: "
      "(1) Eyebrow category label — 11px uppercase, letter-spacing:3px, accent color. "
      "(2) H1 primary title — font-size:48px; font-weight:800; letter-spacing:-1.5px; line-height:1.15; max-width:680px; margin-top:10px. "
      "(3) Context subtitle — font-size:17px; font-weight:300; opacity:0.7; margin-top:10px; max-width:540px. "
      "Thin accent rule — height:2px; width:50px; background: accent; margin:20px 0. "
      "Metric highlight block (display:flex; gap:48px; align-items:flex-end): "
      "Primary metric card: background:rgba(255,255,255,0.06); border:1px solid rgba(accent,0.3); "
      "border-radius:16px; padding:24px 36px; display:inline-flex; flex-direction:column; gap:4px. "
      "  • Metric value — font-size:64px; font-weight:900; color: accent; letter-spacing:-3px; line-height:1. "
      "  • Metric label — font-size:13px; font-weight:400; opacity:0.65; letter-spacing:1px; text-transform:uppercase. "
      "1–2 supporting micro-stat items beside it: "
      "  • Each: font-size:28px; font-weight:700; color:white and small caption label below at 12px opacity:0.55."
    )
  },
  "8": {
    "name": "Timeline Introduction Hero",
    "purpose": "Time-based narrative or phased journey introduction",
    "structure": (
      "Layout: display:flex; flex-direction:column; padding:56px 80px; gap:28px. "
      "Background: dark gradient with optional subtle diagonal stripe or noise texture overlay (opacity:0.04). "
      "Top text block: "
      "(1) Eyebrow phase or date range badge — 11px uppercase, letter-spacing:2.5px, accent, pill shape. "
      "(2) H1 title — font-size:50px; font-weight:800; letter-spacing:-1.5px; line-height:1.15; max-width:680px; margin-top:8px. "
      "(3) Subtitle — font-size:17px; font-weight:300; opacity:0.72; max-width:520px; margin-top:10px. "
      "Thin accent divider — height:2px; width:60px; background: accent; margin:14px 0. "
      "Horizontal timeline bar (display:flex; align-items:center; gap:0; margin-top:8px; width:100%): "
      "Render 3–5 timeline nodes. For each node: "
      "  • Small circle — width:14px; height:14px; border-radius:50%; background: accent (for first/active) or rgba(255,255,255,0.2). "
      "  • Connecting line — flex:1; height:2px; background:rgba(255,255,255,0.15). "
      "Below each node: small phase label — font-size:11px; opacity:0.6; text-align:center; margin-top:8px; letter-spacing:0.5px. "
      "Optional icon container to the right of the title block — border-radius:18px; "
      "background:rgba(255,255,255,0.06); border:1px solid rgba(255,255,255,0.1); padding:24px; "
      "display:flex; align-items:center; justify-content:center; width:140px; height:140px."
    )
  },
  "9": {
    "name": "Feature-Focus Split Hero",
    "purpose": "Product launch or capability-focused opening",
    "structure": (
      "Layout: display:flex; flex-direction:column; padding:0. "
      "Background: dark rich gradient. "
      "Top full-width header bar: padding:28px 80px; border-bottom:1px solid rgba(255,255,255,0.1); "
      "display:flex; align-items:center; justify-content:space-between. "
      "  • Left: presentation brand name or category — 12px uppercase, letter-spacing:3px, opacity:0.6. "
      "  • Right: accent pill tag (e.g. 'LAUNCH 2025') — font-size:11px; background:rgba(accent,0.15); color:accent; "
      "    border-radius:20px; padding:4px 14px; border:1px solid rgba(accent,0.3). "
      "Main body (display:grid; grid-template-columns:1.3fr 1fr; gap:60px; align-items:center; padding:40px 80px; flex:1): "
      "Left column: "
      "(1) H1 product/feature title — font-size:52px; font-weight:800; letter-spacing:-1.5px; line-height:1.15. "
      "(2) Short description paragraph — font-size:16px; font-weight:300; opacity:0.75; line-height:1.7; margin-top:16px; max-width:420px. "
      "(3) Feature highlights list (display:flex; flex-direction:column; gap:14px; margin-top:24px): "
      "Each highlight row: display:flex; align-items:center; gap:14px. "
      "  • Accent-colored number circle (28px, border-radius:50%) or check icon. "
      "  • Feature label — font-size:15px; font-weight:600. "
      "  • Brief micro-description — font-size:13px; opacity:0.6; margin-left:4px. "
      "Right column: "
      "Illustration container — border-radius:20px; background:rgba(255,255,255,0.05); "
      "border:1px solid rgba(255,255,255,0.1); box-shadow:0 24px 64px rgba(0,0,0,0.3); "
      "display:flex; align-items:center; justify-content:center; min-height:340px. "
      "Inside: large symbolic icon (80–100px), abstract shape, or product screenshot placeholder."
    )
  }
}