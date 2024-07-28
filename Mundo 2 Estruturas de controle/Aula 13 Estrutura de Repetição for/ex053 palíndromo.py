f = str(input('Escreva um palíndromo')).upper().strip().split()
f1 = (''.join(f))
f3 = f1[::-1]
if f3 == f1:
    print('A frase "{}" é um palíndromo'.format(f1))
else:
    print('A frase "{}" não é um palíndromo'.format(f1))
print(f3)
