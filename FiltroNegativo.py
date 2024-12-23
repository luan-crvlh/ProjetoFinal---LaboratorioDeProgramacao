from Download import Download
import time
import os
import requests
from tqdm import tqdm
from PIL import Image, ImageFilter, ImageOps

baixar = Download()
url = "https://i.ytimg.com/vi/MkIvvPMpxFs/maxresdefault.jpg"
nome_imagem, imagem = baixar.baixarArquivo(url)
imagem.show()
im_invert = ImageOps.invert(imagem)
im_invert.show()