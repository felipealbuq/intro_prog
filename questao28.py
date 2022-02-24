# Faça um programa que informe o mês de acordo com o número informado pelo usuário.
# (Exemplo: Entrada: 4. Saída: Abril).

# O primeiro índice de um array é zero, logo, subtraí 1 de num para ficar equivelente ao mês
num = int(input('Digite um número inteiro entre 1 e 12:\n')) - 1

meses = ['JANEIRO','FEVEREIRO','MARÇO','ABRIL','MAIO','JUNHO','JULHO','AGOSTO','SETEMBRO','OUTUBRO',
         'NOVEMBRO','DEZEMBRO']

while num < 0 or num > 12:
    num = int(input('Digite um número inteiro entre 1 e 12:\n')) - 1

print(f'{num + 1} corresponde ao mês de {meses[num]}.')