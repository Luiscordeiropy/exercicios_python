s = float(input('Qual é o seu salário? R$'))
d = float(input('De quanto foi o seu aumento? %'))
print('Com o aumento, seu salálario ficou {:.2f}'.format(s + (s * d / 100)))
