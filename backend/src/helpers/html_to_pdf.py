from playwright.sync_api import sync_playwright
from pathlib import Path
from pypdf import PdfWriter
from PIL import Image
import os
import tempfile
from src.api.helpers import load_presentation, PRESENTATIONS_DIR

def generate_presentation_pdf(presentation_id: str) -> str:
    """
    PERFECT BALANCE - great quality, tiny file size.
    ~500KB per slide instead of 2.5MB.
    """
    slides = load_presentation(presentation_id).get("slides_data", [])
    output_path = os.path.join(PRESENTATIONS_DIR, f"{presentation_id}.pdf")
    os.makedirs(PRESENTATIONS_DIR, exist_ok=True)
    
    temp_files = []
    merger = PdfWriter()
    
    # Sweet spot settings
    SCALE = 1.5  # 1.5x is enough (1920x1080)
    QUALITY = 80  # 80% is visually perfect
    
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            
            for idx, slide in enumerate(slides):
                html = slide.get("slide_code", "").strip()
                if not html:
                    continue
                
                # Create temp files
                html_file = tempfile.NamedTemporaryFile(suffix=".html", mode="w", delete=False, encoding="utf-8")
                jpg_file = tempfile.NamedTemporaryFile(suffix=".jpg", delete=False)
                pdf_file = tempfile.NamedTemporaryFile(suffix=".pdf", delete=False)
                temp_files.extend([html_file.name, jpg_file.name, pdf_file.name])
                
                try:
                    # Save HTML
                    html_file.write(html)
                    html_file.close()
                    
                    # Create page
                    page = browser.new_page(
                        viewport={"width": int(1280 * SCALE), "height": int(720 * SCALE)}
                    )
                    
                    # Load
                    page.goto(Path(html_file.name).resolve().as_uri(), wait_until="networkidle")
                    page.wait_for_timeout(1000)
                    
                    # Find container
                    container = page.query_selector('.slide-container') or page.query_selector('body > div')
                    
                    if container:
                        container.screenshot(path=jpg_file.name, type="jpeg", quality=QUALITY)
                    else:
                        page.screenshot(path=jpg_file.name, type="jpeg", quality=QUALITY)
                    
                    page.close()
                    
                    # Convert to PDF
                    img = Image.open(jpg_file.name)
                    
                    # Convert to RGB
                    if img.mode != 'RGB':
                        img = img.convert('RGB')
                    
                    # Save with maximum compression
                    img.save(
                        pdf_file.name,
                        "PDF",
                        quality=QUALITY,
                        optimize=True,
                        dpi=(150, 150)  # Lower DPI for screen viewing
                    )
                    
                    # Check size before adding
                    size_kb = os.path.getsize(pdf_file.name) / 1024
                    merger.append(pdf_file.name)
                    print(f"✓ Slide {idx + 1} - {size_kb:.1f}KB")
                    
                except Exception as e:
                    print(f"⚠ Slide {idx + 1} failed: {e}")
                    continue
            
            browser.close()
        
        # Save final PDF
        if len(merger.pages) > 0:
            merger.write(output_path)
            mb = os.path.getsize(output_path) / (1024 * 1024)
            print(f"✓ Final PDF: {output_path} ({mb:.2f} MB)")
        
        return os.path.abspath(output_path)
        
    finally:
        merger.close()
        for f in temp_files:
            try:
                if os.path.exists(f):
                    os.remove(f)
            except:
                pass