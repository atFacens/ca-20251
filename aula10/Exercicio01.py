# Escreva um programa que leia uma lista de nomes de pessoas e exiba os nomes por ordem alfabética
# (dica: append)

pessoas = []

for i in range(5):
   nome = input('Digite o nome:')
   pessoas.append(nome)

pessoas.sort()

print(pessoas)