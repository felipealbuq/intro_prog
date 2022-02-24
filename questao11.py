# Determinar quanto tempo um corpo em repouso leva para atingir o solo
# a partir de certa altura informada pelo usuário.
# Considere g = 9,8 m/s² e que a queda livre é determinada pela fórmula:
# H = Ho + VoT + (gT^2)/2.

import math

alt_incial = float(input('Digite a altura:\n'))

tempo = math.sqrt(2 * alt_incial / 9.8)

print(f'O tempo para o corpo atingir o solo é de: {tempo:.2f} segundos')
