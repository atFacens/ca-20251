
print('1-somar')
print('2-multiplicar')
print('3-subtrair')
print('4-dividir')

numero = input('Digite sua opção: ')

match numero:
    case '1':
        print('somando...')
    case '2':
        print('multiplicando....')
    case '3':
        print('subtraindo....')
    case '4':
        print('dividindo....')
    case _:
        print('opção incorreta')
        


