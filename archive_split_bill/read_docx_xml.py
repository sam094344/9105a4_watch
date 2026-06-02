import zipfile
import xml.etree.ElementTree as ET

def get_docx_text(path):
    try:
        with zipfile.ZipFile(path) as z:
            xml_content = z.read("word/document.xml")
            root = ET.fromstring(xml_content)
            
            # The XML namespaces for docx
            namespaces = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
            
            text_runs = []
            for para in root.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p'):
                para_text = []
                for run in para.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t'):
                    para_text.append(run.text)
                if para_text:
                    text_runs.append("".join(para_text))
            return text_runs
    except Exception as e:
        return [f"Error: {e}"]

print("=== 介绍页.docx ===")
for p in get_docx_text("介绍页.docx"):
    print(p)

print("\n=== 诉求.docx ===")
for p in get_docx_text("诉求.docx")[:30]:
    print(p)
