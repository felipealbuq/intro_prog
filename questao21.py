# Faça um programa que leia 3 números inteiros e os imprima em ordem crescente.

n1 = int(input('Digite o primeiro número inteiro:\n'))
n2 = int(input('Digite o segundo número inteiro:\n'))
n3 = int(input('Digite o terceiro número inteiro:\n'))

crescente = [n1,n2,n3]
crescente.sort()

print('\nOs valores digitados em ordem crescente ficam:')

for valor in crescente:
    print(f' {valor}',end=' ')

