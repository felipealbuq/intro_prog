#Fazer um programa que pergunta um valor em metros e imprime o correspondente em
#decímetros, centímetros e milímetros.

met = float(input('Digite um valor em metros:\n'))

dec = met * 10
cent = met * 100
mili = met * 1000

print(f'{met} metros em decímetros: {dec}\n{met} metros em centímetros: {cent}\n{met} metros'
      f'em milímetros:{mili}')