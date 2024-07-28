from time import sleep
lista = dict()
pessoas = list()


def linha(tam=50):
    print('-' * tam)


def cabeçalho(txt):
    linha()
    print(txt.center(42))
    linha()


def menu(liste):
    cabeçalho('MENU PRICIPAL')
    for e, item in enumerate(liste):
        print(f'\033[33m{e+1}\033[m - \033[34m{item}\033[m')
    linha()


def leiaint(msg):
    while True:
        try:
            return int(input(msg))
        except KeyboardInterrupt:
            print('\033[31m O usuário preferiu não informar os dados!\033[m')
            return 0
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
