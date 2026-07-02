#!/usr/bin/env python3
"""Replace the navy-gradient icon placeholders in blog.html thumbnails with real topical photos."""
import re

BASE = 'https://images.unsplash.com/'
def u(pid):
    return f'{BASE}{pid}?crop=entropy&cs=srgb&fm=jpg&w=800&q=80&ixlib=rb-4.1.0'

# order matches the blog cards top-to-bottom (2 featured, then 10 posts)
URLS = [
    u('photo-1707902665498-a202981fb5ac'),  # F1  bookkeeper at desk (Strategy)
    u('photo-1586880244406-556ebe35f282'),  # F2  laptop (QuickBooks setup)
    u('photo-1542744095-291d1f67b221'),      # 1   laptop (Use QuickBooks Online)
    u('photo-1642043175009-5997b3a078d8'),  # 2   calculator+papers (Bookkeeping)
    u('photo-1586486855514-8c633cc6fd38'),  # 3   organized paperwork (Monthly checklist)
    u('photo-1707157284454-553ef0a4ed0d'),  # 4   desk + charts (Common mistakes)
    u('photo-1618044733300-9472054094ee'),  # 5   stock chart (Outsourcing)
    u('photo-1554224154-26032ffc0d07'),      # 6   tax documents (Tax season)
    u('photo-1560221328-12fe60f83ab8'),      # 7   monitor graph (P&L reports)
    u('photo-1711097383282-28097ae16b1d'),  # 8   paper over laptop (Cash flow)
    u('photo-1504868584819-f8e8b4b6d7e3'),  # 9   laptop (QuickBooks beginners)
    u('photo-1507208773393-40d9fc670acf'),  # 10  typing laptop (When to hire)
]

p = '/app/blog.html'
s = open(p, encoding='utf-8').read()

pat = re.compile(r'(<div class="blog-card-img"[^>]*>)\s*<span>.*?</span>\s*(<span class="blog-card-tag">)', re.DOTALL)
it = iter(URLS)
def repl(m):
    try:
        url = next(it)
    except StopIteration:
        return m.group(0)
    return f'{m.group(1)}<img src="{url}" alt="" loading="lazy">{m.group(2)}'

s, n = pat.subn(repl, s)
open(p, 'w', encoding='utf-8').write(s)
print(f'replaced {n} blog thumbnails with photos (had {len(URLS)} urls)')
