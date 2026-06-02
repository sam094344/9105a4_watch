import sys
import pypdf

sys.stdout.reconfigure(encoding='utf-8')

try:
    print("Extracting 介绍页.pdf...")
    reader = pypdf.PdfReader("介绍页.pdf")
    print("=== Page 1 Text ===")
    print(reader.pages[0].extract_text()[:1000])
except Exception as e:
    print("Error:", e)
