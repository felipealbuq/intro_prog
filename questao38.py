# Ler a altura e o sexo de 15 pessoas (M para homem e F para mulher) e informe
# 1- a menor e a maior altura,
# 2- media da altura dos homens,
# 3- a altura da mulher mais alta,
# 4- quantos eram os homens.

print('Digite a altura e o sexo de 15 pessoas:\n')

alturas_totais = []
altura_homens = []
altura_mulheres = []
cont = 1
cont_homem = 0

while cont <= 15:
    altura_pessoa = float(input(f'Digite a altura da {cont}º da pessoa (com ".") para a parte decimal:\n'))
    while altura_pessoa < 0:
        print('Digite uma idade válida:\n')
        altura_pessoa = float(input(f'Digite a altura da {cont}º da pessoa:\n'))

    sexo_pessoa = str(input(f'Digite o sexo da {cont}º pessoa (M para homem e F para mulher):\n'))
    while sexo_pessoa not in('mMfF'):
        print('Digite um sexo válido:\n')
        sexo_pessoa = str(input(f'Digite o sexo da {cont}º pessoa (M para homem e F para mulher):\n'))

    cont += 1

    alturas_totais.append(altura_pessoa)
    alturas_totais.sort()

    if sexo_pessoa in 'mM':
        altura_homens.append(altura_pessoa)
        cont_homem += 1

    if sexo_pessoa in 'fF':
        altura_mulheres.append(altura_pessoa)
        altura_mulheres.sort()

media_altura_homens = sum(altura_homens) / cont_homem
mulher_mais_alta = altura_mulheres[-1]


print(f'\nA menor altura é de {alturas_totais[0]:.2f} e a maior é de {alturas_totais[-1]:.2f}\n')
print(f'A média da altura dos homens é de {media_altura_homens:.2f} metros.\n')
print(f'A altura da mulher mais alta é de {mulher_mais_alta:.2f} metros.\n')
print(f'A quantidades de homens é de {cont_homem}.\n')

