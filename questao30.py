# Escreva um aplicativo que mostra todos os números ímpares de 1 até 100.

print('Os números ímpares de 1 até 100 são:')

for c in range(1,100):
    if c % 2 != 0:
        print(f'{c}')
    