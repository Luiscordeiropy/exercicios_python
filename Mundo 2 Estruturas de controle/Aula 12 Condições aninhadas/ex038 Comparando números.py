n1 = int(input('Digite um número:'))
n2 = int(input('Digite outro número:'))
if n1 > n2:
    print('\033[1;35mO primero valor é MAIOR! {}\033[m'.format(n1))
elif n2 > n1:
    print('\033[1;35mO segundo valor é MAIOR! {}\033[m'.format(n2))
else:
    print('\033[1;35mNÃO EXISTE VALOR MAIOR, os dois são iguais!\033[m')
