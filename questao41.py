# Escreva um programa que lê o tamanho do lado de um quadrado e imprime um quadrado daquele
# tamanho com asteriscos e espaços em branco. Seu programa deve funcionar para quadrados com lados
# de todos os tamanhos entre 1 e 20. Para lado igual a 5:

n = int(input("Digite o comprimento do lado do quadrado entre 1 e 20:\n"))

while n < 1 or n > 20:
    n = int(input('Digite o comprimento do lado do quadrado entre 1 e 20:\n'))

for i in range(n):
    print()
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("*", end='')
        else:
            print(" ", end='')

