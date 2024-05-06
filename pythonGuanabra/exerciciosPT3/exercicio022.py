#Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:

#– O nome com todas as letras maiúsculas e minúsculas.

#– Quantas letras ao todo (sem considerar espaços).

#– Quantas letras tem o primeiro nome.

nome = str(input('Qual é seu nome?: ')).strip()

print(f"Seu nome em letra maiúscula {nome.upper()} e seu nome em letra minúscula {nome.lower()}")
noespace = (len(nome)-nome.count(' '))
print(f'Seu nome todo tem {noespace} letras')
primeironome = nome.find(' ')
print(f'Seu primeiro nome tem {primeironome} letras')



