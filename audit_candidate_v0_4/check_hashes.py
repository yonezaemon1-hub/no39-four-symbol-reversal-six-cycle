"""Check packaged original files without changing them."""
from hashlib import sha256
from pathlib import Path

root = Path(__file__).resolve().parent
count = 0
for row in (root/'SHA256SUMS.txt').read_text(encoding='utf-8').splitlines():
    expected, name = row.split('  ', 1)
    p = root/name
    if sha256(p.read_bytes()).hexdigest() != expected:
        raise SystemExit('FAIL '+name)
    print('PASS '+name)
    count += 1
print('PASS',count,'files')
