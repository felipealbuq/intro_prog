# Calcule o salário líquido de um professor. Será fornecido valor da hora aula,
# o número de aulas dadas e a % de desconto do INSS sobre o valor bruto do salário.

hora_aula = float(input('Digite o valor da hora aula:\n'))
num_aulas = int(input('Digite o número de aulas dadas:\n'))
porc_inss = float(input('Digite a porcentagem de desconto do inss:\n'))

sal_bruto = hora_aula * num_aulas

sal_liq = sal_bruto - (porc_inss / 100 * sal_bruto)

print(f'O salário líquido do professor é de: {sal_liq}')