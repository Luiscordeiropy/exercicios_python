termo = int(input('Digite o primeiro termo'))
razao = int(input('Digite a razão'))
p = termo
while p < termo+10*razao:
    print(p, end=' ')
    p += razao
    if p == termo+10*razao:
        n = input('\nVocê quer mostrar mais algum termo?(S/N)')
        if n in 'Ss':
            n1 = int(input('Quantos termos a mais você quer?'))
            p1 = p
            while p1 < termo+(10+n1)*razao:
                print(p1, end=' ')
                p1 += razao
        if n in 'Nn':
            print('Acabou')
