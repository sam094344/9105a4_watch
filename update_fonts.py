import os

file_path = r'c:\Users\rumia\Desktop\9105a4_mobile\index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace fonts globally
content = content.replace("'Outfit', sans-serif", "'Space Grotesk', sans-serif")
content = content.replace("Consolas, Monaco, monospace", "'JetBrains Mono', Consolas, monospace")

# Add colorful borders to pain-point cards
old_css = """        .pain-point-card {
            background: var(--card-bg);
            border: 1px solid var(--card-border);
            border-left: 4.5px solid var(--accent-rust);
            border-radius: 8px;
            padding: 14px 16px;
            box-shadow: var(--shadow-sm);
            transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
        }"""

new_css = """        .pain-point-card {
            background: var(--card-bg);
            border: 1px solid var(--card-border);
            border-left: 4.5px solid var(--accent-rust);
            border-radius: 8px;
            padding: 14px 16px;
            box-shadow: var(--shadow-sm);
            transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
        }
        
        .pain-point-card:nth-child(2) { border-left-color: var(--accent-violet); }
        .pain-point-card:nth-child(3) { border-left-color: var(--accent-cyan); }
        .pain-point-card:nth-child(4) { border-left-color: var(--accent-emerald); }"""

content = content.replace(old_css, new_css)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updates applied successfully.")
