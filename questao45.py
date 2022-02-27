# Leia a nota de 5 alunos. Para cada aluno, leia 4 notas, sendo que a primeira tem peso 3,
# a segunda peso 2 e a terceira e quarta peso 1. Calcule e apresente a média de cada aluno,
# dizendo se ele passou, não passou ou vai para a recuperação (e quantos pontos precisa para ser aprovado).
# Além disso, tire a média da turma.

cont_aluno = 1
cont_nota = 1
nota_alunos = [[],[],[],[],[]]
media_alunos = []
aprovado = 7
cont_aprovados = 1
for c in range(0,5):
    print(f'Em relação ao {cont_aluno}º aluno.')
    for n in range(0,4):
        nota = float(input(f'Digite a {cont_nota}º nota do aluno:\n'))
        while nota < 0 or nota > 10:
            nota = float(input(f'Digite uma nota válida para a {cont_nota}º nota do aluno:\n'))

        cont_nota += 1

        if c == 0 and n == 0:
            nota = nota * 3
            nota_alunos[0].append(nota)
        if c == 0 and n == 1:
            nota = nota * 2
            nota_alunos[0].append(nota)
        if c == 0 and n == 2:
            nota = nota * 1
            nota_alunos[0].append(nota)
        if c == 0 and n == 3:
            nota = nota * 1
            nota_alunos[0].append(nota)


        if c == 1 and n == 0:
            nota = nota * 3
            nota_alunos[1].append(nota)
        if c == 1 and n == 1:
            nota = nota * 2
            nota_alunos[1].append(nota)
        if c == 1 and n == 2:
            nota = nota * 1
            nota_alunos[1].append(nota)
        if c == 1 and n == 3:
            nota = nota * 1
            nota_alunos[1].append(nota)


        if c == 2 and n == 0:
            nota = nota * 3
            nota_alunos[2].append(nota)
        if c == 2 and n == 1:
            nota = nota * 2
            nota_alunos[2].append(nota)
        if c == 2 and n == 2:
            nota = nota * 1
            nota_alunos[2].append(nota)
        if c == 2 and n == 3:
            nota = nota * 1
            nota_alunos[2].append(nota)


        if c == 3 and n == 0:
            nota = nota * 3
            nota_alunos[3].append(nota)
        if c == 3 and n == 1:
            nota = nota * 2
            nota_alunos[3].append(nota)
        if c == 3 and n == 2:
            nota = nota * 1
            nota_alunos[3].append(nota)
        if c == 3 and n == 3:
            nota = nota * 1
            nota_alunos[3].append(nota)


        if c == 4 and n == 0:
            nota = nota * 3
            nota_alunos[4].append(nota)
        if c == 4 and n == 1:
            nota = nota * 2
            nota_alunos[4].append(nota)
        if c == 4 and n == 2:
            nota = nota * 1
            nota_alunos[4].append(nota)
        if c == 4 and n == 3:
            nota = nota * 1
            nota_alunos[4].append(nota)

    cont_nota = 1
    cont_aluno += 1

media_aluno1 = sum(nota_alunos[0]) / 7
media_aluno2 = sum(nota_alunos[1]) / 7
media_aluno3 = sum(nota_alunos[2]) / 7
media_aluno4 = sum(nota_alunos[3]) / 7
media_aluno5 = sum(nota_alunos[4]) / 7

media_alunos.append(media_aluno1)
media_alunos.append(media_aluno2)
media_alunos.append(media_aluno3)
media_alunos.append(media_aluno4)
media_alunos.append(media_aluno5)

for a in media_alunos:
    if a >= aprovado:
        print(f'A média ponderada do {cont_aprovados}º aluno é de {a:.2f}')
        print(f'O {cont_aprovados}º foi aprovado.\n')
    else:
        print(f'A média ponderada do {cont_aprovados}º aluno é de {a:.2f}')
        print(f'O {cont_aprovados}º aluno vai para recuperação e faltam {aprovado - a:.2f}'
              f' pontos para ser aprovado.\n')
    cont_aprovados += 1

media_geral = (media_aluno1 + media_aluno2 + media_aluno3 + media_aluno4 + media_aluno5) / 5

print(f'A média geral da turma é de: {media_geral:.2f}')