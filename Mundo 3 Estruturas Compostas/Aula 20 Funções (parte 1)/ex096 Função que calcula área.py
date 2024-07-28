def area(largura, comprimento):
    a = largura * comprimento
    print(f'a área de um terreno {largura}x{comprimento}  é {a}m²')


l = float(input('largura: '))
c = float(input('comprimento: '))
area(l, c)
