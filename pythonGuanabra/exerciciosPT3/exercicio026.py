#Exercício Python 26: Faça um programa que
# leia uma frase pelo teclado e mostre quantas
# vezes aparece a letra “A”, em que posição ela
# aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input('Escreva uma frase por favor: ')).upper()
quantosA = frase.count('A')
primeiroA = frase.find('A') + 1
ultimoA = frase.rfind('A')
print(f'Tem {quantosA} "a" nesta frase')
print(f'O primeiro "a" aparece na posição: {primeiroA}')
print(f'O último "a" aparece na posição: {ultimoA}')

