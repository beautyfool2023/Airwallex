# Website audit summary

## Existing project

- Static HTML site; no build system or server-side code.
- Existing content identified a Chinese company as the operator.
- Existing business was Amazon-oriented consumer product affiliate content.
- Existing category pages promoted household products, not software.
- No leaked API keys or obvious secrets were found in the working files scanned.
- The archive included `.git` history and a public GitHub remote reference.

## Material onboarding mismatches

1. Operator mismatch: a US LLC application should not present a different Chinese company as the site operator.
2. Business-model mismatch: software affiliate marketing was not reflected in the old product pages.
3. Brand-positioning mismatch: old pages focused heavily on Amazon and unrelated consumer products.
4. Stripe gap: the old site explicitly said it never accepts payments, so it does not explain what a Stripe account would charge for.
5. Contact gap: only one direct contact method was visible; Stripe recommends multiple customer-service contact methods.
6. Direct-sale policy gap: no real digital product, price/currency, delivery method, or product-specific refund terms were supplied.
7. Repository hygiene: `.git` was included in the uploaded archive and should not be included in routine support or onboarding packages.

## Changes made in this draft

- Rebuilt the site around software research and affiliate marketing.
- Added clear, page-level affiliate disclosures.
- Added Microsoft 365 and Autodesk educational guide pages without claiming official status.
- Added About, Contact, How It Works, Privacy, Terms, Cookie, Affiliate Disclosure, and Refund/Delivery pages.
- Clearly separated third-party affiliate purchases from future direct sales.
- Added a non-public direct-product template for future Stripe use.
- Centralised styling and removed duplicated old consumer-product pages.
- Removed `.git` from the revised delivery package.

## Items only the owner can finalise

- US LLC legal name, state, address and support phone.
- Actual affiliate URLs and proof of participation.
- Actual direct digital product/service details, price and currency.
- Exact refund/cancellation promise and delivery workflow.
- Actual analytics, advertising, payment, chat and cookie tools.
- Legal review for the operator’s jurisdictions and target markets.
