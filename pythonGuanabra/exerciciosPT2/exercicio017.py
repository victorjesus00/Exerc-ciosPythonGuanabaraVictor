#Exercício Python 17: Faça um programa que leia o 
# comprimento do cateto oposto e do 
# cateto adjacente de um triângulo retângulo. 
# Calcule e mostre o comprimento da hipotenusa

oposto = float(input('Cateto oposto: '))
adjacente = float(input('Cateto Adjacente: '))

hipotenusa = (oposto ** 2 + adjacente ** 2) ** (1/2)

print(f'A hipotenusa vai medir {hipotenusa:.2f}')

#---------------------------------------------------------------------------------------------------------------
                   #COM IMPORT MATH#

from math import hypot

oposto2 = float(input('Cateto oposto: '))
adjacente2 = float(input('Cateto Adjacente: '))

hipotenusa = hypot(oposto2, adjacente2)

print(f'A hipotenusa vai medir {hipotenusa:.2f}')