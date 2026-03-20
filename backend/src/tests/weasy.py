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
        browser = await p.chromium.launch(
            headless=True,
            args=['--disable-web-security', '--no-sandbox']
        )
        
        page = await browser.new_page(
            viewport={"width": 1280, "height": 720}
        )
        
        # Set realistic user agent
        await page.set_extra_http_headers({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        
        try:
            for idx, slide in enumerate(slides_data):
                raw_html = slide.get("slide_code", "").strip()
                if not raw_html:
                    continue
                
                # Wrap HTML with proper viewport and base URL
                wrapped_html = f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
    /* Minimal reset - let slide content control layout */
    * {{
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }}
    
    body {{
        width: 1280px;
        height: 720px;
        overflow: hidden;
    }}
    
    /* Only set dimensions, let the slide decide how to fill it */
    body > * {{
        width: 100%;
        height: 100%;
    }}
</style>
</head>
<body>
{raw_html}
</body>
</html>
"""
                
                temp_pdf = tempfile.NamedTemporaryFile(suffix=".pdf", delete=False)
                temp_pdf_path = temp_pdf.name
                temp_files.append(temp_pdf_path)
                temp_pdf.close()
                
                try:
                    # Set content with base URL for relative resources
                    await page.set_content(wrapped_html, wait_until="networkidle")
                    
                    # Wait for images to load
                    await page.wait_for_timeout(300)
                    
                    await page.pdf(
                        path=temp_pdf_path,
                        width=PAGE_WIDTH,
                        height=PAGE_HEIGHT,
                        print_background=True,
                        scale=1,
                        margin={'top': '0', 'bottom': '0', 'left': '0', 'right': '0'}
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