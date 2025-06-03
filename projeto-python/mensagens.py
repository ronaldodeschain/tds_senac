import funcoes as f

def boas_vindas():
    # f.limpa()
    print("Bem vindo a tela inicial do seu Pensebem!")

def adios():
    f.limpa()
    print("hasta luego hermanito!")
    
def menu():
    print('\n\n')
    print('\t1.Adicionar Contato')
    print('\t2.Buscar Contato')
    print('\t3.Alterar Contato')
    print('\t4.Apagar Contato')
    print('\t0.Sair')

def novo_contato():
    print("\n")
    print("adicionando novo contato")