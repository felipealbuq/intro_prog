# Informe o tipo de carro (A, B e C) e a distância rodada em km, então mostre
# o consumo estimado, conforme o tipo, sendo (A=8, B=9 e C=12) km/litro.

tipo_carro = str(input('Digite o tipo de carro:\n')).upper()
tipos = ['A','B','C']

while tipo_carro not in tipos:
    tipo_carro = str(input('Digite o tipo de carro válido:\n')).upper()

distancia = float(input('Digite a distância percorrida:\n'))

if tipo_carro == tipos[0]:
    consumo_a = distancia / 8
    print(f'O carro do tipo {tipos[0]} tem consumo estimado de : {consumo_a:.2f} litros.\n')
elif tipo_carro == tipos[1]:
    consumo_b = distancia / 9
    print(f'O carro do tipo {tipos[1]} tem consumo estimado de : {consumo_b:.2f} litros.\n')
elif tipo_carro == tipos[2]:
    consumo_c = distancia / 12
    print(f'O carro do tipo {tipos[2]} tem consumo estimado de : {consumo_c:.2f} litros.\n')