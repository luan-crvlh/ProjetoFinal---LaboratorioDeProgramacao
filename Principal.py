from Download import *
from Filtros import *
from Imagem import *
from tkinter import *
from tkinter import filedialog
import os
import time
from datetime import datetime
from PIL import Image, ImageTk

def criar_janela_principal():
    janela_principal = Tk()
    janela_principal.title("Simple Lens")
    janela_principal.geometry("350x600")

    def on_closing():
        try:
            caminho_imagem_filtrada = os.path.join('corrente', 'imagem_filtrada.jpeg')
            if os.path.exists(caminho_imagem_filtrada):
                os.remove(caminho_imagem_filtrada)
                print(f"Imagem filtrada '{caminho_imagem_filtrada}' apagada.")
        except Exception as e:
            print(f"Erro ao apagar a imagem filtrada: {e}")
        janela_principal.destroy()

    janela_principal.protocol("WM_DELETE_WINDOW", on_closing)

    # Carregar a logo
    try:
        logo_path = "logo.png"
        logo_image = Image.open(logo_path)
        logo_image.thumbnail((200, 200))  # Redimensionar a logo para miniatura
        logo_image_tk = ImageTk.PhotoImage(logo_image)

        label_logo = Label(janela_principal, image=logo_image_tk)
        label_logo.image = logo_image_tk  # Manter uma referência da imagem
        label_logo.pack(pady=34)
    except Exception as e:
        Label(janela_principal, text=f"Erro ao carregar a logo: {e}").pack(pady=10)

    nomemenu = Label(janela_principal, text="MENU", relief=FLAT)
    nomemenu.pack(pady=3)

    def selecionar_pasta():
        pasta_selecionada = filedialog.askdirectory()

        if not os.path.exists('corrente'):
            os.makedirs('corrente')
        escrever_no_arquivo(pasta_selecionada, 'path.txt')

    def criar_sel_imagem():
        janela_principal.destroy()
        criar_janela_escolher_imagem()
        janela_principal.destroy()

    def criar_sel_filtro():
        janela_principal.destroy()
        criar_janela_escolher_filtro()
        janela_principal.destroy()

    def criar_janela_arquivos():
        janela_arquivos = Tk()
        janela_arquivos.title("Arquivos")
        janela_arquivos.geometry("350x600")
        janela_principal.destroy()


        try:
            with open('corrente/path.txt', 'r', encoding='utf-8') as file:
                caminho_pasta = file.read().strip()

            if os.path.exists(caminho_pasta):
                arquivos = os.listdir(caminho_pasta)
                if arquivos:
                    for arquivo in arquivos:
                        Label(janela_arquivos, text=arquivo).pack()
                else:
                    Label(janela_arquivos, text="Nenhum arquivo encontrado.").pack()
            else:
                Label(janela_arquivos, text="Caminho da pasta não encontrado.").pack()
        except Exception as e:
            Label(janela_arquivos, text=f"Erro ao ler a pasta: {e}").pack()

        botao_voltar = Button(janela_arquivos, text="Voltar", command=lambda: (voltar(janela_arquivos)), relief=SOLID)
        botao_voltar.pack(pady=20)

        janela_arquivos.mainloop()

    botao_selecionar_pasta = Button(janela_principal, text="Nova Pasta", command=selecionar_pasta, relief=SOLID)
    botao_selecionar_pasta.pack()

    botao_selecionar_imagem = Button(janela_principal, text="Buscar Imagem", command=criar_sel_imagem, relief=SOLID)
    botao_selecionar_imagem.pack(pady=3)

    botao_escolher_filtro = Button(janela_principal, text="Aplicar Filtros", command=criar_sel_filtro, relief=SOLID)
    botao_escolher_filtro.pack()

    botao_visualizar_pasta = Button(janela_principal, text="Arquivos", command=criar_janela_arquivos, relief=SOLID)
    botao_visualizar_pasta.pack(pady=3)

    botao_sair = Button(janela_principal, text="Sair", command=on_closing, relief=SOLID)
    botao_sair.pack(pady=30)

    janela_principal.mainloop()

def criar_janela_visualizar_imagem(caminho_imagem):
    janela_visualizar_imagem = Tk()
    janela_visualizar_imagem.title("Visualizar Imagem")
    janela_visualizar_imagem.geometry("350x600")

    try:
        imagem = Image.open(caminho_imagem)
        imagem.thumbnail((320, 320))  # Redimensionar a imagem para miniatura
        imagem_tk = ImageTk.PhotoImage(imagem)

        label_imagem = Label(janela_visualizar_imagem, image=imagem_tk)
        label_imagem.image = imagem_tk  # Manter uma referência da imagem
        label_imagem.pack(pady=10)
    except Exception as e:
        Label(janela_visualizar_imagem, text=f"Erro ao carregar a imagem: {e}").pack(pady=10)

