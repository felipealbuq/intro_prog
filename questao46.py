# Capture uma lista de 5 valores inteiros representando as coordenadas cartesianas X e Y,
# salvando-a em uma matriz (tabela): int coordenadas [5][5]. Em seguida, escolha entre as opções:
# 1 - Listar em ordem crescente os valores de X, e ao lado deve ser listado os valores correspondentes de Y.
# 2 - Listar em ordem decrescente os valores de Y, e ao lado deve ser listado os valores correspondentes de X.
# 3 - Listar na ordem original
# 4 - Listar com salto de posições: peça ao usuário para dizer quantas posições da tabela ele deseja
# imprimir o valor, em seguida imprima conforme ele desejou.

coordenadas = [[],[]]
cont = 1

print('Entrada de 5 valores de abscissas e ordenadas.')
for c in range (0,5):
    abscissa = int(input(f'Digite o valor inteiro da {cont}º abscissa (X):\n'))
    ordenada = int(input(f'Digite o valor inteiro da {cont}º ordenada (Y):\n'))

    cont += 1

    coordenadas[0].append(abscissa)
    coordenadas[1].append(ordenada)

for a,o in zip(coordenadas[0],coordenadas[1]):
    print(f'{a} ------ {o}')


