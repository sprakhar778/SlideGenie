import io
import os
from PIL import Image
from pypdf import PdfReader, PdfWriter

from src.api.helpers import PRESENTATIONS_DIR, get_browser, load_presentation

async def generate_presentation_pdf(presentation_id: str):
    state = load_presentation(presentation_id)
    slides = state.get("slides_data", [])
    if not slides:
        raise Exception("No slides found in presentation")

    output_path = os.path.join(PRESENTATIONS_DIR, f"{presentation_id}.pdf")
    os.makedirs(PRESENTATIONS_DIR, exist_ok=True)

    merger = PdfWriter()
    browser = get_browser()

    # Use a high device scale factor (e.g., 3) for extra detail
    context = await browser.new_context(device_scale_factor=3)
    page = await context.new_page()

    # Set a large viewport – the slide will be scaled accordingly
    await page.set_viewport_size({"width": 1280, "height": 720})  # moderate size, scale factor multiplies pixels

    try:
        for idx, slide in enumerate(slides):
            html = slide.get("slide_code", "").strip()
            if not html:
                continue

            # Load HTML directly
            await page.set_content(html, wait_until="networkidle")
        
            # Inject print CSS so mobile printers respect page size
            await page.add_style_tag(content="""
            @page {
            size: 1280px 720px;
            margin: 0;
            }

            html {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            }
            """)
            try:
                await page.wait_for_selector(".slide-container", state="visible", timeout=500)
            except:
                pass
            await page.wait_for_timeout(200)  # short extra wait

            container = await page.query_selector(".slide-container")
            if container:
                # Screenshot at the increased pixel density
                png_bytes = await container.screenshot(type="png", scale="device")  # scale uses deviceScaleFactor
            else:
                png_bytes = await page.screenshot(type="png", scale="device")

            # Convert PNG bytes → PDF bytes (in‑memory)
            img = Image.open(io.BytesIO(png_bytes))
            if img.mode != "RGB":
                img = img.convert("RGB")
            pdf_bytes_io = io.BytesIO()
            # Save with 72 DPI – 1 pixel = 1 point, so page size matches image dimensions
            img.save(pdf_bytes_io, format="PDF", resolution=72, optimize=True,save_all=True)
            pdf_bytes_io.seek(0)

            # Append in‑memory PDF
            reader = PdfReader(pdf_bytes_io)
            merger.append(reader)

        if not merger.pages:
            raise Exception("No valid slides generated")

        merger.write(output_path)
        return os.path.abspath(output_path)
    finally:
        await context.close()
        merger.close()
        