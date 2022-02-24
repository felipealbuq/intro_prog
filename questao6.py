#Receber um valor qualquer do teclado e imprimir esse valor com reajuste
# superior de 10%.

valor = float(input('Digite um valor qualquer:\n'))

print(f'{valor} com reajuste superior de 10% é de: {(valor * 0.1) + valor}')