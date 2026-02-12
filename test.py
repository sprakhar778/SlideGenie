

from weasyprint import HTML, CSS

# 1. Define the fix: 
# - Force page size to match CSS
# - Hide the #333 body background that's causing overflow
# - Remove margins


extra_css = CSS(string="""
    @page {
        
        size: 1400px 920px;      /* Match slide dimensions exactly */
        margin: 0;
    }

    html, body {
        width: 1400px !important;
        height: 920px !important;
        margin: 0 !important;
        padding: 0 !important;
        background: white !important;
      
       
    }

    .slide {
        width: 1400px !important;
        height: 920px !important;
      
        padding: 30px;            /* Your design padding */
        padding-bottom: 30px;     /* Adjust if needed */
        margin: 0 !important;
        overflow: hidden !important;
        box-sizing: border-box;   /* Padding included in width/height */
        position: relative;       /* Anchor for absolute children */
        break-inside: avoid;     /* Prevent page break inside slide */
        page-break-inside: avoid; /* Legacy support */
    }

    /* Ensure all content respects boundaries */
    .slide * {
        max-width: 100% !important;
        max-height: 100% !important;
        box-sizing: border-box;
    }

    /* Images – use object-fit inside explicit containers */
    .slide img {
        display: block;
        max-width: 100%;
        height: auto;
        object-fit: cover;
    }

    /* Font rendering – keep your existing improvements */
    * {
        -webkit-font-smoothing: antialiased;
        font-smooth: always;
        text-rendering: optimizeLegibility;
        letter-spacing: 0.01em !important;
    }
""")

# IMPORTANT: Add presentational_hints=True to support HTML attributes like 'width'
HTML("slides.html").write_pdf(
    "output.pdf", 
    stylesheets=[extra_css],
    
    presentational_hints=True
)
# 2. Generate the PDF
