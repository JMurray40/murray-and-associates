#!/usr/bin/env python3
"""Replace the placeholder testimonials section in index.html with a Google Reviews badge."""
p = '/app/index.html'
s = open(p, encoding='utf-8').read()

start_marker = '<!-- ============================================================\n         TESTIMONIALS'
i = s.find(start_marker)
assert i != -1, 'testimonials comment not found'
# find enclosing section end (first </section> after the testimonials heading)
j = s.find('</section>', i)
assert j != -1
j += len('</section>')

google_g = ('<svg viewBox="0 0 48 48" width="30" height="30" aria-hidden="true" focusable="false">'
            '<path fill="#EA4335" d="M24 9.5c3.54 0 6.71 1.22 9.21 3.6l6.85-6.85C35.9 2.38 30.47 0 24 0 14.62 0 6.51 5.38 2.56 13.22l7.98 6.19C12.43 13.72 17.74 9.5 24 9.5z"/>'
            '<path fill="#4285F4" d="M46.98 24.55c0-1.57-.15-3.09-.38-4.55H24v9.02h12.94c-.58 2.96-2.26 5.48-4.78 7.18l7.73 6c4.51-4.18 7.09-10.36 7.09-17.65z"/>'
            '<path fill="#FBBC05" d="M10.53 28.59c-.48-1.45-.76-2.99-.76-4.59s.27-3.14.76-4.59l-7.98-6.19C.92 16.46 0 20.12 0 24c0 3.88.92 7.54 2.56 10.78l7.97-6.19z"/>'
            '<path fill="#34A853" d="M24 48c6.48 0 11.93-2.13 15.89-5.81l-7.73-6c-2.15 1.45-4.92 2.3-8.16 2.3-6.26 0-11.57-4.22-13.47-9.91l-7.98 6.19C6.51 42.62 14.62 48 24 48z"/>'
            '</svg>')
star = ('<svg width="1em" height="1em" viewBox="0 0 24 24" fill="currentColor" stroke="none" aria-hidden="true">'
        '<polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>')

new = '''<!-- ============================================================
         REVIEWS — Google Reviews badge
         ------------------------------------------------------------
         HOW TO UPDATE WHEN YOU HAVE REVIEWS:
         1. GOOGLE LINKS: replace the two placeholders below with your
            real links from your Google Business Profile dashboard:
              GOOGLE_WRITE_REVIEW_URL  -> your "leave a review" short link
              GOOGLE_REVIEWS_URL       -> your public reviews page
         2. WRITTEN TESTIMONIALS: when you collect genuine client quotes,
            copy the commented-out <div class="testimonials-grid"> TEMPLATE
            at the bottom of this section, fill in the real quote / name /
            business, and move it out of the comment (delete the wrappers).
            You can keep the Google badge above it or remove it.
         ============================================================ -->
    <section class="section" aria-labelledby="reviews-heading">
      <div class="container">
        <div class="section-header centered">
          <span class="section-label">Reviews</span>
          <h2 id="reviews-heading">Building Our Reputation, One Client at a Time</h2>
          <div class="divider-gold"></div>
          <p>We're a growing firm and we let our work speak for itself. If we've helped your business, we'd be grateful for a review — and if you're considering us, you can read verified feedback on Google.</p>
        </div>

        <div class="reviews-badge" data-testid="google-reviews-badge">
          <div class="reviews-badge-google">
            ''' + google_g + '''
            <span>Google Reviews</span>
          </div>
          <div class="reviews-badge-stars" aria-hidden="true">
            ''' + (star * 5) + '''
          </div>
          <p class="reviews-badge-note">Verified client reviews appear here. Be the first to share your experience working with Murray &amp; Associates.</p>
          <div class="reviews-badge-actions">
            <a href="GOOGLE_WRITE_REVIEW_URL" target="_blank" rel="noopener" class="btn btn-primary btn-arrow" data-testid="write-google-review-btn">Leave a Google Review</a>
            <a href="GOOGLE_REVIEWS_URL" target="_blank" rel="noopener" class="btn btn-outline-navy" data-testid="read-google-reviews-btn">Read Our Reviews</a>
          </div>
        </div>

        <!-- ============================================================
             TESTIMONIALS TEMPLATE — currently hidden (no reviews yet).
             When you have real testimonials, duplicate a card, replace the
             placeholder text/name/business, then move this grid OUT of the
             comment by deleting this opening line and the closing line below.
        <div class="testimonials-grid">
          <div class="testimonial-card">
            <div class="testimonial-stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
            <p class="testimonial-text">"Paste a genuine client quote here."</p>
            <div class="testimonial-author">
              <div class="author-avatar">AB</div>
              <div>
                <div class="author-name">Full Name</div>
                <div class="author-biz">Business Name &middot; City, ST</div>
              </div>
            </div>
          </div>
        </div>
             ============================================================ -->
      </div>
    </section>'''

s = s[:i] + new + s[j:]
open(p, 'w', encoding='utf-8').write(s)
print('testimonials section replaced with Google Reviews badge')
