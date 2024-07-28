p = float(input('Qual é o preço do produto? R$'))
d = float(input('De quanto é o desconto? %'))
print('O preço com o desconto será {:.2f}'.format(p - p * (d / 100)))
