# Fazer uma calculadora simples com as quatro operações.

print('------------Calculadora simples-------------')

n1 = float(input('Digite o primeiro valor:\n'))
n2 = float(input('Digite o segundo valor:\n'))

op = int(input('Digite a operação:\n'
               '1 - SOMA\n'
               '2 - SUBTRAÇÃO\n'
               '3 - MULTIPLICAÇÃO\n'
               '4 - DIVISÃO\n'))

while op not in (1,2,3,4):
    op = int(input('Digite uma operação válida:\n'))

if op == 1:
    soma = n1+n2
    print(f'A soma de {n1} com {n2} é {soma}')
elif op == 2:
    sub = n1-n2
    print(f'A subtração de {n1} com {n2} é {sub}')
elif op == 3:
    mult = n1 * n2
    print(f'A multiplicação de {n1} com {n2} é {mult}')
elif op == 4:
    div = n1/n2
    print(f'A divisão de {n1} com {n2} é {div}')

