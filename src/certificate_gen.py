import os
from dotenv import load_dotenv
from PIL import Image,ImageDraw,ImageFont
from pytesseract import pytesseract

load_dotenv()
pytesseract.tesseract_cmd = os.getenv('TESSERACT_CMD')

def test_pytesseract():
    image_path = r'templates\certi.png' 
    image = Image.open(image_path)
    
    data = pytesseract.image_to_data(image, output_type=pytesseract.Output.DICT)
    for i in range(len(data['text'])):
        if "name" in data['text'][i].lower():
            x, y, w, h = data['left'][i], data['top'][i], data['width'][i], data['height'][i]
            print(f"Word 'name' found at position: ({x}, {y}) with width {w} and height {h}")
            
            draw=ImageDraw.Draw(image)
            draw.rectangle([x-50,y,x+w,y+h],fill='white')

            font=ImageFont.truetype("arial.ttf",102)
            new_text = "John Doe"
            bbox = draw.textbbox((0, 0), new_text, font=font)
            text_width = bbox[2] - bbox[0]
            text_height = bbox[3] - bbox[1]
            text_x = x + (w - text_width) // 2
            text_y = y + (h - text_height) // 2
            
            draw.text((text_x, text_y), new_text, font=font, fill="black")

            image.save("output.png")

if __name__ == "__main__":
    test_pytesseract()
