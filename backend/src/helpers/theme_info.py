from pydantic import BaseModel, Field
from typing import Literal

def get_theme_info(theme_name: str) -> str:
    themes = {

        "Obsidian Pro": """### Theme: Obsidian Pro
Identity: Ultra-dark, ultra-premium. Built for high-impact executive decks and tech keynotes.

#### CSS Background
background: linear-gradient(135deg, #0a0a0f 0%, #12121f 50%, #0d0d1a 100%);

#### Colors
- Text (primary): #f0f0f8
- Text (secondary / muted): rgba(240,240,248,0.55)
- Accent: #6366f1  (Indigo Electric)
- Accent glow: rgba(99,102,241,0.25)
- Card surface: rgba(255,255,255,0.05)
- Card border: rgba(255,255,255,0.09)
- Divider: rgba(255,255,255,0.08)

#### Typography (Google Fonts)
- Headings: 'Plus Jakarta Sans', sans-serif — weight 800
- Body: 'Inter', sans-serif — weight 300/400
- Eyebrow labels: uppercase, letter-spacing 3-4px, accent color, opacity 0.65""",


        "Glacier Light": """### Theme: Glacier Light
Identity: Clean, airy, and confident. Ideal for corporate, finance, and health decks.

#### CSS Background
background: linear-gradient(160deg, #f0f4ff 0%, #e6ecff 60%, #dce6ff 100%);

#### Colors
- Text (primary): #0f172a
- Text (secondary / muted): rgba(15,23,42,0.55)
- Accent: #3b82f6  (Sky Blue)
- Accent surface: rgba(59,130,246,0.10)
- Card surface: rgba(255,255,255,0.80)
- Card border: rgba(59,130,246,0.12)
- Divider: rgba(15,23,42,0.08)

#### Typography (Google Fonts)
- Headings: 'Inter', sans-serif — weight 800
- Body: 'Inter', sans-serif — weight 400
- Eyebrow labels: uppercase, letter-spacing 3px, #3b82f6, opacity 0.7""",


        "Aurora Dark": """### Theme: Aurora Dark
Identity: Cosmic and creative. Vivid purple-to-green gradient for innovation and AI decks.

#### CSS Background
background: linear-gradient(135deg, #0f0c29 0%, #302b63 45%, #1a3a2a 100%);

#### Colors
- Text (primary): #e8fff5
- Text (secondary / muted): rgba(232,255,245,0.55)
- Accent: #10b981  (Emerald)
- Accent glow: rgba(16,185,129,0.22)
- Card surface: rgba(255,255,255,0.06)
- Card border: rgba(16,185,129,0.18)
- Divider: rgba(255,255,255,0.09)

#### Typography (Google Fonts)
- Headings: 'Space Grotesk', sans-serif — weight 700
- Body: 'Inter', sans-serif — weight 300
- Eyebrow labels: uppercase, letter-spacing 4px, #10b981, opacity 0.7""",


        "Ember Slate": """### Theme: Ember Slate
Identity: Moody, bold, and warm. Great for creative agencies, design, and startup pitches.

#### CSS Background
background: linear-gradient(135deg, #1c1410 0%, #2d1b0e 50%, #1a1208 100%);

#### Colors
- Text (primary): #fff7ed
- Text (secondary / muted): rgba(255,247,237,0.55)
- Accent: #f97316  (Coral Orange)
- Accent glow: rgba(249,115,22,0.22)
- Card surface: rgba(255,255,255,0.06)
- Card border: rgba(249,115,22,0.18)
- Divider: rgba(255,255,255,0.08)

#### Typography (Google Fonts)
- Headings: 'Plus Jakarta Sans', sans-serif — weight 800
- Body: 'DM Sans', sans-serif — weight 300/400
- Eyebrow labels: uppercase, letter-spacing 3px, #f97316, opacity 0.65""",


        "Arctic Frost": """### Theme: Arctic Frost
Identity: Crisp, precise, and minimal. Built for data, analytics, and consulting decks.

#### CSS Background
background: linear-gradient(160deg, #f8faff 0%, #eef4ff 100%);

#### Colors
- Text (primary): #0c1a3a
- Text (secondary / muted): rgba(12,26,58,0.50)
- Accent: #0ea5e9  (Cyan Blue)
- Accent surface: rgba(14,165,233,0.10)
- Card surface: rgba(255,255,255,0.90)
- Card border: rgba(14,165,233,0.14)
- Divider: rgba(12,26,58,0.07)

#### Typography (Google Fonts)
- Headings: 'Inter', sans-serif — weight 800
- Body: 'Inter', sans-serif — weight 400
- Eyebrow labels: uppercase, letter-spacing 4px, #0ea5e9, opacity 0.65""",


        "Midnight Galaxy": """### Theme: Midnight Galaxy
Identity: Rich deep-space aesthetic. Ultra-premium for product launches and tech keynotes.

#### CSS Background
background: linear-gradient(135deg, #0d0221 0%, #1a0545 50%, #0a0a2e 100%);

#### Colors
- Text (primary): #e8e4ff
- Text (secondary / muted): rgba(232,228,255,0.52)
- Accent: #a855f7  (Vivid Violet)
- Accent glow: rgba(168,85,247,0.28)
- Card surface: rgba(255,255,255,0.06)
- Card border: rgba(168,85,247,0.20)
- Divider: rgba(255,255,255,0.09)

#### Typography (Google Fonts)
- Headings: 'Space Grotesk', sans-serif — weight 700
- Body: 'Inter', sans-serif — weight 300
- Eyebrow labels: uppercase, letter-spacing 4px, #a855f7, opacity 0.65""",


        "Forest Executive": """### Theme: Forest Executive
Identity: Trustworthy, grounded, and premium. Ideal for sustainability, healthcare, and NGO decks.

#### CSS Background
background: linear-gradient(135deg, #071a10 0%, #0d2b18 50%, #061208 100%);

#### Colors
- Text (primary): #ecfdf5
- Text (secondary / muted): rgba(236,253,245,0.52)
- Accent: #34d399  (Mint Green)
- Accent glow: rgba(52,211,153,0.22)
- Card surface: rgba(255,255,255,0.05)
- Card border: rgba(52,211,153,0.16)
- Divider: rgba(255,255,255,0.08)

#### Typography (Google Fonts)
- Headings: 'DM Sans', sans-serif — weight 700
- Body: 'Inter', sans-serif — weight 400
- Eyebrow labels: uppercase, letter-spacing 3px, #34d399, opacity 0.65""",


        "Solar Flare": """### Theme: Solar Flare
Identity: Energetic and warm. Perfect for marketing, growth, and sales decks.

#### CSS Background
background: linear-gradient(135deg, #1a0a00 0%, #2d1200 50%, #1a0800 100%);

#### Colors
- Text (primary): #fff8f0
- Text (secondary / muted): rgba(255,248,240,0.52)
- Accent: #f59e0b  (Amber Gold)
- Accent glow: rgba(245,158,11,0.25)
- Card surface: rgba(255,255,255,0.06)
- Card border: rgba(245,158,11,0.18)
- Divider: rgba(255,255,255,0.08)

#### Typography (Google Fonts)
- Headings: 'Plus Jakarta Sans', sans-serif — weight 800
- Body: 'Inter', sans-serif — weight 400
- Eyebrow labels: uppercase, letter-spacing 3px, #f59e0b, opacity 0.65""",


        "Ocean Depths": """### Theme: Ocean Depths
Identity: Calm, authoritative, and trustworthy. Built for finance, strategy, and leadership decks.

#### CSS Background
background: linear-gradient(135deg, #020d18 0%, #051f35 50%, #031627 100%);

#### Colors
- Text (primary): #e0f2fe
- Text (secondary / muted): rgba(224,242,254,0.52)
- Accent: #38bdf8  (Sky Teal)
- Accent glow: rgba(56,189,248,0.22)
- Card surface: rgba(255,255,255,0.05)
- Card border: rgba(56,189,248,0.16)
- Divider: rgba(255,255,255,0.08)

#### Typography (Google Fonts)
- Headings: 'Inter', sans-serif — weight 800
- Body: 'Inter', sans-serif — weight 300/400
- Eyebrow labels: uppercase, letter-spacing 4px, #38bdf8, opacity 0.65""",


        "Modern Minimalist": """### Theme: Modern Minimalist
Identity: Pure white canvas with high contrast. Lets content speak. Ideal for all-purpose professional decks.

#### CSS Background
background: linear-gradient(160deg, #ffffff 0%, #f4f6f9 100%);

#### Colors
- Text (primary): #111827
- Text (secondary / muted): rgba(17,24,39,0.50)
- Accent: #6366f1  (Indigo)
- Accent surface: rgba(99,102,241,0.09)
- Card surface: rgba(255,255,255,0.95)
- Card border: rgba(99,102,241,0.12)
- Divider: rgba(17,24,39,0.07)

#### Typography (Google Fonts)
- Headings: 'Inter', sans-serif — weight 800
- Body: 'Inter', sans-serif — weight 400
- Eyebrow labels: uppercase, letter-spacing 3px, #6366f1, opacity 0.65""",

        "Neon Cyberpunk": """### Theme: Neon Cyberpunk
Identity: High-energy, futuristic, and edgy. Perfect for gaming, Web3, and disruptive tech decks.

#### CSS Background
background: linear-gradient(135deg, #050510 0%, #0d0d2b 50%, #050510 100%);

#### Colors
- Text (primary): #f0f0ff
- Text (secondary / muted): rgba(240,240,255,0.52)
- Accent: #00f5d4  (Neon Cyan)
- Accent glow: rgba(0,245,212,0.28)
- Card surface: rgba(0,245,212,0.05)
- Card border: rgba(0,245,212,0.18)
- Divider: rgba(0,245,212,0.12)

#### Typography (Google Fonts)
- Headings: 'Space Grotesk', sans-serif — weight 700
- Body: 'Inter', sans-serif — weight 300
- Eyebrow labels: uppercase, letter-spacing 4px, #00f5d4, opacity 0.7""",


        "Rose Quartz": """### Theme: Rose Quartz
Identity: Soft, warm, and elegant. Ideal for lifestyle, beauty, wellness, and fashion decks.

#### CSS Background
background: linear-gradient(160deg, #fff5f7 0%, #ffe4ec 60%, #ffd6e8 100%);

#### Colors
- Text (primary): #2d0a1a
- Text (secondary / muted): rgba(45,10,26,0.52)
- Accent: #e91e8c  (Hot Rose)
- Accent surface: rgba(233,30,140,0.09)
- Card surface: rgba(255,255,255,0.82)
- Card border: rgba(233,30,140,0.14)
- Divider: rgba(45,10,26,0.07)

#### Typography (Google Fonts)
- Headings: 'DM Sans', sans-serif — weight 700
- Body: 'Inter', sans-serif — weight 400
- Eyebrow labels: uppercase, letter-spacing 3px, #e91e8c, opacity 0.65""",


        "Slate Steel": """### Theme: Slate Steel
Identity: Industrial, neutral, and no-nonsense. Great for engineering, B2B SaaS, and operations decks.

#### CSS Background
background: linear-gradient(160deg, #1a1f2e 0%, #232a3b 60%, #1a1f2e 100%);

#### Colors
- Text (primary): #e2e8f0
- Text (secondary / muted): rgba(226,232,240,0.52)
- Accent: #94a3b8  (Steel Silver)
- Accent glow: rgba(148,163,184,0.20)
- Card surface: rgba(255,255,255,0.05)
- Card border: rgba(148,163,184,0.18)
- Divider: rgba(255,255,255,0.08)

#### Typography (Google Fonts)
- Headings: 'Inter', sans-serif — weight 800
- Body: 'Inter', sans-serif — weight 400
- Eyebrow labels: uppercase, letter-spacing 4px, #94a3b8, opacity 0.65""",


        "Tropical Punch": """### Theme: Tropical Punch
Identity: Bold, vibrant, and playful. Perfect for consumer apps, social media, and Gen-Z audience decks.

#### CSS Background
background: linear-gradient(135deg, #0d2137 0%, #0a1a2e 40%, #1a0d2e 100%);

#### Colors
- Text (primary): #fff0f8
- Text (secondary / muted): rgba(255,240,248,0.52)
- Accent: #ff6b9d  (Vibrant Pink)
- Accent glow: rgba(255,107,157,0.28)
- Card surface: rgba(255,255,255,0.06)
- Card border: rgba(255,107,157,0.20)
- Divider: rgba(255,255,255,0.09)

#### Typography (Google Fonts)
- Headings: 'Plus Jakarta Sans', sans-serif — weight 800
- Body: 'DM Sans', sans-serif — weight 400
- Eyebrow labels: uppercase, letter-spacing 3px, #ff6b9d, opacity 0.65""",


        "Crimson Noir": """### Theme: Crimson Noir
Identity: Dramatic, intense, and sophisticated. Ideal for finance, law, luxury brand, and leadership decks.

#### CSS Background
background: linear-gradient(135deg, #0f0006 0%, #200010 50%, #0a0003 100%);

#### Colors
- Text (primary): #fff0f2
- Text (secondary / muted): rgba(255,240,242,0.52)
- Accent: #e11d48  (Crimson Red)
- Accent glow: rgba(225,29,72,0.25)
- Card surface: rgba(255,255,255,0.05)
- Card border: rgba(225,29,72,0.18)
- Divider: rgba(255,255,255,0.08)

#### Typography (Google Fonts)
- Headings: 'Plus Jakarta Sans', sans-serif — weight 800
- Body: 'Inter', sans-serif — weight 300/400
- Eyebrow labels: uppercase, letter-spacing 4px, #e11d48, opacity 0.65""",

    }

    return themes.get(theme_name, themes["Modern Minimalist"])
