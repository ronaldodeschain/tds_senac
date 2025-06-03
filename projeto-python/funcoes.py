import json
import os 
import mensagens as m


def limpa():
    os.system("cls")

def adiciona_contato():
    limpa()
    m.novo_contato()
    contato = {}
    print("Digite o nome do contato: ", end='')
    contato['nome'] = input(" : ")
    print("Digite o idade do contato: ", end='')
    contato['idade'] = input(" : ")
    print("Digite o classe do contato: ", end='')
    contato['classe'] = input(" : ")
    print("Digite o email do contato: ", end='')
    contato['email'] = input(" : ")

    carrega_contatos()

    print(contato)

def carrega_contatos():
    try:
        with open('contatos.json','r',encoding='utf-8') as arq:
            contatos = json.load(arq)
    except FileNotFoundError as erro:
        open('contatos.json','w',encoding='utf-8').close()
        with open('contatos.json','r',encoding='utf-8') as arq:
            contatos = json.load(arq)
    return contatos