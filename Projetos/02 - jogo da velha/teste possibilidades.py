# lista_click = [["x", "y", "z"], ["x", "x", "z"], ["x", "y", "x"]]

# for j in range(3):
#     for i in range(1):
#         if lista_click[j][i] == lista_click[j][1+i] == lista_click[j][2+i]:
#             vencedor("o vencedor foi ", jogando)

# for j in range(1):
#     for i in range(3):
#         if lista_click[j][i] == lista_click[1+j][i] == lista_click[2+j][i]:
#             print(lista_click[j][i], lista_click[1+j][i], lista_click[2+j][i])

# for j in range(1):
#     if lista_click[j][j] == lista_click[1+j][1+j] == lista_click[2+j][2+j]:
#         print(lista_click[j][j], lista_click[1+j][1+j], lista_click[2+j][2+j])



# botao_1 = Button(frame_baixo, command=lambda: controlar(1), text="", height=1, width=3, bg=fundo, fg=co7,
#                  font="Ivy 40 bold", overrelief=RIDGE, relief="flat")
# botao_1.place(x=42, y=12)
# botao_2 = Button(frame_baixo, command=lambda: controlar(2), text="", height=1, width=3, bg=fundo, fg=co7,
#                  font="Ivy 40 bold", overrelief=RIDGE, relief="flat")
# botao_2.place(x=163, y=12)
# botao_3 = Button(frame_baixo, command=lambda: controlar(3), text="", height=1, width=3, bg=fundo, fg=co7,
#                  font="Ivy 40 bold", overrelief=RIDGE, relief="flat")
# botao_3.place(x=282, y=12)
#
# #LINHA 2
#
# botao_4 = Button(frame_baixo, command=lambda: controlar(4), text="", height=1, width=3, bg=fundo, fg=co7,
#                  font="Ivy 40 bold", overrelief=RIDGE, relief="flat")
# botao_4.place(x=42, y=137)
# botao_5 = Button(frame_baixo, command=lambda: controlar(5), text="", height=1, width=3, bg=fundo, fg=co7,
#                  font="Ivy 40 bold", overrelief=RIDGE, relief="flat")
# botao_5.place(x=163, y=137)
# botao_6 = Button(frame_baixo, command=lambda: controlar(6), text="", height=1, width=3, bg=fundo, fg=co7,
#                  font="Ivy 40 bold", overrelief=RIDGE, relief="flat")
# botao_6.place(x=282, y=137)
#
# #LINHA 3
#
# botao_7 = Button(frame_baixo, command=lambda: controlar(7), text="", height=1, width=3, bg=fundo, fg=co7,
#                  font="Ivy 40 bold", overrelief=RIDGE, relief="flat")
# botao_7.place(x=42, y=262)
# botao_8 = Button(frame_baixo, command=lambda: controlar(8), text="", height=1, width=3, bg=fundo, fg=co7,
#                  font="Ivy 40 bold", overrelief=RIDGE, relief="flat")
# botao_8.place(x=163, y=262)
# botao_9 = Button(frame_baixo, command=lambda: controlar(9), text="", height=1, width=3, bg=fundo, fg=co7,
#                  font="Ivy 40 bold", overrelief=RIDGE, relief="flat")
# botao_9.place(x=282, y=262)
# Se for a sétima jogada ou posterior, remover a primeira jogada do jogador atual

#
# def imprimir_tabuleiro(tabuleiro):
#     for linha in tabuleiro:
#         print(" | ".join(linha))
#         print("-" * 9)
#
#
# def verificar_vencedor(tabuleiro):
#     # Verificar linhas
#     for linha in tabuleiro:
#         if linha.count(linha[0]) == len(linha) and linha[0] != " ":
#             return True
#
#     # Verificar colunas
#     for coluna in range(len(tabuleiro)):
#         if tabuleiro[0][coluna] == tabuleiro[1][coluna] == tabuleiro[2][coluna] and tabuleiro[0][coluna] != " ":
#             return True
#
#     # Verificar diagonais
#     if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] and tabuleiro[0][0] != " ":
#         return True
#     if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] and tabuleiro[0][2] != " ":
#         return True
#
#     return False
#
#
# def main():
#     tabuleiro = {1: "", 2: "", "3": "",
#                  "4": "", "5": "", "6": "",
#                  "7": "", "8": "", "9": ""}
#     # tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
#     jogador = "X"
#
#     contador_jogadas = 0
#
#     while True:
#         imprimir_tabuleiro(tabuleiro)
#
#         linha = int(input(f"Jogador {jogador}, escolha a linha (0, 1, 2): "))
#         coluna = int(input(f"Jogador {jogador}, escolha a coluna (0, 1, 2): "))
#
#         # Verificar se a posição escolhida está vazia
#         if tabuleiro[linha][coluna] == " ":
#             tabuleiro[linha][coluna] = jogador
#             contador_jogadas += 1
#
#             # Verificar se há um vencedor
#             if verificar_vencedor(tabuleiro):
#                 imprimir_tabuleiro(tabuleiro)
#                 print(f"Jogador {jogador} vence!")
#                 break
#
#             # Se for a sétima jogada ou posterior, remover a primeira jogada do jogador atual
#             if contador_jogadas >= 7:
#                 for v, k in tabuleiro.items():
#                     if tabuleiro[] == jogador:
#                         tabuleiro[i] = " "
#                         break
#                 else:
#                     continue
#                 break
#
#             # Alternar jogadores
#             jogador = "O" if jogador == "X" else "X"
#         else:
#             print("Essa posição já está ocupada. Tente novamente.")
#
# main()

# jogando = "x"
#
# tabuleiro = {1: "", 2: "", 3: "",
#              4: "", 5: "", 6: "",
#              7: "", 8: "", 9: ""}
#
# for c in range(1, 10):
#     tabuleiro[c] = jogando

# print(tabuleiro)
# for v, k in tabuleiro.items():
#     if tabuleiro[i] == jogador:
#         tabuleiro[i] = " "


def ordem_de_jogada():
    global contordem
    lista_ordem_de_jogada[contador] = jogando
    if contordem >= 1:
        print(lista_botoes, "\n", lista_ordem_de_jogada)
        if lista_botoes[contordem - 1]["text"] == lista_ordem_de_jogada[contordem - 1]:
            lista_botoes[contordem - 1]["text"] = ""
            lista_ordem_de_jogada[0] = ""
            contordem += 1
            if contordem == 9:
                contordem = 1
            print(lista_click)
            print(contador, contordem)
