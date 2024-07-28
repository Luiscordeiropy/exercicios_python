def moeda(valor=0, moeda='R$'):
    return f'{moeda}{valor}'.replace('.', ',')


def aumentar(n=0, e=0):
    return n * e/100 + n


def diminuir(n=0, e=0):
    return n - e/100 * n


def dobro(n=0):
    return n * 2


def metade(n):
    return n / 2


