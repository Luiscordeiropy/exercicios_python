from random import randint
m = str(input('Escreva "M" se você quer simulação manualmente \nEscreva "A" se quer uma simulação automática')).strip().upper()
if m == 'M':
    sm = float(input('digite a velocidade do carro em KM/h: '))
    if sm >= 80.1:
        print('Você recebeu uma multa de {}R$ SE FERROU!'.format((sm - 80)*7))
    else:
        print('você não recebeu multa! mais azar da proxima vez! 😪😭')
if m == "A":
    r = randint(45, 150)
    if r >= 80.1:
        print('Sua velocidade era de {}KM/H Você tomou uma multa de {}R$ SE FERROU!'.format(r, (r-80)*7))
    else:
        print('Sua velocidade era de {}KM/H Você nao recebeu multa! mais azar da proxima vez!'.format(m))