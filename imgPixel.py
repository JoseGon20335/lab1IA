from PIL import Image, ImageDraw
from numpy import asarray
import matplotlib.pyplot as plt
from numpy import array


# Regresa un array reducido de pixeles de la imagen
# Recibe como parametro la ruta de la imagen

def imgPixel(img):
    myimg = Image.open(img)
    myimg = myimg.resize((250, 250))

    pequeImg = myimg.resize((40, 40), Image.BILINEAR)
    iSize = (70, 70)
    pixelart = pequeImg.resize(iSize, Image.NEAREST)
    resultado = "pixelart.png"
    pixelart.save(resultado)
    im_1 = Image.open(resultado)
    ar = array(im_1)
    x = ar.tolist()
    matrix = []
    salida = []
    entrada = 0
    for i in range(0, len(x), 2):
        temp = []
        for j in range(0, len(x), 2):
            if x[i][j][0] == x[i][j][1] and x[i][j][0] >= 255 or x[i][j][0] >= 250 and x[i][j][1] >= 20 or x[i][j][1] >= 250 and x[i][j][0] >= 20:
                temp.append(0)
            elif x[i][j][1] >= 250 and x[i][j][0] <= 20:
                temp.append(2)
                salida.append((int(i/2), int(j/2)))
            elif x[i][j][0] >= 250 and x[i][j][1] <= 20:
                temp.append(3)
                entrada = (int(i/2), int(j/2))
            else:
                temp.append(1)

        matrix.append(temp)

    return matrix, entrada, salida

