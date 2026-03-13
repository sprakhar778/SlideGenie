from playwright.sync_api import sync_playwright
from pathlib import Path
from pypdf import PdfWriter
import os
import tempfile
import logging
from src.api.helpers import load_presentation, PRESENTATIONS_DIR

logger = logging.getLogger(__name__)

def generate_presentation_pdf(presentation_id: str) -> str:
    """
    Generates a PDF directly from HTML using Playwright's PDF generation.
    Fixed version that preserves all visual elements including cards.
    """
    state = load_presentation(presentation_id)
    slides_data = state.get("slides_data", [])
    
    output_dir = PRESENTATIONS_DIR
    os.makedirs(output_dir, exist_ok=True)
    final_pdf_path = os.path.join(output_dir, f"{presentation_id}.pdf")
    
    merger = PdfWriter()
    temp_files = []
    
    try:
        with sync_playwright() as p:
            # Launch browser with specific args for better rendering
            browser = p.chromium.launch(
                headless=True,
                args=['--font-render-hinting=medium', '--force-device-scale-factor=1']
            )
            
            for idx, slide in enumerate(slides_data):
                html_content = slide.get("slide_code", "").strip()
                if not html_content:
                    continue
                
                # Create a temporary HTML file for this slide with proper viewport settings
                temp_html = tempfile.NamedTemporaryFile(suffix=".html", mode="w", delete=False, encoding="utf-8")
                
                # Wrap HTML with proper viewport settings and ensure backdrop-filter works
                wrapped_html = f"""
                <!DOCTYPE html>
                <html>
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=1280, initial-scale=1">
                    <style>
                        /* Ensure backdrop-filter works in PDF */
                        * {{
                            -webkit-print-color-adjust: exact;
                            print-color-adjust: exact;
                        }}
                        body {{
                            margin: 0;
                            padding: 0;
                            width: 1280px;
                            height: 720px;
                            overflow: hidden;
                            background: #0f172a;
                        }}
                     
                    </style>
                </head>
                <body>
                    {html_content}
                </body>
                </html>
                """
                
                temp_html.write(wrapped_html)
                temp_html.close()
                temp_files.append(temp_html.name)
                
                # Create a temporary PDF file for this slide
                temp_pdf = tempfile.NamedTemporaryFile(suffix=".pdf", delete=False)
                temp_pdf.close()
                temp_files.append(temp_pdf.name)
                
                try:
                    # Create new page with specific viewport
                    page = browser.new_page(
                        viewport={"width": 1280, "height": 720}
                    )
                    
                    file_url = Path(temp_html.name).resolve().as_uri()
                    
                    # Navigate and wait for network idle
                    page.goto(file_url, wait_until="networkidle")
                    
                    # Wait longer for fonts and backdrop-filter to render
                    page.wait_for_timeout(200)
                    
                    # Ensure all elements are visible
                    page.evaluate("""() => {
                        // Force repaint for backdrop-filter
                        document.body.style.transform = 'translateZ(0)';
                        // Ensure all cards are visible
                        document.querySelectorAll('.card').forEach(card => {
                            card.style.transform = 'translateZ(0)';
                        });
                    }""")
                    
                    # Generate PDF with specific settings
                    page.pdf(
                        path=temp_pdf.name,
                        width="1280px",
                        height="720px",
                        print_background=True,
                        margin={
                            "top": "0px",
                            "right": "0px",
                            "bottom": "0px",
                            "left": "0px"
                        },
                        scale=1.0,
                        prefer_css_page_size=True
                    )
                    
                    page.close()
                    
                    # Verify PDF was created and has content
                    if os.path.getsize(temp_pdf.name) > 1000:  # Basic check
                        merger.append(temp_pdf.name)
                    else:
                        logger.error(f"PDF for slide {idx} appears to be empty")
                        
                except Exception as e:
                    logger.error(f"Failed to generate PDF for slide {idx}: {e}")
                    
                    # Fallback: Try screenshot method for this slide
                    try:
                        fallback_pdf = fallback_screenshot_method(html_content, idx)
            
                        if fallback_pdf and os.path.exists(fallback_pdf):
                            merger.append(fallback_pdf)
                            temp_files.append(fallback_pdf)
                    except:
                        continue
                    
            browser.close()
            
        # Write the merged PDF
        if len(merger.pages) > 0:
            merger.write(final_pdf_path)
        else:
            raise Exception("No slides were successfully converted to PDF")
        
    finally:
        merger.close()
        # Clean up temporary files
        for temp_file in temp_files:
            if os.path.exists(temp_file):
                try:
                    os.remove(temp_file)
                except Exception as e:
                    logger.warning(f"Failed to remove temporary file {temp_file}: {e}")
                    
    return os.path.abspath(final_pdf_path)




#------Fallback Method------

def fallback_screenshot_method(html_content: str, idx: int) -> str:
    """
    Fallback method using screenshot for slides that don't render properly in PDF.
    """
    from PIL import Image
    import tempfile
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        
        # Create temp files
        temp_html = tempfile.NamedTemporaryFile(suffix=".html", mode="w", delete=False, encoding="utf-8")
        temp_html.write(html_content)
        temp_html.close()
        
        temp_png = tempfile.NamedTemporaryFile(suffix=".png", delete=False)
        temp_png.close()
        
        temp_pdf = tempfile.NamedTemporaryFile(suffix=".pdf", delete=False)
        temp_pdf.close()
        
        try:
            # Use higher resolution for better quality
            context = browser.new_context(
                viewport={"width": 2560, "height": 1440},  # 2x resolution
                device_scale_factor=2
            )
            page = context.new_page()
            
            file_url = Path(temp_html.name).resolve().as_uri()
            page.goto(file_url, wait_until="networkidle")
            page.wait_for_timeout(2000)
            
            # Take screenshot
            page.screenshot(
                path=temp_png.name,
                full_page=False,
                scale="css"
            )
            
            page.close()
            context.close()
            
            # Convert to PDF
            image = Image.open(temp_png.name)
            
            # Resize to target size using high-quality resampling
            target_size = (1280, 720)
            if image.size != target_size:
                image = image.resize(target_size, Image.Resampling.LANCZOS)
            
            if image.mode != 'RGB':
                image = image.convert('RGB')
            
            image.save(temp_pdf.name, "PDF", quality=95, dpi=(300, 300))
            
            browser.close()
            
            # Clean up HTML and PNG
            os.unlink(temp_html.name)
            os.unlink(temp_png.name)
            
            return temp_pdf.name
            
        except Exception as e:
            browser.close()
            # Clean up on error
            for f in [temp_html.name, temp_png.name, temp_pdf.name]:
                if os.path.exists(f):
                    os.unlink(f)
            raise e