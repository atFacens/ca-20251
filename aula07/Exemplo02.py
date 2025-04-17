
inicio = int(input('Qual valor inicial? '))
qtde = int(input('Quantos números vc quer? '))

numeros = list(range(inicio, inicio + qtde))

print(numeros)

media = 0
for valor in numeros:
    print('somando o', valor)
    media += valor

media /= qtde
print('média =', media)