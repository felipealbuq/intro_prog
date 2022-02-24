# Faça um programa que receba a idade de uma pessoa e mostre na saída em qual
# categoria ela se encontra:
# 10-14 infantil
# 15-17 juvenil
# 18-25 adulto

idade = int(input('Digite a idade:\n'))

if 10<= idade <=14:
    print('Jogador infantil')
elif 15<= idade <=17:
    print('Jogador juvenil')
elif 18<= idade <=25:
    print('Jogador adulto')
else:
    print('Jogador não se enquadra em nenhuma categoria.')