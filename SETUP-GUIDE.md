# Murray & Associates — Website Setup Guide
## Complete Instructions for Launch, Hosting & Integrations

---

## 📁 FILE STRUCTURE

```
murray-associates/
├── index.html          ← Homepage
├── about.html          ← About page
├── services.html       ← All services (with anchor links)
├── contact.html        ← Contact form
├── consultation.html   ← Book a consultation + Calendly placeholder
├── blog.html           ← Blog / Resources page
├── styles.css          ← All design styles (edit colors here)
└── assets/             ← CREATE this folder for your images
    ├── logo.png        ← Your business logo (optional)
    ├── logo-dark.png   ← Dark version of logo (optional)
    ├── favicon.png     ← Browser tab icon
    └── team-photo.jpg  ← Team or office photo (for About page)
```

---

## 🎨 CUSTOMIZING THE DESIGN

### Changing Colors
Open `styles.css` and find the `:root` block at the top (line ~25).
Edit these variables to change the color scheme:

```css
:root {
  --navy:   #0C2340;   /* Main navy — Notre Dame blue */
  --gold:   #C99700;   /* Gold accent */
  --white:  #FFFFFF;   /* Background */
}
```

### Adding Your Logo
**Option 1 — Image logo** (recommended):
1. Place your logo file in the `/assets/` folder as `logo.png`
2. In each HTML file, find the `<!-- OPTION 1 -->` comment in the `<nav>` section
3. Uncomment the `<img>` tag and comment out the text logo
4. Adjust the `.logo-img` height in CSS if needed (default: 48px)

**Option 2 — Text logo** (default, no image needed):
The "M&A" icon shield + firm name text shows by default.
Edit the text in the `.logo-icon` and `.logo-text` spans within each nav.

---

## 📝 ESSENTIAL TEXT EDITS (before launch)

Search each file for `EDIT:` comments. Key items to update:

| Item | Location | What to change |
|------|----------|----------------|
| Phone number | All footers + contact.html | (202) 555-0100 |
| Email address | All footers + contact.html | info@murrayandassociates.com |
| Website URL | `<link rel="canonical">` in each page | Your actual domain |
| Hero stats | index.html hero section | Your real experience numbers |
| Testimonials | index.html testimonials section | Real client quotes |
| About story | about.html | Your actual company story |
| Credentials | about.html | Your real certifications |
| Copyright year | All footers | Current year |
| Social links | index.html footer | Your LinkedIn/Facebook URLs |

---

## 🌐 UPLOADING TO IONOS (or any web host)

### Step 1: Purchase hosting
- Go to ionos.com and purchase a hosting plan (Starter or Essential works)
- Register your domain (e.g., murrayandassociates.com)

### Step 2: Access File Manager
- Log in to your IONOS control panel
- Click "Websites & Stores" → Select your domain → "File Manager"
- Or use FTP (FileZilla is a free FTP client)

### Step 3: Upload files
- Navigate to the `/htdocs/` or `/public_html/` folder
- Upload ALL files: index.html, about.html, services.html, contact.html, consultation.html, blog.html, styles.css
- Create an `/assets/` subfolder and upload your logo and images

### Step 4: Test your site
- Visit your domain in a browser
- Check all navigation links work
- Test on mobile (resize browser window)
- Verify forms display correctly

### Step 5: SSL Certificate
- In IONOS, enable the free SSL certificate (HTTPS)
- This is required for Google ranking and user trust

---

## 📅 SETTING UP CALENDLY (Consultation Booking)

### Step 1: Create Calendly account
- Go to calendly.com → Sign up free
- Choose "30-Minute Meeting" template

### Step 2: Configure your event
- Name it "Free Bookkeeping Consultation"
- Set your available hours (Mon–Fri, 9am–5pm ET recommended)
- Add a description explaining what clients should expect
- Add Zoom, Google Meet, or phone call as the location

### Step 3: Get embed code
- In Calendly: Settings → Integrations → Add to Website
- Select "Inline Embed"
- Copy the code snippet

### Step 4: Replace the placeholder in consultation.html
Find this comment in consultation.html:
```html
<!-- PLACEHOLDER — Replace this entire div with your Calendly embed code -->
```
Replace the placeholder div with your Calendly embed code:
```html
<div class="calendly-inline-widget" 
  data-url="https://calendly.com/YOUR-USERNAME/consultation"
  style="min-width:320px;height:700px;">
</div>
<script type="text/javascript" 
  src="https://assets.calendly.com/assets/external/widget.js" 
  async>
</script>
```

---

## 📧 SETTING UP THE CONTACT FORM

### Option A: Formspree (easiest, free tier)
1. Go to formspree.io and create a free account
2. Create a new form — you'll get a URL like `https://formspree.io/f/xabc1234`
3. In contact.html, change the form tag:
   ```html
   <form action="https://formspree.io/f/xabc1234" method="POST">
   ```
4. Remove the `onclick` from the submit button and change type to "submit"

### Option B: Netlify Forms (if hosting on Netlify)
1. Deploy your site to Netlify (free tier available)
2. Add `netlify` attribute to your form: `<form netlify>`
3. Netlify automatically captures form submissions

### Option C: EmailJS (no server required)
Visit emailjs.com for a JavaScript-based solution that sends directly to your email.

---

## 📬 SETTING UP THE LEAD MAGNET (Email Checklist)

