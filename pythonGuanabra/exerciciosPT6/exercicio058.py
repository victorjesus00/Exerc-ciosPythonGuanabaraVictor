#Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar”
#em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, 
#mostrando no final quantos palpites foram necessários para vencer.

from random import randint

print('Jogo da adivinhação 2.0')
print('-='*42)
jogador = int(input('Qual número acha que estou pensando??: '))
pc = randint(0,6)

while jogador != pc:
    print(f'Errou!! HAHAHA, pensei no número {pc} e você disse {jogador}.')
    pc = randint(0,6)
    jogador = int(input('Tente novamente!!: '))
if jogador == pc:
    print(f'Ahh, você ganhou de mim, você disse {jogador} e eu {pc} >:C ')