d = float(input('Por quantos dias o carro foi alugado? :'))
k = float(input('Qual foi a quantidade de KM percorrido? :'))
p = (k * 0.15) + (d * 60)

print('Com {:.0f} dias e {} KM percorridos o total a pagar é {:.2f}'.format(d, k, p))

