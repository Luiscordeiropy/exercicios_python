from math import radians, sin, cos, tan
a = float(input('digite um angulo: '))
rad = radians(a)
seno = sin(rad)
cosseno = cos(rad)
tangente = tan(rad)
print('O valor do seno {:.2f}, cosseno {:.2f} e da tangente {:.2f}'.format(seno, cosseno, tangente))
