from Download import Download
from Imagem import Imagem
import time
import os
import requests
from tqdm import tqdm
from PIL import Image, ImageFilter, ImageEnhance, ImageOps, ImageChops

baixar = Download()
class Filtro_Negativo:
    def _init_(self):
        self.negativo_file_name = None
        self.negativo_image = None

    #def aplicar_filtro(self, url):
    def aplicar_filtro_negativo(self, objeto_imagem, path):

        objeto_imagem.imagem.show()

        self.negativo_image = ImageOps.invert(objeto_imagem.imagem)

        self.negativo_image.format = objeto_imagem.imagem.format

        self.negativo_image.show()

        self.negativo_file_name = f"{objeto_imagem.nome}"

        self.negativo_image.save(path, self.negativo_image.format)

class Filtro_Cartoon:
  def _init_(self):
    self.cartoon_file_name = None
    self.cartoon_image = None
  def aplicar_filtro_cartoon(self, image, file_name):
  #def aplicar_filtro_cartoon(self, objeto_imagem):
          if image:
            print("Imagem carregada com sucesso pela classe Filtro_Cartoon.")
            # Passo 1: Converter para escala de cinza
            gray_image = image.convert("L")

            # Passo 2: Aplicar um desfoque gaussiano à imagem original
            blurred_image = gray_image.filter(ImageFilter.GaussianBlur(radius=2))  # Diminuiu o desfoque

            # Passo 3: Realçar as bordas com maior intensidade
            edges = gray_image.filter(ImageFilter.FIND_EDGES).filter(ImageFilter.EDGE_ENHANCE_MORE)

            # Passo 4: Combinar as bordas com a imagem colorida
            combined_image = Image.composite(image, image, edges)

            # Passo 5: Reduzir a paleta de cores
            reduced_palette_image = ImageOps.posterize(combined_image, bits=3)

            # Passo 6: Realçar a imagem final
            final_image = ImageEnhance.Sharpness(reduced_palette_image).enhance(2.0)

            if final_image:
              self.cartoon_image = final_image
              self.cartoon_file_name = f"cartoon_{file_name}"
              self.cartoon_image.save(self.cartoon_file_name)
              print("Sucesso na aplicação do filtro cartoon!")
              print(f"Imagem com filtro cartoon salva como '{self.cartoon_file_name}'.")
            else:
              print("Erro ao aplicar o filtro cartoon.")
          else:
            print("Erro ao carregar a imagem.")

          return self.cartoon_image
  
class Filtro_Blurred:
  def __init__(self):
    self.blurred_file_name = None
    self.blurred_image = None

  def aplicar_filtro_blurred(self, objeto_imagem):
     #mostrar imagem sem o filtro
     objeto_imagem.imagem.show()
     
     #aplicar filtro na imagem
     self.blurred_image = objeto_imagem.imagem.filter(ImageFilter.BLUR)
     self.blurred_image.format = objeto_imagem.imagem.format

     #mostrar imagem com filtro
     self.blurred_image.show()

     #salvar imagem com o nome "blured" antes do nome da imagem
     self.blurred_file_name = f"blurred_{objeto_imagem.nome}"
     self.blurred_image.save(self.blurred_file_name)
     
     #path = rf"C:\Users\Gabri\OneDrive\Documentos\GitHub\ProjetoFinal---LaboratorioDeProgramacao\corrente\{objeto_imagem.nome}"     

     #self.blurred_image.save(path, self.blurred_image.format)
class Filtro_Contorno:
    def __init__(self):
        self.contorno_file_name = None
        self.contorno_image = None

    def aplicar_filtro(self, url):
        # Baixar a imagem
        nome_imagem, imagem = baixar.baixarArquivo(url)
        imagem.show(title="Imagem Original")  # Exibir imagem original (opcional)

        # Aplicar o filtro de contorno
        contorno_image = imagem.filter(ImageFilter.CONTOUR)

        # Manter as cores originais ao sobrepor o contorno
        contorno_image_color = ImageChops.multiply(imagem, contorno_image.convert("RGB"))

        # Salvar a imagem com o filtro de contorno no diretório atual
        base_nome_imagem = os.path.basename(nome_imagem)
        self.contorno_file_name = f"contorno_{base_nome_imagem}"
        contorno_image_color.save(self.contorno_file_name, format=imagem.format)

        # Exibir a imagem com o filtro de contorno com o título "FILTROCONTORNO"
        contorno_image_color.show(title="FILTROCONTORNO")

        print(f"Imagem com filtro de contorno salva como '{self.contorno_file_name}'")

class Filtro_PretoBranco:
    def __init__(self):
        self.preto_branco_file_name = None
        self.preto_branco_image = None

    def aplicar_filtro_preto_branco(self, objeto_imagem, limiar=128):
        # Mostrar imagem original
        objeto_imagem.imagem.show()

        # Converter para preto e branco usando um limiar
        self.preto_branco_image = objeto_imagem.imagem.convert("L").point(lambda p: p > limiar and 255, mode='1')
        self.preto_branco_image.format = objeto_imagem.imagem.format

        # Mostrar imagem com filtro
        self.preto_branco_image.show()

        # Salvar imagem com o nome "preto_branco" antes do nome da imagem
        self.preto_branco_file_name = f"preto_branco_{objeto_imagem.nome}"
        self.preto_branco_image.save(self.preto_branco_file_name)

class Filtro_EscalaCinza:
    def __init__(self):
        self.escala_cinza_file_name = None
        self.escala_cinza_image = None

    def aplicar_filtro_escala_cinza(self, objeto_imagem):
        objeto_imagem.imagem.show()
        self.escala_cinza_image = objeto_imagem.imagem.convert("L")
        self.escala_cinza_image.format = objeto_imagem.imagem.format
        self.escala_cinza_image.show()
        self.escala_cinza_file_name = f"escala_cinza_{objeto_imagem.nome}"
        self.escala_cinza_image.save(self.escala_cinza_file_name)

"""
if __name__ == "__main__":
  #url = r"C:\Users\luand\OneDrive\Documentos\2024-indefinido\UFPI\2024.2\Estrutura de Dados\PDF's\11895-verde.jpg"
  url = "https://mobilidade.estadao.com.br/wp-content/uploads/2021/11/carro-por-assinatura-o-ano-todo.jpg"
  id, imagem = baixar.baixarArquivo(url)
  atual = Imagem(id, imagem)
  filtro = Filtro_Blurred()
  filtro.aplicar_filtro_blurred(atual)
  filtro_contorno = Filtro_Contorno()
  filtro_contorno.aplicar_filtro(url_imagem)
"""
