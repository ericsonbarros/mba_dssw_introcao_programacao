print('-='*5 + '\033[1;36;40mOla!\033[m' + '-='*5)
name = str(input('Insira o nome do paciente: '))
weight = float(input('Insira o peso(Kg) do paciente: '))
heigth = float(input('Insira a altura(m) do paciente: '))
imc = weight / (pow(heigth,2))
print(f'{name} o seu IMC corresponde a {imc:.1f} a sua condição é de: ',end = '')
if imc < 18.5:
    print('Abaixo do peso')
elif imc < 25:
    print('Peso normal')
elif imc < 30:
    print('Sobrepeso')
elif imc <35:
    print('Obesidade grau I')
elif imc < 40:
    print('Obesidade grau II')
else:
    print('Obesidade grau III')

