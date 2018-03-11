from __future__ import unicode_literals
import io
import glob

for filename in glob.glob('*.srt'):
    with io.open(filename) as f:
        data = f.read()
    with io.open(filename, 'w', encoding='utf-8') as f:
        f.write(data)
        print("Converted "+filename)
