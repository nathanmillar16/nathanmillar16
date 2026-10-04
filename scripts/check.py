from pathlib import Path
import re
import xml.etree.ElementTree as ET
root = Path(__file__).resolve().parent.parent
readme = (root / 'README.md').read_text()
for asset in re.findall(r'src="(assets/[^"]+)"', readme):
    assert (root / asset).is_file(), f'Missing asset: {asset}'
for svg in (root / 'assets').glob('*.svg'):
    ET.parse(svg)
    assert '<script' not in svg.read_text(), f'Script found: {svg}'
assert 'Jet2' not in readme
print('PASS: README images resolve; SVGs are valid and script-free.')
