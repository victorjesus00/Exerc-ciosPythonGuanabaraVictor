#Exercício Python 48: Faça um programa que calcule a soma entre
# todos os números que são múltiplos de três e que se encontram
# no intervalo de 1 até 500.


print('Vamos ver quantos números são divísiveis por 3 de 1 até 500 ')

soma = 0
contador = 0

for i in range(1, 501, 2):
    if i % 3 == 0:
        contador = contador + 1
        soma = soma + i
print(f'A soma de todos os valores foi: {soma}')
print(f'E a quantidade de valores identificados foi: {contador}')
    