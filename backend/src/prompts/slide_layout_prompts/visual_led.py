VISUAL_SLIDE_LAYOUT = {
  "1": {
    "name": "Split-Screen / Image-Dominant",
    "purpose": "Strong visual impact with supporting narrative and CTA",
    "structure": (
      "Layout: display:grid; grid-template-columns:1fr 1fr; height:720px; overflow:hidden. "
      "Background: dark gradient on right panel. "
      "Left column (image panel): bg:rgba(255,255,255,0.05); border-right:1px solid rgba(255,255,255,0.1); "
      "display:flex; align-items:center; justify-content:center; overflow:hidden. "
      "  Hero image placeholder: width:100%; height:100%; object-fit:cover; "
      "  or abstract CSS art (large gradient blobs, geometric shapes) filling the full left panel. "
      "  Optional corner accent badge (position:absolute bottom-left): accent bg pill, caption text 12px. "
      "Right column (narrative panel): padding:60px 52px; display:flex; flex-direction:column; gap:18px; justify-content:center. "
      "  • Eyebrow — 11px uppercase, letter-spacing:3px, accent, opacity:0.65. "
      "  • Headline — font-size:40px; font-weight:800; letter-spacing:-1px; line-height:1.15; max-width:420px. "
      "  • Short narrative copy — font-size:16px; font-weight:300; opacity:0.75; line-height:1.7; max-width:380px; margin-top:4px. "
      "  • Accent rule — height:2px; width:50px; bg:accent; margin:8px 0. "
      "  • Primary CTA button — padding:12px 30px; border-radius:30px; bg:accent; font-size:14px; font-weight:700; margin-top:4px."
    )
  },
  "2": {
    "name": "Full-Bleed Hero Visual",
    "purpose": "Bold brand statement or high-impact opener",
    "structure": (
      "Layout: position:relative; width:1280px; height:720px; overflow:hidden. "
      "Background layer: full-bleed rich gradient (3+ stops, e.g. linear-gradient(135deg, #0f0c29, #302b63, #24243e)) or bold abstract CSS visual. "
      "Gradient overlay (position:absolute; inset:0): linear-gradient(to bottom, rgba(0,0,0,0.1), rgba(0,0,0,0.6)). "
      "Content layer (position:absolute; inset:0; display:flex; flex-direction:column; justify-content:center; align-items:center; text-align:center; padding:80px 120px): "
      "  • Eyebrow pill — 11px uppercase, letter-spacing:4px, accent bg faint, border-radius:20px, padding:4px 16px; margin-bottom:20px. "
      "  • Main headline — font-size:68px; font-weight:900; letter-spacing:-2.5px; line-height:1.05; max-width:800px; color:white. "
      "  • Subheading — font-size:20px; font-weight:300; opacity:0.8; max-width:560px; margin-top:18px; line-height:1.6; color:white. "
      "  • CTA group (display:flex; gap:16px; margin-top:28px; align-items:center): "
      "    Primary button (padding:14px 40px; border-radius:30px; bg:accent; font-size:15px; font-weight:700). "
      "    Secondary ghost button (border:1px solid rgba(255,255,255,0.4); same padding; opacity:0.8)."
    )
  },
  "3": {
    "name": "Split-Screen / Feature-Focus",
    "purpose": "Problem/solution storytelling with supporting visual explanation",
    "structure": (
      "Layout: display:flex; flex-direction:column; padding:44px 64px; gap:14px. "
      "Background: deep dark gradient. "
      "Header bar: eyebrow + H1 (font-size:36px; font-weight:800) + expanding accent rule. "
      "Main body (display:grid; grid-template-columns:1fr 1fr; gap:32px; flex:1; align-items:start): "
      "Left column (Problem/Solution statement + feature cards): display:flex; flex-direction:column; gap:12px. "
      "  Problem/solution intro — font-size:16px; font-weight:300; opacity:0.75; line-height:1.65. "
      "  Vertical feature card list (display:flex; flex-direction:column; gap:10px): "
      "  Each card: bg:rgba(255,255,255,0.05); border:1px solid rgba(255,255,255,0.1); border-radius:12px; padding:14px 18px. "
      "    display:flex; align-items:center; gap:14px. "
      "    Icon (32px; border-radius:8px; bg:rgba(accent,0.15); color:accent) + "
      "    text (title 14px/700 + note 12px opacity:0.6). "
      "Right column (central visual/diagram): "
      "bg:rgba(255,255,255,0.04); border:1px solid rgba(255,255,255,0.1); border-radius:20px; "
      "padding:28px; display:flex; align-items:center; justify-content:center; "
      "box-shadow:0 20px 60px rgba(0,0,0,0.3); min-height:320px. "
      "  Large diagram icon (90px; accent-tinted) or abstract shape."
    )
  },
  "4": {
    "name": "Image Grid with Narrative Rail",
    "purpose": "Multiple visual highlights with structured explanatory rail",
    "structure": (
      "Layout: display:flex; flex-direction:column; padding:44px 64px; gap:14px. "
      "Background: deep dark gradient. "
      "Header bar: eyebrow + H1 (font-size:36px; font-weight:800) + accent rule. "
      "Main body (display:grid; grid-template-columns:1fr 1.2fr; gap:32px; flex:1; align-items:start): "
      "Left column (vertical text rail): display:flex; flex-direction:column; gap:14px; justify-content:center. "
      "  • Narrative headline — font-size:22px; font-weight:800; letter-spacing:-0.5px; line-height:1.3. "
      "  • Bullet points (display:flex; flex-direction:column; gap:10px): "
      "    Each: display:flex; gap:12px; font-size:13px; line-height:1.5; opacity:0.82. "
      "    Accent dot (8px; border-radius:50%; bg:accent; flex-shrink:0; margin-top:5px). "
      "  • CTA element (margin-top:16px): pill button or underline link (accent color; 14px; font-weight:600). "
      "Right column (2×2 or masonry image grid): display:grid; grid-template-columns:1fr 1fr; gap:12px. "
      "Each image card: bg:rgba(255,255,255,0.06); border:1px solid rgba(255,255,255,0.1); "
      "border-radius:14px; overflow:hidden; min-height:140px; display:flex; align-items:center; justify-content:center. "
      "  Abstract CSS art or large icon (40px; accent-tinted) inside each. "
      "  Optional caption overlay (position:absolute; bottom:0; background:rgba(0,0,0,0.4); padding:6px 12px; font-size:11px; width:100%)."
    )
  },
  "5": {
    "name": "Visual Timeline / Image-Led",
    "purpose": "Chronological story supported by milestone imagery",
    "structure": (
      "Layout: display:flex; flex-direction:column; padding:44px 64px; gap:14px. "
      "Background: deep dark gradient. "
      "Header bar: eyebrow + H1 (font-size:36px; font-weight:800) + accent rule. "
      "Main body (display:grid; grid-template-columns:220px 1fr; gap:32px; flex:1; align-items:start): "
      "Left column (vertical timeline with icons + year badges): display:flex; flex-direction:column; gap:0. "
      "  For each milestone: display:flex; gap:12px; align-items:flex-start; margin-bottom:16px. "
      "  • Timeline marker: circle (28px; border-radius:50%; accent bg for active; rgba(255,255,255,0.1) others) "
      "    + connecting line below (width:2px; flex:1; min-height:22px; bg:rgba(255,255,255,0.12); margin:0 auto). "
      "  • Year/phase badge (11px; accent; border-radius:20px; bg:rgba(accent,0.12); padding:2px 10px) "
      "    + milestone label (13px; font-weight:600; margin-top:4px). "
      "Right column (contextual image panels): display:flex; flex-direction:column; gap:12px. "
      "  Each image panel: bg:rgba(255,255,255,0.05); border:1px solid rgba(255,255,255,0.1); "
      "  border-radius:14px; min-height:100px; display:flex; align-items:center; justify-content:center; gap:14px; padding:16px 20px. "
      "  Large icon (40px; accent) + image caption/description (13px; opacity:0.75; line-height:1.5)."
    )
  },
  "6": {
    "name": "Centered Core Visual",
    "purpose": "Concept-centric presentation anchored around one visual idea",
    "structure": (
      "Layout: display:flex; flex-direction:column; padding:40px 64px; gap:14px. "
      "Background: deep dark gradient + large centered radial glow (position:absolute; pointer-events:none). "
      "Header (text-align:center): eyebrow + H1 (font-size:36px; font-weight:800) + centered accent rule. "
      "Core diagram container (flex:1; position:relative; display:flex; align-items:center; justify-content:center; min-height:300px): "
      "  Center circle: width:130px; height:130px; border-radius:50%; bg:linear-gradient(135deg, accent-light, accent); "
      "  box-shadow:0 0 56px rgba(accent,0.45); display:flex; align-items:center; justify-content:center; "
      "  font-size:14px; font-weight:800; color:white; text-align:center; padding:14px. "
      "  Surrounding radial labels (6–8; position:absolute distributed): "
      "  bg:rgba(255,255,255,0.07); border:1px solid rgba(255,255,255,0.12); border-radius:10px; "
      "  padding:10px 14px; max-width:140px; text-align:center; font-size:12px; font-weight:600; line-height:1.3. "
      "  Connector lines (thin; rgba(255,255,255,0.1)). "
      "Bottom caption (text-align:center): font-size:14px; font-weight:300; opacity:0.65; max-width:600px; margin:0 auto."
    )
  },
  "7": {
    "name": "Stacked Visual Story",
    "purpose": "Sequential narrative driven primarily by imagery",
    "structure": (
      "Layout: display:flex; flex-direction:column; padding:0; height:720px; overflow:hidden. "
      "Background: dark gradient. "
      "Hero section (position:relative; height:320px; overflow:hidden; flex-shrink:0): "
      "  bg:rgba(255,255,255,0.04); border-bottom:1px solid rgba(255,255,255,0.1); "
      "  display:flex; align-items:center; justify-content:center. "
      "  Large hero icon or abstract graphic (100px; accent-tinted) in center. "
      "  Overlay headline (position:absolute; bottom:24px; left:48px): "
      "    font-size:36px; font-weight:800; letter-spacing:-1px; color:white. "
      "Secondary image strip (display:flex; gap:0; height:140px; flex-shrink:0): "
      "  3 equal-width image tiles: display:flex; align-items:center; justify-content:center; flex:1; "
      "  bg:rgba(255,255,255,0.04); border-right:1px solid rgba(255,255,255,0.08) (except last); "
      "  font-size:32px (icon). "
      "Text blocks and CTA row (flex:1; display:flex; flex-direction:column; justify-content:center; padding:20px 48px; gap:12px): "
      "  • Explanatory text — font-size:14px; opacity:0.75; line-height:1.6; max-width:700px. "
      "  • CTA bottom bar (margin-top:auto): display:flex; gap:16px; align-items:center. "
      "    Primary button (accent) + secondary ghost button."
    )
  },
  "8": {
    "name": "Visual with Metrics Emphasis",
    "purpose": "Value proposition reinforced by key statistics",
    "structure": (
      "Layout: display:flex; flex-direction:column; padding:44px 64px; gap:14px. "
      "Background: deep dark gradient. "
      "Header: eyebrow + H1 (font-size:36px; font-weight:800) + accent rule. "
      "Main body (display:grid; grid-template-columns:1fr 1fr; gap:32px; flex:1; align-items:center): "
      "Left column (large illustrative image panel): "
      "bg:rgba(255,255,255,0.05); border:1px solid rgba(255,255,255,0.1); border-radius:18px; "
      "padding:28px; display:flex; align-items:center; justify-content:center; min-height:280px; "
      "box-shadow:0 20px 56px rgba(0,0,0,0.3). "
      "  Large icon, illustration, or abstract visual (80–100px; accent-tinted). "
      "Right column (value proposition + metrics): display:flex; flex-direction:column; gap:14px. "
      "  • Value prop headline — font-size:22px; font-weight:800; letter-spacing:-0.5px; line-height:1.3. "
      "  • Value prop text — font-size:15px; font-weight:300; opacity:0.75; line-height:1.65. "
      "Bottom stats bar (display:grid; grid-template-columns:repeat(3,1fr); gap:12px; margin-top:8px): "
      "Each stat: bg:rgba(255,255,255,0.06); border:1px solid rgba(255,255,255,0.1); border-radius:12px; padding:14px 18px. "
      "  Stat value (28px/900; accent) + stat label (10px uppercase; opacity:0.55)."
    )
  },
  "9": {
    "name": "Immersive Showcase Panel",
    "purpose": "Premium product or concept display with minimal distraction",
    "structure": (
      "Layout: display:flex; flex-direction:column; justify-content:center; align-items:center; padding:56px 80px; gap:24px. "
      "Background: dark neutral gradient (very controlled, near-black preferred). "
      "  Optional: subtle grid-line texture overlay (bg-image repeating-linear-gradient opacity:0.04). "
      "Framed product/concept display: "
      "  Outer frame container — bg:rgba(255,255,255,0.04); border:1px solid rgba(255,255,255,0.12); "
      "  border-radius:24px; padding:24px; box-shadow:0 32px 80px rgba(0,0,0,0.5); max-width:880px; width:100%. "
      "  Inner content area — bg:rgba(255,255,255,0.03); border-radius:16px; "
      "  min-height:380px; display:flex; align-items:center; justify-content:center. "
      "  Large product icon or abstract concept visual (120px; accent-tinted; optional glow). "
      "  Optional annotation markers (position:absolute; small circles with accent border + tooltip text label). "
      "Below the frame (text-align:center): "
      "  Minimal headline — font-size:22px; font-weight:800; letter-spacing:-0.5px; margin-top:16px. "
      "  Sub-caption — font-size:13px; font-weight:300; opacity:0.6; letter-spacing:0.5px; margin-top:6px."
    )
  }
}
