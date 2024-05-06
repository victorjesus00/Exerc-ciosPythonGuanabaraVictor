#Exercício Python 54: Crie um programa que
# leia o ano de nascimento de sete pessoas. 
# No final, mostre quantas pessoas ainda não 
# atingiram a maioridade e quantas já são maiores.

from datetime import date
contador = 0
contadormenor = 0
anoatual = date.today().year
print('=-'*42)
for a in range(1, 8):
    anonasc = int(input(f'Qual o ano de nascimento da {a}ª pessoa?: '))
    print('--'*42)
    anoatual = date.today().year
    idade = anoatual - anonasc 
    if idade > 18:
        contador = contador + 1
    if idade < 18:
        contadormenor = contadormenor + 1
print(f'O total de pessoas que completaram maior idade ou à alcançarão esse ano são: {contador}')
print('--'*42)
print(f'E o total de pessoas que são menores de idade e não alcançarão a maior idade esse ano são: {contadormenor} ')
print('--'*42)
    
