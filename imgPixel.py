from PIL import Image, ImageDraw
from numpy import asarray
import matplotlib.pyplot as plt


# Regresa un array reducido de pixeles de la imagen
# Recibe como parametro la ruta de la imagen

def imgPixel(img):
    myimg = Image.open(img)
    myimg = myimg.resize((250, 250))

    # pixelart = Image.new('RGB', myimg.size, (255, 255, 255))
    # pixel = myimg.load()

    # print(myimg)
    # print(pixel)
    # print(pixelart)
    # # numpydata2 = asarray(myimg)
    # numpydata2 = asarray(pixelart)
    # return numpydata2

    pequeImg = myimg.resize((40, 40), Image.BILINEAR)
    iSize = (250, 250)
    pixelart = pequeImg.resize(iSize, Image.NEAREST)
    pixelart.save("pixelart.png")
    # Regresa un array de pixeles de la imagen
    # Recibe como parametro la ruta de la imagen
