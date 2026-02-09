TEST="""

# Expert Presentation Designer Prompt

## **Task**
Generate a high-fidelity, single-slide HTML/CSS component. Use relevant images via working web links. Always wrap slide code in `<div class="slide">` inside the body.

**Design Priorities:**
- Visual hierarchy
- Clarity
- Engagement
- Adherence to provided design parameters

---

## **🚫 Do Not**
- Create "webpage" aesthetics – the output must feel like a **slide**, not a full webpage.
- Use external CSS, JS files, or animations. All styles must be contained within an internal `<style>` block.
- Mention any owner info, name, date, department, or personal details unless explicitly provided in the content.
- Include code that causes overflow beyond the specified dimensions (1280×720 px).

---

## **Design Parameters**

### **Dimensions**
- **Width:** 1280px
- **Height:** 720px
- **Aspect Ratio:** 16:9
- **Padding:** 70px

---

### **Theme**

#### **Color Distribution**
- Follow the **60-30-10 Rule**.

#### **Palette**
- **Primary:** `#F5F7FA`
- **Secondary:** `#1F2933`
- **Accent:** `#2563EB`
- **Header Background:** `#003366`
- **Header Text:** `#FFFFFF`

#### **Typography**
- **Heading Font:** `Playfair Display, serif`
- **Body Font:** `Inter, system-ui, sans-serif`
- **H1 Size:** 42px
- **Body Size:** 20px
- **Scale Ratio:** 1.618 (Golden Ratio)

---

### **Layout**

**Type:** *Hero / Title-Focus*

**Grid Unit:** 8px

**Components (Ordered):**
1. **Background:** Subtle geometric gradient (Quantum-inspired)
2. **Center:** Large Typographic Title (Playfair Display)
3. **Center:** Secondary subtitle with high letter-spacing
4. **Bottom-Left:** Presenter credentials / Department badge
5. **Bottom-Right:** Date & Version control
6. **Bottom Edge:** Thick Primary Blue accent bar

---

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