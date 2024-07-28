numero_1 = float(input('digite o primeiro número '))
lista = ('soma', 'Subtração', 'Multiplicação', 'Divisão', 'Potenciação', 'Porcentagem', 'Raiz quadrada', )
print('-='*35)
for e, c in enumerate(lista):
    print(f'{c:-<15}[{e+1}]')
print('-='*35)
operacoes = int(input('Digite qual operador você quer utilizar: '))
numero_2 = float(input('digite o segundo número '))
dicionario = numero_1 + numero_2, numero_1 - numero_2, numero_1 ** numero_2, numero_1 / numero_2, numero_1 ** numero_2, numero_1 * (numero_2 / 100), numero_1 ** 1 / numero_2
nu = 0
operacao = ''
for n in range(1, 8):
    if operacoes == n:
        nu = dicionario[n-1]
    if operacoes == n:
        operacao = lista[n-1]
print('-='*35, f'\nO resultado da sua {operacao} é {nu}')
print('-='*35)
