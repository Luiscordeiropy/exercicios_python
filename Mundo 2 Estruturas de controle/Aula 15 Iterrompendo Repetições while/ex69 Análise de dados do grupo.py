cont = contm = contf = 0
while True:
    print('CADASTRE UMA PESSOA')
    while True:
        try:
            i = int(input('Idade: '))
            break
        except ValueError:
            print("Por favor, insira um número.")
    s = 'g'
    while s not in 'FfMm':
        s = str(input('Sexo [F/M]\n'))
    q = 0
    if i >= 18:
        cont += 1
    if s in "Mm":
        contm += 1
    if s in "Ff" and i < 20:
        contf += 1
    while q != 'S' and q != 'N':
        q = str(input('Quer continuar?[S/N]')).upper()
    if q in "Nn":
        break
print(f'Total de pessoas com mais de 18 anos: {cont}\nAo todo temos {contm} homens cadastrados\nE temos {contf} mulhere(s) com menos de 20')
