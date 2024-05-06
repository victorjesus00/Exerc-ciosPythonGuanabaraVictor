#Exercício Python 27: Faça um programa que
# leia o nome completo de uma pessoa, mostrando
# em seguida o primeiro e o último nome separadamente.

nome = str(input('Qual teu nome?: ')).split()
primeironome = nome[0]
segundonome = nome[1]
ultimo = nome[-1]
print(f'Seu nome inteiro é {nome}')
print(f'Seu primeiro nome é: {primeironome}')
print(f'Seu último nome é: {ultimo}')
#==========================================================================


nom3 = str(input('Nome: ')).strip()
name = nom3.split()
print(f'Seu nome é {nom3}')
print(f'Seu primeiro nome: {name[0]}')
print(f'Seu segundo nome: {name[-1]}')

#================================================================================