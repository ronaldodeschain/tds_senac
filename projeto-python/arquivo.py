# Crie uma função sem parâmetros que exiba "Hello World!".
# def ola():
#  print('Hello World!')

# ola()
# Crie uma função que receba um nome e exiba "Olá, [nome]!".
# def ola(nome):
#     print(f'Ola,{nome}')

# nome = input('digite seu nome ')
# ola(nome)
# Crie uma função que retorne o quadrado de um número.
# def quadrado(n1):
#     quad = n1*n1
#     return quad

# num = 5
# print(quadrado(num))
# Crie uma função que verifique se um número é primo e retorne verdadeiro/falso.

# Crie uma função que receba dois números e retorne o maior deles.
# def eh_maior(n1,n2):
#     if n1 > n2:
#         return f'{n1} é maior'
    
#     return f'{n2} é maior'

# num1 = int(input('digite o primeiro numero: '))
# num2 = int(input('digite o segundo numero: '))

# print(eh_maior(num1,num2))
# Crie uma função que converta minutos para horas e minutos (ex: 125min = 2h05min).
def horas_minutos(minutos):
    print(f'convertido fica:{int(minutos/60)} e {minutos%60} minutos ')

horas = 145
horas_minutos(horas)
# Crie uma função que inverta uma string (ex: "ola" → "alo").