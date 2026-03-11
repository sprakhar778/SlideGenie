CONCEPT_EXPLAIN_SLIDE_LAYOUT = {
  "1": {
    "name": "Split-Screen / Timeline Explanation",
    "purpose": "Explaining historical development, evolution, or phased growth",
    "structure": (
      "Layout: display:flex; flex-direction:column; padding:44px 64px; gap:14px. "
      "Background: deep dark gradient. "
      "Header bar (display:flex; align-items:baseline; gap:16px): "
      "  • Eyebrow — 11px uppercase, letter-spacing:3px, accent, opacity:0.65. "
      "  • H1 — font-size:36px; font-weight:800; letter-spacing:-1px. "
      "  • Thin expanding accent rule (flex:1; height:2px; background:linear-gradient(90deg, accent, transparent)). "
      "Main body (display:grid; grid-template-columns:1fr 1fr; gap:36px; flex:1; align-items:start): "
      "Left column (timeline): display:flex; flex-direction:column; gap:0. "
      "  For each chronological step: display:flex; gap:16px; align-items:flex-start; margin-bottom:18px. "
      "  • Left: timeline marker group (circle 32px border-radius:50% accent bg + connecting line below flex:1 width:2px bg:rgba(255,255,255,0.12)). "
      "  • Right: content block: "
      "    - Year/phase badge — 11px uppercase, accent color, background:rgba(accent,0.12), border-radius:20px, padding:2px 10px. "
      "    - Step title — font-size:15px; font-weight:700; margin-top:6px. "
      "    - Description — font-size:12px; opacity:0.65; line-height:1.5; margin-top:4px. "
      "Right column (visual explanation panel): "
      "background:rgba(255,255,255,0.05); border:1px solid rgba(255,255,255,0.1); "
      "border-radius:18px; padding:28px; box-shadow:0 16px 48px rgba(0,0,0,0.3); "
      "display:flex; flex-direction:column; gap:16px. "
      "  • Visual title — font-size:16px; font-weight:700. "
      "  • Main icon or diagram placeholder — flex:1; display:flex; align-items:center; justify-content:center; "
      "    min-height:180px; font-size:72px; color:accent; opacity:0.8. "
      "  • Caption — font-size:12px; opacity:0.6; text-align:center; line-height:1.5."
    )
  },
  "2": {
    "name": "Split-Screen / Problem–Solution Focus",
    "purpose": "Concepts explained through pain points and resolution",
    "structure": (
      "Layout: display:flex; flex-direction:column; padding:40px 60px; gap:12px. "
      "Background: deep dark gradient. "
      "Header bar: eyebrow + H1 (font-size:34px; font-weight:800) + thin accent rule. "
      "Main body (display:grid; grid-template-columns:1fr 1fr; gap:24px; flex:1): "
      "Left column (Problem + Solution breakdown): display:flex; flex-direction:column; gap:14px. "
      "  Problem block: background:rgba(239,68,68,0.07); border:1px solid rgba(239,68,68,0.18); "
      "  border-radius:14px; padding:18px 22px. "
      "  • 'PROBLEM' eyebrow — 10px uppercase, red-tinted, opacity:0.75. "
      "  • Problem statement — font-size:16px; font-weight:700; color:#f87171; margin-top:6px; line-height:1.4. "
      "  Solution breakdown: background:rgba(16,185,129,0.06); border:1px solid rgba(16,185,129,0.18); "
      "  border-radius:14px; padding:18px 22px. "
      "  • 'SOLUTION' eyebrow — 10px uppercase, green, opacity:0.75. "
      "  • Bullet items (display:flex; flex-direction:column; gap:8px; margin-top:8px): "
      "    each: display:flex; gap:10px; font-size:13px; line-height:1.5. "
      "    ✓ icon in green circle (18px). "
      "Right column (Core concept diagram): "
      "background:rgba(255,255,255,0.04); border:1px solid rgba(255,255,255,0.1); "
      "border-radius:18px; padding:24px; display:flex; flex-direction:column; align-items:center; justify-content:center; gap:16px. "
      "  • Central concept circle — width:100px; height:100px; border-radius:50%; background:linear-gradient(135deg, accent-light, accent); "
      "    display:flex; align-items:center; justify-content:center; font-size:13px; font-weight:800; text-align:center; padding:10px. "
      "  • 3–4 surrounding label items radiating outward. "
      "Bottom takeaway strip: background:rgba(accent,0.08); border:1px solid rgba(accent,0.2); "
      "border-radius:10px; padding:12px 20px; font-size:13px; font-weight:600; margin-top:4px."
    )
  },
  "3": {
    "name": "Concept Breakdown / Card Grid",
    "purpose": "Explaining 3–4 subcomponents of a larger concept",
    "structure": (
      "Layout: display:flex; flex-direction:column; padding:44px 64px; gap:16px. "
      "Background: deep dark gradient. "
      "Header: eyebrow + H1 (font-size:38px; font-weight:800; letter-spacing:-1px) + thin accent rule. "
      "Intro text block: font-size:16px; font-weight:300; opacity:0.72; max-width:680px; line-height:1.6. "
      "Card grid (display:grid; grid-template-columns: repeat(2,1fr) or repeat(3,1fr) based on count; gap:16px; flex:1): "
      "Each concept card: background:rgba(255,255,255,0.06); border:1px solid rgba(255,255,255,0.1); "
      "border-radius:16px; padding:22px 24px; display:flex; flex-direction:column; gap:12px. "
      "  • Icon container — width:44px; height:44px; border-radius:12px; background:rgba(accent,0.15); "
      "    display:flex; align-items:center; justify-content:center; font-size:20px; color:accent. "
      "  • Card title — font-size:15px; font-weight:700; line-height:1.3. "
      "  • Short explanation — font-size:13px; font-weight:300; opacity:0.7; line-height:1.5. "
      "  • Bottom accent strip — position:absolute; bottom:0; left:0; right:0; height:3px; "
      "    background: accent; border-radius:0 0 16px 16px (use position:relative on card). "
      "Optional footer summary sentence: font-size:13px; opacity:0.55; text-align:center; margin-top:4px."
    )
  },
  "4": {
    "name": "Visual-First / Diagram-Centered",
    "purpose": "Concept best understood through structure or relationships",
    "structure": (
      "Layout: display:flex; flex-direction:column; padding:40px 64px; gap:12px. "
      "Background: deep dark gradient with large central radial glow (position:absolute, pointer-events:none) for depth. "
      "Header (text-align:center): eyebrow + H1 (font-size:36px; font-weight:800) + thin accent rule centered. "
      "Center diagram container (flex:1; position:relative; display:flex; align-items:center; justify-content:center): "
      "  Core circle — width:130px; height:130px; border-radius:50%; "
      "  background:linear-gradient(135deg, accent-light, accent); "
      "  box-shadow:0 0 56px rgba(accent,0.45); "
      "  display:flex; align-items:center; justify-content:center; "
      "  font-size:14px; font-weight:800; color:white; text-align:center; padding:14px. "
      "  Surrounding label nodes (positioned absolutely around the center, 6–8 nodes): "
      "  Each node: background:rgba(255,255,255,0.07); border:1px solid rgba(255,255,255,0.12); "
      "  border-radius:10px; padding:10px 14px; max-width:140px; text-align:center; "
      "  font-size:12px; font-weight:600; line-height:1.3. "
      "  Connector lines from center to nodes (thin, rgba(255,255,255,0.15), can be simulated with borders). "
      "Bottom caption (text-align:center): font-size:14px; font-weight:300; opacity:0.65; max-width:600px; margin:0 auto."
    )
  },
  "5": {
    "name": "Analogy-Driven Explanation",
    "purpose": "Teaching abstract ideas using relatable real-world parallels",
    "structure": (
      "Layout: display:flex; flex-direction:column; padding:44px 64px; gap:14px. "
      "Background: deep dark gradient. "
      "Header: eyebrow + H1 (font-size:36px; font-weight:800; letter-spacing:-1px) + accent rule. "
      "Main body (display:grid; grid-template-columns:1fr 1fr; gap:32px; flex:1; align-items:start): "
      "Left column (Analogy narrative): display:flex; flex-direction:column; gap:14px. "
      "  • Analogy label pill — 'REAL-WORLD ANALOGY', 10px uppercase, accent bg faint, border-radius:20px, padding:3px 12px. "
      "  • Analogy title — font-size:18px; font-weight:700; margin-top:6px. "
      "  • Narrative paragraph — font-size:14px; font-weight:300; opacity:0.78; line-height:1.7. "
      "  • Analogy visual card — background:rgba(255,255,255,0.05); border-radius:14px; padding:20px; "
      "    display:flex; align-items:center; gap:16px. "
      "    Large analogy icon (48px, accent) + short analogy example text (13px; opacity:0.8). "
      "Right column (Concept mapping): display:flex; flex-direction:column; gap:14px. "
      "  • Concept label pill — 'THE CONCEPT', 10px uppercase, accent color. "
      "  • Concept title — font-size:18px; font-weight:700; color:accent; margin-top:6px. "
      "  • Mapping items (display:flex; flex-direction:column; gap:10px): "
      "    Each: display:flex; align-items:center; gap:14px; font-size:13px; line-height:1.5. "
      "    Analogy term (opacity:0.65) → '=' separator → concept term (font-weight:700; color:accent). "
      "Bottom concept definition strip: background:rgba(accent,0.08); border:1px solid rgba(accent,0.2); "
      "border-radius:10px; padding:14px 20px; font-size:14px; font-weight:500; margin-top:4px; "
      "  'KEY DEFINITION:' eyebrow (10px accent) + definition text below."
    )
  },
  "6": {
    "name": "Step-by-Step Flow",
    "purpose": "Procedural or sequential concept explanation",
    "structure": (
      "Layout: display:flex; flex-direction:column; padding:48px 72px; gap:20px. "
      "Background: deep dark gradient. "
      "Header: eyebrow + H1 (font-size:38px; font-weight:800; letter-spacing:-1px) + accent rule. "
      "Horizontal step flow (display:flex; align-items:flex-start; gap:0; flex:1; margin-top:8px): "
      "For each step (flex:1; display:flex; flex-direction:column; align-items:center; gap:0): "
      "  Top connector row (display:flex; align-items:center; width:100%): "
      "    • Left connecting line (flex:1; height:2px; bg:rgba(255,255,255,0.15)) — hide for first step. "
      "    • Step node circle: width:48px; height:48px; border-radius:50%; "
      "      background: accent (active/first) or rgba(255,255,255,0.1); "
      "      border:2px solid accent or rgba(255,255,255,0.2); "
      "      display:flex; align-items:center; justify-content:center; "
      "      font-size:16px; font-weight:800 (step number or icon). "
      "    • Right connecting line — hide for last step. "
      "  Content card (margin-top:16px; width:90%; max-width:220px; text-align:center; "
      "  background:rgba(255,255,255,0.05); border:1px solid rgba(255,255,255,0.1); border-radius:14px; padding:16px 18px): "
      "    • Step label — 11px uppercase, letter-spacing:2px, accent, opacity:0.7. "
      "    • Step title — font-size:14px; font-weight:700; margin-top:6px; line-height:1.35. "
      "    • Short description — font-size:12px; opacity:0.6; margin-top:6px; line-height:1.5. "
      "Final step card: background:rgba(accent,0.12); border:1px solid rgba(accent,0.3); "
      "accent-tinted title highlighting the outcome. "
      "Optional step counter footer row: display:flex; justify-content:space-between; font-size:11px; opacity:0.4."
    )
  },
  "7": {
    "name": "Before–After Comparison",
    "purpose": "Showing transformation or improvement",
    "structure": (
      "Layout: display:flex; flex-direction:column; padding:44px 64px; gap:14px. "
      "Background: split gradient — left half slightly darker/cooler, right half warmer/accent-tinted, or single deep gradient. "
      "Header: eyebrow + H1 (font-size:36px; font-weight:800) + accent rule. "
      "Main body (display:grid; grid-template-columns:1fr 52px 1fr; gap:0; flex:1; align-items:stretch): "
      "Left panel (Before): background:rgba(100,100,120,0.08); border:1px solid rgba(255,255,255,0.08); "
      "border-radius:16px 0 0 16px; padding:22px 26px. "
      "  • 'BEFORE' label — 10px uppercase, muted, opacity:0.55. "
      "  • State title — font-size:18px; font-weight:700; opacity:0.8; margin-top:8px. "
      "  • State items (display:flex; flex-direction:column; gap:9px; margin-top:12px): "
      "    font-size:13px; opacity:0.7; line-height:1.5; "
      "    optional red ✗ bullets or strikethrough text. "
      "Center indicator: display:flex; flex-direction:column; align-items:center; justify-content:center; gap:6px. "
      "  '→' in accent, font-size:28px, font-weight:800. "
      "  Small 'THEN / NOW' label — 10px; opacity:0.4. "
      "Right panel (After): background:rgba(accent,0.07); border:1px solid rgba(accent,0.2); "
      "border-radius:0 16px 16px 0; padding:22px 26px. "
      "  • 'AFTER' label — 10px uppercase, accent, opacity:0.8. "
      "  • State title — font-size:18px; font-weight:700; color:accent; margin-top:8px. "
      "  • Improvement items with green ✓ bullets; key metrics with large accent text. "
      "Bottom explanation strip: border-top:1px solid rgba(255,255,255,0.1); padding-top:12px; "
      "font-size:13px; opacity:0.65; display:flex; gap:16px; align-items:center. "
      "'WHAT CHANGED:' label (accent, 10px uppercase) + explanation text."
    )
  },
  "8": {
    "name": "Question-Led Concept Reveal",
    "purpose": "Socratic or inquiry-based explanation",
    "structure": (
      "Layout: display:flex; flex-direction:column; padding:48px 80px; gap:18px. "
      "Background: deep dark gradient. "
      "Top guiding question block (text-align:center or left): "
      "  • Small eyebrow tag 'KEY QUESTION' — 10px uppercase, accent, pill shape. "
      "  • Question text — font-size:28px; font-weight:800; letter-spacing:-0.5px; line-height:1.3; "
      "    max-width:720px; margin-top:10px; "
      "    optionally styled with opening quotation mark (font-size:64px; color:accent; opacity:0.3; line-height:0.6; display:block). "
      "Thin accent divider — height:2px; width:80px; background: accent; margin:14px 0 (or auto if centered). "
      "Progressive answer blocks (display:flex; flex-direction:column; gap:12px; flex:1): "
      "Each answer block: display:flex; align-items:flex-start; gap:16px; padding:14px 20px; "
      "background:rgba(255,255,255,0.05); border-radius:12px; border-left:3px solid accent. "
      "  • Step number circle — width:28px; height:28px; border-radius:50%; background:accent; "
      "    display:flex; align-items:center; justify-content:center; font-size:12px; font-weight:700; color:white; flex-shrink:0. "
      "  • Answer text — font-size:14px; line-height:1.6; opacity:0.85. "
      "Bottom final concept definition box: background:rgba(accent,0.08); border:1px solid rgba(accent,0.25); "
      "border-radius:12px; padding:16px 22px. "
      "'CONCEPT:' eyebrow (10px accent uppercase) + definition (font-size:15px; font-weight:600; margin-top:6px)."
    )
  },
  "9": {
    "name": "Minimal Definition + Example",
    "purpose": "Simple, clear, concise concept explanation",
    "structure": (
      "Layout: display:flex; flex-direction:column; justify-content:center; align-items:center; text-align:center; padding:72px 120px. "
      "Background: clean dark gradient or restrained light gradient. "
      "Top: optional icon container — width:72px; height:72px; border-radius:18px; "
      "background:rgba(accent,0.15); display:flex; align-items:center; justify-content:center; "
      "font-size:32px; color:accent; margin-bottom:24px. "
      "Definition block (max-width:760px): "
      "  • 'DEFINITION' eyebrow — 11px uppercase, letter-spacing:4px, accent, opacity:0.6; margin-bottom:12px. "
      "  • Concept definition — font-size:28px; font-weight:700; letter-spacing:-0.5px; line-height:1.35. "
      "Thin accent rule — height:2px; width:80px; background: accent; margin:24px auto. "
      "Example block: background:rgba(255,255,255,0.05); border:1px solid rgba(255,255,255,0.1); "
      "border-radius:14px; padding:20px 32px; max-width:660px; margin:0 auto. "
      "  • 'EXAMPLE' label — 10px uppercase, letter-spacing:3px, accent, opacity:0.7; margin-bottom:10px. "
      "  • Example text — font-size:16px; font-weight:300; opacity:0.8; line-height:1.65."
    )
  }
}