#!/usr/bin/env python3
import os
import re
import json

# Setup directory paths
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BLOG_POSTS_DIR = os.path.join(ROOT_DIR, 'Blog Posts')
HTML_DIR = os.path.join(BLOG_POSTS_DIR, 'HTML')
SCHEMA_DIR = os.path.join(BLOG_POSTS_DIR, 'Schema')

# 12 articles list
ARTICLES = [
    {
        'slug': 'blog-why-every-small-business-needs-a-bookkeeper',
        'title': 'Why Every Small Business Needs a Professional Bookkeeper',
        'category': 'Strategy',
        'date': 'April 9, 2026',
        'read_time': '8 min read',
        'summary': "Hiring a bookkeeper isn't an expense — it's one of the highest-return investments a small business owner can make. Here's why.",
        'thumbnail': 'assets/blog-01.jpg',
        'type': 'existing'
    },
    {
        'slug': 'blog-quickbooks-setup-right',
        'title': 'QuickBooks Setup: Why Getting It Right from Day 1 Saves You Thousands',
        'category': 'QuickBooks',
        'date': 'April 9, 2026',
        'read_time': '9 min read',
        'summary': "A misconfigured QuickBooks account quietly compounds errors for months. Here's what proper setup looks like — and why it matters.",
        'thumbnail': 'assets/blog-02.jpg',
        'type': 'existing'
    },
    {
        'slug': 'blog-how-small-businesses-should-use-quickbooks-online',
        'title': 'How Small Businesses Should Use QuickBooks Online',
        'category': 'QuickBooks',
        'date': 'January 15, 2025',
        'read_time': '6 min read',
        'summary': "QuickBooks Online is a powerful tool — but only when you use it correctly. Here's a practical guide for small business owners just getting started.",
        'thumbnail': 'assets/blog-03.jpg',
        'type': 'txt_draft',
        'source_file': 'How Small Businesses Should Use Qui.txt',
        'lead_magnet': '09_Chart-of-Accounts_Starter.xlsx',
        'lead_magnet_name': 'Chart of Accounts Starter Template',
        'lead_magnet_desc': 'A standard, professionally structured Chart of Accounts — with the equity section broken out by entity type. Free Excel spreadsheet.'
    },
    {
        'slug': 'blog-5-signs-your-business-needs-a-bookkeeper',
        'title': '5 Signs Your Business Needs a Bookkeeper',
        'category': 'Bookkeeping',
        'date': 'January 22, 2025',
        'read_time': '5 min read',
        'summary': "Are you spending more time on your books than your business? Here are the telltale signs it's time to bring in a professional bookkeeper.",
        'thumbnail': 'assets/blog-04.jpg',
        'type': 'txt_draft',
        'source_file': '5 Signs Your Business Needs a Bookk.txt',
        'lead_magnet': '00_Small-Business_Financial-Health-Checklist.pdf',
        'lead_magnet_name': 'Small Business Financial Health Checklist',
        'lead_magnet_desc': '20 checks across cash flow, close, reporting, and taxes — plus the exact tool to fix each gap. Free PDF checklist.'
    },
    {
        'slug': 'blog-monthly-bookkeeping-checklist-for-entrepreneurs',
        'title': 'Monthly Bookkeeping Checklist for Entrepreneurs',
        'category': 'Bookkeeping',
        'date': 'February 5, 2025',
        'read_time': '6 min read',
        'summary': "Stay on top of your finances with this month-by-month bookkeeping checklist. Never miss a critical financial task again.",
        'thumbnail': 'assets/blog-05.jpg',
        'type': 'txt_draft',
        'source_file': 'Monthly Bookkeeping Checklist for E.txt',
        'lead_magnet': '03_Monthly_Bookkeeping_Checklist.pdf',
        'lead_magnet_name': 'Monthly Bookkeeping Checklist',
        'lead_magnet_desc': 'A simple recurring checklist to make sure your monthly bookkeeping stays completely on track. Free PDF.'
    },
    {
        'slug': 'blog-common-bookkeeping-mistakes-small-businesses-make',
        'title': 'Common Bookkeeping Mistakes Small Businesses Make',
        'category': 'Bookkeeping',
        'date': 'February 12, 2025',
        'read_time': '8 min read',
        'summary': 'From mixing personal and business expenses to ignoring reconciliation — avoid these costly bookkeeping errors that trip up most small business owners.',
        'thumbnail': 'assets/blog-06.jpg',
        'type': 'pre_html',
        'source_file': 'common-bookkeeping-mistakes-small-businesses-make.html',
        'meta_desc': 'From mixing personal and business expenses to ignoring reconciliation — avoid these costly bookkeeping errors that trip up most small business owners.'
    },
    {
        'slug': 'blog-why-outsourcing-bookkeeping-saves-money',
        'title': 'Why Outsourcing Bookkeeping Saves Money',
        'category': 'Strategy',
        'date': 'February 20, 2025',
        'read_time': '7 min read',
        'summary': 'The math might surprise you. Here\'s a clear breakdown of why outsourcing your bookkeeping is often more cost-effective than doing it yourself or hiring in-house.',
        'thumbnail': 'assets/blog-07.jpg',
        'type': 'pre_html',
        'source_file': 'why-outsourcing-bookkeeping-saves-money.html',
        'meta_desc': 'Discover why outsourcing your bookkeeping is often more cost-effective than doing it yourself or hiring in-house. A clear financial ROI breakdown.'
    },
    {
        'slug': 'blog-how-to-prepare-your-books-for-tax-season',
        'title': 'How to Prepare Your Books for Tax Season',
        'category': 'Tax Tips',
        'date': 'March 1, 2025',
        'read_time': '8 min read',
        'summary': 'Don\'t wait until April. Here\'s how to get your bookkeeping tax-ready throughout the year so tax season is stress-free, not a scramble.',
        'thumbnail': 'assets/blog-08.jpg',
        'type': 'pre_html',
        'source_file': 'how-to-prepare-your-books-for-tax-season.html',
        'meta_desc': 'Don\'t wait until April. Here\'s how to get your bookkeeping tax-ready throughout the year so tax season is stress-free, not a scramble.'
    },
    {
        'slug': 'blog-understanding-profit-and-loss-reports',
        'title': 'Understanding Profit and Loss Reports',
        'category': 'Finance Basics',
        'date': 'March 10, 2025',
        'read_time': '7 min read',
        'summary': 'Your Profit & Loss statement is one of the most powerful tools in your financial toolkit. Here\'s how to read it and what it\'s telling you about your business.',
        'thumbnail': 'assets/blog-09.jpg',
        'type': 'pre_html',
        'source_file': 'understanding-profit-and-loss-reports.html',
        'meta_desc': 'Your Profit & Loss statement is one of the most powerful tools in your financial toolkit. Learn how to read it and use it to make decisions.'
    },
    {
        'slug': 'blog-cash-flow-tips-for-small-business-owners',
        'title': 'Cash Flow Tips for Small Business Owners',
        'category': 'Cash Flow',
        'date': 'March 18, 2025',
        'read_time': '9 min read',
        'summary': 'A profitable business can still struggle with cash. These practical cash flow strategies will help you keep money moving and avoid the common cash crunches that hurt small businesses.',
        'thumbnail': 'assets/blog-10.jpg',
        'type': 'pre_html',
        'source_file': 'cash-flow-tips-for-small-business-owners.html',
        'meta_desc': 'Profitable businesses still fail when they run out of cash. A controller with 24+ years of experience shares practical cash flow tips.'
    },
    {
        'slug': 'blog-quickbooks-tips-for-beginners',
        'title': 'QuickBooks Tips for Beginners',
        'category': 'QuickBooks',
        'date': 'April 2, 2025',
        'read_time': '8 min read',
        'summary': 'Just getting started with QuickBooks Online? These beginner-friendly tips will help you set up your account correctly and avoid the most common first-timer mistakes.',
        'thumbnail': 'assets/blog-11.jpg',
        'type': 'pre_html',
        'source_file': 'quickbooks-tips-for-beginners.html',
        'meta_desc': 'Just getting started with QuickBooks Online? These beginner-friendly tips will help you set up your account correctly and avoid the most common first-timer mistakes.'
    },
    {
        'slug': 'blog-when-to-hire-a-bookkeeper-for-your-small-business',
        'title': 'When to Hire a Bookkeeper for Your Small Business',
        'category': 'Strategy',
        'date': 'April 15, 2025',
        'read_time': '8 min read',
        'summary': 'Wondering if you\'re ready for professional bookkeeping help? Here are the key milestones and warning signs that tell you it\'s time to bring in an expert.',
        'thumbnail': 'assets/blog-12.jpg',
        'type': 'pre_html',
        'source_file': 'when-to-hire-a-bookkeeper-for-your-small-business.html',
        'meta_desc': 'Wondering if you\'re ready for professional bookkeeping help? Here are the key milestones and warning signs that tell you it\'s time to bring in an expert.'
    }
]

