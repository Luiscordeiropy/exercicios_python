from time import sleep


def contador(inicio, fim, passo):
    '''

    :param inicio: inicio da contagem
    :param fim: fim da contagem
    :param passo: passo da contagem
    :return: sem retorno
    função criada por Luis PretoCUPreto
    '''
    print(f'Contagem de {inicio} até {fim} em {passo} em {passo}')
    cont = inicio
    if inicio < fim:
        while cont <= fim:
            print(f'{cont}', end=' ')
            cont += passo
            sleep(0.5)
    else:
        while cont >= fim:
            print(f'{cont}', end=' ')
            cont -= passo
            sleep(0.5)
    print('fim!\n')


contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez de personalizar  a contagem:')
contador(int(input('Inicio: ')), int(input('Fim: ')), int(input('Passo: ')))
