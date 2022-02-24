# Ler 3 números e verificar se eles podem ou não serem lados de um triângulo.

l1 = float(input('Digite o valor do primeiro lado:\n'))
l2 = float(input('Digite o valor do segundo lado:\n'))
l3 = float(input('Digite o valor do terceiro lado:\n'))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Os valores podem formar um triângulo.')
else:
    print('Os valores não podem formar um triângulo.')
