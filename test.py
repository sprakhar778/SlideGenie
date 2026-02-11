

from weasyprint import HTML, CSS

# 1. Define the fix: 
# - Force page size to match CSS
# - Hide the #333 body background that's causing overflow
# - Remove margins
extra_css = CSS(string="""
    @page { 
        size: 1285px 718px; 
        margin: 0; 
    }
    
    html, body {
        width: 1285px !important;
        height: 718px !important;
        overflow: hidden !important;
        margin: 0 !important;
        padding: 0 !important;
        background-color: white !important;
        /* Fix for merged text */
        -webkit-font-smoothing: antialiased;
        font-smooth: always;
        text-rendering: optimizeLegibility;
    }

    .slide {
        width: 1285px !important;
        height: 718px !important;
        overflow: hidden !important;
        display: flex;
        flex-direction: column;
        box-sizing: border-box;
    }

    /* Prevent text from overlapping vertically */
    p, li, h1, h2, h3 {
        line-height: 1.4 !important;
        margin-bottom: 0.5em;
    }

    /* Prevent characters from squeezing together */
    * {
        letter-spacing: 0.01em !important;
    }
""")
# 2. Generate the PDF
HTML("slides.html").write_pdf("output.pdf", stylesheets=[extra_css])