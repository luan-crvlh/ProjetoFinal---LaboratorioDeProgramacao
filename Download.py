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

        # Verificar se a URL é da internet ou local
        if url.lower().startswith(PROTOCOLOS_SUPORTADOS):
            try:
                file_path = f"downloaded_image_{timestamp}"
                # Fazer o download da imagem com barra de progresso
                response = requests.get(url, stream=True)
                response.raise_for_status()
                # Obter o tamanho total do arquivo (em bytes)
                total_size = int(response.headers.get('content-length', 0))

                # Baixar com barra de progresso
                with open(file_path, "wb") as file, tqdm(
                    desc="Baixando",
                    total=total_size,
                    unit="B",
                    unit_scale=True,
                    unit_divisor=1024,
                ) as bar:
                    for chunk in response.iter_content(chunk_size=1024):
                        file.write(chunk)
                        bar.update(len(chunk))

                print(f"Imagem baixada como '{file_path}'.")

                # Abrir a imagem baixada com Pillow
                image = Image.open(file_path)
                # Verificar se o formato é válido
                if image.format not in FORMATOS:
                    print(f"Formato {image.format} não é válido. A imagem não será salva.")
                    os.remove(file_path)  # Remover o arquivo binário inválido
                    raise ValueError

                # Se o formato for válido, salvar a imagem com o formato correto
                new_file_path = f"{file_path}.{image.format.lower()}"
                path = rf"C:\Users\Gabri\OneDrive\Documentos\GitHub\ProjetoFinal---LaboratorioDeProgramacao\corrente\{new_file_path}"
                image.save(path, image.format.lower())
                print(f"Imagem salva como '{new_file_path}'.")

                # Remover o arquivo binário
                os.remove(file_path)
                # Pegar apenas o nome do arquivo

                return new_file_path, image

            except Exception as e:
                print(f"Erro ao baixar a imagem: {e}")
                raise ConnectionError
        else:
            # Tratar como caminho local
            if os.path.exists(url):
                try:
                    file_path = f"local_image_{timestamp}"
                    # Abrir a imagem local com Pillow
                    image = Image.open(url)
                    print(f"Imagem carregada como {file_path} a partir do caminho local.")

                    # Verificar se o formato da imagem local é válido
                    if image.format not in FORMATOS:
                        print(f"Formato {image.format} não é válido. A imagem não será salva.")
                        raise TypeError
                    file_path = file_path + f".{image.format.lower()}"
                    path = rf"C:\Users\Gabri\OneDrive\Documentos\GitHub\ProjetoFinal---LaboratorioDeProgramacao\corrente\{file_path}"
                    image.save(path, image.format.lower())
                    return file_path, image
                except Exception as e:
                    print(f"Erro ao carregar a imagem local: {e}")
                    raise TypeError
            else:
                print("Caminho local inválido ou arquivo não encontrado.")
                raise NameError
"""
# Testar a classe Download
url = input("Digite a URL da imagem ou o caminho local: ")
download = Download()
file_path, imagem = download.baixarArquivo(url)
#foto = Imagem(file_path, imagem) -- Formato básico esperado para criação de objeto da classe Imagem
if imagem:
    # Recarregar a imagem salva no formato correto fora do método baixarArquivo
    imagem = Image.open(file_path)
    # Exibir a imagem
    imagem.show()
"""