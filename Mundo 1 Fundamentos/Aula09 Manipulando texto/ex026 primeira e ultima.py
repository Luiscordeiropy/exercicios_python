f = str(input('escreva um frase:')).upper().strip()
print('''A letra "a" aparece {} vezes na frase
A primera vez que ela aparece é na numeração {}
A ultima vez que ela aparece e na numeração {}'''.format(f.count('A'), f.find('A')+1, f.rfind('A')+1))