from datetime import date
lista = {'nome': str(input('Nome: ')),
        'nascimento': date.today().year - int(input('Ano de nascimento: ')),
        'carteira': int(input('Carteira de Trabalho (0 não tem): '))}
if lista['carteira'] != 0:
    lista['contratação'] = int(input('Ano de contratação: '))
    lista['salario'] = float(input('Salário: R$ '))
    lista['aposentadoria'] = date.today().year - lista['contratação'] + 35 + lista['nascimento']
print('-='*35)
print(lista)
for k, v in lista.items():
    print(f'{k} tem o valor {v}')
