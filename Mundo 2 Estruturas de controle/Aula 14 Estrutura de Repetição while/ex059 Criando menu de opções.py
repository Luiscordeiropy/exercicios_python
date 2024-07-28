v = 0
n1 = int(input('\033[32mDigite um valor:'))
n2 = int(input('Digite outro valor:\033[m'))

while v != 5:
     v = int(input('\033[35m[1]somar\n[2]multiplicar\n[3]maior\n[4]novos números\n[5]sair do programa:\033[m'))
     if v in [1, 2, 3, 4, 5]:

         if v == 1:
             print('\033[32m{}'.format(n1+n2))

         elif v == 2:
             print('\033[32m{}'.format(n1*n2))

         elif v == 3:
             if n1 > n2:
                 print('\033[32m{}'.format(n1))
             else:
                print('\033[32m{}\033[m'.format(n2))

         elif v == 4:
             n1 = int(input('\033[32mDigite o 1° novo número:'))
             n2 = int(input('Digite o 2° novo número:'))

     else:
        print('Opção invalida')