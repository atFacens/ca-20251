
lista = [1, 2, 3, 4]

lista[1] = 5

print(lista)

matriz = [ 
        [1, 2, 3], 
        [4, 5, 6], 
        [7, 8, 9] ]

matriz[0][1] = 5

print(matriz)

for linha in range(3):
    for coluna in range(3):
        print(matriz[linha][coluna])
