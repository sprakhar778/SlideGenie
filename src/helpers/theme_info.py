from pydantic import BaseModel, Field
from typing import Literal

def get_theme_info(theme_name: str) -> str:
    themes = {
        "Arctic Frost": """### Theme: Arctic Frost
Identity: Cool, crisp, and professional. Designed for precision and clarity.

#### Color Palette (60-30-10 Rule)
- Primary (60%): #fafafa (Crisp White) - Backgrounds and clean space.
- Secondary (30%): #4a6fa5 (Steel Blue) - Headers and core branding.
- Accent (10%): #d4e4f7 (Ice Blue) - Highlights and CTAs.
- Neutral: #c0c0c0 (Silver) - Decorative elements.

#### Typography
- Headers: DejaVu Sans Bold
- Body Text: DejaVu Sans""",

        "Botanical Garden": """### Theme: Botanical Garden
Identity: Fresh and organic. Evokes growth and natural vitality.

#### Color Palette (60-30-10 Rule)
- Primary (60%): #f5f3ed (Cream) - Warm, soft background.
- Secondary (30%): #4a7c59 (Fern Green) - Professional natural text and icons.
- Accent (10%): #f9a620 (Marigold) - Vibrant call-to-actions.
- Contrast: #b7472a (Terracotta) - Depth and accents.

#### Typography
- Headers: DejaVu Serif Bold
- Body Text: DejaVu Sans""",

        "Desert Rose": """### Theme: Desert Rose
Identity: Sophisticated and muted. Ideal for high-end, elegant content.

#### Color Palette (60-30-10 Rule)
- Primary (60%): #e8d5c4 (Sand) - Earthy neutral base.
- Secondary (30%): #d4a5a5 (Dusty Rose) - Soft, professional secondary surfaces.
- Accent (10%): #5d2e46 (Deep Burgundy) - High-contrast text and links.

#### Typography
- Headers: FreeSans Bold
- Body Text: FreeSans""",

        "Forest Canopy": """### Theme: Forest Canopy
Identity: Grounded and stable. Inspired by deep woodland environments.

#### Color Palette (60-30-10 Rule)
- Primary (60%): #faf9f6 (Ivory) - Bright, natural canvas.
- Secondary (30%): #2d4a2b (Forest Green) - Strong, stable headings.
- Accent (10%): #7d8471 (Sage) - Soft UI elements and dividers.

#### Typography
- Headers: FreeSerif Bold
- Body Text: FreeSans""",

        "Golden Hour": """### Theme: Golden Hour
Identity: Inviting and warm. Designed for storytelling and hospitality.

#### Color Palette (60-30-10 Rule)
- Primary (60%): #d4b896 (Warm Beige) - Comforting background.
- Secondary (30%): #4a403a (Chocolate Brown) - Highly readable body text.
- Accent (10%): #f4a900 (Mustard Yellow) - Bold highlights.

#### Typography
- Headers: FreeSans Bold
- Body Text: FreeSans""",

        "Midnight Galaxy": """### Theme: Midnight Galaxy
Identity: Dramatic and high-impact. Uses cosmic tones for a modern edge.

#### Color Palette (60-30-10 Rule)
- Primary (60%): #2b1e3e (Deep Purple) - Immersive dark mode.
- Secondary (30%): #e6e6fa (Silver) - Crisp, luminous text.
- Accent (10%): #4a4e8f (Cosmic Blue) - Structural highlights.

#### Typography
- Headers: FreeSans Bold
- Body Text: FreeSans""",

        "Modern Minimalist": """### Theme: Modern Minimalist
Identity: High-end grayscale. Focuses on content over decoration.

#### Color Palette (60-30-10 Rule)
- Primary (60%): #ffffff (White) - Absolute clarity.
- Secondary (30%): #36454f (Charcoal) - Strong typography contrast.
- Accent (10%): #708090 (Slate Gray) - Subtle UI accents.

#### Typography
- Headers: DejaVu Sans Bold
- Body Text: DejaVu Sans""",

        "Ocean Depths": """### Theme: Ocean Depths
Identity: Calming and trustworthy. Professional maritime aesthetic.

#### Color Palette (60-30-10 Rule)
- Primary (60%): #1a2332 (Deep Navy) - Serious, deep background.
- Secondary (30%): #f1faee (Cream) - High-readability light text.
- Accent (10%): #2d8b8b (Teal) - Dynamic focal points.

#### Typography
- Headers: DejaVu Sans Bold
- Body Text: DejaVu Sans""",

        "Sunset Boulevard": """### Theme: Sunset Boulevard
Identity: Energetic and warm. Perfect for creative storytelling.

#### Color Palette (60-30-10 Rule)
- Primary (60%): #e9c46a (Warm Sand) - Vibrant, sunny canvas.
- Secondary (30%): #264653 (Deep Purple) - Strong contrast for text.
- Accent (10%): #e76f51 (Burnt Orange) - Passionate highlights.

#### Typography
- Headers: DejaVu Serif Bold
- Body Text: DejaVu Sans""",

        "Tech Innovation": """### Theme: Tech Innovation
Identity: Cutting-edge and high-contrast. Bold colors for modern tech.

#### Color Palette (60-30-10 Rule)
- Primary (60%): #F2F2F2 (Off-white) - Clean tech surface.
- Secondary (30%): #028090 (Teal) - Core brand color.
- Accent (10%): #02C39A (Mint) - Actionable elements.

#### Typography
- Headers: DejaVu Sans Bold
- Body Text: DejaVu Sans"""
    }
    
    return themes.get(theme_name, themes["Modern Minimalist"])