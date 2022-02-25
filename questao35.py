# Ler 5 números e informar quantos desses são ímpares.

numeros = []
cont = 1
impares = 0

while cont <= 5:
    numero = float(input(f'Digite o {cont}º número:\n'))
    numeros.append(numero)
    cont += 1

for i in range(len(numeros)):
    if numeros[i] %2 != 0:
        impares += 1

print(f'{impares} números são ímpares.\n')