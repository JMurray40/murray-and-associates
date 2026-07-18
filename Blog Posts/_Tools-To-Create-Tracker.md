# Tools / Lead Magnets Tracker

Status: all built and wired into the blog posts. Files live in `Outputs/Lead Magnets/`. Blog posts link to them at the web path **`/downloads/<filename>`** — upload the Lead Magnets files to that folder on murray-and-associates.us (or change the base path in the posts to wherever you host them).

| # | Tool | File | Linked From (post) | Status |
|---|------|------|--------------------|--------|
| 00 | Small Business Financial Health Checklist | 00_Small-Business_Financial-Health-Checklist.pdf | Common Mistakes | Built + linked |
| 01 | 13-Week Cash Flow Forecast | 01_13-Week_Cash_Flow_Forecast.xlsx | Cash Flow Tips | Built + linked |
| 02 | Year-End Tax Prep Checklist | 02_Year-End_Tax_Prep_Checklist.pdf | Prepare Books for Tax Season | Built + linked |
| 03 | Monthly Bookkeeping Checklist | 03_Monthly_Bookkeeping_Checklist.pdf | QuickBooks Tips | Built + linked |
| 04 | Monthly Close Checklist | 04_Monthly_Close_Checklist.pdf | Common Mistakes | Built + linked |
| 05 | Is It Time to Hire? Self-Assessment | 05_Is-It-Time-to-Hire_Self-Assessment.pdf | When to Hire | Built + linked |
| 06 | Bookkeeper vs. Controller vs. CPA | 06_Bookkeeper_vs_Controller_vs_CPA.pdf | When to Hire | Built + linked |
| 07 | DIY-Bookkeeping ROI Calculator | 07_DIY-Bookkeeping_ROI_Calculator.xlsx | Why Outsourcing Saves Money | Built + linked |
| 08a | How to Read Your P&L One-Pager | 08a_How-to-Read-Your-P&L_One-Pager.pdf | Understanding P&L | Built + linked |
| 08b | Budget vs. Actual Template | 08b_Budget-vs-Actual_Template.xlsx | Understanding P&L | Built + linked |
| 09 | Chart of Accounts Starter | 09_Chart-of-Accounts_Starter.xlsx | Common Mistakes + QuickBooks | Built + linked |
| 10 | Contractor 1099 & W-9 Tracker | 10_Contractor-1099-W9_Tracker.xlsx | Prepare Books for Tax Season | Built + linked |

## Publishing notes
- **Upload location:** put all Lead Magnets files where your site serves `/downloads/`. If your host uses a different path (e.g. `/wp-content/uploads/` or a CDN), do a find-and-replace on `/downloads/` across the 7 posts (markdown + HTML).
- **The `&` in file 08a:** the on-disk name contains a literal `&`. In the HTML it's correctly URL-encoded as `%26`. Keep the served filename as `08a_How-to-Read-Your-P&L_One-Pager.pdf`, or rename it to remove the `&` (e.g. `08a_How-to-Read-Your-PL_One-Pager.pdf`) and update the two references if you prefer a cleaner URL.
- **Each post's "Free download" callout** sits just above the closing CTA, so the tool is offered right when the reader is most engaged. Good spot to gate behind an email capture later if you want the lead-gen.
