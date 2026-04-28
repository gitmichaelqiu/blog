import os
import re
import json
import subprocess
import shutil
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

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

def optimize_html_file(file_path, site_dir):
    with open(file_path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    soup = BeautifulSoup(html, 'html.parser')
    changed = False

    # 1. Optimize Math
    math_elements = soup.find_all(class_='arithmatex')
    for el in math_elements:
        text = el.get_text().strip()
        math_content = text
        math_content = re.sub(r'^(\\\(|\\\[|\s)+', '', math_content)
        math_content = re.sub(r'(\\\)|\\\]|\s)+$', '', math_content)
        is_block = (el.name == 'div') or text.strip().startswith('\\[')

        if math_content:
            rendered = render_katex(math_content, is_block)
            new_soup = BeautifulSoup(rendered, 'html.parser')
            el.replace_with(new_soup)
            changed = True

    # 2. Fix SVG paths
    # We resolve the relative path in <link href="..."> to an absolute path from site root
    # This ensures they work in SPA transitions and deep URL structures
    svg_links = soup.find_all('link', href=re.compile(r'\.svg$'))
    if svg_links:
        print(f"  Found {len(svg_links)} SVG links in {file_path}")
    for link_el in svg_links:
        orig_href = link_el['href']
        # Only resolve relative paths
        if not orig_href.startswith(('http', '/', '#')):
            rel_html_dir = os.path.dirname(os.path.relpath(file_path, site_dir))
            abs_svg_path = os.path.normpath(os.path.join(rel_html_dir, orig_href))
            new_href = '/' + abs_svg_path.replace(os.sep, '/')
            print(f"    Rewriting {orig_href} to {new_href}")
            link_el['href'] = new_href
            changed = True

    if changed:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(str(soup))
        return True
    return False

def copy_svg_assets():
    print("Syncing SVG assets...")
    docs_dir = 'docs'
    site_dir = 'site'
    for root, dirs, files in os.walk(docs_dir):
        for file in files:
            if file.endswith('.svg'):
                rel_path = os.path.relpath(os.path.join(root, file), docs_dir)
                dest_path = os.path.join(site_dir, rel_path)
                os.makedirs(os.path.dirname(dest_path), exist_ok=True)
                shutil.copy2(os.path.join(root, file), dest_path)
                print(f"  Copied {rel_path} to {dest_path}")

def main():
    site_dir = 'site'
    if not os.path.exists(site_dir):
        print(f"Directory {site_dir} not found.")
        return

    copy_svg_assets()

    count = 0
    for root, dirs, files in os.walk(site_dir):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                if optimize_html_file(file_path, site_dir):
                    count += 1
    
    print(f"Optimized {count} HTML files.")

if __name__ == "__main__":
    main()
