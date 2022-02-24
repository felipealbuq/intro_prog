# Receber um número do teclado e informar se ele é divisível por 10, por 5, por 2
# ou se não é divisível por nenhum destes.

num = float(input('Digite um número qualquer:\n'))

if num % 10 == 0 :
    print(f'{num} é divisível por 10')

if num % 5 == 0:
    print(f'{num} é divisível por 5 ')

if num % 2 == 0 :
    print(f'{num} é divisível por 2')

elif num % 10 != 0 and num % 5 !=0 and num % 2 != 0:
    print(f'{num} não é divisível por 10, por 5, nem por 2')
