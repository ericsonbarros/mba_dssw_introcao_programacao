import math
h = float(input('Digite a altura do cilindro: ')) # altura do cilindro
r = float(input('Digite o raio do cilindro: ')) # raio do cilindro
a_base = 3.14 * math.pow(r, 2)
a_lateral = 2 * 3.14 * r * h
a_total = 2 * a_base + a_lateral # area total do cilindro
rendimento = float(input('Digite o rendimento da lata de tinta: ' ))
litros_necessarios = a_total / rendimento # quantidade de litros para pintar o cilindro
volume_lata = float(input('Digite o volume da lata de tinta: '))
num_lata = math.ceil(litros_necessarios / volume_lata) # quantidade de lata necessaria para pintura
custo_lata = float(input('Digite o valor unitario da lata de pinta: '))
custo_total = num_lata * custo_lata
print('Sabendo que 1 lata de tinta pinta {} metros, cada lata contem {} litros, e a lata custa {} reais'.format(rendimento, volume_lata, custo_lata))
print('É necessario comprar {} latas de tinta, tendo o custo total de {} reais para pintar todo'.format(num_lata, custo_total))
