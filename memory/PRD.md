# Murray & Associates — Website De-"AI" Refresh

Static marketing site (plain HTML/CSS, no build step). Bookkeeping/accounting firm, Washington DC + remote nationwide. Notre Dame navy (#0C2340) + gold (#C99700) palette. Live at murray-and-associates.us; source also in this repo.

## Goal
Make the site feel custom/professional (remove "AI-made" tells) WITHOUT changing the navy/gold vibe.

## Done
- **Emoji → SVG line icons** (2026-07-01): Replaced all ~30 emoji-as-icons across every page (trust bar, service cards, benefits, QuickBooks section, About credentials/values, contact info, footers, blog cards, blog-article callouts) with consistent Lucide-style stroke icons. Also converted 2 decorative CSS emojis (`.location-tag::before` pin, `.remote-box::after` globe) to inline-SVG data URIs. Icons use `width:1em` + `currentColor`; colors set per container in styles.css. Kept `★` rating glyphs and `✓` checkmarks (intentional, monochrome).
- **Number inconsistencies fixed**: Years of experience standardized to 20+ (was 10+ on home). Consultation length standardized to 15 min (was 30 on services page + one meta).
- **Removed inflated "100+" claims**: dropped hero stat "100+ Small Businesses Served" and trust-bar "Trusted by 100+ Businesses" (per owner: count included non-M&A clients).
- **Testimonials → Google Reviews badge**: placeholder fake testimonials removed; replaced with a Google Reviews badge card (`data-testid="google-reviews-badge"`) in index.html. Contains TWO placeholder links to swap later: `GOOGLE_WRITE_REVIEW_URL`, `GOOGLE_REVIEWS_URL`. A commented-out `.testimonials-grid` TEMPLATE is kept in that same section for pasting real testimonials in future (see HTML comments in index.html reviews section).
- **DC photo**: added real Washington DC aerial (Capitol/National Mall) at `/assets/dc-skyline.jpg`, placed in the "Washington DC & Beyond" Service Area section (`.area-photo`).

## Helper scripts
- `/app/scripts/replace_icons.py` — emoji→SVG mapping + copy fixes (idempotent-ish; re-run safe).
- `/app/scripts/reviews.py` — one-time testimonials→Google badge swap.

## Backlog / Next
- P1: Owner to provide real Google Business Profile links → replace `GOOGLE_WRITE_REVIEW_URL` / `GOOGLE_REVIEWS_URL` in index.html.
- P1: Missing favicon variants referenced but absent: `favicon.ico`, `favicon-16.png`, `favicon-32.png`, `favicon-180.png` (only `favicon.png` exists). Either add files or update the `<link rel="icon">` tags.
- P2: Blog card thumbnails still navy gradients — optionally swap for real/topical imagery.
- P2: Tighten marketing-cliché copy ("takes the burden off your plate", "peace of mind", "The Smart Business Decision") into founder's real voice.
- P2: Consider more DC/office photography (hero, blog) if owner likes the dc-skyline direction.
