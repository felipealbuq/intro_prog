# Escreva um programa que pergunte o dia, mês e ano do aniversário de uma
# pessoa e diga se a data é válida ou não. Caso não seja, diga o motivo.
# Suponha que todos os meses têm 31 dias e que estejamos no ano de 2013.

dia = int(input('Digite o dia do nascimento:\n'))
mes = int(input('Digite o mês (valor numérico) do nascimento:\n'))
ano = int(input('Digite o ano nascimento:'))

if dia >= 1 and dia <= 31 and mes >= 1 and mes <= 12 and ano <= 2013:
    print('Data válida.')
else:
    if dia < 1 or dia > 31:
        print('\nDia do nascimento inválido.\n')
    if mes < 1 or mes > 12:
        print('Mês do nascimento inválido.\n')
    if ano > 2013:
        print('Ano de nascimento inválido.\n')



