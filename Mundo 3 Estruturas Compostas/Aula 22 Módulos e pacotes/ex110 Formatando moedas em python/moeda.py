def moeda(valor=0, moeda='R$'):
    return f'{moeda}{valor:.2f}'.replace('.', ',')


def aumentar(n=0, e=0, format1=False):
    res = n * e/100 + n
    return res if format1 is False else moeda(res)


def diminuir(n=0, e=0, format2=False):
    res = n - e/100 * n
    return res if format2 is False else moeda(res)


def dobro(n=0, format3=False):
    res = 2 * n
    return res if format3 is False else moeda(res)


def metade(n, format4=False):
    res = n / 2
    return res if format4 is False else moeda(res)


def resumo(n=0, a=10, d=5):
    print('-'*35)
    print('RESUMO DO VALOR')
    print('-'*35)
    print(f'preço analisado: \t{moeda(n)}')
    print(f'dobro do preço: \t{dobro(n, True)}')
    print(f'Metade do preço: \t{metade(n, True)}')
    print(f'{a}% de aumento: \t{aumentar(n, a, True)}')
    print(f'{d}% de reduçao: \t{diminuir(n, d, True)}')
