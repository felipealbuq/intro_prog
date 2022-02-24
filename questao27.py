# Faça um programa que recebe uma letra, escreva na tela se essa letra é ou não uma vogal.

letra = str(input('Digite uma letra qualquer do alfabeto:\n')).upper()
vogais = ['A','E','I','O','U']

if letra in vogais:
    print(f'{letra} é vogal.\n')
else:
    print(f'{letra} não é vogal.\n')
