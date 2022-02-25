# Ler 10 números e informar quantos desses são pares.

numeros = []
cont = 1
pares = 0

while cont <= 10:
    numero = float(input(f'Digite o {cont}º número:\n'))
    numeros.append(numero)
    cont += 1

for i in range(len(numeros)):
    if numeros[i] %2 == 0:
        pares += 1

print(f'\n{pares} números são pares.\n')