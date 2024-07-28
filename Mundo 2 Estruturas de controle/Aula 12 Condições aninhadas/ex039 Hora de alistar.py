from datetime import date
i = int(input('Informe o ano que você nasceu:'))
a = date.today().year
al = a - i
t = 18 - al
if al <= 17:
    print('\033[1;35mAinda não está na hora de se alistar! Você tem {} anos e ainda falta {} ano(s) para você se alistar!\033[m'.format(al, t))
elif al == 18:
    print('\033[1;35mEstá na hora de você se alistar! você tem {} anos!\033[m'.format(al))
else:
    print('\033[1;31mO tempo para você se alistar já passou! Você tem {} anos e já se passou {} ano(s) desde que você completou 18 anos!\033[m'.format(al, (-1)*t))