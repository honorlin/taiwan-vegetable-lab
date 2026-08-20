#!/usr/bin/env python3
from pathlib import Path
from urllib.parse import urlparse
import yaml
from PIL import Image
root = Path(__file__).resolve().parents[1]
policy = yaml.safe_load((root/'automation/content-policy.yml').read_text())
trusted = yaml.safe_load((root/'automation/trusted-sources.yml').read_text())['approved_domains']
categories = {x['key'] for x in yaml.safe_load((root/'_data/site.yml').read_text())['categories']}
failed=[]
for item in sorted((root/'_posts').glob('*.md')):
    text=item.read_text(); _,raw,body=text.split('---',2); meta=yaml.safe_load(raw); errors=[]
    for key in policy['required_meta']:
        if not meta.get(key): errors.append(f'missing {key}')
    if meta.get('category') not in categories: errors.append('unknown category')
    for heading in policy['required_sections']:
        if heading not in body: errors.append(f'missing section {heading}')
    for claim in policy['blocked_claims']:
        if claim in text: errors.append(f'blocked claim {claim}')
    if len(meta.get('sources') or []) < policy['minimum_sources']: errors.append('not enough sources')
    for source in meta.get('sources') or []:
        host=(urlparse(source.get('url','')).hostname or '').lower()
        if not any(host==d or host.endswith('.'+d) for d in trusted): errors.append(f'untrusted source {host}')
    image=root/str(meta.get('image','')).lstrip('/')
    if not image.exists(): errors.append('image missing')
    elif Image.open(image).size != (1200,630): errors.append('image must be 1200x630')
    if errors: failed.append(f'{item.name}: '+ '; '.join(errors))
if failed: raise SystemExit('\n'.join(failed))
print(f'Validated {len(list((root/"_posts").glob("*.md")))} article(s).')
