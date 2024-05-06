#Exercício Python 49: Refaça o DESAFIO 9, mostrando a tabuada
# de um número que o usuário escolher, só que agora utilizando
#um laço for.


user = int(input('Escolha um número INTEIRO para fazermos a tabuada dele do 1 até o 10: '))


for i in range(1, 11):
    print(f'{user} X {i} = {(user * i)}')