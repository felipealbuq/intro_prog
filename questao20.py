# Ler a idade de uma pessoa e informar a sua classe eleitoral.
# Não-eleitor (abaixo de 16 anos)
# Eleitor obrigatório (entre 18 e 65 anos)
# Eleitor facultativo (entre 16 e 18 e maior de 65 anos).

idade = int(input('Digite a idade:\n'))

if idade < 16:
    print('Não-eleitor.')
elif 16 <= idade < 18 or idade > 65:
    print('Eleitor facultativo.')
else:
    print('Eleitor obrigatório.')

