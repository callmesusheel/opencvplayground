import PIL
from PIL import Image

basewidth = 300
img = Image.open('result11.png')
print("Size : " + `img.size[0]`)
wpercent = (basewidth/float(img.size[0]))
hsize = int((float(img.size[1])*float(wpercent)))
img = img.resize((basewidth,hsize), PIL.Image.ANTIALIAS)
img.save('sompic.jpg') 