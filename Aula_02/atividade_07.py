temp = float(input('Digite a temperatura: '))
escala = str(input('Digite a escala escolhida da temperatura: '))
if escala == 'celsius':
    temp_convertida_c = (temp * 9 / 5) + 32
    print(f'A temperatura de {temp} °C corresponde a {temp_convertida_c} Fahrenheit')
elif escala == 'fahrenheit':
    temp_convertida_f = (temp - 32) * 5/ 9
    print(f'A temperatura de {temp} °F corresponde a {temp_convertida_f} Celsius')
