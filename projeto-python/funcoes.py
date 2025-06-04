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

    lista = [contato]
    contatos = carrega_contatos()
    contatos['contatos'].append(contato)

    print(contato)
    print(contatos)

def busca_contato():
     limpa()
     m.busca_contato()
     nome_alvo = input(" >>> ")

     contatos = carrega_contatos() 
     for item in contatos['contatos']:
          if nome_alvo == item['nome']:
               print(f'{item= }')
     else:
          print("alvo não encontrado! Deve ter fugido òÓ")

def carrega_contatos():
    try:
        with open('contatos.json','r',encoding='utf-8') as arq:
            contatos = json.load(arq)
    except FileNotFoundError as erro:
            contatos = {'contatos':[]}
    return contatos

def salva_contatos(contatos):
     with open('contatos.json','a',encoding='utf-8') as arq:
          json.dump(contatos,arq, indent=2)

def alterar_contato():
    limpa()
    m.alterar_contato()
    nome_consulta = input(" >>> ")

    contatos= carrega_contatos()
    for indice, item in enumerate(contatos['contatos']):
         if nome_consulta == item['nome']:
              print(f'{item= }')
              novo_nome = input("nome: ")
              nova_idade = input("idade: ")
              nova_classe = input("classe: ")
              novo_email = input("email: ")
              
              novo_dado = {'nome':novo_nome,'idade':nova_idade,'classe':nova_classe,'email':novo_email}
              contatos['contatos'][indice] = novo_dado

def apaga_contato():
    limpa()
    m.apaga_contato()
    nome_consulta = input(" >>> ")

    contatos = carrega_contatos()
    for item in contatos['contatos']:
         if nome_consulta == item['nome']:
              contatos['contatos'].remove(item)
              salva_contatos(contatos)
              break
    else:
         print("alvo está inalcançavel!")