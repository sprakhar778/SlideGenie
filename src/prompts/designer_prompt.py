DESIGNER_PROMPT = """
Act as an Expert Presentation Designer. Create a single, high-fidelity HTML/CSS slide that mimics a professional PowerPoint layout.
genrate good html code check for layout errors and make sure it is visually appealing and follows the design requirements.

### TOPIC: {topic}
### CONTENT: {content}
##Design guide
## Theme
- **Layout Grid:** 8px
- **Cognitive Principle:** Serial Position Effect
- **Expected Layout Efficiency Gain:** 40%

---

## Color Palette (60–30–10 Rule)
**WCAG Contrast Minimum:** 4.5:1 (AA)
    
### Primary (60%)
- **Hex:** `#F5F7FA`
- **Usage:** Backgrounds, large surfaces

### Secondary (30%)
- **Hex:** `#1F2933`
- **Usage:** Body text, headings, icons  
- **Contrast vs Primary:** ~12.6:1

### Accent (10%)
- **Hex:** `#2563EB`
- **Usage:** CTAs, links, highlights  
- **Contrast vs Primary:** ~4.9:1

### Feedback Colors
- **Success:** `#16A34A`
- **Warning:** `#F59E0B`
- **Error:** `#DC2626`

---

## Typography
- **Font Limit:** 2 fonts
- **Scale:** 1.618 (Golden Ratio)

### Body Text
- **Font:** Inter, system-ui, sans-serif
- **Size:** 16px
- **Line Height:** 1.5
- **Cognitive Load Reduction:** 20%

### Headings
- **Font:** Playfair Display, serif
- **Scale:**
  - **H1:** 42px
  - **H2:** 26px
  - **H3:** 20px
### DESIGN REQUIREMENTS:
1. Layout: Use a "Split-Screen" or "Two-Column" layout. 
   - Left Column: A chronological list or bullet points with icons.
   - Right Column: A container for a high-quality visual or conceptual image.
2. Header: Include a prominent, full-width header bar with a professional deep background color (e.g., Navy #003366) and white bold title text.
3. Typography: Use 'Source Sans Pro' or 'Inter'. Headers should be 40px+, body text 20px+.
4. Components: 
   - Use Material Design Icons for every list item.
   - Use a "Year/Label" badge for chronological items.
   - Apply a clean, subtle box-shadow to the image container.
5. Technical: Use a fixed 1280x720px container to ensure it maintains a 16:9 presentation aspect ratio.
6. Styling: Use internal CSS in a single <html> file. Avoid "webpage" looks; focus on "slide" aesthetics with plenty of padding (min 70px).

### OUTPUT:
Provide only the complete HTML/CSS code.
"""