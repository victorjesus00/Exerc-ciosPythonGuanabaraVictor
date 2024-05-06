#Sorteando um item na lista
from random import choice
nome1 = str(input("nome 1: "))
nome2 = str(input("nome 2: "))
nome3 = str(input('nome 3: '))
nome4 = str(input("nome 4: "))
lista = [nome1, nome2, nome3, nome4]
escolhido = choice(lista)
print(f'O aluno escolhido foi {escolhido} ' )

