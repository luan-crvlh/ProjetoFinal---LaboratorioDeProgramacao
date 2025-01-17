import os
from PIL import Image, ImageFilter, ImageEnhance, ImageOps, ImageChops
from Imagem import Imagem

def obter_caminho_imagem():
    try:
        with open('corrente/imgpath.txt', 'r', encoding='utf-8') as file:
            caminho_imagem = file.read().strip()
            if os.path.exists(caminho_imagem):
                return caminho_imagem
            else:
                raise FileNotFoundError(f"Caminho da imagem não encontrado: {caminho_imagem}")
    except Exception as e:
        print(f"Erro ao ler o caminho da imagem: {e}")
        raise

def salvar_imagem(imagem, nome):
    try:
        caminho_salvar = os.path.join('corrente', nome)
        imagem.save(caminho_salvar)
        print(f"Imagem salva como '{caminho_salvar}'")
    except Exception as e:
        print(f"Erro ao salvar a imagem: {e}")

def aplicar_filtro_negativo():
    caminho_imagem = obter_caminho_imagem()
    imagem = Image.open(caminho_imagem)
    objeto_imagem = Imagem("imagem_filtrada.jpeg", imagem)
    imagem_negativa = ImageOps.invert(objeto_imagem.imagem)
    salvar_imagem(imagem_negativa, objeto_imagem.nome)

def aplicar_filtro_cartoon():
    caminho_imagem = obter_caminho_imagem()
    imagem = Image.open(caminho_imagem)
    objeto_imagem = Imagem("imagem_filtrada.jpeg", imagem)
    gray_image = objeto_imagem.imagem.convert("L")
    blurred_image = gray_image.filter(ImageFilter.GaussianBlur(radius=2))
    edges = gray_image.filter(ImageFilter.FIND_EDGES).filter(ImageFilter.EDGE_ENHANCE_MORE)
    combined_image = Image.composite(objeto_imagem.imagem, objeto_imagem.imagem, edges)
    reduced_palette_image = ImageOps.posterize(combined_image, bits=3)
    final_image = ImageEnhance.Sharpness(reduced_palette_image).enhance(2.0)
    salvar_imagem(final_image, objeto_imagem.nome)

def aplicar_filtro_blurred():
    caminho_imagem = obter_caminho_imagem()
    imagem = Image.open(caminho_imagem)
    objeto_imagem = Imagem("imagem_filtrada.jpeg", imagem)
    imagem_blurred = objeto_imagem.imagem.filter(ImageFilter.BLUR)
    salvar_imagem(imagem_blurred, objeto_imagem.nome)

def aplicar_filtro_contorno():
    caminho_imagem = obter_caminho_imagem()
    imagem = Image.open(caminho_imagem)
    objeto_imagem = Imagem("imagem_filtrada.jpeg", imagem)
    contorno_image = objeto_imagem.imagem.filter(ImageFilter.CONTOUR)
    contorno_image_color = ImageChops.multiply(objeto_imagem.imagem, contorno_image.convert("RGB"))
    salvar_imagem(contorno_image_color, objeto_imagem.nome)

def aplicar_filtro_preto_branco():
    caminho_imagem = obter_caminho_imagem()
    imagem = Image.open(caminho_imagem)
    objeto_imagem = Imagem("imagem_filtrada.jpeg", imagem)
    preto_branco_image = objeto_imagem.imagem.convert("L").point(lambda p: p > 128 and 255, mode='1')
    salvar_imagem(preto_branco_image, objeto_imagem.nome)

def aplicar_filtro_escala_cinza():
    caminho_imagem = obter_caminho_imagem()
    imagem = Image.open(caminho_imagem)
    objeto_imagem = Imagem("imagem_filtrada.jpeg", imagem)
    escala_cinza_image = objeto_imagem.imagem.convert("L")
    salvar_imagem(escala_cinza_image, objeto_imagem.nome)