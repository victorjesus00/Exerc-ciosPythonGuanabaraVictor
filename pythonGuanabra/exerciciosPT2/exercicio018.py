#Exercício Python 18: Faça um 
# programa que leia um ângulo
# qualquer e mostre na tela o valor do seno, 
# cosseno e tangente
# desse ângulo.

import math 

math.radians


angulo = float(input('Digite o valor que você deseja: '))
seno = math.sin(math.radians(angulo))
coseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print(f'O ângulo de {angulo} tem o SENO de {seno}')
print(f'O ângulo de {angulo} tem o COSENO de {coseno}')
print(f'O ângulo de {angulo} tem o TANGENTE de {tangente}')