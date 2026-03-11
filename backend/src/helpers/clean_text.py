import re
def clean_html_output(text: str) -> str:
    # This regex removes ```html at the start and ``` at the end
    cleaned = re.sub(r'^```html\s*|^```\s*', '', text, flags=re.MULTILINE)
    cleaned = re.sub(r'```\s*$', '', cleaned, flags=re.MULTILINE)
    return cleaned.strip()