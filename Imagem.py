from Download import Download
import time
import os
import requests
from tqdm import tqdm
from PIL import Image, ImageFilter, ImageEnhance, ImageOps, ImageChops
#ESSA CLASSE FOI CRIADA PARA TESTE EM FILTROS
class Imagem:
    def __init__(self, nome_imagem, imagem):
        self.imagem = imagem
        self.nome = nome_imagem