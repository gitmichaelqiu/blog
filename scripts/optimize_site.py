import os
import re
import json
import subprocess
from bs4 import BeautifulSoup

def render_katex(source, is_block):
    js_code = f"""
const katex = require('katex');
try {{
    const html = katex.renderToString({json.dumps(source)}, {{
        displayMode: {str(is_block).lower()},
        throwOnError: false
    }});
    process.stdout.write(html);
}} catch (e) {{
    process.stderr.write(e.message);
    process.exit(1);
}}
"""
    try:
        result = subprocess.run(
            ['node', '-e', js_code],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except Exception as e:
        print(f"Error rendering KaTeX: {e}")
        return source

def optimize_html_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    soup = BeautifulSoup(html, 'html.parser')
    changed = False

    # Find all arithmatex spans and divs
    # pymdownx.arithmatex with generic=true outputs \(...\) or \[...\]
    math_elements = soup.find_all(class_='arithmatex')
    for el in math_elements:
        text = el.get_text().strip()
        is_block = False
        math_content = ""

        if text.startswith('\\(') and text.endswith('\\)'):
            math_content = text[2:-2].strip()
            is_block = False
        elif text.startswith('\\[') and text.endswith('\\]'):
            math_content = text[2:-2].strip()
            is_block = True
        elif el.name == 'div':
            math_content = text
            is_block = True
        else:
            # Fallback for other formats
            math_content = text
            is_block = (el.name == 'div')

        if math_content:
            rendered = render_katex(math_content, is_block)
            new_soup = BeautifulSoup(rendered, 'html.parser')
            el.replace_with(new_soup)
            changed = True

    if changed:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(str(soup))
        return True
    return False

def main():
    site_dir = 'site'
    if not os.path.exists(site_dir):
        print(f"Directory {site_dir} not found.")
        return

    count = 0
    for root, dirs, files in os.walk(site_dir):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                print(f"Processing {file_path}...")
                if optimize_html_file(file_path):
                    count += 1
    
    print(f"Optimized {count} HTML files.")

if __name__ == "__main__":
    main()
