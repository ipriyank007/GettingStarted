from PIL import Image

img = Image.open("45.jpg")
print(img.size)
print(img.format)
img.show()