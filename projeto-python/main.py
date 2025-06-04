import mensagens
import funcoes

while True:
   mensagens.boas_vindas()
   mensagens.menu()
   opcao = input("\n >>> ")

   if opcao == '0':
      mensagens.adios()
      break   
   if opcao == '1':
      funcoes.adiciona_contato()
   if opcao == '2':
      funcoes.busca_contato() 
   if opcao == '3':
      funcoes.alterar_contato()
   if opcao == '4':
      funcoes.apaga_contato()
   else:
      print("errado isso ai manin")  
   input()
   