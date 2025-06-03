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
      print("buscando contato")    
   if opcao == '3':
      print("atualizando contato") 
   if opcao == '4':
      print("apagando contato")
   else:
      print("errado isso ai manin")  
   