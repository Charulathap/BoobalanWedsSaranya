import os
import glob

button_html = """
<a href="index.html" style="position:fixed; bottom: 20px; right: 20px; z-index: 999999; background: #8a0c1a; color: white; padding: 12px 20px; border-radius: 30px; font-family: sans-serif; text-decoration: none; font-weight: bold; box-shadow: 0 4px 10px rgba(0,0,0,0.3); font-size: 14px; transition: transform 0.2s;" onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'">← See Other Designs</a>
"""

for file_path in glob.glob('*.html'):
    if file_path == 'index.html':
        continue
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if button_html in content:
        continue
        
    if '</body>' in content:
        new_content = content.replace('</body>', button_html + '\n</body>')
    else:
        new_content = content + button_html
        
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
print("Updated all HTML files.")