def criar_janela_path():
    janela_path = Tk()
    janela_path.title("Simple Lens")
    janela_path.geometry("350x600")

    logo_path = "logo.png"
    logo_image = Image.open(logo_path)
    logo_image.thumbnail((200, 200))  # Redimensionar a logo para miniatura
    logo_image_tk = ImageTk.PhotoImage(logo_image)

    label_logo = Label(janela_path, image=logo_image_tk)
    label_logo.image = logo_image_tk  # Manter uma referência da imagem
    label_logo.pack(pady=34)

    def selecionar_pasta():
        pasta_selecionada = filedialog.askdirectory()

        if not os.path.exists('corrente'):
            os.makedirs('corrente')
        escrever_no_arquivo(pasta_selecionada, 'path.txt')

        janela_path.destroy()
        criar_janela_principal()

    botao_selecionar_pasta = Button(janela_path, text="Selecionar Pasta", command=selecionar_pasta, relief=SOLID)
    botao_selecionar_pasta.pack(pady=50)

    inicializando = Label(janela_path, text="inicializando...", relief=FLAT)
    inicializando.pack(pady=10)

    janela_path.mainloop()

def criar_janela_escolher_imagem():
    janela_escolher_imagem = Tk()
    janela_escolher_imagem.title("Escolher Imagem")
    janela_escolher_imagem.geometry("350x600")
    label = Label(janela_escolher_imagem, text=" ")
    label.pack(pady=100)

    def selecionar_imagem():
        caminho_imagem = filedialog.askopenfilename()
        if caminho_imagem:
            download = Download()
            try:
                file_path, imagem = download.baixarArquivo(caminho_imagem)
                escrever_no_arquivo(file_path, 'imagem.txt')
                label_mensagem.config(text="Imagem salva!")
                janela_escolher_imagem.after(4000, lambda: label_mensagem.config(text=""))
                janela_escolher_imagem.destroy()
                criar_janela_escolher_filtro()
            except Exception as e:
                aviso = Toplevel(janela_escolher_imagem)
                aviso.title("Erro")
                Label(aviso, text=f"Erro ao salvar a imagem: {e}").pack(pady=10)
                Button(aviso, text="OK", command=aviso.destroy).pack(pady=5)

    botao_local = Button(janela_escolher_imagem, text="Selecione uma imagem local", command=selecionar_imagem, relief=SOLID)
    botao_local.pack()

    botao_local = Label(janela_escolher_imagem, text="ou...", relief=FLAT)
    botao_local.pack()

    entrada = Entry(janela_escolher_imagem, width=23, font=("Arial", 12), relief=GROOVE)
    entrada.pack(pady=10)

    def escrever_link():
        link = entrada.get()
        entrada.delete(0, END)
        download = Download()
        try:
            file_path, imagem = download.baixarArquivo(link)
            escrever_no_arquivo(file_path, 'imagem.txt')
            label_mensagem.config(text="Imagem salva!")
            janela_escolher_imagem.after(3000, lambda: label_mensagem.config(text=""))
        except Exception as e:
            aviso = Toplevel(janela_escolher_imagem)
            aviso.title("Erro")
            Label(aviso, text=f"Erro ao baixar a imagem: {e}").pack(pady=10)
            Button(aviso, text="OK", command=aviso.destroy).pack(pady=5)

    textoinsira = Label(janela_escolher_imagem, text="Insira endereço de imagem da web", relief=FLAT)
    textoinsira.pack()

    botao_baixar = Button(janela_escolher_imagem, text="Buscar", command=escrever_link, relief=RAISED)
    botao_baixar.pack()

    label_mensagem = Label(janela_escolher_imagem, text="", fg="green")
    label_mensagem.pack(pady=10)

    botao_voltar = Button(janela_escolher_imagem, text="Voltar", command=lambda: voltar(janela_escolher_imagem), relief=SOLID)
    botao_voltar.pack(pady=60)

    janela_escolher_imagem.mainloop()

def escrever_no_arquivo(arquivo_selecionado, txt):
    try:
        with open(os.path.join('corrente', f'{txt}'), 'w', encoding='utf-8') as file:
            file.write(arquivo_selecionado)
            print(f"Pasta selecionada salva: {arquivo_selecionado}")
    except Exception as e:
        print(f"Erro ao salvar o arquivo: {e}")

def salvar_img():
    try:
        with open('corrente/path.txt', 'r', encoding='utf-8') as file:
            caminho_pasta = file.read().strip()

        if os.path.exists(caminho_pasta):
            caminho_imagem_filtrada = os.path.join('corrente', 'imagem_filtrada.jpeg')
            imagem = Image.open(caminho_imagem_filtrada)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filtro_nome = "filtro"  # Define filtro_nome here
            nome_arquivo = f"{filtro_nome}_{timestamp}.jpeg"
            caminho_salvar = os.path.join(caminho_pasta, nome_arquivo)
            imagem.save(caminho_salvar)
            print(f"Imagem filtrada salva em: {caminho_salvar}")
        else:
            print("Caminho da pasta não encontrado.")
    except Exception as e:
        print(f"Erro ao salvar a imagem filtrada: {e}")

