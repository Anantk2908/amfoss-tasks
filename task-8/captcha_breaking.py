from PIL import Image

import pytesseract

def captcha_breaking(src):
    pytesseract.pytesseract.tesseract_cmd ='C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'   

    text = pytesseract.image_to_string(Image.open(src))
    return text

print(captcha_breaking("add1.png"))
