matriz = [ 
        [1, 2, 3], 
        [4, 5, 6], 
        [7, 8, 9] ]


# 1 2 3
# 4 5 6
# 7 8 9


for linha in range(3):
    for coluna in range(3):
        print(matriz[linha][coluna], " ", end="")
    print()