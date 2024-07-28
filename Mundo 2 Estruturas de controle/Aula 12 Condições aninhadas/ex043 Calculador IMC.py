altura = float(input('Digite sua altura:'))
peso = float(input('Digite seu peso:'))
imc = peso / (altura ** 2)
print('\033[1;33m-=\033[m'*25)
print('\033[1;33m               Seu IMC é {:.2f}\033[m'.format(imc))
print('\033[1;33m-=\033[m'*25)
if imc < 18.5:
    print('\033[1;31mABAIXO do peso!')
elif imc < 25:
    print('\033[1;35mPeso ideal!')
elif imc < 30:
    print('\033[1;34mSOBREPESO')
elif imc < 40:
    print('\033[1;31mOBESIDADE')
else:
    print('\033[1;31mOBESIDADE MÓRBIDA')

