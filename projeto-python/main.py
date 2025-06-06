import tkinter as tk
import os
from tkinter.filedialog import askopenfilename, asksaveasfile

def abre_arquivo():
    arq_caminho = askopenfilename()
    print(f'{arq_caminho= }')
    with open(arq_caminho,mode='r',encoding='utf-8') as arq:
        conteudo = ''
        for linha in arq.readlines():
            conteudo += linha

    caixa_texto.delete('1.0','end')
    caixa_texto.insert('1.0',conteudo)

def novo_arquivo():
    caixa_texto.delete('1.0','end')

def salva_arquivo():
    conteudo = caixa_texto.get('1.0','end')
    print(f'{conteudo= }')
    arquivo = asksaveasfile()
    arquivo.write(conteudo)
    arquivo.close()
janela = tk.Tk()
janela.title('uma janela, azul caneta')
janela.geometry('400x400')
janela.resizable(False,False)

#widgets
#menu, Text area
menu_principal = tk.Menu(janela)
janela.config(menu=menu_principal)

menu_arquivo = tk.Menu(menu_principal,tearoff=0)
menu_principal.add_cascade(label='arquivo',menu=menu_arquivo)
menu_arquivo.add_command(label='Novo',command=novo_arquivo)
menu_arquivo.add_command(label='Abrir',command=abre_arquivo)
menu_arquivo.add_command(label='Salvar',command=salva_arquivo)
menu_arquivo.add_separator()
menu_arquivo.add_command(label='Sair',command=janela.quit)

caixa_texto = tk.Text(janela,font=('Arial',23))
caixa_texto.pack()


janela.mainloop()