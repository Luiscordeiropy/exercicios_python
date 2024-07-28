def leiaDinheiro(p=0):
    valido = False
    while not valido:
        entrada = str(input(p)).replace(',', '.').strip()
        if not entrada.isnumeric() or entrada == '':
            print(f'\033[0;31mERRO: \"{entrada}\" é um preço inválido \033[m')
        else:
            valido = True
            return float(entrada)
