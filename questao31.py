# Escreva um aplicativo que mostra todos os números pares de 1 até 100.
# Esse não precisa nem de código, basta você alterar apenas um número do exercício anterior.

print('Os números pares de 1 até 100 são:')

for c in range(1, 101):
    if c % 2 == 0:
        print(f'{c}')
