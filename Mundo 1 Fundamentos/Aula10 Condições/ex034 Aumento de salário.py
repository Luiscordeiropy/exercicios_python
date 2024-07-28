s = float(input('Qual é o seu salario?:'))
if s > 1250.00:
    print('Seu salário com o aumento é {}'.format(s + (s * 0.10)))
else:
    print('Seu salario com o aumento é {}'.format(s + (s*0.15)))
