#Exercício Python 041: A Confederação Nacional de Natação precisa de um
# programa que leia o ano de nascimento de um atleta e mostre sua
# categoria, de acordo com a idade:

from datetime import date

anonasc = int(input('Data de nascimento: '))
idade = date.today().year - anonasc

if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JÚNIOR')
elif idade <= 25:
    print('SÊNIOR')
else:
    print('MASTER')