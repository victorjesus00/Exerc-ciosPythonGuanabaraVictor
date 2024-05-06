#Exercício Python 56: Desenvolva um programa que leia o nome,
# idade e sexo de 4 pessoas. No final do programa, mostre:
# a média de idade do grupo, qual é o nome do homem mais velho e
# quantas mulheres têm menos de 20 anos.

print('=-'*42)

somaidade = 0
mediaidade = 0
mulheres20 = 0
maisvelho = 0 
nomemaisvelho = ''
for i in range(1, 5):
    print(f' <>--------{i}ª PESSOA -------<>')
    nome = str(input(f'Nome: ').strip)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    somaidade += idade
    mediaidade = somaidade / 4
    if idade < 20 and sexo == 'F' or sexo == 'f':
        mulheres20 =  mulheres20 + 1
    if i == 1 and sexo in 'Mm':
        maisvelho = idade
        nomemaisvelho = nome
    if sexo in "Mm" and idade > maisvelho:
        maisvelho = idade
        nomemaisvelho = nome
print('=-'*42)
print(f'A media de idade do grupo é de {mediaidade:.0f}')
print('=-'*42)
print(f'A quantidade de mulheres com menos de vinte anos é de {mulheres20}')
print('=-'*42)
print(f'O homem mais velho tem {maisvelho} e seu nome é {nomemaisvelho}')
    
    