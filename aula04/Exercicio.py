# Leia um número inteiro digitado pelo usuário
# e informe se esse valor é positivo ou negativo

entrada = input('Digite um número inteiro: ')

numero = int(entrada)

if numero > 0:
    print('esse número é positivo')
else:
    if(numero < 0):
        print('Esse valor é negativo')
    else:
        print('Esse número é zero')