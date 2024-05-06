#Exercício Python 45: Crie um programa que faça o computador jogar
# Jokenpô com você.


#IMPORTAÇÕES
from random import choice
from time import sleep
#==========================


print('=-'*42)
print('VAMOS JOGAR JONKENPÔ?!')
print('=-'*42)

#ESCOLHAS DO PC.
lista = ['PEDRA', 'PAPEL', 'TESOURA']
pc = choice(lista)

#ESCOLHAS DO USUÁRIO.
print('[ PEDRA ] [ PAPEL ] [ TESOURA ]')

print('=-'*42)
jogador = str(input('Faça sua escolha: '))
print('=-'*42)
print(f'Escolha do PC: {pc}')


#VARIÁVEIS DE OPÇÃO.
pedra = 'PEDRA'
tesoura = 'TESOURA'
papel = 'PAPEL'


#REGRAS
pedra > tesoura
tesoura > papel
papel > pedra


# ============ PERDEU ===========
if pc == pedra and jogador == tesoura:
    print(f'O PC jogou {pc} e você jogou {jogador} então você PERDEU!')
elif pc == tesoura and jogador == papel:
    print(f'O PC jogou {pc} e você jogou {jogador} então você PERDEU!')
elif pc == papel and jogador == pedra:
    print(f'O PC jogou {pc} e você jogou {jogador} então você PERDEU! ')

    
# ========== GANHOU ============
elif pc == tesoura and jogador == pedra:
    print(f'O PC escolheu {pc} e você escolheu {jogador} então você GANHOU!')
elif pc == papel and jogador == tesoura:
    print(f'O PC escolheu {pc} e você escolheu {jogador} então você GANHOU!!')
elif pc == pedra and jogador == papel:
    print(f'O PC escolheu {pc} e você escolheu {jogador} então você GANHOU!!')
else:
    print('Você não escolheu nenhuma das opções acima.')

