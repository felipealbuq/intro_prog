# Capture uma lista de 5 valores inteiros representando o dia e mes do ano, salvando-a em uma
# matriz (tabela): int diaMes [5][5]. Em seguida, o programa deve dizer quais dias e meses foram digitados:
# quantidade de pares dias/mes corretos
# quantidade de pares dias/mes incorretos (lembre de quantos dias existem por mês e quantos meses existem por ano).
# Imprimi as informações a) e b) na tela.
# Em seguida, peça ao usuário para digitar corretamente as posições da tabela diaMes que
# foram invalidadas. Realize este processo enquanto houverem informações inválidas.

cont_errado = 0

calendario = [[],[]]

for c in range(0,5):
    mes = int(input('Digite o mês:\n'))
    while mes < 1 or mes > 12:
        dia = int(input('Digite o mês válido:\n'))
        cont_errado += 1
    calendario[1].append(mes)
    if mes == 1:

        dia = int(input('Digite o dia:\n'))
        while dia < 1 or dia > 31:
            dia = int(input('Digite o dia válido para janeiro:\n'))
            cont_errado += 1
        calendario[0].append(dia)
    elif mes == 2:

        dia = int(input('Digite o dia:\n'))
        while dia < 1 or dia > 28:
            dia = int(input('Digite o dia válido para fevereiro:\n'))
            cont_errado += 1
        calendario[0].append(dia)
    elif mes == 3:

        dia = int(input('Digite o dia:\n'))
        while dia < 1 or dia > 31:
            dia = int(input('Digite o dia válido para março:\n'))
            cont_errado += 1
        calendario[0].append(dia)
    elif mes == 4:

        dia = int(input('Digite o dia:\n'))
        while dia < 1 or dia > 30:
            dia = int(input('Digite o dia válido para abril:\n'))
            cont_errado += 1
        calendario[0].append(dia)
    elif mes == 5:

        dia = int(input('Digite o dia:\n'))
        while dia < 1 or dia > 31:
            dia = int(input('Digite o dia válido para maio:\n'))
            cont_errado += 1
        calendario[0].append(dia)
    elif mes == 6:

        dia = int(input('Digite o dia:\n'))
        while dia < 1 or dia > 30:
            dia = int(input('Digite o dia válido para junho:\n'))
            cont_errado += 1
        calendario[0].append(dia)
    elif mes == 7:

        dia = int(input('Digite o dia:\n'))
        while dia < 1 or dia > 31:
            dia = int(input('Digite o dia válido para julho:\n'))
            cont_errado += 1
        calendario[0].append(dia)
    elif mes == 8:

        dia = int(input('Digite o dia:\n'))
        while dia < 1 or dia > 31:
            dia = int(input('Digite o dia válido para agosto:\n'))
            cont_errado += 1
        calendario[0].append(dia)
    elif mes == 9:

        dia = int(input('Digite o dia:\n'))
        while dia < 1 or dia > 30:
            dia = int(input('Digite o dia válido para setembro:\n'))
            cont_errado += 1
        calendario[0].append(dia)
    elif mes == 10:

        dia = int(input('Digite o dia:\n'))
        while dia < 1 or dia > 31:
            dia = int(input('Digite o dia válido para outubro:\n'))
            cont_errado += 1
        calendario[0].append(dia)
    elif mes == 11:
        dia = int(input('Digite o dia:\n'))
        while dia < 1 or dia > 30:
            dia = int(input('Digite o dia válido para novembro:\n'))
            cont_errado += 1
        calendario[0].append(dia)
    elif mes == 12:
        dia = int(input('Digite o dia:\n'))
        while dia < 1 or dia > 31:
            dia = int(input('Digite o dia válido para dezembro:\n'))
            cont_errado += 1
        calendario[0].append(dia)

print('dia ---- mês')
for d,m in zip(calendario[0],calendario[1]):

    print(f'{d} ------ {m}')

if cont_errado == 0:
    print('Você não digitou nenhuma valor inválido.\n')
else:
    print(f'Você digitou {cont_errado} valores iválidos que foram corrigidos posteriormente.\n')

print(f'Você digitou {len(calendario[0])} dias e {len(calendario[1])} meses válidos ao final.\n')

