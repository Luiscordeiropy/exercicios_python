def moeda(valor=0, moeda='R$',):
    return f'{moeda}{valor:.2f}'.replace('.', ',')


def aumentar(n=0, e=0, format=False):
    res = n * e/100 + n
    return res if format is False else moeda(res)


def diminuir(n=0, e=0, format=False):
    res = n - e/100 * n
    return res if format is False else moeda(res)


def dobro(n=0, format=False):
    res = n * 2
    return res if format is False else moeda(res)


def metade(n, format=False):
    res = n / 2
    return res if format is False else moeda(res)
