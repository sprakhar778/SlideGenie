THEME_PROMPT = """
You are a design strategist. Based on the topic and content below, select the single best theme for the presentation.
Return the result in JSON format.
## Topic:
{topic}

## Content:
{content}

## Available Themes:

### Dark Themes
1.  Obsidian Pro      — Ultra-dark indigo. Executive, tech keynotes, product launches.
2.  Midnight Galaxy   — Deep-space violet. Space, gaming, high-impact storytelling.
3.  Aurora Dark       — Purple-to-green cosmic. AI, innovation, research decks.
4.  Ember Slate       — Dark warm brown + orange. Creative agencies, startups, design pitches.
5.  Forest Executive  — Dark forest green + mint. Sustainability, healthcare, NGO decks.
6.  Ocean Depths      — Deep navy + sky teal. Finance, strategy, leadership, consulting.
7.  Solar Flare       — Dark burnt sienna + amber. Marketing, growth, sales decks.
8.  Neon Cyberpunk    — Near-black + neon cyan. Web3, gaming, disruptive tech.
9.  Tropical Punch    — Dark navy + vibrant pink. Consumer apps, social, Gen-Z audience.
10. Crimson Noir      — Near-black + crimson red. Law, luxury, finance, leadership.
11. Slate Steel       — Dark slate + silver. Engineering, B2B SaaS, operations.

### Light Themes
12. Glacier Light     — Soft blue-white gradient. Corporate, finance, health decks.
13. Arctic Frost      — Ice-white + cyan. Data, analytics, scientific, pharma decks.
14. Modern Minimalist — Pure white + indigo. All-purpose professional, architecture, portfolios.
15. Rose Quartz       — Pale pink gradient + hot rose. Lifestyle, beauty, wellness, fashion.

## Instructions:
- Consider the topic, audience, and emotional tone.
- Dark themes suit tech, innovation, drama, and impact.
- Light themes suit corporate, clinical, minimalist, or elegant contexts.
- Output ONLY the theme name exactly as listed above (e.g. `Ocean Depths`). No explanation, no punctuation.

Return JSON only:

{{
 "theme": "theme name"
}}
"""