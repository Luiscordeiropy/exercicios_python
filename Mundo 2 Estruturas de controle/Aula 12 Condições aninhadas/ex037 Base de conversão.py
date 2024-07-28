n = int(input('Escreva um número :'))
b = input('Para qual base de conversão você que mudar? (Binário, octal, hexadecimal):').strip().upper()
if b in ('BINARIO, BINÁRIO'):
    print('{}'.format(bin(n)[2:]))
if b in ('OCTAL'):
    print('{}'.format(oct(n)[2:]))
if b in ('hexadecimal'):
    print('{}'.format(hex(n)[2:]))
