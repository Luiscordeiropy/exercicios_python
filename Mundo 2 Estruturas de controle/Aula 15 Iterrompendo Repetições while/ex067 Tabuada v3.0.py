while True:
    t = int(input('Quer ver a tabuada de qual valor?'))
    if t >= 0:
        for c in range(1,11):
           print(f'{t} x {c:2} = {t*c}')
    if t < 0:
        break
print('Tabuada encerrada. Volte sempre')