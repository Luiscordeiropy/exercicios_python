n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))
m = (n1 + n2)/2
if m < 5:
    print('\033[1;31mREPROVADO! Vai estudar INÚTIL. Média {}'.format(m))
elif 7 > m >= 5:
    print('\033[1;31mRECUPERAÇÃO! Fez o que podia, NADA! Média {}'.format(m))
else:
    print('\033[1;35mAPROVADO! SORTE! Média {}'.format(m))
