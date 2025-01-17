from PIL import Image

def converter_png_para_jpg(image):
    # Converter a imagem para RGBA
    image = image.convert("RGBA")
    # Criar um fundo branco
    background = Image.new("RGB", image.size, (255, 255, 255))
    # Colar a imagem no fundo branco usando a máscara alfa
    background.paste(image, mask=image.split()[3])  # 3 is the alpha channel
    # Converter para JPG
    jpg_image = background.convert("RGB")
    return jpg_image