def criar_janela_escolher_filtro():

    def chamar_seleção():
        janela_escolher_filtro.destroy()
        criar_janela_escolher_imagem()

    def atualizar_imagem(caminho_imagem):
        imagem = Image.open(caminho_imagem)
        imagem = ImageOps.expand(imagem, border=10, fill='silver')
        imagem.thumbnail((290, 290))
        imagem_tk = ImageTk.PhotoImage(imagem)
        label_imagem.config(image=imagem_tk)
        label_imagem.image = imagem_tk

    def exibir_original():
        with open(os.path.join('corrente', 'imgpath.txt'), 'r', encoding='utf-8') as file:
            caminho_imagem = file.read().strip()

        imagem = Image.open(caminho_imagem)
        imagem = ImageOps.expand(imagem, border=10, fill='silver')
        imagem.thumbnail((290, 290))
        imagem_tk = ImageTk.PhotoImage(imagem)
        label_imagem.config(image=imagem_tk)
        label_imagem.image = imagem_tk

    janela_escolher_filtro = Tk()
    janela_escolher_filtro.title("Escolher Filtro")
    janela_escolher_filtro.geometry("350x600")

    # Carregar a imagem de imgpath.txt
    try:
        with open(os.path.join('corrente', 'imgpath.txt'), 'r', encoding='utf-8') as file:
            caminho_imagem = file.read().strip()

        imagem = Image.open(caminho_imagem)
        imagem = ImageOps.expand(imagem, border=10, fill='silver')
        imagem.thumbnail((290, 290))  # Redimensionar a imagem para miniatura
        imagem_tk = ImageTk.PhotoImage(imagem)

        label_imagem = Label(janela_escolher_filtro, image=imagem_tk)
        label_imagem.image = imagem_tk  # Manter uma referência da imagem
        label_imagem.pack(pady=10)
    except Exception as e:
        Label(janela_escolher_filtro, text=f"Erro ao carregar a imagem: {e}").pack(pady=10)

    botao_selecionar_imagem = Button(janela_escolher_filtro, text="Selecionar nova imagem", command=chamar_seleção, relief=SOLID)
    botao_selecionar_imagem.pack(pady=3)

    frame_botoes = Frame(janela_escolher_filtro)
    frame_botoes.pack(pady=10)

    botao_salvar = Button(frame_botoes, text="Salvar", command=lambda: (salvar_img()), relief=RAISED, width=20)
    botao_salvar.grid(row=0, column=0)

    botao_desfazer = Button(frame_botoes, text="Desfazer Filtro", command=lambda: (exibir_original()), relief=RAISED, width=20)
    botao_desfazer.grid(row=0, column=1)

    label_filtro = Label(janela_escolher_filtro, text="FILTROS", relief=FLAT)
    label_filtro.pack(pady=5)

    frame_botoes_filtro = Frame(janela_escolher_filtro)
    frame_botoes_filtro.pack()

    botao_Cinza = Button(frame_botoes_filtro, text="Escala de Cinza", command=lambda: (aplicar_filtro_escala_cinza(), atualizar_imagem("corrente/imagem_filtrada.jpeg")), relief=RAISED, width=14)
    botao_Cinza.grid(row=0, column=0)

    botao_Preto_Branco = Button(frame_botoes_filtro, text="Preto e Branco", command=lambda: (aplicar_filtro_preto_branco(), atualizar_imagem("corrente/imagem_filtrada.jpeg")), relief=RAISED, width=14)
    botao_Preto_Branco.grid(row=1, column=0)

    botao_Negativo = Button(frame_botoes_filtro, text="Negativo", command=lambda: (aplicar_filtro_negativo(), atualizar_imagem("corrente/imagem_filtrada.jpeg")), relief=RAISED, width=12)
    botao_Negativo.grid(row=0, column=1)

    botao_Cartoon = Button(frame_botoes_filtro, text="Cartoon", command=lambda: (aplicar_filtro_cartoon(), atualizar_imagem("corrente/imagem_filtrada.jpeg")), relief=RAISED, width=12)
    botao_Cartoon.grid(row=0, column=2)

    botao_Blurred = Button(frame_botoes_filtro, text="Blurred", command=lambda: (aplicar_filtro_blurred(), atualizar_imagem("corrente/imagem_filtrada.jpeg")), relief=RAISED, width=12)
    botao_Blurred.grid(row=1, column=1)

    botao_Contorno = Button(frame_botoes_filtro, text="Contorno", command=lambda: (aplicar_filtro_contorno(), atualizar_imagem("corrente/imagem_filtrada.jpeg")), relief=RAISED, width=12)
    botao_Contorno.grid(row=1, column=2)

    botao_voltar = Button(frame_botoes_filtro, text="Voltar", command=lambda: voltar(janela_escolher_filtro), relief=RAISED, width=40)
    botao_voltar.grid(row=2, column=0, columnspan=3, pady=40)

    janela_escolher_filtro.mainloop()

def voltar(janela):
    janela.destroy()
    criar_janela_principal()

criar_janela_path()