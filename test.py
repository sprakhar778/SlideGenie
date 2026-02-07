

from weasyprint import HTML, CSS

# 1. Define the fix: 
# - Force page size to match CSS
# - Hide the #333 body background that's causing overflow
# - Remove margins
extra_css = CSS(string="""
    @page { 
        size: 1280px 900px; 
        margin: 0; 
    }
    
    html, body {
        /* Hard limit: nothing exists outside these bounds */
        width: 1280px !important;
        height: 900px !important;
        overflow: hidden !important;
        margin: 0 !important;
        padding: 0 !important;
        background-color: white !important;
    }

    .slide {
        /* Force the slide to fit the page exactly */
        width: 1280px !important;
        height: 900px !important;
  
        /* Cut off anything that hangs over the edge */
        overflow: hidden !important;
        
        /* Remove things that bleed outside the box */
        box-shadow: none !important; 
        margin: 0 !important;
        border: none !important;

        /* Instruct the PDF engine not to jump to a new page */
        page-break-inside: avoid !important;
        page-break-after: avoid !important;
    }

  
""")
# 2. Generate the PDF
HTML("slides.html").write_pdf("output.pdf", stylesheets=[extra_css])