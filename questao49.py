# Imprimir a tabuada de multiplicação de 0 a 10 de um número escolhido pelo usuário.

n = float(input('Digite um número qualquer:\n'))
cont = 0

for c in range(0,11):
    print(f'{n} * {cont} = {n * cont}')
    cont += 1
