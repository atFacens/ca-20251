
candidato1 = 0
candidato2 = 0
candidato3 = 0
candidato4 = 0
nulos = 0
brancos = 0

numero_eleitores = int(input('Quantos eleitores teremos?'))

## Solução com FOR e IF

# for eleitor in range(numero_eleitores):
#    print("1 - 4 voto do candidato, 5 - nulo, 6 - branco:")
#    voto = int(input('Qual o seu voto? '))
   
#    if(voto == 1):
#       candidato1 += 1
#    elif(voto == 2):
#       candidato2 += 1
#    elif(voto == 3):
#       candidato3 += 1
#    elif(voto == 4):
#       candidato4 += 1
#    elif(voto == 5):
#       nulos += 1
#    elif(voto == 6):
#       brancos += 1
#    else:
#       nulos += 1


## Solução com while e match

cont = 0
while(cont < numero_eleitores):
   print("1 - 4 voto do candidato, 5 - nulo, 6 - branco:")
   voto = int(input('Qual o seu voto? '))

   if(voto < 1 or voto > 6):
       print('Opção inválida')
       continue

   match voto:
      case 1:
          candidato1 += 1
      case 2:
          candidato2 += 1
      case 3:
          candidato3 += 1
      case 4:
          candidato4 += 1
      case 5:
          nulos += 1
      case _:
          brancos += 1

   cont += 1


votos_validos = numero_eleitores - nulos

print('-----------------------------')
print(f'Candidato 1: {candidato1} {(candidato1 / votos_validos) * 100} %')
print(f'Candidato 2: {candidato2} {(candidato2 / votos_validos) * 100} %')
print(f'Candidato 3: {candidato3} {(candidato3 / votos_validos) * 100} %')
print(f'Candidato 4: {candidato4} {(candidato4 / votos_validos) * 100} %')
print(f'Brancos: {brancos}')
print(f'Nulos: {nulos}')
print(f'Brancos + Nulos: {((brancos + nulos)/ votos_validos) * 100} %')