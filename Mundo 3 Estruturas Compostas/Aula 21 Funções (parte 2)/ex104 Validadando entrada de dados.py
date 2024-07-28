def leiaint(msg):
    n = input(msg)
    while not n.isnumeric():
        print('\033[31mErro! Digite um número inteiro válido.\033[m')
        n = input(msg)
    return n


n = leiaint('Digite um número')
print(f'Você avabou de digitar o número {n}')
