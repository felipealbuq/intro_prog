# Um comerciante comprou um produto e quer vendê-lo com lucro de 45% se o
# valor da compra for menor que 20,00; caso contrário, o lucro será de 30%.
# Entrar com o valor do produto e imprimir o valor da venda.

valor = float(input('Digite o valor do produto:\n'))

if valor < 20:
    venda = valor + (valor * 45/100)
    print(f'A venda será de R$ {venda:.2f}')
else:
    venda = valor + (valor * 30/100)
    print(f'A venda será de R$ {venda:.2f}')
