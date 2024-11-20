from PIL import Image

im=Image.open("templates\certi.png")
print(im.format,im.size,im.mode)
im.show()