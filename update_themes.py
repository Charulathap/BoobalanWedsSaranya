import os

# Update postcard.html
with open('postcard.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('--pk-mint:#e8f3ec', '--pk-mint:#f3e6cc')
content = content.replace('--pk-mint2:#d6ebe0', '--pk-mint2:#c9b48a')
content = content.replace('--pk-teal:#0e6870', '--pk-teal:#1f3560')
content = content.replace('--pk-emerald:#1d7a52', '--pk-emerald:#145f8f')
content = content.replace('--pk-ink:#103a3e', '--pk-ink:#1a2b4d')
content = content.replace('content="#0e6870"', 'content="#1f3560"')

with open('postcard.html', 'w', encoding='utf-8') as f:
    f.write(content)

# Update elephant.html
with open('elephant.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('--pk-mint:#e8f3ec', '--pk-mint:#fbf3e4')
content = content.replace('--pk-mint2:#d6ebe0', '--pk-mint2:#e7cf9a')
content = content.replace('--pk-teal:#0e6870', '--pk-teal:#1d3a7a')
content = content.replace('--pk-emerald:#1d7a52', '--pk-emerald:#bcd8c8')
content = content.replace('--pk-ink:#103a3e', '--pk-ink:#1d3a7a')
content = content.replace('content="#0e6870"', 'content="#1d3a7a"')

with open('elephant.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated themes for postcard and elephant.")
