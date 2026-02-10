def get_theme_info(theme_name: str) -> str:
    themes = {
        "Arctic Frost": "Theme name-Arctic Frost Cool and crisp winter-inspired theme. Hex: #d4e4f7 (Ice Blue), #4a6fa5 (Steel Blue), #c0c0c0 (Silver), #fafafa (Crisp White). Typography: Headers: DejaVu Sans Bold, Body Text: DejaVu Sans.",
        
        "Botanical Garden": "Theme name-Botanical Garden Fresh and organic theme featuring vibrant garden-inspired colors. Hex: #4a7c59 (Fern Green), #f9a620 (Marigold), #b7472a (Terracotta), #f5f3ed (Cream). Typography: Headers: DejaVu Serif Bold, Body Text: DejaVu Sans.",
        
        "Desert Rose": "Theme name-Desert Rose Soft and sophisticated theme with dusty, muted tones. Hex: #d4a5a5 (Dusty Rose), #b87d6d (Clay), #e8d5c4 (Sand), #5d2e46 (Deep Burgundy). Typography: Headers: FreeSans Bold, Body Text: FreeSans.",
        
        "Forest Canopy": "Theme name-Forest Canopy Natural and grounded theme inspired by dense forests. Hex: #2d4a2b (Forest Green), #7d8471 (Sage), #a4ac86 (Olive), #faf9f6 (Ivory). Typography: Headers: FreeSerif Bold, Body Text: FreeSans.",
        
        "Golden Hour": "Theme name-Golden Hour Rich and warm autumnal palette for inviting atmospheres. Hex: #f4a900 (Mustard Yellow), #c1666b (Terracotta), #d4b896 (Warm Beige), #4a403a (Chocolate Brown). Typography: Headers: FreeSans Bold, Body Text: FreeSans.",
        
        "Midnight Galaxy": "Theme name-Midnight Galaxy Dramatic and cosmic theme with deep purples. Hex: #2b1e3e (Deep Purple), #4a4e8f (Cosmic Blue), #a490c2 (Lavender), #e6e6fa (Silver). Typography: Headers: FreeSans Bold, Body Text: FreeSans.",
        
        "Modern Minimalist": "Theme name-Modern Minimalist Clean and contemporary grayscale palette. Hex: #36454f (Charcoal), #708090 (Slate Gray), #d3d3d3 (Light Gray), #ffffff (White). Typography: Headers: DejaVu Sans Bold, Body Text: DejaVu Sans.",
        
        "Ocean Depths": "Theme name-Ocean Depths Professional and calming maritime theme. Hex: #1a2332 (Deep Navy), #2d8b8b (Teal), #a8dadc (Seafoam), #f1faee (Cream). Typography: Headers: DejaVu Sans Bold, Body Text: DejaVu Sans.",
        
        "Sunset Boulevard": "Theme name-Sunset Boulevard Warm and vibrant theme inspired by golden sunsets. Hex: #e76f51 (Burnt Orange), #f4a261 (Coral), #e9c46a (Warm Sand), #264653 (Deep Purple). Typography: Headers: DejaVu Serif Bold, Body Text: DejaVu Sans.",
        
        "Tech Innovation": "Theme name-Tech Innovation Bold and modern theme with high-contrast tech colors. Hex: #028090 (Teal), #00A896 (Seafoam), #02C39A (Mint), #F2F2F2 (Off-white). Typography: Headers: DejaVu Sans Bold, Body Text: DejaVu Sans."
    }
    
    # Returns the theme info if found, otherwise returns a default message
    return themes.get(theme_name, themes["Arctic Frost"])