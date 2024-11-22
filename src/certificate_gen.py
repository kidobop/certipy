import os
from dotenv import load_dotenv
from PIL import Image,ImageDraw
from pytesseract import pytesseract

load_dotenv()
pytesseract.tesseract_cmd = os.getenv('TESSERACT_CMD')

def test_pytesseract():
    image_path = 'templates\certi.png' 
    image = Image.open(image_path)
    
    data = pytesseract.image_to_data(image, output_type=pytesseract.Output.DICT)
    for i in range(len(data['text'])):
        if "name" in data['text'][i].lower():
            x, y, w, h = data['left'][i], data['top'][i], data['width'][i], data['height'][i]
            print(f"Word 'name' found at position: ({x}, {y}) with width {w} and height {h}")
            break

if __name__ == "__main__":
    test_pytesseract()
