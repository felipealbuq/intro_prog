# Escreva um aplicativo que recebe um inteiro e mostra os números pares e
# ímpares (separados, em duas colunas), de 1 até esse inteiro. Como o primeiro
# número é ímpar (1), os ímpares serão exibidos primeiro. Após cada ímpar, damos o espaço
# de um TAB (\t), e na mesma linha imprimimos o par, e logo em seguinte o caractere (\n).

n = int(input('Digite um número inteiro:\n'))

numeros = [[],[]]

for i in range(1, n+1, 2):
    numeros[0].append(i)

for p in range(2, n+1, 2):
    numeros[1].append(p)

for impar,par in zip(numeros[0],numeros[1]):
    print(f'{impar} {par}')

