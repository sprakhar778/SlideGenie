from playwright.sync_api import sync_playwright
from pathlib import Path
from pypdf import PdfWriter
from PIL import Image
import os
import tempfile
from src.api.helpers import load_presentation, PRESENTATIONS_DIR

def generate_presentation_pdf(presentation_id: str) -> str:
    """
    UNIVERSAL PDF GENERATOR – works for ANY HTML/CSS, no vanishing elements.
    Uses high‑quality screenshot of the slide container and embeds it into a PDF.
    Optimized for file size (~300‑500KB per slide) while retaining crisp text.
    """
    slides = load_presentation(presentation_id).get("slides_data", [])
    output_path = os.path.join(PRESENTATIONS_DIR, f"{presentation_id}.pdf")
    os.makedirs(PRESENTATIONS_DIR, exist_ok=True)

    temp_files = []
    merger = PdfWriter()

    # Sweet‑spot settings: quality vs. file size
    SCALE = 1.5      # 1920×1080 – plenty for screen
    JPEG_QUALITY = 100  # 80% is visually lossless for most slides
    PDF_DPI = 100        # good for on‑screen viewing

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)

            for idx, slide in enumerate(slides):
                html = slide.get("slide_code", "").strip()
                if not html:
                    continue

                # Temporary files
                html_file = tempfile.NamedTemporaryFile(suffix=".html", mode="w", delete=False, encoding="utf-8")
                jpg_file = tempfile.NamedTemporaryFile(suffix=".jpg", delete=False)
                pdf_file = tempfile.NamedTemporaryFile(suffix=".pdf", delete=False)
                temp_files.extend([html_file.name, jpg_file.name, pdf_file.name])

                try:
                    # Write raw HTML (no modifications)
                    html_file.write(html)
                    html_file.close()

                    # Create page at scaled resolution
                    page = browser.new_page(
                        viewport={"width": int(1280 * SCALE), "height": int(720 * SCALE)}
                    )

                    # Load and wait for everything
                    page.goto(Path(html_file.name).resolve().as_uri(), wait_until="networkidle")
                    page.wait_for_timeout(150)  # extra time for fonts/animations

                    # Locate the slide container (most reliable selector)
                    container = page.query_selector('.slide-container')
                    if not container:
                        container = page.query_selector('body > div')  # fallback

                    if container:
                        # Screenshot only the container (excludes any body background)
                        container.screenshot(path=jpg_file.name, type="jpeg", quality=JPEG_QUALITY)
                    else:
                        # Ultimate fallback – whole page
                        page.screenshot(path=jpg_file.name, type="jpeg", quality=JPEG_QUALITY)

                    page.close()

                    # Convert image to PDF with compression
                    img = Image.open(jpg_file.name)
                    if img.mode != 'RGB':
                        img = img.convert('RGB')

                    # Save as PDF with optimization
                    img.save(
                        pdf_file.name,
                        "PDF",
                        quality=JPEG_QUALITY,
                        optimize=True,
                        dpi=(PDF_DPI, PDF_DPI)
                    )

                    merger.append(pdf_file.name)
                    print(f"✓ Slide {idx+1} – {os.path.getsize(pdf_file.name)/1024:.1f}KB")

                except Exception as e:
                    print(f"⚠ Slide {idx+1} failed: {e}")
                    continue

            browser.close()

        if len(merger.pages) > 0:
            merger.write(output_path)
            mb = os.path.getsize(output_path) / (1024 * 1024)
            print(f"✓ PDF saved: {output_path} ({mb:.2f} MB)")
        else:
            raise Exception("No slides generated")

        return os.path.abspath(output_path)

    finally:
        merger.close()
        # Cleanup temporary files
        for f in temp_files:
            try:
                if os.path.exists(f):
                    os.remove(f)
            except:
                pass