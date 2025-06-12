# Escreva um programa em Python que leia uma palavra digitada pelo usuário e:
# 1. informe a quantidade de caracteres da palavra
# 2. exiba cada uma das letra da palavra separadamente
# 3. exiba a palavra ao contrário
# 4. verifique se a palavra digitada é um palíndromo: lida ao contrário é "igual"
# ex: ovo    

palavra = input('Digite uma palavra: ')

print('Você digitou:', palavra)

numeroLetras = len(palavra)
print('Essa palavra possui', numeroLetras, 'letra(s)')

for i in range(numeroLetras):
    print(palavra[i], end=' ')

print()

# cont = numeroLetras - 1
# while cont > -1:
#     print(palavra[cont], end= ' ')
#     cont -= 1

for i in range(numeroLetras-1, -1, -1):
    print(palavra[i], end= ' ')

#  4.
posicaoFinal = numeroLetras - 1
posicaoInicial = 0
palindromo = True
while (posicaoInicial < posicaoFinal and palindromo == True):
    if(palavra[posicaoInicial] != palavra[posicaoFinal]):
        palindromo = False
    posicaoInicial += 1
    posicaoFinal -= 1

print()

if(palindromo == True):
    print('Essa palavra é um palindromo')
else:   
    print('Essa palavra Não é um palindromo')

lista = []
posicao = 0

for i in range(numeroLetras-1, -1, -1):
    lista.insert(posicao, palavra[i])
    posicao += 1

palavraInvertida = ''.join(lista)
# print(lista)
# print(palavraInvertida)

if(palavra == palavraInvertida):
    print('Essa palavra é um palindromo')
else:   
    print('Essa palavra Não é um palindromo') 