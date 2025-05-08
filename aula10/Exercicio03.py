
# Dado um conjunto contendo o número de itens vendidos em 20 dias de trabalho,
# deseja-se saber:
# - a quantidade total de itens vendidos
# - a media de vendas por dia
# - qual a maior quantidade de itens vendidos

vendas = [20, 21, 30, 15, 10, 12, 22, 25, 9, 32, 40, 15, 23, 43, 32, 11, 9, 7, 10, 12]

# usando o método de soma:
totalVendas = sum(vendas)
print('Total de vendas:', totalVendas)

# sem usar o método de soma:
totalVendas = 0
for i in range(len(vendas)):
    totalVendas = totalVendas + vendas[i]
print('Total de vendas:', totalVendas)

mediaVendas = totalVendas / len(vendas)
print('A média de vendas foi:', mediaVendas)

# procurando o maior valor na lista
maior = vendas[0] # inicia assumindo o primeiro sendo o maior
for venda in vendas:
    if(venda > maior): # se achar alguém maior, esse passa a ser o maior
        maior = venda
print('A maior quantidade de vendas foi', maior)
