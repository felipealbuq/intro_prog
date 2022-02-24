#Informe o tempo gasto numa viagem (em horas), a velocidade média e mostre
#a distância percorrida.

tempo = float(input('Digite o tempo gasto em horas:\n'))
vel_media = float(input('Digite a velocidade média:\n'))

dist = vel_media * tempo

print(f'A distância percorrida é de {dist} Km')