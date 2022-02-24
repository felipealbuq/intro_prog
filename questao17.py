# Faça um programa que receba três inteiros e diga qual deles é o
# maior e qual o menor.

n1 = int(input('Digite o primeiro número inteiro:\n'))
n2 = int(input('Digite o segundo número inteiro:\n'))
n3 = int(input('Digite o terceiro número inteiro:\n'))

menor = n1
maior = n1

if n2<n1 and n2<n3:
    menor = n2
elif n3<n1 and n3<n2:
    menor = n3

if n2>n1 and n2>n3:
    maior = n2
elif n3>n1 and n3>n2:
    maior = n3

print(f'O menor número é {menor} e o maior é {maior}')