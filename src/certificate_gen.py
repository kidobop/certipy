import os
from dotenv import load_dotenv
from PIL import Image
from pytesseract import pytesseract

load_dotenv()
pytesseract.tesseract_cmd = os.getenv('TESSERACT_CMD')

def test_pytesseract():
    image_path = 'templates\certi.png' 
    image = Image.open(image_path)
    
    extracted_text = pytesseract.image_to_string(image)
    
    print("Extracted Text:")
    print(extracted_text)

if __name__ == "__main__":
    test_pytesseract()

'''
im=Image.open("templates\certi.png")
print(im.format,im.size,im.mode)
im.show()
'''