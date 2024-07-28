l1 = int(input('Digite o valor da 1° reta:'))
l2 = int(input('Digite o valor da 2° reta:'))
l3 = int(input('Digite o valor da 3° reta:'))
if l1 + l2 > l3 and l1 + l3 > l2 and l3 + l2 > l1:
    print('\033[1;32m-='*25)
    print('É possivel formar um triângulo com essas retas!')
    print('-='*25)
    if l1 == l2 == l3:
        print('\033[1;35mEsse triângulo é EQUILÁTERO!')
    elif l1 == l2 !=l3:
        print('\033[1;35mEsse triângulo é ISÓCELES!')
    else:
        print('\033[1;35mEsse triângulo é ESCALENO!')
else:
    print('\033[1;31mNão é possivel fazer um triângulo com essas retas!')