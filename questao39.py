# Elaborar um programa que efetue a leitura sucessiva de valores numéricos e apresente no final
# o total do somatório, a média e o total de valores lidos. O programa deve fazer as leituras dos
# valores enquanto o usuário estiver fornecendo valores positivos. Ou seja, o programa deve parar
# quando o usuário fornecer um valor negativo.

cont = 1
numeros = []

while True:
    numero = float(input('Digite um número (número negativo para encerrar):\n'))
    if numero <0:
        break
    else:
        numeros.append(numero)
        cont += 1

somatorio = sum(numeros)
media = somatorio / (cont - 1)

print(f'O somatório dos números digitados foi de: {somatorio}')
print(f'A média dos números digitados foi de: {media:.2f}')
print(f'O total de números digitados foi de: {cont - 1}')