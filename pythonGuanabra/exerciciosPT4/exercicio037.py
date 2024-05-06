#Exercício Python 37: Escreva um programa
# em Python que leia um número inteiro qualquer
# e peça para o usuário escolher qual será a base
# de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

#Meu código===========================================================
num = int(input('Digite um número inteiro: '))
print('Escolha umas das bases para conversão:')
print('[ 1 ] converter para BINÁRIO')
print('[ 2 ] converter para OCTAL')
print('[ 3 ] converter para HEXADECIMAL')
opção = int(input('Sua opção: '))

if opção == 1 :
    print(f"{num} convertido para BINÁRIO é {bin(num)}")
elif opção == 2 :
    print(f'{num} convertido para OCTAL é {oct(num)}')
elif opção == 3 :
    print(f'{num} convertido para HEXADECIMAL é {hex(num)}')
else:
    print('Você não escolheu nenhum dos números acima.')
#=====================================================================