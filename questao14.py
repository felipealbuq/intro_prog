# Escreva um programa que recebe um inteiro e diga se é par ou ímpar.

n = int(input('Digite um número inteiro:\n'))

if n % 2 == 0:
    print(f'{n} é par')
else:
    print(f'{n} é ímpar')