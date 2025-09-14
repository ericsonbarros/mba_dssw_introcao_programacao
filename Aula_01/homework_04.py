print('-='*5 + 'Ola!' + '-='*5)
altura = float(input('Digite a sua altura em metros: '))
kg = float(input('Digite quantos quilogramas voce tem: '))
print('Com base na sua altura de {} metros, e em {} quilogramas que possui, o seu IMC e de {}'.format(altura, kg, (kg/(altura**2))))
