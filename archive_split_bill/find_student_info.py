import os
import zipfile
import xml.etree.ElementTree as ET

student_keywords = ["student", "name", "id", "sid", "uid", "unikey", "rumia", "user", "author"]
found_details = []

for root_dir, dirs, files in os.walk("."):
    for file in files:
        if file.endswith((".txt", ".md", ".json")):
            path = os.path.join(root_dir, file)
            try:
                with open(path, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()
                    for kw in student_keywords:
                        if kw in content.lower():
                            found_details.append((path, kw))
            except:
                pass
        elif file.endswith(".docx"):
            path = os.path.join(root_dir, file)
            try:
                with zipfile.ZipFile(path) as z:
                    xml_content = z.read("word/document.xml")
                    content = xml_content.decode('utf-8', errors='ignore')
                    for kw in student_keywords:
                        if kw in content.lower():
                            found_details.append((path, kw))
            except:
                pass

print("=== Found details containing keywords ===")
for p, kw in list(set(found_details))[:30]:
    print(f"File: {p} | Keyword: {kw}")
