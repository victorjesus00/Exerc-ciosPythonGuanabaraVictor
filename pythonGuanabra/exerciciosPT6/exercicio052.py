#Exercício Python 52: Faça um 
# programa que leia um número 
# inteiro e diga se ele é ou não um número primo.

#Número primo = numero divisível por 1 e por ele mesmo.

print('Vamos verificar se o número é primo')
print('=-'*42)
NUMERO = int(input('Digite um número: '))

for c in range(1, NUMERO + 1):
    if NUMERO % c == 0:
        print('\033[34m', end=' ')
else:
    print()
    
    