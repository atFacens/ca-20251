
'''
Escreva um programa que leia as notas de vários ? alunos,
calcule a média da turma e exiba uma das mensagens a seguir:
"Parabéns para a turma" - caso a média da turma seja >= 7
"Precisamos melhorar" - caso contrário

'''
# 1. Entrada de dados: ler as notas dos diversos alunos
# 2. Processamento: Calculo da média da turma
# 3. Saída: Exibir uma das mensagens

numeroAlunos = int(input('Quantos alunos serão informados? '))

soma = 0
cont = 1
while cont <= numeroAlunos:
    nota = float(input('Digite a próxima nota: '))
    soma = soma + nota
    cont = cont + 1
    print('nota lida:', nota, 'Soma acumulada:', soma)

media = soma / numeroAlunos
print('Média =', media)

if media >= 7:
    print('Parabéns para a turma')
else:
    print('Precisamos melhorar')