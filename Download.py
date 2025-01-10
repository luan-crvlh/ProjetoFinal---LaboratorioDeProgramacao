import time
import os
import requests
from tqdm import *
from PIL import Image

PROTOCOLOS_SUPORTADOS = ('http', 'https', 'ftp')
FORMATOS = ("PNG", "JPG", "JPEG")

class Download:
    def baixarArquivo(self, url, path):
        timestamp = int(time.time())

        if url.lower().startswith(PROTOCOLOS_SUPORTADOS):
            try:
                # Fazer o download da imagem com barra de progresso
                response = requests.get(url, stream=True)
                response.raise_for_status()
                total_size = int(response.headers.get('content-length', 0))

                # Baixar com barra de progresso
                with open(f"temp_image_{timestamp}", "wb") as file, tqdm(
                    desc="Baixando",
                    total=total_size,
                    unit="B",
                    unit_scale=True,
                    unit_divisor=1024,
                ) as bar:
                    for chunk in response.iter_content(chunk_size=1024):
                        file.write(chunk)
                        bar.update(len(chunk))

                print(f"Imagem baixada como 'temp_image_{timestamp}'.")

                # Abrir a imagem baixada com Pillow
                image = Image.open(f"temp_image_{timestamp}")
                if image.format not in FORMATOS:
                    print(f"Formato {image.format} não é válido. A imagem não será salva.")
                    os.remove(f"temp_image_{timestamp}")
                    raise ValueError
                path_arquivo = path +"\\"+ f"downloaded_image_{timestamp}.{image.format}"
                # Salvar a imagem no caminho desejado
                image.save(path_arquivo, image.format.lower())
                print(f"Imagem salva como '{path_arquivo}'.")

                # Remover o arquivo temporário
                os.remove(f"temp_image_{timestamp}")

                return path_arquivo, image

            except Exception as e:
                print(f"Erro ao baixar a imagem: {e}")
                raise ConnectionError
        else:
            # Tratar como caminho local
            if os.path.exists(url):
                try:
                    image = Image.open(url)
                    print(f"Imagem carregada a partir do caminho local.")

                    if image.format not in FORMATOS:
                        print(f"Formato {image.format} não é válido. A imagem não será salva.")
                        raise TypeError

                    # Salvar a imagem no caminho desejado
                    path_arquivo = path +"\\"+ f"local_image_{timestamp}.{image.format}"
                    image.save(path_arquivo, image.format.lower())
                    return path_arquivo, image
                except Exception as e:
                    print(f"Erro ao carregar a imagem local: {e}")
                    raise TypeError
            else:
                print("Caminho local inválido ou arquivo não encontrado.")
                raise NameError