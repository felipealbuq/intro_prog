# Imprimir o calendário de um ano escolhido pelo usuário.

import calendar

ano = int(input('Digite o ano para ver seu respectivo calendário:\n'))

print (calendar.TextCalendar(calendar.SUNDAY).formatyear(ano))