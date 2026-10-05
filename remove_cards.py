import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove postcard card
content = re.sub(r'<a class="card" href="postcard\.html">.*?</a>\s*', '', content, flags=re.DOTALL)

# Remove elephant card
content = re.sub(r'<a class="card" href="elephant\.html">.*?</a>\s*', '', content, flags=re.DOTALL)

# Renumber remaining designs starting from 1
counter = 1
def renumber(match):
    global counter
    result = f'<div class="num">DESIGN {counter}</div>'
    counter += 1
    return result

content = re.sub(r'<div class="num">DESIGN \d+</div>', renumber, content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Removed cards and renumbered {counter - 1} remaining designs.")
