SLIDE_DESIGN_PROMPT = """
## *Role*
Expert Presentation Designer

## **Task**
Generate a high-fidelity, single-slide HTML/CSS component. Use relevant images via working web links. Always wrap slide code in `<div class="slide">` inside the body.

**Design Priorities:**
- Visual hierarchy
- Clarity
- Engagement
- Adherence to provided design parameters

##Don'ts
- Avoid 'webpage' aesthetics; the output should feel like a 'slide' rather than a full webpage.
- Do not use external CSS or JS files or animationsall styles must be contained within an internal <style> block.
- Do not mention any owner info ,name date,department  or personal info if  not provided in content
- Strictly avoid any code that would cause overflow beyond the specified dimensions (1280x720px).]
##Constraints
-**Image Handling:** Images must be wrapped in a container with a defined height/width and use `object-fit: cover;` to prevent layout shifting.
-**No Margin Bleed:** Ensure no negative margins or absolute positioning pushes content beyond the 1280x900 boundary
-No overflow: All content must fit within the defined dimensions without scrollbars or hidden overflow.





## Prameters

#Dimensions
- Width: 1280px
- Height: 720px
- Aspect Ratio: 16:9
- Padding: 70px

#Theme
- Color Distribution: 60-30-10 Rule
- Palette:{palette}

#Typography
- Header Font:{heading_font}
- Body Font:{body_font}
- H1 Size: 42px
- Body Size: 20px 
- Scale Ratio: 1.618 (Golden Ratio)

 
 ##Layout
 -Grid Unit: 8px or what you think is best for the layout
  -Type of Slide:{slide_type}
  -Components: {components}
  


### **Cognitive Principles Applied**
- **Serial Position Effect** (Primacy & Recency)
- **WCAG AA Contrast Compliance** (Minimum 4.5:1)


---

## **Input Data**   
Topic: {topic}
Content: {content}
---
## **Output Format**
- **Type:** Single HTML file
- **CSS Style:** Internal `<style>` block only
- **Constraints:** Strictly avoid "webpage" aesthetics. Prioritize "slide" presentation feel.
- **Provide:** **Code only**, no explanations.

"""


    # "layout": {{
    #   "type": "Split-Screen/Two-Column",
    #   "grid_unit": "8px",
    #   "components": [
    #     "Full-width header bar",
    #     "Left column: Chronological list with Material Design Icons",
    #     "Left column: Year/Label badges",
    #     "Right column: Visual container with subtle box-shadow"
    #   ]
    # }},

  #       "layout": {{
  #   "type": "Split-Screen / Feature-Focus",
  #   "grid_unit": "8px",
  #   "components": [
  #     "Full-width header bar (Primary Blue)",
  #     "Left column: Problem/Solution Statement (High-contrast text block)",
  #     "Left column: Interactive 'Feature Cards' with hover-effect styling",
  #     "Right column: Central 'Core' diagram (Hexagonal or Circular structure)",
  #     "Right column: Dynamic Metrics footer (3-column stat bar)"
  #   ]
  # }},

  #  "layout": {{
  #   "type": "Hero / Title-Focus",
  #   "grid_unit": "8px",
  #   "components": [
  #     "Background: Subtle geometric gradient (Quantum-inspired)",
  #     "Center: Large Typographic Title (Playfair Display)",
  #     "Center: Secondary subtitle with high tracking (letter-spacing)",
  #     "Bottom-Left: Presenter credentials / Department badge",
  #     "Bottom-Right: Date & Version control",
  #     "Bottom Edge: Thick Primary Blue accent bar"
  #   ]
  # }}