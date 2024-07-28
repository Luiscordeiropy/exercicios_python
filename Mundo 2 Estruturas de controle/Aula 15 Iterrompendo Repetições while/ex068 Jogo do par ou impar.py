from random import randint
cont = r = p = p1 = 0
while True:
    r = randint(0,10)
    p = int(input('Diga um valor:'))
    i = str(input('Par ou impar? [P/I]'))
    p1 = r + p
    if i in 'Pp':
        if p1 % 2 == 0:
            print('\033[32m-=\033[m' * 30)
            print(f'você jogou {p} e o computador {r}. O total deu {p1}.\n Você ganhou! jogue novamente')
            print('\033[32m-=\033[m' * 30)
            cont += 1
        else:
            break
    if i in 'Ii':
        if p1 % 2 != 0:
            print('\033[32m-=\033[m' * 30)
            print(f'você jogou {p} e o computador {r}. O total deu {p1}.\n Você ganhou! jogue novamente')
            print('\033[32m-=\033[m' * 30)
            cont += 1
        else:
            break
print('Você perdeu!!')
print(f'Você jogou {p} e o computador {r}. O total deu {p1}.Você teve {cont} vitórias consecutivas')