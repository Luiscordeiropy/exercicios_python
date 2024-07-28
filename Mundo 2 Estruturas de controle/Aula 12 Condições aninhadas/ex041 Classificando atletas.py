from datetime import date
n = int(input('Digite a sua idade:'))
atual = date.today().year
i = atual - n
if i <= 9:
    print('\033[1;35mCom {} anos, você é MIRIM!'.format(i))
elif 14>= i:
    print('\033[1;35mCom {} anos, você é INFANTIl!'.format(i))
elif 19 >= i:
    print('\033[1;35mCom {} anos, você é JUNIOR!'.format(i))
elif i == 25:
    print('\033[1;35mCom {} anos, você é SÊNIOR!'.format(i))
else:
    print('\033[1;35mAcima de 25 anos você ja é MASTER!')
