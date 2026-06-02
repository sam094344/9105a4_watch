import sys

# Set output to utf-8
sys.stdout.reconfigure(encoding='utf-8')

with open("poster_text.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

print("=== First 50 lines of poster_text.txt ===")
for i in range(min(100, len(lines))):
    line_clean = lines[i].replace('\u2028', ' ').strip()
    print(f"{i+1}: {line_clean}")

print("\n=== Search for headings ===")
for i, l in enumerate(lines):
    l_clean = l.replace('\u2028', ' ').strip()
    if len(l_clean) > 5 and len(l_clean) < 100:
        if any(keyword in l_clean for keyword in ["Prototype", "KTV", "Split", "Bill", "IDEA", "A4", "Title"]):
            print(f"Line {i+1}: {l_clean}")
