import sys
import pypdf

sys.stdout.reconfigure(encoding='utf-8')

try:
    print("pypdf installed. Extracting...")
    reader = pypdf.PdfReader("IDEA9105 Split Bill Poster Draft VIP (Copy).pdf")
    print("=== Page 1 Text (1000 chars) ===")
    print(reader.pages[0].extract_text()[:1000])
    print("=== Page 2 Text (1000 chars) ===")
    print(reader.pages[1].extract_text()[:1000])
except Exception as e:
    print("Error:", e)
