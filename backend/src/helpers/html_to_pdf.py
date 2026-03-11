from weasyprint import HTML, CSS
from pypdf import PdfWriter
import os
import tempfile
import logging

from src.api.helpers import load_presentation, PRESENTATIONS_DIR

logger = logging.getLogger(__name__)

# 1. Define the fix with updated dimensions matching the new prompt structure
extra_css = CSS(string="""
    @page {
        size: 1380px 900px;      /* Match wrapper dimensions exactly */
        margin: 0;
    }

    html, body {
        width: 1380px !important;
        height: 900px !important;
        margin: 0 !important;
        padding: 0 !important;
        background: white !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
    }

    /* Outer wrapper - matches page size */
    .wrapper {
        width: 1380px !important;
        height: 900px !important;
        position: relative !important;
        overflow: hidden !important;
        box-sizing: border-box !important;
        margin: 0 !important;
        padding: 0 !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
    }

    /* Inner slide - with proper padding */
    .slide {
        width: 1360px !important;  /* 1380px - 20px for margin */
        height: 880px !important;   /* 900px - 20px for margin */
        margin: 10px auto !important; /* Centers slide within wrapper */
        padding: 30px !important;
        padding-bottom: 40px !important;
        overflow: hidden !important;
        box-sizing: border-box !important;
        position: relative !important;
        break-inside: avoid !important;
        page-break-inside: avoid !important;
        background: white !important;
    }

    /* Ensure all content respects boundaries */
    .slide * {
        max-width: 100% !important;
        box-sizing: border-box !important;
    }

    /* Image wrapper enforcement */
    .image-wrapper {
        width: 400px !important;
        height: 300px !important;
        overflow: hidden !important;
    }

    .image-wrapper img {
        width: 100% !important;
        height: 100% !important;
        object-fit: cover !important;
        display: block !important;
    }

    /* Text overflow prevention */
    p, h1, h2, h3, h4, h5, h6, li, div:not(.image-wrapper) {
        max-width: 100% !important;
        word-wrap: break-word !important;
        overflow-wrap: break-word !important;
        line-height: 1.4 !important;
    }

    /* Typography scale enforcement */
    h1 { font-size: 42px !important; }
    body, p, li { font-size: 20px !important; }

    /* Grid unit enforcement */
    .grid-unit {
        width: 8px !important;
        height: 8px !important;
    }

    /* Font rendering improvements */
    * {
        -webkit-font-smoothing: antialiased;
        font-smooth: always;
        text-rendering: optimizeLegibility;
        letter-spacing: 0.01em !important;
    }

    /* Prohibit any overflow */
    .wrapper, .slide, .slide * {
        max-height: 100% !important;
    }

    /* Flex/Grid layouts only - no floats */
    .slide {
        display: flex !important;
        flex-direction: column !important;
    }
""")

def generate_presentation_pdf(presentation_id: str) -> str:
    """
    Generates a PDF from the saved HTML of each slide in the presentation.
    If a slide fails to render, it skips it and continues.
    Returns the absolute path to the generated PDF.
    """
    state = load_presentation(presentation_id)
    slides_data = state.get("slides_data", [])
    
    output_dir = PRESENTATIONS_DIR
    os.makedirs(output_dir, exist_ok=True)
    final_pdf_path = os.path.join(output_dir, f"{presentation_id}.pdf")
    
    merger = PdfWriter()
    temp_files = []
    
    try:
        for idx, slide in enumerate(slides_data):
            html_content = slide.get("slide_code", "").strip()
            if not html_content:
                continue
                
            # Create a temporary PDF file for this slide
            temp_pdf = tempfile.NamedTemporaryFile(suffix=".pdf", delete=False)
            temp_files.append(temp_pdf.name)
            temp_pdf.close()
            
            try:
                # Add presentational_hints=True to support HTML attributes like 'width'
                HTML(string=html_content).write_pdf(
                    temp_pdf.name, 
                    stylesheets=[extra_css],
                    presentational_hints=True
                )
                merger.append(temp_pdf.name)
            except Exception as e:
                logger.error(f"Failed to generate PDF for slide {idx}: {e}")
                # Skip the slide but keep going
                continue
                
        merger.write(final_pdf_path)
    finally:
        merger.close()
        # Clean up temporary individual slide PDFs
        for temp_file in temp_files:
            if os.path.exists(temp_file):
                try:
                    os.remove(temp_file)
                except Exception as e:
                    logger.warning(f"Failed to remove temporary file {temp_file}: {e}")
                    
    return os.path.abspath(final_pdf_path)