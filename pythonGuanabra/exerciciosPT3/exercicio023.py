#Exercício Python 23: Faça um programa que leia um número de
# 0 a 9999 e mostre na tela cada um dos dígitos separados.

numero = int(input('Digite um número: '))
print(f'Analisando o número {numero}')
numerouni = str(numero // 1 % 10)
numerodeze = str(numero // 10 % 10)
numerocente = str(numero // 100 % 10)
numeromilhar = str(numero // 1000 % 10)


print(f'Unidade: {numerouni} ')
print(f'Dezena: {numerodeze} ')
print(f'Centena: {numerocente}')
print(f'Milhar {numeromilhar}')