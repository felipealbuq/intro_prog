# Fazer um programa que solicite 2 números e informe:
# A soma dos números;
# O produto do primeiro número pelo quadrado do segundo;
# O quadrado do primeiro número;
# A raiz quadrada da soma dos quadrados;
# O seno da diferença do primeiro número pelo segundo;
# O módulo do primeiro número.

import math

num1 = float(input('Digite o primeiro número:\n'))
num2 = float(input('Digite o segundo número:\n'))

soma = num1 + num2
prod = num1 * math.pow(num2,2)
quad = math.pow(num1,2)
raiz = math.sqrt(num1+num2)
seno = math.sin(num1-num2)
modulo = math.fabs(num1)

print(f'A soma de {num1} com {num2} é {soma}')
print(f'O produto de {num1} com {num2}² é {prod}')
print(f'{num1}² é {quad}')
print(f'A raiz da soma de {num1} com {num2} é {raiz}')
print(f'O seno da diferença de {num1} com {num2} é {seno}')
print(f'O módulo de {num1} é {modulo}')