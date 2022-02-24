# Escreva um programa que pergunte ao usuário quantos alunos tem na sala dele.
# Em seguida, através de um laço while, pede ao usuário para que entre com as notas de
# todos os alunos da sala, um por vez. Por fim, o programa deve mostrar a média aritmética da turma.

quant_alunos = int(input('Digite a quantidade de alunos da turma:\n'))
notas = []
cont = 1

while cont <= quant_alunos:
    nota = float(input(f'Digite a nota do(a) {cont}º aluno(a):\n'))
    cont += 1
    notas.append(nota)

media = sum(notas) / quant_alunos


print(f'A média aritmética da turma é de: {media}\n')
