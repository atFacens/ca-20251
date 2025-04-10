
opcao = 0

while(opcao != '5'):
    print('1-somar')
    print('2-multiplicar')
    print('3-subtrair')
    print('4-dividir')
    print('5-sair')

    opcao = input('Digite sua opção: ')

    match opcao:
        case '1':
            print('somando...')
        case '2':
            print('multiplicando....')
        case '3':
            print('subtraindo....')
        case '4':
            print('dividindo....')
        case '5':
            print('tchau!')
        case _:
            print('opção incorreta')
        


