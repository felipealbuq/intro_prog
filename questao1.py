#Escreva um programa que pergunte o raio de uma circunferência, e em seguida
#mostre o diâmetro, comprimento e área da circunferência.

import math

raio = float(input('Digite o raio da circunferência:\n'))

diam = 2 * raio
comp = 2 * math.pi * raio
area = math.pi * math.pow(raio,2)

print(f'O diâmetro é de {diam} , o comprimento é de {comp:.2f} e a área é de {area:.2f}')