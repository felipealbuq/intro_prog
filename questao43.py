# Ler a idade e o peso de 15 pessoas. Calcular e imprimir as médias de peso das pessoas da
# mesma faixa etária e quantas são de cada faixa etária.
# As faixas de 1 a 10 anos, de 11-20, de 21-30 e maiores de 30.

faixa1 = []
faixa2 = []
faixa3 = []
faixa4 = []
cont = 1

for i in range(0,15):
    idade = int(input(f"Digite a idade da {cont}º da pessoa:\n"))
    peso = float(input(f'Digite o peso da {cont}º pessoa:\n'))

    if idade <= 10:
        faixa1.append(peso)
    elif idade > 11 and idade < 20:
        faixa2.append(peso)
    elif idade > 21 and idade < 30:
        faixa3.append(peso)
    else:
        faixa4.append(peso)
    cont += 1

peso_medio_faixa1 = sum(faixa1) / len(faixa1)
peso_medio_faixa2 = sum(faixa2) / len(faixa2)
peso_medio_faixa3 = sum(faixa3) / len(faixa3)
peso_medio_faixa4 = sum(faixa4) / len(faixa4)

print(f'Peso médio da faixa hetária de 1 a 10 é de {peso_medio_faixa1} e há {len(faixa1)} pessoas.')
print(f'Peso médio da faixa hetária de 11 a 20 é de {peso_medio_faixa2} e há {len(faixa2)} pessoas.')
print(f'Peso médio da faixa hetária de 21 a 30 é de {peso_medio_faixa3} e há {len(faixa3)} pessoas.')
print(f'Peso médio da faixa hetária acima de 30 é de {peso_medio_faixa4} e há {len(faixa4)} pessoas.')
