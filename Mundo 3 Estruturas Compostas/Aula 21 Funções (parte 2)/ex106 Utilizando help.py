def ajuda():
    n = str(input('Digite um uma função ou biblioteca >'))
    while n not in 'fim':
        print('\033[40m~' * 50)
        print(f'Acessando o manual do comando "{n}"')
        print('~' * 50)
        print('\033[m')
        print('\033[42m')
        help(n)
        print('\033[m')
        n = str(input('Função ou Biblioteca ("fim" para terminar o programa)'))


ajuda()