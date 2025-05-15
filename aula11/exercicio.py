matriz = [ 
        [1, 2, 3], 
        [4, 5, 6], 
        [7, 8, 9] ]


# matriz[0][0] = 1
# matriz[0][1] = 2
# matriz[0][2] = 3
# matriz[1][0] = 4
# matriz[1][1] = 5


for linha in range(3):
    for coluna in range(3):
        print('matriz[', linha, '][', coluna, '] = ', matriz[linha][coluna])


