def leiaint(msg):
    while True:
        try:
            return int(input(msg))
        except KeyboardInterrupt:
            print('\033[31m O usuário preferiu não informar os dados!\033[m')
            return 0
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')


def leiafloat(msg):
    while True:
        try:
            return float(input(f'{msg}'))
        except KeyboardInterrupt:
            print('\033[31m O usuário preferiu não informar os dados!\033[m')
            return 0
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número real válido. \033[m')


i = leiaint('Digite um número inteiro: ')
f = leiafloat('Digite um número real')
print(f'O valor inteiro digitado foi {i} e o real foi {f}')
