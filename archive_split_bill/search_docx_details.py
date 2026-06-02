import zipfile
import xml.etree.ElementTree as ET
import re

def search_details(path):
    try:
        with zipfile.ZipFile(path) as z:
            xml_content = z.read("word/document.xml")
            root = ET.fromstring(xml_content)
            text_runs = []
            for run in root.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t'):
                if run.text:
                    text_runs.append(run.text)
            full_text = "".join(text_runs)
            
            # Find any numbers of length 7-10
            numbers = re.findall(r'\b\d{7,10}\b', full_text)
            # Find any email addresses
            emails = re.findall(r'[\w\.-]+@[\w\.-]+', full_text)
            # Find any english names
            names = re.findall(r'[A-Z][a-z]+ [A-Z][a-z]+', full_text)
            
            print(f"=== {path} ===")
            print("Numbers:", numbers)
            print("Emails:", emails)
            print("Names:", names)
    except Exception as e:
        print("Error:", e)

search_details("介绍页.docx")
search_details("诉求.docx")
