import os
import re

with open("extracted_fig/canvas.fig", "rb") as f:
    data = f.read()

# Let's find all sequences of printable ASCII characters of length >= 4
ascii_strings = re.findall(b"[ -~]{4,100}", data)

# Let's decode and filter them
decoded_strings = []
for s in ascii_strings:
    try:
        decoded_strings.append(s.decode('ascii'))
    except:
        pass

# Let's print unique decoded strings containing common words
print("=== Searching for Title Keywords ===")
seen = set()
for s in decoded_strings:
    s_clean = s.strip()
    if s_clean not in seen and len(s_clean) > 8:
        # Check if it has uppercase letters or typical title words
        if any(w in s_clean for w in ["Hi-Fi", "Fidelity", "Prototype", "Poster", "Split", "Bill", "KTV", "IDEA", "A4"]):
            seen.add(s_clean)
            print(s_clean)
