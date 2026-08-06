#!/usr/bin/env python3
"""Generate a deployable static site from site-config.json."""
from pathlib import Path
import html, json, re, shutil, sys

ROOT = Path(__file__).resolve().parent
CONFIG_PATH = ROOT / 'site-config.json'
OUTPUT = ROOT / 'configured-site'

cfg = json.loads(CONFIG_PATH.read_text(encoding='utf-8'))
required = ['brand_name','domain','site_url','contact_email','support_phone','legal_company_name','registered_state','business_address','effective_date']
errors=[]
for key in required:
    value=str(cfg.get(key,'')).strip()
    if not value or value.upper().startswith('REPLACE'):
        errors.append(key)
if errors:
    print('Complete these fields in site-config.json before generating:', ', '.join(errors), file=sys.stderr)
    raise SystemExit(2)

if OUTPUT.exists(): shutil.rmtree(OUTPUT)
OUTPUT.mkdir()
shutil.copytree(ROOT/'assets', OUTPUT/'assets')

old = {
    'Web Daily Lifetyles': cfg['brand_name'],
    'webdailylifetyles.com': cfg['domain'],
    'https://webdailylifetyles.com': cfg['site_url'].rstrip('/'),
    'contact@webdailylifetyles.com': cfg['contact_email'],
    '<span class="placeholder">REPLACE WITH YOUR US LLC LEGAL NAME</span>': html.escape(cfg['legal_company_name']),
    '<span class="placeholder">REPLACE WITH LLC STATE</span>': html.escape(cfg['registered_state']),
    '<span class="placeholder">REPLACE WITH VALID BUSINESS ADDRESS</span>': html.escape(cfg['business_address']),
    '<span class="placeholder">REPLACE WITH SUPPORT PHONE</span>': html.escape(cfg['support_phone']),
    'August 6, 2026': cfg['effective_date'],
}

for src in ROOT.glob('*.html'):
    text=src.read_text(encoding='utf-8')
    # Replace longer strings first so site URL is handled before bare domain.
    for before in sorted(old, key=len, reverse=True):
        text=text.replace(before, old[before])
    (OUTPUT/src.name).write_text(text,encoding='utf-8')

# Public support files.
robots=(ROOT/'robots.txt').read_text(encoding='utf-8').replace('https://webdailylifetyles.com',cfg['site_url'].rstrip('/'))
(OUTPUT/'robots.txt').write_text(robots,encoding='utf-8')
sitemap=(ROOT/'sitemap.xml').read_text(encoding='utf-8').replace('https://webdailylifetyles.com',cfg['site_url'].rstrip('/'))
(OUTPUT/'sitemap.xml').write_text(sitemap,encoding='utf-8')

# Check internal links.
href_re=re.compile(r'href="([^"]+)"')
missing=[]
for f in OUTPUT.glob('*.html'):
    for href in href_re.findall(f.read_text(encoding='utf-8')):
        if href.startswith(('http://','https://','mailto:','#')): continue
        if not (OUTPUT/href.split('#')[0]).exists(): missing.append((f.name,href))
if missing:
    print('Missing internal links:',missing,file=sys.stderr)
    raise SystemExit(3)

remaining=[]
for f in OUTPUT.rglob('*'):
    if f.is_file() and f.suffix in {'.html','.xml','.txt'}:
        if 'REPLACE WITH' in f.read_text(encoding='utf-8',errors='ignore'):
            remaining.append(str(f.relative_to(OUTPUT)))
if remaining:
    print('Warning: deployment files still contain replacement markers:',', '.join(remaining),file=sys.stderr)

print(f'Configured site generated at: {OUTPUT}')
