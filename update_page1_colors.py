import os

file_path = r'c:\Users\rumia\Desktop\9105a4_mobile\index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add gradient to h1
old_h1 = """        .title-area h1 {
            font-family: 'Playfair Display', serif;
            font-size: 3.3rem;
            font-weight: 900;
            letter-spacing: -0.015em;
            color: var(--text-main);
            line-height: 1.05;
        }"""
new_h1 = """        .title-area h1 {
            font-family: 'Playfair Display', serif;
            font-size: 3.3rem;
            font-weight: 900;
            letter-spacing: -0.015em;
            background: linear-gradient(90deg, var(--text-main) 0%, var(--accent-rust) 50%, var(--accent-violet) 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            line-height: 1.05;
        }"""
content = content.replace(old_h1, new_h1)

# 2. Add color to flow-arrow
old_arrow = """        .flow-arrow {
            color: var(--text-muted);
            font-weight: 900;
            font-size: 1.25rem;
            padding-bottom: 32px;
        }"""
new_arrow = """        .flow-arrow {
            background: linear-gradient(90deg, var(--accent-cyan) 0%, var(--accent-emerald) 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-weight: 900;
            font-size: 1.25rem;
            padding-bottom: 32px;
        }"""
content = content.replace(old_arrow, new_arrow)

# 3. Color page-header-line second span
content = content.replace(
    "<span>KTV Helper Smartwear Companion Poster</span>",
    "<span style=\"color: var(--accent-cyan);\">KTV Helper Smartwear Companion Poster</span>"
)

# 4. Give the watch labels a bit of color
old_watch_label = """        .watch-label {
            font-size: 0.74rem;
            font-weight: 800;
            color: var(--text-main);
            margin-top: 2px;
        }"""
new_watch_label = """        .watch-label {
            font-size: 0.74rem;
            font-weight: 800;
            color: var(--accent-emerald);
            margin-top: 2px;
        }"""
content = content.replace(old_watch_label, new_watch_label)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Page 1 visual tweaks applied.")
