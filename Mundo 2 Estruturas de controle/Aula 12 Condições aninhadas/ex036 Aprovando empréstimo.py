casa = float(input('Qual o valor da casa?'))
salario = float(input('Qual o seu salário?'))
anos = float(input('Em quantos anos voce vai pagar?'))
max = salario * 0.30
valor = casa / (anos * 12)
if valor <= max:
    print('\033[0;32mSeu finaciamento foi aprovado! O total a pagar nos proximos {} anos em cada mês será: {:.2f}\033[m'.format(anos, valor))
else:
    print('\033[1;31mSinto muito em informar que seu pedido de empréstimo foi negado. De acordo com nossas\npolíticas, o valor do empréstimo não pode exceder 30% do seu salário, que equivale a R${:.2f}. \nComo o valor solicitado é de R$ {:.2f}, não podemos aprovar.\033[m' .format(max, valor))