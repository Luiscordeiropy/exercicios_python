v = float(input('\033[1;32mQual o valor do produto?'))
d1 = v - (v * 0.10)
d2 = v - (v * 0.05)
p = str(input('\033[1;32mQual a forma de pagamento? (À vista ou Parcelado) :')).strip().upper()
if 'À VISTA' in p or 'A VISTA' in p or 'AVISTA' in p:
    a = input('\033[1;32mNo dinheiro/cheque ou no cartao? :').strip().upper()
    print('\033[1;37m--'*40)
    if a in 'DINHEIRO DINHEIRO/CHEQUE CHEQUE':
        print('\033[1;35mPara pagamentos à vista em dinheiro ou cheque, oferecemos um desconto de 10%.\nPortanto, o valor de R${} será reduzido para R${}\033[m'.format(v, d1))
    if a in 'CARTÃO CARTAO':
        print('\033[1;35mpara pagamentos à vista no cartão, oferecemos um desconto de 5%. \nPortanto, o valor de R${} será reduzido para R${}\033[m'.format(v, d2))
    print('\033[1;37m--'*40)
if p == 'PARCELADO':
    x = str(input('\033[1;32mEm quantas vezes você quer parcelar? (disponiveis: 2x ou 3x ou mais) :')).upper()
    print('\033[1;37m--'*40)
    if x in '2 2x 2X ':
        print('\033[1;35mPara pagamentos parcelados no cartão, não tem adicional de juros e fica com o preço normal.\nPortanto o valor parcelado será 2x de R${}'.format(v/2))
    if x in '3 3x 3X 3x OU MAIS':
        par = int(input('Quantas parcelas?'))
        print('\033[1;35mPara pagamentos parcelados no cartão, tem um custo adicional de 20% de juros.\nPortanto, o valor de R${} será {} vezes de R${}'.format(v, par, (v+(v * 0.20))/par))
    print('\033[1;37m--'*40)