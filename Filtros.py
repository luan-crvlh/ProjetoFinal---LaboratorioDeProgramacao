from Download import Download
from Imagem import Imagem
import time
import os
import requests
from tqdm import tqdm
from PIL import Image, ImageFilter, ImageEnhance, ImageOps, ImageChops

baixar = Download()
class Filtro_Negativo:
    #def _init_(self):
    def _init_(self):
        self.negativo_file_name = None
        self.negativo_image = None

    #def aplicar_filtro(self, url):
    def aplicar_filtro_negativo(self, objeto_imagem):

        #nome_imagem, imagem = baixar.baixarArquivo(url)
        objeto_imagem.imagem.show()
        #Retirar as duas linhas acima

        #im_invert = ImageOps.invert(imagem)
        self.negativo_image = ImageOps.invert(objeto_imagem.imagem)
        self.negativo_image.format = objeto_imagem.imagem.format

        #im_invert.show()
        self.negativo_image.show()
        #name = f"negative_{nome_imagem}"
        self.negativo_file_name = f"{objeto_imagem.nome}"

        #im_invert.save(name, format=imagem.format)
        path = rf"C:\Users\luand\OneDrive\Documentos\2024-indefinido\UFPI\2024.2\Laboratorio de Programacao\ProjetoFinal\DataAnalysis---Laboratorio-de-Programacao\corrente\negative_{objeto_imagem.nome}"

        self.negativo_image.save(path, self.negativo_image.format)
"""
if __name__ == "__main__":
  #url = r"C:\Users\luand\OneDrive\Documentos\2024-indefinido\UFPI\2024.2\Estrutura de Dados\PDF's\11895-verde.jpg"
  url = "https://www.aviamentossaopaulo.com.br/octopus/design/images/228/products/b/Botao-4-furos-50-unidades-Amarelo.jpg"
  baixar = Download()
  id, imagem = baixar.baixarArquivo(url)
  atual = Imagem(id, imagem)
  filtro = Filtro_Negativo()
  filtro.aplicar_filtro_negativo(atual)
"""
class Filtro_Cartoon:
  def _init_(self):
  #def _init_(self):
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