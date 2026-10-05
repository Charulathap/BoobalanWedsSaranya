import os
import glob

button_html = """
<div style="text-align: center; padding: 40px 20px 80px 20px; position: relative; z-index: 999;">
  <a href="index.html" style="display: inline-block; background: #8a0c1a; color: white; padding: 14px 28px; border-radius: 30px; font-family: 'Cinzel', 'Marcellus', 'Cormorant Garamond', serif; letter-spacing: 0.05em; text-decoration: none; font-weight: bold; box-shadow: 0 4px 15px rgba(0,0,0,0.4); font-size: 16px; transition: transform 0.2s;" onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'">← See Other Designs</a>
</div>
"""

for file_path in glob.glob('*.html'):
    if file_path == 'index.html':
        continue
        
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Remove the existing button block, handling any extra newlines
    if button_html.strip() in content:
        # Simple removal
        content = content.replace(button_html, '')
        content = content.replace('\n' + button_html.strip() + '\n', '')
        content = content.replace(button_html.strip(), '')

    # Insert the button exactly at the very end (before script block or before </body>)
    # Actually, the safest and cleanest way is to put it immediately before </body> for all except envelope.
    
    if file_path == 'envelope.html':
        target = '</section>\n  </div>\n\n  <!-- WhatsApp Modal -->'
        if target in content:
            content = content.replace(target, button_html + '\n' + target)
        else:
            content = content.replace('</body>', button_html + '\n</body>')
    else:
        # In premium.html, <footer> is outside <main>. In lotus.html, it's inside <main>.
        # We can just put it right after </footer> if it exists.
        # But wait, what if there's no footer? Putting it before </body> works universally because 
        # any modals/fixed buttons before </body> won't affect document flow.
        content = content.replace('</body>', button_html + '\n</body>')
            
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Moved button to the very end of all pages.")
