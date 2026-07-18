document.addEventListener('DOMContentLoaded', () => {
  // Mobile Nav Toggle
  const toggle = document.getElementById('navToggle');
  const menu = document.getElementById('navMenu');
  if (toggle && menu) {
    toggle.addEventListener('click', () => {
      const isOpen = menu.classList.toggle('open');
      toggle.setAttribute('aria-expanded', isOpen);
    });
    // Close menu when a link is clicked
    menu.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', () => {
        menu.classList.remove('open');
        toggle.setAttribute('aria-expanded', false);
      });
    });
  }

  // Dynamic Ticker Injection
  const tickerPlaceholder = document.getElementById('ticker-placeholder');
  if (tickerPlaceholder) {
    const footballSvg = `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M2.5 12c2.5-4.5 16.5-4.5 19 0-2.5 4.5-16.5 4.5-19 0Z"/><path d="M8.5 12h7"/><path d="M10 10.5v3"/><path d="M12 10.5v3"/><path d="M14 10.5v3"/></svg>`;
    const sep = `<span class="ticker-sep">${footballSvg}</span>`;
    const items = [
      `<span class="ticker-item"><span class="date">Jan 15</span> — Q4 estimated taxes due</span>`,
      `<span class="ticker-item"><span class="date">Jan 31</span> — 1099-NEC &amp; W-2 forms due</span>`,
      `<span class="ticker-item"><span class="date">Mar 15</span> — S-corp &amp; partnership returns due</span>`,
      `<span class="ticker-item"><span class="date">Apr 15</span> — Individual &amp; C-corp returns + Q1 estimated taxes</span>`,
      `<span class="ticker-item"><span class="date">Jun 15</span> — Q2 estimated taxes due</span>`,
      `<span class="ticker-item"><span class="date">Sep 15</span> — Q3 estimated taxes due</span>`,
      `<span class="ticker-item"><span class="date">Oct 15</span> — Extended individual returns due</span>`,
      `<span class="ticker-item">QuickBooks Certified ProAdvisor</span>`,
      `<span class="ticker-item">Serving Washington DC &amp; all 50 states</span>`
    ];
    const tickerContent = items.join(sep);
    tickerPlaceholder.outerHTML = `
      <div class="ticker" aria-label="Key financial and tax deadlines">
        <span class="ticker-label">${footballSvg} Game Plan</span>
        <div class="ticker-viewport">
          <div class="ticker-track">
            <span class="ticker-set">${tickerContent}</span>
            <span class="ticker-set" aria-hidden="true">${tickerContent}</span>
          </div>
        </div>
      </div>
    `;
  }
});
