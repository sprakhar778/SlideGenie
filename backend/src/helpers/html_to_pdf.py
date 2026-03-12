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
        size: 1300px 740px;
        margin: 0;
    }

    html, body {
        width: 1300px !important;
        height: 740px !important;
        margin: 0 !important;
        padding: 0 !important;
        overflow: hidden !important;
        background: white !important;
        /* Reset any display flex injected by the prompt preview styling */
        display: block !important;
    }

    /* Target the generated slide container */
    .slide-container {
        width: 1300px !important;
        height: 740px !important;
        min-width: 1300px !important;
        min-height: 740px !important;
        margin: 0 !important;
        position: absolute !important;
        top: 0 !important;
        left: 0 !important;
        box-sizing: border-box !important;
        break-inside: avoid !important;
        page-break-inside: avoid !important;
    }

    * {
        -webkit-font-smoothing: antialiased;
        text-rendering: optimizeLegibility;
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