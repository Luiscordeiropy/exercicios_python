from datetime import date
b = int(input('Informe algum ano :'))
if b == 0:
    b = date.today().year
if b % 4 == 0 and b % 100 != 0 or b % 400 == 0:
    print('Esse ano de {} é bissexto!'.format(b))
else:
    print('Esse ano nao é bissexto!')
