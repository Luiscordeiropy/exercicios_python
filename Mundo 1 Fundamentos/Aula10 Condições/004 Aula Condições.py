n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a seugunda nota:'))
m = (n1 + n2)/2
print('A sua média foi {:.1f}'.format(m))
if m >= 6.0:
    print('Sua média foi boa! PARABÉNS!')
else:
    print('sua média foi ruim! ESTUDE MAIS!')
