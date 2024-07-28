i1 = 0
i2 = 0
from datetime import date
t = date.today().year
for c in range(1, 8):
    n = int(input('Em que ano a {}° pessoa nasceu'.format(c)))
    i = t - n
    if i < 18:
        i1 += 1
    else:
        i2 += 1
print('{} Pessoas ainda não atingiram a maioridade!'.format(i1))
print('{} Pessoas atingiram a maioridade!'.format(i2))