# Construa um programa que peça os lados de um triângulo e mostre o tipo do
# triângulo: como isósceles, escaleno ou equilátero.

l1 = float(input('Digite o valor do primeiro lado:\n'))
l2 = float(input('Digite o valor do segundo lado:\n'))
l3 = float(input('Digite o valor do terceiro lado:\n'))

if l1 == l2 and l2 == l3:
    print('Triângulo equilátero.')

elif l1 == l2 or l1 == l3 or l2 == l3:
    print('Triângulo isóceles.')
else:
    print('Triãngulo escaleno.')