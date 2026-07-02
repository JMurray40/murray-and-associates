#!/usr/bin/env python3
"""Generate the favicon variants referenced in the HTML from assets/favicon.png."""
from PIL import Image
src = Image.open('/app/assets/favicon.png').convert('RGBA')
for size, name in [(16, 'favicon-16.png'), (32, 'favicon-32.png'), (180, 'favicon-180.png')]:
    src.resize((size, size), Image.LANCZOS).save(f'/app/assets/{name}')
# multi-size .ico
src.save('/app/assets/favicon.ico', sizes=[(16, 16), (32, 32), (48, 48)])
print('generated favicon-16.png, favicon-32.png, favicon-180.png, favicon.ico')
