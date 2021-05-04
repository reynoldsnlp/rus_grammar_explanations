from glob import glob
import re

with open('head.html.copyme') as f:
    head = f.read().strip()

for filename in glob('*.html'):
    with open(filename) as f:
        old_src = f.read()
    new_src = re.sub('<head>.*</head>', head, old_src, flags=re.S)
    with open(filename, 'w') as f:
        f.write(new_src)
