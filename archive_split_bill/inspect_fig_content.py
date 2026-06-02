import os

with open("extracted_fig/canvas.fig", "rb") as f:
    header = f.read(100)
    print("Header bytes:", header)
    
# Let's search for strings in canvas.fig
try:
    with open("extracted_fig/canvas.fig", "rb") as f:
        data = f.read()
        import re
        # find ascii words of length 5 to 50
        words = re.findall(b"[a-zA-Z0-9\s\-\:\.\_]{5,50}", data)
        print("Found words count:", len(words))
        # print first 50 unique words
        seen = set()
        unique_words = []
        for w in words:
            w_str = w.decode('ascii', errors='ignore').strip()
            if w_str and w_str not in seen and len(w_str) > 5:
                seen.add(w_str)
                unique_words.append(w_str)
        print("First 100 unique words:", unique_words[:100])
except Exception as e:
    print("Error:", e)
