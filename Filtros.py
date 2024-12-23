from Download import Download
import cv2
import time
import os
import requests
from tqdm import tqdm
from PIL import Image, ImageFilter, ImageOps, ImageChops, ImageEnhance

url = "https://tribunadejundiai.com.br/wp-content/uploads/2023/05/607B2DAC-3D4A-463E-828A-D26A9C76498F.jpeg"
baixar = Download()
class Negativo:
    def aplicar_filtro(self, url):
        nome_imagem, imagem = baixar.baixarArquivo(url)
        imagem.show()
        im_invert = ImageOps.invert(imagem)
        im_invert.show()
        name = f"negative_{nome_imagem}.{imagem.format}"
        im_invert.save(name, format=imagem.format)

class Cartoon:
    # Função para aplicar o filtro Cartoon
    def cartoon_filter(self, url):
        # Baixar a imagem
        nome_imagem, imagem = baixar.baixarArquivo(url)
        if imagem is None:
            print("Erro ao carregar a imagem.")
            return None

        # Exibir a imagem original para comparação
        imagem.show(title="Imagem Original")

        # Passo 1: Reduzir o ruído na imagem usando desfoque
        smoothed_image = imagem.filter(ImageFilter.GaussianBlur(radius=3))

        # Passo 2: Converter para escala de cinza
        gray_image = smoothed_image.convert("L")

        # Passo 3: Detectar bordas (FIND_EDGES) e aumentar contraste
        edges = gray_image.filter(ImageFilter.FIND_EDGES)
        edges = edges.point(lambda x: 255 if x > 50 else 0)  # Binarização das bordas

        # Passo 4: Suavizar as bordas
        edges_smooth = edges.filter(ImageFilter.SMOOTH_MORE)

        # Passo 5: Realçar a saturação e contraste da imagem original
        enhanced_image = ImageEnhance.Color(imagem).enhance(1.7)  # Aumentar a saturação
        enhanced_image = ImageEnhance.Contrast(enhanced_image).enhance(1.4)  # Melhorar o contraste

        # Passo 6: Combinar as bordas com a imagem realçada
        cartoon_image = Image.composite(enhanced_image, Image.new("RGB", imagem.size, "white"), edges_smooth)

        # Exibir e retornar a imagem final
        cartoon_image.show(title="Filtro Cartoon")
        return cartoon_image


# Aplicando o filtro cartoon
a = Cartoon()
imagem = a.cartoon_filter(url)