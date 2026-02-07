SLIDE_PROMPT = """
{{
  "role": "Expert Presentation Designer",
  "task": "Generate a high-fidelity, single-slide HTML/CSS component.use relvant image via working web links alway wrap slide code in <div class="slide"> slide code <div/ > inside body The design should prioritize visual hierarchy, clarity, and engagement while adhering to the provided design parameters.",
  "do'nts"[
    "Avoid 'webpage' aesthetics; the output should feel like a 'slide' rather than a full webpage.",
    "Do not use external CSS or JS files or animationsall styles must be contained within an internal <style> block.",
    "Do not mention any owner info ,name date,department  or personal info if  not provided in content",
    "Strictly avoid any code that would cause overflow beyond the specified dimensions (1280x720px).]
  "parameters": {{
    "dimensions": {{
      "width": "1280px",
      "height": "720px",
      "aspect_ratio": "16:9",
      "padding": "70px"
    }},
    "theme": {{
      "color_distribution": "60-30-10 Rule",
      "palette": {{
        "primary": "#F5F7FA",
        "secondary": "#1F2933",
        "accent": "#2563EB",
        "header_bg": "#003366",
        "header_text": "#FFFFFF"
      }},
      "typography": {{
        "heading_font": "Playfair Display, serif",
        "body_font": "Inter, system-ui, sans-serif",
        "h1_size": "42px",
        "body_size": "20px",
        "scale_ratio": 1.618
      }}
    }},
   "layout": {{
    "type": "Hero / Title-Focus",
    "grid_unit": "8px",
    "components": [
      "Background: Subtle geometric gradient (Quantum-inspired)",
      "Center: Large Typographic Title (Playfair Display)",
      "Center: Secondary subtitle with high tracking (letter-spacing)",
      "Bottom-Left: Presenter credentials / Department badge",
      "Bottom-Right: Date & Version control",
      "Bottom Edge: Thick Primary Blue accent bar"
    ]
   }}
    ,
    "cognitive_principles": [
      "Serial Position Effect",
      "WCAG AA Contrast Compliance (4.5:1 min)"
    ]
  }},
  "input_data": {{
    "topic": "{topic}",
    "content": "{content}"
  }},
  "output_format": {{
    "type": "Single HTML file",
    "css_style": "Internal <style> block",
    "constraints": "Strictly avoid 'webpage' aesthetics; prioritize 'slide' presentation feel. Provide code only."
  }}
}}
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