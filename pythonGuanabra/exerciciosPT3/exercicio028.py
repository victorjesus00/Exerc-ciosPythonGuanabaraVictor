print('Vou pensar em um número entre 0 e 5. Tente adivinhar qual é.')
from time import sleep
from random import randint
numero = int(input('Em qual número eu pensei?: '))
pensou = randint(0, 5)
processando = 'PROCESSANDO..'

print('PROCESSANDO...')

for processando in range(1):
        sleep(1)
        if numero == pensou:
            print('Você acertou cuzão')
        else:
            print('Voce errou otário ')