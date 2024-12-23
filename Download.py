import time
import os
import requests
from tqdm import tqdm
from PIL import Image

PROTOCOLOS_SUPORTADOS = ('http', 'https', 'ftp')
FORMATOS = ["PNG", "JPG", "JPEG"]

class Download:
    def baixarArquivo(self, url): # Verifica a origem do arquivo e já retorna o nome do arquivo e um objeto ImageFile correspondente. OBS: NESSA ORDEM!!!!!
        # Gerar um nome único para o arquivo baseado no timestamp
        timestamp = int(time.time())  # Usar o timestamp atual
        file_name = f"downloaded_image_{timestamp}"

        # Verificar se a URL é da internet ou local
        if url.lower().startswith(PROTOCOLOS_SUPORTADOS):
            try:
                # Fazer o download da imagem com barra de progresso
                response = requests.get(url, stream=True)
                response.raise_for_status()

                # Obter o tamanho total do arquivo (em bytes)
                total_size = int(response.headers.get('content-length', 0))

                # Baixar com barra de progresso
                with open(file_name, "wb") as file, tqdm(
                    desc="Baixando",
                    total=total_size,
                    unit="B",
                    unit_scale=True,
                    unit_divisor=1024,
                ) as bar:
                    for chunk in response.iter_content(chunk_size=1024):
                        file.write(chunk)
                        bar.update(len(chunk))

                print(f"Imagem baixada como '{file_name}'.")

                # Abrir a imagem baixada com Pillow
                image = Image.open(file_name)

                # Verificar se o formato é válido
                if image.format not in FORMATOS:
                    print(f"Formato {image.format} não é válido. A imagem não será salva.")
                    os.remove(file_name)  # Remover o arquivo binário inválido
                    return None, None

                # Se o formato for válido, salvar a imagem com o formato correto
                new_file_name = f"{file_name}.{image.format.lower()}"
                image.save(new_file_name, image.format.lower())
                print(f"Imagem salva como '{new_file_name}'.")

                # Remover o arquivo binário
                os.remove(file_name)

                return new_file_name, image

            except Exception as e:
                print(f"Erro ao baixar a imagem: {e}")
                return None, None
        else:
            # Tratar como caminho local
            if os.path.exists(url):
                try:
                    # Abrir a imagem local com Pillow
                    image = Image.open(url)
                    print("Imagem carregada a partir do caminho local.")

                    # Verificar se o formato da imagem local é válido
                    if image.format not in FORMATOS:
                        print(f"Formato {image.format} não é válido. A imagem não será salva.")
                        return None, None

                    return url, image
                except Exception as e:
                    print(f"Erro ao carregar a imagem local: {e}")
                    return None, None
            else:
                print("Caminho local inválido ou arquivo não encontrado.")
                return None, None
"""
# Testar a classe Download
url = input("Digite a URL da imagem ou o caminho local: ")
download = Download()
file_name, imagem = download.baixarArquivo(url)
#foto = Imagem(file_name, imagem) -- Formato básico esperado para criação de objeto da classe Imagem
if imagem:
    # Recarregar a imagem salva no formato correto fora do método baixarArquivo
    imagem = Image.open(file_name)
    # Exibir a imagem
    imagem.show()
"""