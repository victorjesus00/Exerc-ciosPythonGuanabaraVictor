#Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando
# o recurso de mostrar que tipo de triângulo será formado:

#– EQUILÁTERO: todos os lados iguais

#– ISÓSCELES: dois lados iguais, um diferente

#– ESCALENO: todos os lados diferentes


lado1 = float(input('Comprimento do lado 1: '))
lado2 = float(input('Comprimento do lado 2: '))
lado3 = float(input('Comprimento do lado 3: '))


if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print('Os segmentos acima podem formar um triangulo', end='')
    if lado1 == lado2 == lado3:
        print(' EQUILÁTERO')
    elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3 and lado3 != lado1:
        print(' ESCALENO')
    else:
        print(' ISOCELES')
else:
    print('Os segmentos acima não podem formar um triangulo')