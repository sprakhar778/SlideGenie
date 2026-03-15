from playwright.async_api import async_playwright
from pypdf import PdfWriter
import os
import tempfile
import logging
 
from src.api.helpers import load_presentation, PRESENTATIONS_DIR
 
logger = logging.getLogger(__name__)
 
PAGE_WIDTH = "1280px"
PAGE_HEIGHT = "720px"
 
 
async def generate_presentation_pdf(presentation_id: str) -> str:
 
    state = await load_presentation(presentation_id)
    slides_data = state.get("slides_data", [])
 
    os.makedirs(PRESENTATIONS_DIR, exist_ok=True)
    final_pdf_path = os.path.join(PRESENTATIONS_DIR, f"{presentation_id}.pdf")
 
    merger = PdfWriter()
    temp_files = []
 
    async with async_playwright() as p:
 
        browser = await p.chromium.launch()
        page = await browser.new_page(
            viewport={"width": 1280, "height": 720}
        )
 
        try:
 
            for idx, slide in enumerate(slides_data):
 
                raw_html = slide.get("slide_code", "").strip()
                if not raw_html:
                    continue
 
                wrapped_html = f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
html, body {{
    width:1280px;
    height:720px;
    margin:0 !important;
    padding:0 !important;
    overflow:hidden;
    background:#000;
}}
 
.slide-container {{
    width:1280px;
    height:720px;
    position:relative;
    padding:10px !important;
 
    box-sizing:border-box !important;
  
}}
img {{
    display:block;
    max-width:100%;
    max-height:100%;
    
}}
 
</style>
</head>
 
<body>
<div class="slide-container">
{raw_html}
</div>
</body>
</html>
"""
 
                temp_pdf = tempfile.NamedTemporaryFile(
                    suffix=".pdf",
                    delete=False
                )
 
                temp_pdf_path = temp_pdf.name
                temp_files.append(temp_pdf_path)
                temp_pdf.close()
 
                try:
 
                    await page.set_content(
                        wrapped_html,
                        wait_until="networkidle"
                    )
 
                    await page.pdf(
                        path=temp_pdf_path,
                        width=PAGE_WIDTH,
                        height=PAGE_HEIGHT,
                        print_background=True,
                        scale=1
                       
                    )
 
                    merger.append(temp_pdf_path)
 
                except Exception as e:
                    logger.error(f"Slide {idx} render failed: {e}")
                    continue
 
            merger.write(final_pdf_path)
 
        finally:
 
            await browser.close()
            merger.close()
 
            for file in temp_files:
                if os.path.exists(file):
                    try:
                        os.remove(file)
                    except Exception as e:
                        logger.warning(f"Temp cleanup failed: {e}")
 
    return os.path.abspath(final_pdf_path)
 