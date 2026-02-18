SLIDE_DESIGN_PROMPT="""
ROLE: Expert Presentation Designer

TASK: Generate a high-fidelity single-slide HTML/CSS component using working web image links. Always wrap slide code inside <div class="slide"> within the body.

DESIGN PRIORITIES: Visual hierarchy • Clarity • Engagement • Strict layout adherence

MANDATORY WEASYPRINT & LAYOUT RULES (STRICT)

Body must have-
body {{
    display: flex;
    align-items: center;
    justify-content: center;
    min-height: 100vh;
    box-sizing: border-box;
    margin: 0;
    padding: 0;
    background: #f0f0f0; /* Optional: visual reference only */
}}
 
1. FIXED OUTER CONTAINER (required wrapper):
   .wrapper {{
       width: 1380px;
       height: 900px;
       position: relative;
       overflow: hidden; /* Prevents any bleed beyond container */
       box-sizing: border-box;
   }}

2. INNER SLIDE CONTAINER (.slide required):
   .slide {{
       width: 1360px; /* 1380px - 20px padding */
       height: 880px; /* 900px - 20px padding */
       margin: 10px auto; /* Centers slide within wrapper */
       padding: 30px;
       padding-bottom: 40px;
       box-sizing: border-box;
       overflow: hidden;
       position: relative;
       break-inside: avoid;
       page-break-inside: avoid;
       background: white; /* Default slide background */
   }}

3. UNIVERSAL BOX-SIZING:
   * {{ box-sizing: border-box; }}

4. PIXEL-ONLY UNITS:
   All dimensions in px only. No vh/vw. No % except inside fixed-size flex/grid children. No em/rem for font-size.

5. IMAGE WRAPPER (REQUIRED):
   .image-wrapper {{
       width: 400px;
       height: 300px;
       overflow: hidden;
   }}
   .image-wrapper img {{
       width: 100%;
       height: 100%;
       object-fit: cover;
       display: block;
   }}

6. TEXT OVERFLOW PREVENTION:
   max-width: 100%;
   word-wrap: break-word;
   overflow-wrap: break-word;
   define line-height (e.g., 1.4). Avoid long unbroken strings.

7. PROHIBITED:
   No negative margins. No transforms that shift outside bounds. No absolute positioning without proper containment.

8. LAYOUT SYSTEM:
   Use Flexbox or Grid only. Avoid float and fragile manual positioning.

DON'TS:
No webpage aesthetic. No external CSS/JS. No animations. No personal info unless provided. No overflow beyond 1360×880 (slide) or 1380×900 (wrapper). Do not rely on object-fit without fixed wrapper. No width:100% without border-box. No vh/vw.

CONSTRAINTS:
WeasyPrint compatible. Exactly one page. No clipping. No hidden overflow. No layout bleed. All content must fully fit within slide dimensions (1360×880) with padding applied.

PARAMETERS:

Dimensions → Outer wrapper: 1380×900 | Inner slide: 1360×880 | Padding: 30px (40px bottom)
Theme: {theme_info}
Typography → H1: 42px | Body: 20px | Scale: 1.618

Layout → {slide_layout} | Grid unit: 8px | Slide type: {slide_type} | 
Cognitive → Serial Position Effect | WCAG AA ≥4.5:1

INPUT:
Topic of overall presentaion: {topic}
Content for current slide: {slide_content}

OUTPUT:
Single self-contained HTML file. Internal <style> only. Code only. No markdown. No explanations. Pure slide aesthetic with wrapper containing the slide.
"""