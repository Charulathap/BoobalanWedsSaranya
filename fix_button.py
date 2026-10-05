import os
import glob

old_button = """<a href="index.html" style="position:fixed; bottom: 20px; right: 20px; z-index: 999999; background: #8a0c1a; color: white; padding: 12px 20px; border-radius: 30px; font-family: sans-serif; text-decoration: none; font-weight: bold; box-shadow: 0 4px 10px rgba(0,0,0,0.3); font-size: 14px; transition: transform 0.2s;" onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'">← See Other Designs</a>"""

new_button = """
<div style="text-align: center; padding: 40px 20px 80px 20px; position: relative; z-index: 999;">
  <a href="index.html" style="display: inline-block; background: #8a0c1a; color: white; padding: 14px 28px; border-radius: 30px; font-family: sans-serif; text-decoration: none; font-weight: bold; box-shadow: 0 4px 15px rgba(0,0,0,0.4); font-size: 16px; transition: transform 0.2s;" onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'">← See Other Designs</a>
</div>
"""

for file_path in glob.glob('*.html'):
    if file_path == 'index.html':
        continue
        
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Remove old button if it exists
    if old_button in content:
        content = content.replace(old_button, '')
        content = content.replace(old_button + '\n', '')
        
    # If new button is already there, remove it so we can place it cleanly
    if new_button in content:
        content = content.replace(new_button, '')

    # Insert new button in specific locations
    if file_path == 'envelope.html':
        target = '</section>\n  </div>\n\n  <!-- WhatsApp Modal -->'
        if target in content:
            content = content.replace(target, new_button + '\n' + target)
        else:
            # Fallback
            content = content.replace('</body>', new_button + '\n</body>')
    else:
        if '</main>' in content:
            content = content.replace('</main>', new_button + '\n</main>')
        else:
            content = content.replace('</body>', new_button + '\n</body>')
            
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
        
print("Updated all HTML files.")
