# Escreva um programa que pergunta um número ao usuário e mostra sua tabuada completa
# (de 1 até 10).

n = float(input('Digite um número qualquer:\n'))
cont = 1

for c in range(1,11):
    print(f'{n} * {cont} = {n * cont}')
    cont += 1