### Step 1: Create your checklist document
- Use Google Docs, Canva, or Word to create the "Small Business Bookkeeping Checklist" PDF
- Export as PDF and add to your `/assets/` folder as `bookkeeping-checklist.pdf`

### Step 2: Connect to email marketing
Choose a platform:
- **Mailchimp** (free up to 500 subscribers) — mailchimp.com
- **ConvertKit** (great for creators) — convertkit.com
- **MailerLite** (simple and affordable) — mailerlite.com

### Step 3: Create an automation
- In your email platform, create a "Lead Magnet" automation
- Trigger: New subscriber from your checklist form
- Action: Send welcome email with PDF download link

### Step 4: Connect the form
Get the embed form code from your email platform and replace the placeholder form in index.html (in the Lead Magnet section).

---

## 🔍 SEO SETUP

### Google Search Console
1. Go to search.google.com/search-console
2. Add your domain property
3. Verify ownership (add a TXT record to your domain DNS)
4. Submit your sitemap: `yourdomain.com/sitemap.xml`

### Google Analytics
1. Go to analytics.google.com and create an account
2. Get your Measurement ID (starts with G-)
3. Add this to the `<head>` of each HTML file:
```html
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXXXX');
</script>
```

### Google Business Profile (Local SEO)
1. Go to business.google.com
2. Create or claim your business listing
3. Add: business name, phone, address, hours, services
4. Upload photos of your team/office
5. Request reviews from satisfied clients

---

## 📊 SEO TITLES & META DESCRIPTIONS

| Page | Title | Meta Description |
|------|-------|-----------------|
| Home | Murray & Associates \| Bookkeeping & Accounting for Small Businesses \| Washington DC | Murray & Associates provides expert bookkeeping, QuickBooks Online setup, and small business accounting in Washington DC and remotely nationwide. Book a free consultation today. |
| About | About Murray & Associates \| Bookkeeping Firm Washington DC | Learn about Murray & Associates — a trusted bookkeeping and accounting firm serving small businesses in Washington DC and nationwide. Our mission is to simplify your finances. |
| Services | Bookkeeping & Accounting Services \| Murray & Associates Washington DC | Monthly bookkeeping, QuickBooks Online setup and training, financial reporting, catch-up bookkeeping, and accounting support for small businesses in DC and nationwide. |
| Contact | Contact Murray & Associates \| Bookkeeping Services Washington DC | Get in touch with Murray & Associates for bookkeeping and accounting support. Serving Washington DC and remote clients nationwide. Book a free consultation today. |
| Consultation | Book a Free Consultation \| Murray & Associates Bookkeeping | Schedule a free 30-minute consultation with Murray & Associates. We'll discuss your bookkeeping needs and how we can help your small business. Available in DC and remotely. |
| Blog | Bookkeeping Resources & Blog \| Murray & Associates | Free bookkeeping and accounting resources for small business owners. Tips on QuickBooks, financial reporting, tax prep, cash flow, and more. |

---

## 🗺️ BLOG CONTENT PLAN

10 Planned Posts (write 1-2 per month):

1. **How Small Businesses Should Use QuickBooks Online** — QuickBooks setup, chart of accounts, connecting banks
2. **5 Signs Your Business Needs a Bookkeeper** — Relatable pain points, ROI of professional bookkeeping
3. **Monthly Bookkeeping Checklist for Entrepreneurs** — Promote lead magnet, expand on checklist items
4. **Common Bookkeeping Mistakes Small Businesses Make** — Mixing accounts, no reconciliation, cash basis vs accrual
5. **Why Outsourcing Bookkeeping Saves Money** — Cost comparison: DIY vs hire vs outsource
6. **How to Prepare Your Books for Tax Season** — Year-round tips, what CPAs need, common deductions
7. **Understanding Profit and Loss Reports** — How to read P&L, what it tells you, red flags
8. **Cash Flow Tips for Small Business Owners** — Invoice timing, emergency fund, forecasting basics
9. **QuickBooks Tips for Beginners** — Top 10 tips, shortcuts, common beginner mistakes
10. **When to Hire a Bookkeeper for Your Small Business** — Revenue milestones, time cost, growth indicators

**Content writing tips:**
- Aim for 1,000–1,500 words per post
- Include your target keywords naturally (don't force them)
- End each post with a CTA to book a consultation
- Link between related posts and service pages
- Add a featured image to each post

---

## ✅ PRE-LAUNCH CHECKLIST

- [ ] Update all phone numbers and email addresses
- [ ] Add real testimonials (get permission from clients)
- [ ] Update the hero stats with real numbers
- [ ] Write/refine the About page with your real story
- [ ] Add your logo image (or keep text logo)
- [ ] Set up Calendly and embed in consultation.html
- [ ] Connect contact form to Formspree or similar
- [ ] Set up email marketing for lead magnet
- [ ] Create and upload the bookkeeping checklist PDF
- [ ] Upload all files to your hosting provider
- [ ] Enable SSL (HTTPS) on your domain
- [ ] Set up Google Analytics
- [ ] Set up Google Search Console
- [ ] Create Google Business Profile
- [ ] Test all pages on mobile
- [ ] Test all links and navigation
- [ ] Test contact form submission
- [ ] Write and publish your first blog post
- [ ] Share the site on LinkedIn and social media
