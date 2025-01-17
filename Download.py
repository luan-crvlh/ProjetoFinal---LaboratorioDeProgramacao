import time
import os
import requests
from tqdm import tqdm
from PIL import Image
from converte_png import converter_png_para_jpg

PROTOCOLOS_SUPORTADOS = ('http', 'https', 'ftp')
FORMATOS = ["PNG", "JPG", "JPEG"]

def obter_caminho_salvar():
    try:
        with open('corrente/path.txt', 'r', encoding='utf-8') as file:
            caminho = file.read().strip()
            if not os.path.exists(caminho):
                os.makedirs(caminho)
            return caminho
    except Exception as e:
        print(f"Erro ao ler o caminho de salvamento: {e}")
        raise

def salvar_caminho_imagem(caminho_imagem):
    try:
        with open('corrente/imgpath.txt', 'w', encoding='utf-8') as file:
            file.write(caminho_imagem)
            print(f"Caminho da imagem salvo: {caminho_imagem}")
    except Exception as e:
        print(f"Erro ao salvar o caminho da imagem: {e}")

class Download:
    def baixarArquivo(self, url): # Verifica a origem do arquivo e já retorna o nome do arquivo e um objeto ImageFile correspondente. OBS: NESSA ORDEM!!!!!
        # Gerar um nome único para o arquivo baseado no timestamp
        timestamp = int(time.time())  # Usar o timestamp atual
        caminho_salvar = obter_caminho_salvar()

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
                path = os.path.join(caminho_salvar, new_file_path)
                image.save(path, image.format.lower())
                print(f"Imagem salva como '{new_file_path}'.")

                # Remover o arquivo binário
                os.remove(file_path)


                # Salvar o caminho da imagem em imgpath.txt
                salvar_caminho_imagem(path)

                return new_file_path, image

            except Exception as e:
                print(f"Erro ao baixar a imagem: {e}")
                raise ConnectionError
        else:
            # Tratar como caminho local
            if os.path.exists(url):
                try:
                    # Abrir a imagem local com Pillow
                    image = Image.open(url)
                    print(f"Imagem carregada a partir do caminho local.")

                    # Verificar se o formato da imagem local é válido
                    if image.format not in FORMATOS:
                        print(f"Formato {image.format} não é válido.")
                        raise TypeError

                    # Se o formato for PNG, converter para JPG
                    if image.format == "PNG":
                        image = converter_png_para_jpg(image)
                        new_file_path = f"{os.path.splitext(url)[0]}.jpg"
                        image.save(new_file_path, "JPEG")
                        os.remove(url)
                        salvar_caminho_imagem(new_file_path)
                        return new_file_path, image
                    else:
                        salvar_caminho_imagem(url)
                        return url, image

                except Exception as e:
                    print(f"Erro ao carregar a imagem local: {e}")
                    raise TypeError
            else:
                print("Caminho local inválido ou arquivo não encontrado.")
                raise NameError