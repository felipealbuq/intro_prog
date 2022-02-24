# Escreva um programa que solicita 10 números ao usuário, através de um laço while,
# e ao final mostre qual destes números é o maior.

print('Entre com 10 números:')

numeros = []

cont = 1
valor = 0
while cont <= 10:
    valor = float(input(f'Digite o {cont}º valor:\n'))
    cont += 1
    numeros.append(valor)
    numeros.sort()

print(f'O maior número digitado foi: {numeros[9]}')









