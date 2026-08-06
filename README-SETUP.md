# Airwallex / Stripe website draft

This is a revised static website based on the uploaded project. It is designed around a truthful business model:

- US LLC operator
- software-focused affiliate marketing
- PartnerBoost / YeahPromos relationships
- third-party checkout for affiliate purchases
- possible future direct digital products

## Critical: not ready to submit as-is

Search all files for `REPLACE` and complete every item before deployment or onboarding. The most important values are:

1. Exact US LLC legal name (must match EIN, formation document, Airwallex, bank and Stripe).
2. LLC registration state.
3. Valid business mailing address.
4. Monitored support phone or another genuine second direct contact channel.
5. Confirm that `contact@webdailylifetyles.com` works and is monitored.
6. Add genuine PartnerBoost / YeahPromos affiliate links only where approved.
7. If applying for Stripe card payments, add at least one real direct-sale product page with exact product, USD price, delivery method, support and refund terms.

## Generate the final site

1. Open `site-config.json`.
2. Replace every value beginning with `REPLACE`.
3. Run:

```bash
python configure.py
```

4. Deploy the newly generated `configured-site` folder. Do not deploy the draft root folder.

## Deployment

This is plain static HTML. Upload `configured-site` to Cloudflare Pages, Netlify, GitHub Pages, or another HTTPS host.

Cloudflare Pages:
- Framework preset: None
- Build command: leave blank
- Output directory: `/`

## Domain changes

Changing the domain later is acceptable when the business remains the same, but update:
- `site_url` and `domain` in `site-config.json`
- canonical URLs in every HTML file
- `robots.txt`
- `sitemap.xml`
- email addresses if they use the old domain
- Airwallex and Stripe business-profile URL

## Stripe limitation

An affiliate-only site does not by itself explain what you will charge customers for through Stripe. Do not activate direct card payments until a real direct-sale product or service is live with accurate pricing, currency, delivery, refund/cancellation, and support information.

## Security

The uploaded archive contained a `.git` directory and full Git history. This revised package excludes `.git`. Do not upload API keys, `.env` files, bank documents, identity documents, or onboarding screenshots to the public website repository.
