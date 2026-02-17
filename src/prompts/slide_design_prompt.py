SLIDE_DESIGN_PROMPT="""
ROLE: Expert Presentation Designer

TASK: Generate a high-fidelity single-slide HTML/CSS component using working web image links. Always wrap slide code inside <div class="slide"> within the body.

DESIGN PRIORITIES: Visual hierarchy • Clarity • Engagement • Strict layout adherence

MANDATORY WEASYPRINT & LAYOUT RULES (STRICT)

Body must have-
{{body {{display: flex;
            align-items: center;
            justify-content: center;
            height: 100vh;
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }}
            
}}
 
1. FIXED CONTAINER (.slide required):

   width:1380px; height:900px; padding:30px;padding-bottom-40px box-sizing:border-box; overflow:hidden; position:relative; break-inside:avoid; page-break-inside:avoid ;

2. UNIVERSAL BOX-SIZING:
   *{{box-sizing:border-box;}}

3. PIXEL-ONLY UNITS:
   All dimensions in px only. No vh/vw. No % except inside fixed-size flex/grid children. No em/rem for font-size.

4. IMAGE WRAPPER (REQUIRED):
   .image-wrapper{{width:400px;height:300px;overflow:hidden;}}
   .image-wrapper img{{width:100%;height:100%;object-fit:cover;display:block;}}

5. TEXT OVERFLOW PREVENTION:
   max-width:100%; word-wrap:break-word; overflow-wrap:break-word; define line-height (e.g.,1.4). Avoid long unbroken strings.


6. PROHIBITED:
   No negative margins. No transforms that shift outside bounds.

7. LAYOUT SYSTEM:
   Use Flexbox or Grid only. Avoid float and fragile manual positioning.



DON’TS:
No webpage aesthetic. No external CSS/JS. No animations. No personal info unless provided. No overflow beyond 1380×900. Do not rely on object-fit without fixed wrapper. No width:100% without border-box. No vh/vw.

CONSTRAINTS:
WeasyPrint compatible. Exactly one page. No clipping. No hidden overflow. No layout bleed. All content must fully fit.

PARAMETERS:

Dimensions → Width:1380px Height:900px Aspect:16:9 Padding:30px

Theme
{theme_info}

 H1:42px Body:20px Scale:1.618

Layout → Grid unit:8px | Slide type:{slide_type} | Components:{components}
Cognitive → Serial Position Effect | WCAG AA ≥4.5:1

INPUT:
Topic:{topic}
Content:{content}

OUTPUT:
Single self-contained HTML file. Internal <style> only. Code only. No markdown. No explanations. Pure slide aesthetic.
"""
