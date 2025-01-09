from Download import *
#import Filtros as Filtros
from Imagem import *
from tkinter import *
from tkinter import filedialog
import os

def criar_janela_principal():
    janela_principal = Tk()
    janela_principal.title("Principal")
    janela_principal.geometry("300x200")
    def criar_sel_imagem():
        criar_janela_escolher_imagem()
        janela_principal.destroy()

    def criar_sel_filtro():
        criar_janela_escolher_filtro()
        janela_principal.destroy()

    botao_selecionar_imagem = Button(janela_principal, text="Selecionar Imagem", command=criar_sel_imagem)
    botao_selecionar_imagem.pack()

    #falta implemantar algo para ao clicar no botão escolher filtro, so deixa entrar 
    #na nova janela para escolher se já tiver selecionado uma imagem
    botao_escolher_filtro = Button(janela_principal, text="Selecionar Filtro", command=criar_sel_filtro)
    botao_escolher_filtro.pack()

    botao_sair = Button(janela_principal, text="Sair", command=janela_principal.destroy)
    botao_sair.pack()

    janela_principal.mainloop()


def criar_janela_path():
    janela_path = Tk()
    janela_path.title("Caminho para salvar Imagem")
    janela_path.geometry("300x100")

    def selecionar_pasta():
        pasta_selecionada = filedialog.askdirectory()

        if not os.path.exists('corrente'):
            os.makedirs('corrente')
        escrever_no_arquivo(pasta_selecionada, 'path.txt')

        janela_path.destroy()  
        criar_janela_principal()
        
    botao_selecionar_pasta = Button(janela_path, text="Selecionar Pasta", command= selecionar_pasta)
    botao_selecionar_pasta.pack(pady=20)

    janela_path.mainloop()

def criar_janela_escolher_imagem():
        janela_escolher_imagem = Tk()
        janela_escolher_imagem.title("Escolher Imagem")
        janela_escolher_imagem.geometry("500x400")
        label = Label(janela_escolher_imagem, text="Escolha entre selecionar a imagem ou escrever o link para download")
        label.pack()
        def selecionar_imagem():
            caminho_imagem = filedialog.askopenfilename()
            escrever_no_arquivo(caminho_imagem, 'imagem.txt')
            #nesse ponto deve ser chamada a função da classe download para executar os métodos sobre a imagem
            voltar(janela_escolher_imagem)

        botao_local = Button(janela_escolher_imagem, text="Selecionar Imagem Local", command=selecionar_imagem)
        botao_local.pack()

        entrada = Entry(janela_escolher_imagem, width=20, font=("Arial", 12))
        entrada.pack(side=LEFT, padx=5)
        def escrever_link():
            link = entrada.get()
            entrada.delete(0,END)
            escrever_no_arquivo(link, 'imagem.txt')
            #Nesse ponto a classe download deve ler o link desse arquivo e baixar a imagem
            voltar(janela_escolher_imagem)

        botao_baixar = Button(janela_escolher_imagem, text="Baixar Imagem", command=escrever_link)
        botao_baixar.pack()

        botao_voltar = Button(janela_escolher_imagem, text="Voltar", command=lambda: voltar(janela_escolher_imagem))
        botao_voltar.pack(pady=10)

def escrever_no_arquivo(arquivo_selecionado, txt):
    try:
        with open(os.path.join('corrente', f'{txt}'), 'w', encoding='utf-8') as file:
            file.write(arquivo_selecionado)
            print(f"Pasta selecionada salva: {arquivo_selecionado}")
    except Exception as e:
        print(f"Erro ao salvar o arquivo: {e}")

def criar_janela_escolher_filtro():
    janela_escolher_filtro = Tk()
    janela_escolher_filtro.title("Escolher Filtro")
    janela_escolher_filtro.geometry("500x600")
    label = Label(janela_escolher_filtro, text="Escolha entre um dos filtros abaixo para aplicar na sua imagem")
    label.pack()

    botao_Negativo = Button(janela_escolher_filtro, text="Filtro Negativo", command=lambda: """aplicar o filtro do backend""")
    botao_Negativo.pack(pady=10)

    botao_Cartoon = Button(janela_escolher_filtro, text="Filtro Cartoon", command=lambda: """aplicar o filtro do backend""")
    botao_Cartoon.pack(pady=10)

    botao_Blurred = Button(janela_escolher_filtro, text="Filtro Blurred", command=lambda: """aplicar o filtro do backend""")
    botao_Blurred.pack(pady=10)

    botao_Contorno = Button(janela_escolher_filtro, text="Filtro Contorno", command=lambda: """aplicar o filtro do backend""")
    botao_Contorno.pack(pady=10)

    botao_Cinza = Button(janela_escolher_filtro, text="Filtro Escala de Cinza", command=lambda: """aplicar o filtro do backend""")
    botao_Cinza.pack(pady=10)

    botao_Preto_Branco = Button(janela_escolher_filtro, text="Filtro Preto e Branco", command=lambda: """aplicar o filtro do backend""")
    botao_Preto_Branco.pack(pady=10)

    botao_voltar = Button(janela_escolher_filtro, text="Voltar", command=lambda: voltar(janela_escolher_filtro))
    botao_voltar.pack(pady=10)

def voltar(janela):
    janela.destroy()
    criar_janela_principal()

criar_janela_path()