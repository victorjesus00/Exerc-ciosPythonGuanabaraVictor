#Exercício Python 30: Crie um programa que
# leia um número inteiro
# e mostre na tela se ele é PAR ou ÍMPAR.

print('Digite um número inteiro e veremos se é par ou ímpar')
numero = int(input('Digite um número INTEIRO: '))



if numero % 2 == 0:
    print('Este número é par')
else:
    print('Este número ímpar')
