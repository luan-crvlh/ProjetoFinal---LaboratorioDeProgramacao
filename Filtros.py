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
    blurred_image = objeto_imagem.imagem.filter(ImageFilter.GaussianBlur(radius=2))  # Redução no raio do desfoque
    edges = objeto_imagem.imagem.filter(ImageFilter.FIND_EDGES).filter(ImageFilter.EDGE_ENHANCE)
    edges = edges.convert("L")  # Certifica-se de que a máscara esteja no modo correto
    combined_image = Image.composite(objeto_imagem.imagem, blurred_image, edges)
    reduced_palette_image = ImageOps.posterize(combined_image, bits=3)
    enhancer = ImageEnhance.Color(reduced_palette_image)
    saturated_image = enhancer.enhance(1.40)  # Saturação ajustada para 1.65
    contrast_enhancer = ImageEnhance.Contrast(saturated_image)
    high_contrast_image = contrast_enhancer.enhance(1.10)  # Contraste ajustado para 1.15
    final_image = ImageEnhance.Sharpness(high_contrast_image).enhance(2.00)  # Sharpness ajustado para 2.25
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
    contorno_image = imagem.filter(ImageFilter.CONTOUR)
    contorno_image = contorno_image.filter(ImageFilter.SHARPEN)  # Aplique o filtro de nitidez
    imagem_gray = imagem.convert("L")
    mascara = imagem_gray.point(lambda x: 255 if x > 128 else 0, mode='1')
    contorno_image_masked = Image.composite(contorno_image, Image.new("RGB", imagem.size, (255, 255, 255)), mascara)
    salvar_imagem(contorno_image_masked, "imagem_filtrada.jpeg")

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