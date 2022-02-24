# Calcular e imprimir o volume e a área de superfície de um cone reto,
# um cilindro ou uma esfera. O programa deverá ler a opção da figura desejada.

import math

figura = str(input('Digite o nome da figura que você deseja calcular o volume e a área:\n'
                 'Figuras disponíveis: Cone reto , cilindro e esfera.\n')).upper().replace(" ","")


while figura not in ('CONERETO','CILINDRO','ESFERA'):
    figura = str(input('Digite um nome válido:\n')).upper().replace(" ","")


if figura == 'CONERETO':
    raio_base_cone = float(input('Digite o raio da base do cone em cm:\n'))
    altura_cone = float(input('Digite a altura do cone em cm:\n'))

    geratriz_cone = math.sqrt(math.pow(raio_base_cone,2) + math.pow(altura_cone,2))
    volume_cone = (math.pi * math.pow(raio_base_cone,2) * altura_cone) / 3
    area_cone = math.pi * raio_base_cone * (raio_base_cone + geratriz_cone)

    print(f'O volume do cone é de {volume_cone:.2f} cm³')
    print(f'A área total do cone é de {area_cone:.2f} cm²')

elif figura == 'CILINDRO':
    raio_base_cilindro = float(input('Digite o raio da base do cilindro em cm:\n'))
    altura_cilindro = float(input('Digite a altura do cilindro:\n'))

    volume_cilindro = math.pi * math.pow(raio_base_cilindro,2)* altura_cilindro
    area_base = 2 * math.pi * math.pow(raio_base_cilindro,2)
    area_lateral = 2 * math.pi * raio_base_cilindro * altura_cilindro
    area_total = area_base + area_lateral

    print(f'O volume do cilindro é de {volume_cilindro:.2f} cm³')
    print(f'A área total do cilindro é de {area_total:.2f} cm²')

elif figura == 'ESFERA':
    raio_esfera = float(input('Digite o raio da esfera em cm:\n'))

    volume_esfera = (4 * math.pi * math.pow(raio_esfera,3)) / 3
    area_esfera = 4 * math.pi * math.pow(raio_esfera,2)

    print(f'O volume da esfera é de {volume_esfera:.2f} cm³')
    print(f'A área da esfera é de {area_esfera:.2f} cm²')











