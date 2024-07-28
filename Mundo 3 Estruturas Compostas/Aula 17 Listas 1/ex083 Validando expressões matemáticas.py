lista = list(input('Digite a expressão: '))
if lista.count('(') == lista.count(')'):
    print('Sua expressão está válida')
else:
    print('Sua expressão não está válida')
