# APENAS FUNÇÃO: Imagine que você tem um joguinho da cobrinha no espaço cartesiano X e Y,
# onde o par ordenado (X, Y) = (0, 0) corresponde ao canto superior esquerdo da tela. O usuário deve
# digitar o tamanho do comprimento máximo do mapa do jogo (Xmax) e deve digitar o tamanho máximo da
# altura do mapa (Ymax). Crie uma função que recebe como entrada o valor Xmax, Ymax e os valores X e Y em
# que a cabeça da cobrinha está posicionado. Realize o processamento para saber se a cabeça do cobrinha está
# dentro ou fora do mapa do jogo. Como resposta da função, retorne um valor inteiro que diz se a cabeça da
# cobrinha está 0. dentro do jogo, ou fora do jogo nas posições.
# 1. Norte, 2. Nordeste, 3. Leste, 4. Sudeste, 5. Sul, 6. Sudoeste, 7. Oeste, 8. Noroeste.

def ponto_cardeal_mapa_cobra(xMax, yMax, x, y):
  #PROCESSAMENTO
  if x < 0 and y < 0:
    return [8, "Noroeste"]
  elif x >= 0 and x <= xMax and y < 0:
    return [1, "Norte"]
  elif x > xMax and y < 0:
    return [2, "Nordeste"]
  elif x > xMax and y >= 0 and y <= yMax:
    return [3, "Leste"]
  elif x > xMax and y > yMax:
    return [4, "Sudeste"]
  elif x >= 0 and x <= xMax and y > yMax:
    return [5, "Sul"]
  elif x < 0 and y > yMax:
    return [6, "Sudoeste"]
  elif x < 0 and y >= 0 and y <= yMax:
    return [7, "Oeste"]
  elif x >= 0 and x <= xMax and y >= 0 and y <= yMax:
    return [0, "Dentro"]


assert ponto_cardeal_mapa_cobra(100, 100, -1, -1) == [8, "Noroeste"]
assert ponto_cardeal_mapa_cobra(100, 100, 50, -1) == [1, "Norte"]
assert ponto_cardeal_mapa_cobra(100, 100, 100, -1) == [1, "Norte"]
assert ponto_cardeal_mapa_cobra(100, 100, 200, -1) == [2, "Nordeste"]
assert ponto_cardeal_mapa_cobra(100, 100, 200, 50) == [3, "Leste"]
assert ponto_cardeal_mapa_cobra(100, 100, 200, 200) == [4, "Sudeste"]
assert ponto_cardeal_mapa_cobra(100, 100, 0, 200) == [5, "Sul"]
assert ponto_cardeal_mapa_cobra(100, 100, -1, 200) == [6, "Sudoeste"]
assert ponto_cardeal_mapa_cobra(100, 100, -1, 50) == [7, "Oeste"]
assert ponto_cardeal_mapa_cobra(100, 100, 0, 0) == [0, "Dentro"]
assert ponto_cardeal_mapa_cobra(100, 100, 50, 50) == [0, "Dentro"]
assert ponto_cardeal_mapa_cobra(100, 100, 100, 100) == [0, "Dentro"]
assert ponto_cardeal_mapa_cobra(100, 100, 0, 100) == [0, "Dentro"]
assert ponto_cardeal_mapa_cobra(100, 100, 100, 0) == [0, "Dentro"]

print("Mapa do jogo da cobrinha")

xMax = float(input("Digite o comprimento do mapa: "))
yMax = float(input("Digite a altura do mapa: "))

x = float(input("Digite a posição X da cabeça da cobrinha: "))
y = float(input("Digite a posição Y da cabeça da cobrinha: "))


pontoCardeal = ponto_cardeal_mapa_cobra(xMax, yMax, x, y)


print(pontoCardeal)