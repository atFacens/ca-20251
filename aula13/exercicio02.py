# escreva um programa que leia uma frase digitada pelo usuário e:
# 1. conte quantas vogais existem na frase
# 2. monte uma nova frase removendo todas as vogais da frase anterior

frase = input('Digite uma frase: ')

numeroLetras = len(frase)

frase = frase.lower()
lista = []
vogais = 0
for i in range(numeroLetras):
   if(frase[i] == 'a' or frase[i] == 'e' or frase[i] == 'i' or frase[i] == 'o' or frase[i] == 'u'):
       vogais += 1
   else:
       lista.append(frase[i])

print('vogais:', vogais)

fraseSemVogais = ''.join(lista)
print('frase sem vogais:', fraseSemVogais)