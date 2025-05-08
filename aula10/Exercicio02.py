# Dado um conjunto de valores representando as idades de pessoas que visitaram uma exposição
# calcular o número de adultos (idade >=18 ) e o número de crianças (idade < 18)


idades = [23, 34, 12, 16, 45, 23, 11, 56, 33, 10]

numeroAdultos = 0
numeroCriancas = 0

# for i in range(len(idades)):
#     if(idades[i] >= 18):
#         numeroAdultos += 1
#     else:
#         numeroCriancas += 1

# print('Tivemos', numeroAdultos, 'adultos')
# print('Tivemos', numeroCriancas, 'crianças')

for idade in idades:
    if(idade >= 18):
        numeroAdultos += 1
    else:
        numeroCriancas += 1

print('Tivemos', numeroAdultos, 'adultos')
print('Tivemos', numeroCriancas, 'crianças')