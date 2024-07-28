r1 = int(input('Escreva o valor da 1° reta!:'))
r2 = int(input('Escreva o valor da 2°:'))
r3 = int(input('Escreva o valor da 3°'))
if (r1 + r2 > r3) and (r1 + r3 > r2) and (r3 + r2 > r1):
    print('Com essas retas é possivel fazer um triângulo!')
else:
    print('Com essas retas não é possivél fazer uma reta!')
