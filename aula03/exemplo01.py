# comentário de linha

'''

Comentário de bloco

autor:
data:

'''

# Operadores aritméticos: + - * / 

print(2 + 5 * 5)
print((2 + 5) * 5)
print((2.0 + 5) * 5)

# Operadores relacionais > >= < <= != ==

print(5 > 2)
print(5 >= 5)
print(5 != 5)
print(5 == 5)

print('--------')

print( 2 + 3 < 4 - 2)

# Operadores lógicos: E (and) OU (or) Não (not)

# 1. encontrar 2 chaves
# 2. pontos 100

# passar de fase: 1 E 2
# passar de fase: 1 OU 2

encontrou = False
pontos = 50

print('---game---')
print(encontrou and pontos >= 100)
print(encontrou or pontos >= 100)

print('Fica na fase atual', not encontrou)