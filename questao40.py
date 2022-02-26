# Escreva um programa que lê o tamanho do lado de um quadrado e imprime um quadrado daquele
# tamanho com asteriscos. Seu programa deve funcionar para quadrados com lados de todos os
# tamanhos entre 1 e 20.

import math

n = int(input('Digite o comprimento do lado do quadrado entre 1 e 20:\n'))
cont = 1

while n < 1 or n > 20:
    n = int(input('Digite o comprimento do lado do quadrado entre 1 e 20:\n'))

while cont <= math.pow(n,2):
    if cont % n == 0:
        print('*',end=' ')
        print('')

    else:
        print('*',end=' ')
    cont += 1