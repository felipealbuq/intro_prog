# Ler 1 número. Se positivo, imprimir raiz quadrada se não o quadrado.

import math

n = float(input('Digite um número qualquer diferente de 0:\n'))

while n == 0:
    n = float(input('Digite um número qualquer diferente de 0:\n'))
if n > 0:
    print(f'A raiz quadrade de {n} é {math.sqrt(n)}')

else:
    print(f'O quadrado de {n} é {math.pow(n,2)}')