# Shared templates
HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{meta_title} | Murray & Associates</title>
  <meta name="description" content="{meta_description}">
  <link rel="canonical" href="https://www.murray-and-associates.us/{slug}">
  <link rel="stylesheet" href="/styles.css">
  <link rel="icon" type="image/x-icon" href="/assets/favicon.ico">
  <link rel="icon" type="image/png" sizes="32x32" href="/assets/favicon-32.png">
  <link rel="icon" type="image/png" sizes="16x16" href="/assets/favicon-16.png">
  <link rel="apple-touch-icon" sizes="180x180" href="/assets/favicon-180.png">
  <!-- Start of HubSpot Embed Code -->
  <script type="text/javascript" id="hs-script-loader" async defer src="//js-na2.hs-scripts.com/245510475.js"></script>
  <!-- End of HubSpot Embed Code -->

  <!-- Google Analytics (G-3TS0QE46ZF) -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-3TS0QE46ZF"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){{dataLayer.push(arguments);}}
    gtag('js', new Date());
    gtag('config', 'G-3TS0QE46ZF');
  </script>
  <!-- MailerLite Universal -->
  <script>
    (function(w,d,e,u,f,l,n){{w[f]=w[f]||function(){{(w[f].q=w[f].q||[])
    .push(arguments);}},l=d.createElement(e),l.async=1,l.src=u,
    n=d.getElementsByTagName(e)[0],n.parentNode.insertBefore(l,n);}})(window,document,'script','https://assets.mailerlite.com/js/universal.js','ml');
    ml('account', '2271701');
  </script>
  <!-- End MailerLite Universal -->
  {schema_scripts}
  <style>
    .article-hero {{ background: linear-gradient(135deg, var(--navy) 0%, #14325a 100%); padding: 80px 0 60px; }}
    .article-hero .breadcrumb a, .article-hero .breadcrumb .sep {{ color: rgba(255,255,255,0.55); }}
    .article-hero .breadcrumb .current {{ color: rgba(255,255,255,0.75); }}
    .article-meta {{ display: flex; align-items: center; gap: 20px; margin-top: 24px; flex-wrap: wrap; }}
    .article-tag {{ background: var(--gold); color: var(--navy); font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; padding: 4px 12px; border-radius: 100px; }}
    .article-date {{ color: rgba(255,255,255,0.55); font-size: 0.85rem; }}
    .article-read {{ color: rgba(255,255,255,0.55); font-size: 0.85rem; }}
    .article-layout {{ display: grid; grid-template-columns: 1fr 320px; gap: 72px; align-items: start; }}
    .article-body h2 {{ font-size: 1.55rem; color: var(--navy); margin: 48px 0 16px; }}
    .article-body h3 {{ font-size: 1.2rem; color: var(--navy); margin: 32px 0 12px; }}
    .article-body p {{ line-height: 1.8; color: var(--gray-dark); margin-bottom: 20px; }}
    .article-body ul, .article-body ol {{ margin: 0 0 20px 24px; line-height: 1.8; color: var(--gray-dark); }}
    .article-body li {{ margin-bottom: 10px; }}
    .article-body strong {{ color: var(--navy); }}
    .article-callout {{ background: var(--gold-pale); border-left: 4px solid var(--gold); border-radius: 0 var(--radius) var(--radius) 0; padding: 24px 28px; margin: 36px 0; }}
    .article-callout p {{ margin: 0; color: var(--navy); font-weight: 500; }}
    .sidebar-card {{ background: var(--off-white); border: 1px solid var(--gray-light); border-radius: var(--radius-lg); padding: 28px; margin-bottom: 28px; }}
    .sidebar-card h4 {{ font-size: 1rem; color: var(--navy); margin-bottom: 12px; }}
    .sidebar-card p {{ font-size: 0.88rem; color: var(--gray-dark); line-height: 1.6; margin-bottom: 16px; }}
    .sidebar-cta {{ background: var(--navy); border-radius: var(--radius-lg); padding: 32px; text-align: center; }}
    .sidebar-cta h4 {{ color: var(--white); margin-bottom: 12px; }}
    .sidebar-cta p {{ color: rgba(255,255,255,0.65); font-size: 0.88rem; margin-bottom: 20px; }}
    .back-to-blog {{ display: inline-flex; align-items: center; gap: 8px; color: var(--gold); font-weight: 600; font-size: 0.9rem; text-decoration: none; margin-bottom: 32px; }}
    .back-to-blog:hover {{ text-decoration: underline; }}
    @media (max-width: 860px) {{ .article-layout {{ grid-template-columns: 1fr; }} }}
  </style>
</head>
<body>

  <header class="site-header">
    <div class="container">
      <nav class="nav-inner">
        <a href="/" class="logo" aria-label="Murray & Associates Home">
          <img src="/assets/logo.png" alt="Murray &amp; Associates" class="logo-img" style="height:44px; width:auto;">
        </a>
        <ul class="nav-menu" id="navMenu">
          <li><a href="/">Home</a></li>
          <li><a href="/about">About</a></li>
          <li><a href="/services">Services</a></li>
          <li><a href="/blog" class="active">Resources</a></li>
          <li><a href="/contact">Contact</a></li>
          <li><a href="/consultation" class="nav-cta">Book a Consultation</a></li>
        </ul>
        <button class="nav-toggle" id="navToggle" aria-label="Toggle navigation" aria-expanded="false">
          <span></span><span></span><span></span>
        </button>
      </nav>
    </div>
  </header>
  <div id="ticker-placeholder"></div>

  <main>
    <section class="article-hero">
      <div class="container">
        <div class="breadcrumb">
          <a href="/">Home</a>
          <span class="sep">›</span>
          <a href="/blog">Resources</a>
          <span class="sep">›</span>
          <span class="current">{title}</span>
        </div>
        <h1 style="color: var(--white); max-width: 760px; margin-top: 20px;">{title}</h1>
        <div class="article-meta">
          <span class="article-tag">{category}</span>
          <span class="article-date">{date}</span>
          <span class="article-read">{read_time}</span>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="article-layout">

          <!-- Article Body -->
          <article class="article-body">
            <a href="/blog" class="back-to-blog">← Back to All Resources</a>
            {content}
          </article>

          <!-- Sidebar -->
          <aside>
            <div class="sidebar-cta">
              <h4>Ready to Stop Doing This Yourself?</h4>
              <p>Book a free 15-minute consultation and let's talk about what your business actually needs.</p>
              <a href="/consultation" class="btn btn-primary btn-arrow" style="width: 100%; justify-content: center;">Book Free Consultation</a>
            </div>

            <div class="sidebar-card" style="margin-top: 28px;">
              <h4>Our Services</h4>
              <ul style="display: flex; flex-direction: column; gap: 10px; margin: 0; padding: 0; list-style: none;">
                <li><a href="/services#monthly-bookkeeping" style="color: var(--navy); font-size: 0.9rem;">→ Monthly Bookkeeping</a></li>
                <li><a href="/services#quickbooks-setup" style="color: var(--navy); font-size: 0.9rem;">→ QuickBooks Setup</a></li>
                <li><a href="/services#quickbooks-training" style="color: var(--navy); font-size: 0.9rem;">→ QuickBooks Training</a></li>
                <li><a href="/services#financial-reporting" style="color: var(--navy); font-size: 0.9rem;">→ Financial Reporting</a></li>
                <li><a href="/services#cleanup-bookkeeping" style="color: var(--navy); font-size: 0.9rem;">→ Catch-Up Bookkeeping</a></li>
                <li><a href="/services#accounting-support" style="color: var(--navy); font-size: 0.9rem;">→ Ongoing Support</a></li>
              </ul>
            </div>

            <div class="sidebar-card">
              <h4>Contact Us Directly</h4>
              <p>Have a quick question? Reach out anytime.</p>
              <div style="display: flex; flex-direction: column; gap: 10px;">
                <a href="tel:+12027095015" style="color: var(--gold); font-weight: 600; font-size: 0.9rem;"><svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg> (202) 709-5015</a>
                <a href="mailto:j.s.murrayllc@gmail.com" style="color: var(--gold); font-weight: 600; font-size: 0.9rem; word-break: break-all;"><svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><rect width="20" height="16" x="2" y="4" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/></svg> j.s.murrayllc@gmail.com</a>
              </div>
            </div>

            <div class="sidebar-card">
              <h4>Also in Resources</h4>
              <ul style="display: flex; flex-direction: column; gap: 10px; margin: 0; padding: 0; list-style: none;">
                {sidebar_links}
              </ul>
            </div>
          </aside>

        </div>
      </div>
    </section>
  </main>

  <footer class="site-footer">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-brand">
          <div class="firm-name">Murray &amp; Associates</div>
          <p>Professional bookkeeping and accounting services for small businesses in Washington DC and nationwide. We make your finances simple.</p>
          <div style="margin-top: 20px; display: flex; gap: 12px;">
            <a href="https://www.facebook.com/profile.php?id=61582744538991" target="_blank" rel="noopener" aria-label="Facebook" style="width: 36px; height: 36px; background: rgba(255,255,255,0.08); border-radius: 6px; display: flex; align-items: center; justify-content: center; color: rgba(255,255,255,0.5); font-size: 0.9rem; transition: all 0.28s;" onmouseover="this.style.background='rgba(201,151,0,0.2)'; this.style.color='var(--gold)'" onmouseout="this.style.background='rgba(255,255,255,0.08)'; this.style.color='rgba(255,255,255,0.5)'">f</a>
            <a href="https://www.instagram.com/murray_and_associates/" target="_blank" rel="noopener" aria-label="Instagram" style="width: 36px; height: 36px; background: rgba(255,255,255,0.08); border-radius: 6px; display: flex; align-items: center; justify-content: center; color: rgba(255,255,255,0.5); font-size: 1rem; transition: all 0.28s;" onmouseover="this.style.background='rgba(201,151,0,0.2)'; this.style.color='var(--gold)'" onmouseout="this.style.background='rgba(255,255,255,0.08)'; this.style.color='rgba(255,255,255,0.5)'"><svg xmlns="http://www.w3.org/2000/svg" width="15" height="15" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/></svg></a>
          </div>
        </div>

        <div class="footer-col">
          <h5>Services</h5>
          <ul>
            <li><a href="/services#monthly-bookkeeping">Monthly Bookkeeping</a></li>
            <li><a href="/services#quickbooks-setup">QuickBooks Setup</a></li>
            <li><a href="/services#quickbooks-training">QuickBooks Training</a></li>
            <li><a href="/services#financial-reporting">Financial Reporting</a></li>
            <li><a href="/services#cleanup-bookkeeping">Catch-Up Bookkeeping</a></li>
            <li><a href="/services#accounting-support">Accounting Support</a></li>
          </ul>
        </div>

        <div class="footer-col">
          <h5>Company</h5>
          <ul>
            <li><a href="/about">About Us</a></li>
            <li><a href="/blog">Resources &amp; Blog</a></li>
            <li><a href="/consultation">Book a Consultation</a></li>
            <li><a href="/contact">Contact Us</a></li>
            <li><a href="/privacy-policy">Privacy Policy</a></li>
            <li><a href="/terms">Terms of Service</a></li>
            <li><a href="/sitemap.xml">Sitemap</a></li>
          </ul>
        </div>

        <div class="footer-col">
          <h5>Contact</h5>
          <div class="footer-contact-item">
            <span class="icon"><svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg></span>
            <span><a href="tel:+12027095015" style="color: rgba(255,255,255,0.55); transition: color 0.28s;" onmouseover="this.style.color='var(--gold)'" onmouseout="this.style.color='rgba(255,255,255,0.55)'">(202) 709-5015</a></span>
          </div>
          <div class="footer-contact-item">
            <span class="icon"><svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><rect width="20" height="16" x="2" y="4" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/></svg></span>
            <span><a href="mailto:j.s.murrayllc@gmail.com" style="color: rgba(255,255,255,0.55); transition: color 0.28s;" onmouseover="this.style.color='var(--gold)'" onmouseout="this.style.color='rgba(255,255,255,0.55)'">j.s.murrayllc@gmail.com</a></span>
          </div>
          <div class="footer-contact-item">
            <span class="icon"><svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/></svg></span>
            <span>Washington, DC Metro Area</span>
          </div>
          <div class="footer-contact-item">
            <span class="icon"><svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg></span>
            <span>Mon–Fri: 9am–5pm ET</span>
          </div>
        </div>
      </div>

      <div class="footer-bottom">
        <p>&copy; 2026 Murray &amp; Associates. All rights reserved.</p>
        <div class="footer-links">
          <a href="/privacy-policy">Privacy Policy</a>
          <a href="/terms">Terms of Service</a>
          <a href="/sitemap.xml">Sitemap</a>
        </div>
      </div>
    </div>
  </footer>

  <script src="/js/main.js" defer></script>
</body>
</html>
"""

def extract_body(html_content):
    # Extract content inside <article>
    m = re.search(r'<article[^>]*>(.*?)</article>', html_content, re.DOTALL | re.IGNORECASE)
    if not m:
        return html_content
    body = m.group(1).strip()
    # Strip the H1 from body if present (as it is rendered in the hero banner)
    body = re.sub(r'<h1[^>]*>.*?</h1>', '', body, count=1, flags=re.DOTALL | re.IGNORECASE).strip()
    return body

def convert_txt_to_html(txt_content, lead_magnet, lead_magnet_name, lead_magnet_desc):
    lines = txt_content.strip().split('\n')
    title = lines[0].strip()
    
    html_paragraphs = []
    current_list = []
    
    # Simple stateful parsing
    in_list = False
    
    for line in lines[1:]:
        line = line.strip()
        if not line:
            if in_list:
                html_paragraphs.append("<ul>\n" + "\n".join(current_list) + "\n</ul>")
                current_list = []
                in_list = False
            continue
            
        # Check if heading
        if re.match(r'^\d+\.\s+\w+', line) or line.startswith("Final Thought"):
            if in_list:
                html_paragraphs.append("<ul>\n" + "\n".join(current_list) + "\n</ul>")
                current_list = []
                in_list = False
            html_paragraphs.append(f"<h2>{line}</h2>")
        # Check if list item
        elif line.startswith('- ') or line.startswith('* '):
            in_list = True
            current_list.append(f"  <li>{line[2:]}</li>")
        elif re.match(r'^\d+\.\s*$', line) or line.startswith('“') or line.startswith('”'):
            # blockquotes or custom items
            if in_list:
                html_paragraphs.append("<ul>\n" + "\n".join(current_list) + "\n</ul>")
                current_list = []
                in_list = False
            html_paragraphs.append(f"<p><em>{line}</em></p>")
        else:
            if in_list:
                html_paragraphs.append("<ul>\n" + "\n".join(current_list) + "\n</ul>")
                current_list = []
                in_list = False
            html_paragraphs.append(f"<p>{line}</p>")
            
    if in_list:
        html_paragraphs.append("<ul>\n" + "\n".join(current_list) + "\n</ul>")
        
    body_content = "\n".join(html_paragraphs)
    
    # Inject lead magnet box before the closing callout/final thought
    if lead_magnet:
        download_box = f"""
            <hr>
            <div style="background: var(--gold-pale); border: 2px solid var(--gold); border-radius: var(--radius-lg); padding: 32px; margin: 40px 0;">
              <h3 style="margin-top: 0; color: var(--navy);">Free Tool: {lead_magnet_name}</h3>
              <p>{lead_magnet_desc}</p>
              <a href="/assets/Lead Magnets/{lead_magnet}" class="btn btn-primary btn-arrow" download>Download Free Template</a>
            </div>
            <hr>
        """
        # Find where to inject: insert before "<h2>Final Thought</h2>" or at the very end
        if "<h2>Final Thought</h2>" in body_content:
            body_content = body_content.replace("<h2>Final Thought</h2>", download_box + "\n<h2>Final Thought</h2>")
        else:
            body_content = body_content + "\n" + download_box
            
    # Add closing call to action
    cta_box = """
            <div class="article-callout">
              <p><svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><rect width="18" height="18" x="3" y="4" rx="2" ry="2"/><line x1="16" x2="16" y1="2" y2="6"/><line x1="8" x2="8" y1="2" y2="6"/><line x1="3" x2="21" y1="10" y2="10"/></svg> <strong>Need help sorting out your business finances?</strong> Book a free 15-minute consultation with Murray &amp; Associates. We'll look at your books and suggest a game plan to keep them accurate and tax-ready all year.</p>
            </div>
            
            <div style="margin-top: 48px; padding-top: 36px; border-top: 1px solid var(--gray-light);">
              <p style="font-style: italic; font-size: 0.9rem; color: var(--gray-mid);">Murray &amp; Associates provides professional bookkeeping and fractional controller services to small businesses in the Washington DC area and remotely nationwide. <a href="/consultation" style="color: var(--gold); font-weight: 600;">Book a free consultation</a> to get started.</p>
            </div>
    """
    body_content = body_content + "\n" + cta_box
    return body_content

def build_schemas(slug, is_faq=False):
    schemas = []
    # Load Article Schema
    article_schema_path = os.path.join(SCHEMA_DIR, f"{slug.replace('blog-', '')}.article-schema.json")
    if os.path.exists(article_schema_path):
        with open(article_schema_path, 'r', encoding='utf-8') as f:
            schemas.append(f'<script type="application/ld+json">\n{f.read().strip()}\n</script>')
            
    # Load FAQ Schema
    if is_faq:
        faq_schema_path = os.path.join(SCHEMA_DIR, f"{slug.replace('blog-', '')}.faq-schema.json")
        if os.path.exists(faq_schema_path):
            with open(faq_schema_path, 'r', encoding='utf-8') as f:
                schemas.append(f'<script type="application/ld+json">\n{f.read().strip()}\n</script>')
                
    return '\n  '.join(schemas)

def clean_internal_links(content):
    pattern = r'href=["\'](index|about|services|blog|contact|consultation|privacy-policy|terms|blog-[a-zA-Z0-9\-]+)\.html(#[a-zA-Z0-9\-]+)?["\']'
    
    def repl(match):
        page = match.group(1)
        anchor = match.group(2) or ""
        if page == 'index':
            return f'href="/{anchor}"'
        else:
            return f'href="/{page}{anchor}"'
            
    return re.sub(pattern, repl, content)

# Main integration runner
def run():
    print("Starting Blog Integration...")
    
    # Process all articles
    for idx, art in enumerate(ARTICLES):
        slug = art['slug']
        title = art['title']
        category = art['category']
        date = art['date']
        read_time = art['read_time']
        
        print(f"Processing: {title} ({slug})")
        
        # Determine schema scripts
        has_faq = art['type'] == 'pre_html'  # pre-rendered html articles have FAQ schemas
        schema_scripts = build_schemas(slug, is_faq=has_faq)
        
        # Determine sidebar links (pick 3 other articles)
        other_arts = [a for a in ARTICLES if a['slug'] != slug]
        sidebar_arts = other_arts[idx % len(other_arts) : idx % len(other_arts) + 3]
        if len(sidebar_arts) < 3:
            sidebar_arts += other_arts[:3 - len(sidebar_arts)]
            
        sidebar_links = ""
        for s_art in sidebar_arts:
            sidebar_links += f'<li><a href="/{s_art["slug"]}" style="color: var(--navy); font-size: 0.88rem; line-height: 1.4;">{s_art["title"]} →</a></li>\n'
            
        # Get content
        content = ""
        meta_title = title
        meta_desc = art.get('summary', '')
        
        if art['type'] == 'existing':
            # Read from existing html page body
            existing_file_path = os.path.join(ROOT_DIR, f"{slug}.html")
            if os.path.exists(existing_file_path):
                with open(existing_file_path, 'r', encoding='utf-8') as f:
                    raw_html = f.read()
                    content = extract_body(raw_html)
                    # Extract meta desc
                    m_desc = re.search(r'<meta name="description" content="(.*?)"', raw_html, re.IGNORECASE)
                    if m_desc:
                        meta_desc = m_desc.group(1)
            else:
                print(f"Warning: Existing file {slug}.html not found!")
                continue
                
        elif art['type'] == 'pre_html':
            # Read from Blog Posts/HTML/
            html_file_path = os.path.join(HTML_DIR, art['source_file'])
            if os.path.exists(html_file_path):
                with open(html_file_path, 'r', encoding='utf-8') as f:
                    raw_html = f.read()
                    content = extract_body(raw_html)
                    # Map the href="/downloads/" to the local "/assets/Lead Magnets/" folder
                    content = content.replace('/downloads/', '/assets/Lead Magnets/')
                    # Also replace clean blog links if needed
                    content = content.replace('/blog/understanding-profit-and-loss-reports', '/blog-understanding-profit-and-loss-reports')
                    meta_desc = art['meta_desc']
            else:
                print(f"Warning: Pre-rendered HTML file {art['source_file']} not found!")
                continue
                
        elif art['type'] == 'txt_draft':
            # Convert text draft from root
            txt_file_path = os.path.join(ROOT_DIR, art['source_file'])
            if os.path.exists(txt_file_path):
                with open(txt_file_path, 'r', encoding='utf-8') as f:
                    txt_content = f.read()
                    content = convert_txt_to_html(
                        txt_content, 
                        art.get('lead_magnet'), 
                        art.get('lead_magnet_name'), 
                        art.get('lead_magnet_desc')
                    )
            else:
                print(f"Warning: Text draft {art['source_file']} not found!")
                continue
                
        # Inject into HTML template
        final_html = HTML_TEMPLATE.format(
            meta_title=meta_title,
            meta_description=meta_desc,
            slug=slug,
            schema_scripts=schema_scripts,
            title=title,
            category=category,
            date=date,
            read_time=read_time,
            content=content,
            sidebar_links=sidebar_links
        )
        
        # Clean internal links to pretty URLs
        final_html = clean_internal_links(final_html)
        
        # Save output to root folder
        output_file_path = os.path.join(ROOT_DIR, f"{slug}.html")
        with open(output_file_path, 'w', encoding='utf-8') as f:
            f.write(final_html)
            
        print(f"Saved: {output_file_path}")

    # Regenerate blog.html listing page
    print("Regenerating blog.html...")
    blog_list_path = os.path.join(ROOT_DIR, 'blog.html')
    if os.path.exists(blog_list_path):
        with open(blog_list_path, 'r', encoding='utf-8') as f:
            blog_html = f.read()
            
        # First 2 articles are featured
        featured_html = f"""
        <!-- Featured Posts -->
        <div style="margin-bottom: 48px;">
          <span class="section-label">Featured Articles</span>
          <div class="blog-grid" style="margin-top: 24px; grid-template-columns: repeat(2, 1fr);">
            <article class="blog-card" style="border: 2px solid var(--gold);">
              <div class="blog-card-img" style="background: linear-gradient(135deg, #0C2340 0%, #14325a 100%);"><img src="/{ARTICLES[0]['thumbnail']}" alt="" loading="lazy"><span class="blog-card-tag">{ARTICLES[0]['category']}</span>
              </div>
              <div class="blog-card-body">
                <div class="blog-card-date">{ARTICLES[0]['date']}</div>
                <h3>{ARTICLES[0]['title']}</h3>
                <p>{ARTICLES[0]['summary']}</p>
                <a href="/{ARTICLES[0]['slug']}" class="blog-read-link">Read Article →</a>
              </div>
            </article>
            <article class="blog-card" style="border: 2px solid var(--gold);">
              <div class="blog-card-img" style="background: linear-gradient(135deg, #14325a 0%, #0C2340 100%);"><img src="/{ARTICLES[1]['thumbnail']}" alt="" loading="lazy"><span class="blog-card-tag">{ARTICLES[1]['category']}</span>
              </div>
              <div class="blog-card-body">
                <div class="blog-card-date">{ARTICLES[1]['date']}</div>
                <h3>{ARTICLES[1]['title']}</h3>
                <p>{ARTICLES[1]['summary']}</p>
                <a href="/{ARTICLES[1]['slug']}" class="blog-read-link">Read Article →</a>
              </div>
            </article>
          </div>
        </div>
        """
        
        # Remaining 10 posts
        remaining_html = '<span class="section-label">All Articles</span>\n        <div class="blog-grid" style="margin-top: 24px;">\n'
        for art in ARTICLES[2:]:
            remaining_html += f"""
          <!-- Post -->
          <article class="blog-card">
            <div class="blog-card-img" style="background: linear-gradient(135deg, #0C2340 0%, #14325a 100%);"><img src="/{art['thumbnail']}" alt="" loading="lazy"><span class="blog-card-tag">{art['category']}</span>
            </div>
            <div class="blog-card-body">
              <div class="blog-card-date">{art['date']}</div>
              <h3>{art['title']}</h3>
              <p>{art['summary']}</p>
              <a href="/{art['slug']}" class="blog-read-link">Read Article →</a>
            </div>
          </article>\n"""
        remaining_html += "        </div><!-- end all-articles grid -->"
        
        # Replace section in blog.html
        start_pat = r'<!-- Featured Posts -->.*?<!-- Blog CTA -->'
        blog_html = re.sub(start_pat, featured_html + '\n        ' + remaining_html + '\n        <!-- Blog CTA -->', blog_html, flags=re.DOTALL)
        
        # Replace ticker placeholder & scripts
        blog_html = re.sub(r'<div class="ticker".*?</div>\s*</div>\s*</div>', '<div id="ticker-placeholder"></div>', blog_html, flags=re.DOTALL)
        blog_html = re.sub(r'<!-- Navigation toggle script -->\s*<script>.*?</script>', '<script src="/js/main.js" defer></script>', blog_html, flags=re.DOTALL)
        
        # Clean links
        blog_html = clean_internal_links(blog_html)
        
        with open(blog_list_path, 'w', encoding='utf-8') as f:
            f.write(blog_html)
        print("blog.html successfully updated!")
        
    print("Blog Integration Complete!")

if __name__ == '__main__':
    run()
