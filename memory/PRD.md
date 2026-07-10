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

- **Favicons generated** (2026-07-01): created `favicon-16.png`, `favicon-32.png`, `favicon-180.png`, `favicon.ico` from existing `favicon.png` (250×250) via `/app/scripts/gen_favicons.py`. All referenced files now resolve (200). To upgrade: drop a square 512×512 `favicon.png` in /assets and re-run the script.
- **Blog thumbnails → real photos** (2026-07-01): replaced all 12 navy-gradient icon placeholders in blog.html with topical photos via `/app/scripts/blog_images.py`. Now DOWNLOADED locally to `/assets/blog-01.jpg`..`blog-12.jpg` (self-contained, no external dependency); blog.html references local paths. Gold category tags overlaid; `.blog-card-img img` CSS added.
- **Copywriting pass** (2026-07-01): rewrote cliché marketing phrasing across index/about/services/blog/consultation into founder's plain, specific voice (kept SEO keywords + structure). Removed: "Finally Under Control", "off your plate", "The Smart Business Decision", "Peace of Mind", "financial clarity", "business you love", "no strings attached / pressure tactics". New hero: "Accurate Books. Numbers You Can Actually Use."
- **Google 5.0 trust chip** (2026-07-01): added a "5.0 on Google" chip (Google logo + gold stars) as a 5th trust-bar item in index.html — currently COMMENTED OUT/off. Enable once real reviews exist: remove the two comment wrapper lines and set GOOGLE_REVIEWS_URL. Styled via `.trust-google*` in styles.css. `data-testid="google-rating-chip"`.

## Backlog / Next
- **Key Dates ticker** (2026-07-01): added a football-styled (Notre Dame nod — owner is a former ND football player) scrolling ticker under the nav on all 10 pages. Navy band, gold "Game Plan" label w/ football icon, football separators; shows real tax/bookkeeping deadlines (Jan 15 / Jan 31 / Mar 15 / Apr 15 / Jun 15 / Sep 15 / Oct 15) + QuickBooks Certified + service-area items. CSS `.ticker*` in styles.css; markup inserted after `</header>`. Pauses on hover; respects prefers-reduced-motion. To edit items: update the ticker `<span class="ticker-item">`s in each HTML (or re-run a small script). NOTE: statutory dates shift to next business day on weekends/holidays — review annually.
- P1: Owner to provide real Google Business Profile links → replace `GOOGLE_WRITE_REVIEW_URL` / `GOOGLE_REVIEWS_URL` in index.html. (Owner sourcing as of 2026-07-01.)
- P2: Blog thumbnails are hotlinked from Unsplash CDN — optionally download into /assets for full self-containment (esp. if going offline/behind firewall).
- P2: Tighten marketing-cliché copy ("takes the burden off your plate", "peace of mind", "The Smart Business Decision") into founder's real voice.
- P2: Consider more DC/office photography (hero, blog) if owner likes the dc-skyline direction.
