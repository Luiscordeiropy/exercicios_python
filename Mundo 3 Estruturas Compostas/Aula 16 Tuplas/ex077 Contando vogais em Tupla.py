palavras = ('aprender', 'programar', 'linguagem', 'pythonm', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')
a = 'a'
e = 'e'
i = 'i'
o = 'o'
u = 'u'
vogais = a
for palavra in palavras:
    print(f'\nNa palavra {palavra.upper()} temos', end=' ')
    cont = 0
    while True:
        if cont == 0:
            vogais = a
        cont += 1
        vezes = palavra.count(vogais)
        if vezes >0:
            print(f'{vogais} '* vezes, end='')
        if cont == 1:
            vogais = e
        if cont == 2:
            vogais = i
        if cont == 3:
            vogais = o
        if cont == 4:
            vogais = u
        if cont == 5:
            break



