# Faça um programa que diz quantos dias um mês possui.

mes = str(input('Digite o mês:\n')).upper()
meses = ['JANEIRO','FEVEREIRO','MARÇO','ABRIL''MAIO','JUNHO','JULHO','AGOSTO','SETEMBRO','OUTUBRO',
         'NOVEMBRO','DEZEMBRO']

while mes not in(meses):
    mes = str(input('Digite um mês válido:\n')).upper()

if mes == 'FEVEREIRO':
    print(f'{mes} tem 28 dias.')
elif mes in ('JANEIRO','MARÇO','MAIO','JULHO','AGOSTO','OUTUBRO','DEZEMBRO'):
    print(f'{mes} tem 31 dias.')
else:
    print(f'{mes} tem 30 dias.\n')