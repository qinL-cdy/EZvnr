import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'D:\Tesseract-OCR\tesseract.exe'
text = pytesseract.image_to_string(Image.open('d.jpg'),lang='jpn')

for i in text:
    try:
        print(i,end="")
    except:
        continue
