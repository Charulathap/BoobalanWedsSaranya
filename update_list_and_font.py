import re

# Update index.html numbers
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

def increment_design(match):
    num = int(match.group(1))
    return f'<div class="num">DESIGN {num + 1}</div>'

content = re.sub(r'<div class="num">DESIGN (\d+)</div>', increment_design, content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

# Update font-family for the button in all HTML files
import glob
for file_path in glob.glob('*.html'):
    if file_path == 'index.html':
        continue
    with open(file_path, 'r', encoding='utf-8') as f:
        file_content = f.read()
    
    # The current button has 'font-family: sans-serif;'
    if 'font-family: sans-serif;' in file_content:
        file_content = file_content.replace('font-family: sans-serif;', "font-family: 'Cinzel', 'Marcellus', 'Cormorant Garamond', serif; letter-spacing: 0.05em;")
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(file_content)

print("Updated numbering and button font-family.")
