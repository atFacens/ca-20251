# Escreva um programa que leia do teclado 4 valores digitados
# pelo usuário e mostre a soma destes valores

print('Digite 4 números inteiros:')

soma = 0

for i in range(1, 5):
    msg = 'Digite o '+ str(i) + 'º número: '
    numero = int(input(msg))
    soma += numero

print('soma =', soma)
    