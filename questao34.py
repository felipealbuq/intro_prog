# Faça um programa que, para um número indeterminado de pessoas: leia a idade de cada uma,
# sendo que a idade 0 (zero) indica o fim da leitura e não deve ser considerada. A seguir calcule:
# • o número de pessoas;
# • a idade média do grupo;
# • a menor idade e a maior idade.

pessoas = []
cont = 0


print('Leitura da idade de indeterminadas pessoas (digite 0 para parar).')

while True:

    idade = int(input(f'Digite a idade da {cont + 1}º pessoa:\n'))

    if idade == 0:
        break
    else:
        pessoas.append(idade)
        cont += 1


pessoas.sort()

if cont == 0:
    print('Você não digitou a idade de ninguém.')
else:

    idade_media = sum(pessoas) / cont

    print(f'\nVocê digitou um total de {cont} pessoas.\n')
    print(f'A idade média do grupo é de: {idade_media:.2f}\n')
    print(f'A menor idade é de: {pessoas[0]} e a maior é de: {pessoas[-1]}')
