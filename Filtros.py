from Download import Download
import time 
import os 
import requests 
from tqdm import tqdm 
from PIL import Image, ImageFilter, ImageEnhance, ImageOps, ImageChops
baixar = Download()
class Filtro_Negativo:
    def _init_(self):
#def _init_(self,objeto_imagem):
        self.negativo_file_name = None
        self.negativo_image = None

    def aplicar_filtro(self, url):
    #def aplicar_filtro(self, objeto_imagem):

        nome_imagem, imagem = baixar.baixarArquivo(url)
        imagem.show()
        #Retirar as duas linhas acima

        im_invert = ImageOps.invert(imagem)
        #self.negativo_image = ImageOps.invert(objeto_imagem.imagem)

        im_invert.show()
        #Retirar essa linha acima também

        name = f"negative_{nome_imagem}"
        #self.negativo_file_name = f"negative_{objeto_imagem.name}"

        im_invert.save(name, format=imagem.format)
        #self.negative_image.save(self.negative_file_name)



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