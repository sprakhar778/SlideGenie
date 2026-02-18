from weasyprint import HTML, CSS

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

# IMPORTANT: Add presentational_hints=True to support HTML attributes like 'width'
HTML("slides.html").write_pdf(
    "output.pdf", 
    stylesheets=[extra_css],
    presentational_hints=True
)