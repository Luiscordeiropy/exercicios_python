from math import hypot
co = float(input('valor do cateto oposto:'))
ca = float(input('Valor do cateto adjacente:'))
h = hypot(co, ca) #math.sqrt(math.pow(co, 2) + math.pow(ca, 2))
print('o valor da hipotenusa é: {:.0f}'.format(h))