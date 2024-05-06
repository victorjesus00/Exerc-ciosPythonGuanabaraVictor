#Exercício Python 24: Crie um programa que leia o nome de
# uma cidade diga se ela começa ou não com o nome “SANTO”.

city = str(input('Qual o nome da cidade?: ')).strip()
citysanto = (city[:5].upper() == 'SANTO' )
print(citysanto)
