#Exercício Python 35: Desenvolva um programa que leia 
# o comprimento de três retas e diga ao usuário se elas
# podem ou não formar um triângulo.


lado1 = float(input('Comprimento do lado 1: '))
lado2 = float(input('Comprimento do lado 2: '))
lado3 = float(input('Comprimento do lado 3: '))


if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 < lado1 + lado2:
    print('Os segmentos acima podem formar um triangulo')
else:
    print('Os segmentos acima podem formar um triangulo')