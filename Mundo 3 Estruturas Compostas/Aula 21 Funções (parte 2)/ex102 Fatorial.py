def fatorial(numero, show=0):
    '''
    -> Caucula o Fatorial de um número.
    :para numero: O número a ser cauculado
    :para show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    '''
    f = 1
    for c in range(numero, 1, -1):
        f *= c
        if show:
            print(f'{c}x', end='')
            if c == 2:
                print('1 = ', end='')
    return f


print(fatorial(int(input('Digite um número ')), show=True))
help(fatorial)
