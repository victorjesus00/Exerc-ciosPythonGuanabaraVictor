#Exercício Python 32: Faça um programa 
# que leia um ano qualquer
# e mostre se ele é bissexto.
from datetime import date 
ano = int(input('Qual ano? (DIGITE 0 PARA O ANO ATUAL.) ' ))



if ano == 0:
    ano = date.today().year

if ano  % 4  == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Este ano é bissexto!!!')

else:
    print('Este ano não é bissexto.')

