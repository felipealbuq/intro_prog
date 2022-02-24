# Para doar sangue é necessário ter entre 18 e 67 anos. Faça um aplicativo
# que pergunte a idade de uma pessoa e diga se ela pode doar sangue ou não.

idade = int(input('Digite a sua idade:\n'))

if 18 <= idade <= 67:
    print('Doação permitida.')
else:
    print('Doação não permitida.')