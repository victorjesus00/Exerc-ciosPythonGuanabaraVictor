#Exercício Python 50: Desenvolva
# um programa que leia seis números inteiros
# e mostre a soma apenas
# daqueles que forem pares. Se o valor digitado
# for ímpar, desconsidere-o.

soma = 0
cont = 0

for c in range(1, 4):
    num = int(input(f'Digite o {c} número para ser somado '))
    if num % 2 == 0:
        soma = soma + num
        cont = cont + 1
print(f'o total de números foi {cont} e a soma total dos números foi {soma}')
        

   