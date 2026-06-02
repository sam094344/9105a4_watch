from PIL import Image
import os

img1_path = "带机型照片/1.png"
img2_path = "平面照片/1.PNG"

if os.path.exists(img1_path):
    with Image.open(img1_path) as img:
        print(f"带机型 1.png size: {img.size}")
else:
    print("带机型 1.png not found")

if os.path.exists(img2_path):
    with Image.open(img2_path) as img:
        print(f"平面 1.PNG size: {img.size}")
else:
    print("平面 1.PNG not found")
