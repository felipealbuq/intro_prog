# Capture uma lista de 10 valores inteiros, salvando-a em um vetor: int lista [10].
# Em seguida, escolha entre as opções:
# 1 - Listar em ordem crescente
# 2 - Listar em ordem decrescente
# 3 - Listar na ordem original

lista = []
cont = 1

print('Digite 10 números inteiros.')

for n in range(0,10):
    valor = int(input(f'Digite o {cont}º valor:\n'))
    lista.append(valor)
    cont += 1

lista.reverse()

print('Os valores em ordem decrescente são:')
for c in lista:
    print(f'{c}',end= '   ')
