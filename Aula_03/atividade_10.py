from random import randint
from time import sleep
print('='*40)
print('JOGO DA ADVINHAÇÃO')
print('='*40)
computer = randint(1,100)
print('Vou pensar em um numero tente adivinhar qual e...')
player = int(input('Qual numero pensei? '))
while True:
    if computer != player:
        print('PROCESSANDO...')
        sleep(2)
        print('-' * 60)
        if computer > player:
            print(f'voce errou!!, o numero {player} e MENOR que o numero que escolhi')
            player = int(input('Vamos tentar novamente!, escolha um novo numero: '))
        elif computer < player:
            print(f'voce errou!!, o numero {player} e MAIOR que o numero que escolhi')
            player = int(input('Vamos tentar novamente!, escolha um novo numero: '))
    else:
        break
print('PARABENS VOCE ACERTOU O NUMERO!!!!')
