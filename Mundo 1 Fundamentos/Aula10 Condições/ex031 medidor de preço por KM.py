n = float(input('digite a distancia da sua viagem em KM:'))
if n <= 200:
    print('Você pagará {} pela sua viagem de {}'.format(n * 0.5, n))
else:
    print('Você pagará {} pela sua viagem de {}'.format(n*0.45, n))