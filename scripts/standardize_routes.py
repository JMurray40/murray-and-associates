#!/usr/bin/env python3
import os
import re

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

FILES_TO_PROCESS = [
    'index.html',
    'about.html',
    'services.html',
    'contact.html',
    'consultation.html',
    'privacy-policy.html',
    'terms.html'
]

def clean_links(html):
    pattern = r'href=["\'](index|about|services|blog|contact|consultation|privacy-policy|terms|blog-[a-zA-Z0-9\-]+)\.html(#[a-zA-Z0-9\-]+)?["\']'
    
    def repl(match):
        page = match.group(1)
        anchor = match.group(2) or ""
        if page == 'index':
            return f'href="/{anchor}"'
        else:
            return f'href="/{page}{anchor}"'
            
    return re.sub(pattern, repl, html)

def process_files():
    print("Standardizing routes and layout components...")
    
    for filename in FILES_TO_PROCESS:
        path = os.path.join(ROOT_DIR, filename)
        if not os.path.exists(path):
            print(f"Warning: File {filename} not found.")
            continue
            
        with open(path, 'r', encoding='utf-8') as f:
            html = f.read()
            
        # 1. Clean links
        html = clean_links(html)
        
        # 2. Replace static key dates ticker with placeholder div
        html = re.sub(
            r'<div class="ticker".*?</div>\s*</div>\s*</div>', 
            '<div id="ticker-placeholder"></div>', 
            html, 
            flags=re.DOTALL
        )
        
        # 3. Replace navigation toggle script at the bottom with js/main.js defer
        html = re.sub(
            r'<!-- Navigation toggle script -->\s*<script>.*?</script>', 
            '<script src="/js/main.js" defer></script>', 
            html, 
            flags=re.DOTALL
        )
        
        # 4. Enable Google Reviews rating chip in index.html
        if filename == 'index.html':
            google_chip_html = """<div class="trust-item trust-google" data-testid="google-rating-chip">
            <span class="trust-icon"><svg viewBox="0 0 48 48" width="1em" height="1em" aria-hidden="true" focusable="false"><path fill="#EA4335" d="M24 9.5c3.54 0 6.71 1.22 9.21 3.6l6.85-6.85C35.9 2.38 30.47 0 24 0 14.62 0 6.51 5.38 2.56 13.22l7.98 6.19C12.43 13.72 17.74 9.5 24 9.5z"/><path fill="#4285F4" d="M46.98 24.55c0-1.57-.15-3.09-.38-4.55H24v9.02h12.94c-.58 2.96-2.26 5.48-4.78 7.18l7.73 6c4.51-4.18 7.09-10.36 7.09-17.65z"/><path fill="#FBBC05" d="M10.53 28.59c-.48-1.45-.76-2.99-.76-4.59s.27-3.14.76-4.59l-7.98-6.19C.92 16.46 0 20.12 0 24c0 3.88.92 7.54 2.56 10.78l7.97-6.19z"/><path fill="#34A853" d="M24 48c6.48 0 11.93-2.13 15.89-5.81l-7.73-6c-2.15 1.45-4.92 2.3-8.16 2.3-6.26 0-11.57-4.22-13.47-9.91l-7.98 6.19C6.51 42.62 14.62 48 24 48z"/></svg></span>
            <a href="https://g.page/r/CYoVScCmvh3-EAI/review" target="_blank" rel="noopener" style="text-decoration: none; color: inherit; display: inline-flex; align-items: center; gap: 4px;">
              <strong>5.0 on Google</strong>
              <span class="trust-google-stars" style="color: var(--gold); font-size: 0.85rem; display: inline-flex; gap: 1px;">★★★★★</span>
            </a>
          </div>"""
            html = re.sub(
                r'<!-- Google 5.0 rating chip can be added here once real reviews exist. -->', 
                google_chip_html, 
                html
            )
            
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"Processed: {filename}")
        
    print("Standardization of pages complete!")

if __name__ == '__main__':
    process_files()
