#Exercício Python 46: Faça um programa que mostre na tela
# uma contagem regressiva para o estouro de fogos de artifício,
# indo de 10 até 0, com uma pausa de 1 segundo entre eles.



from time import sleep
print('Contagem regressiva para os fogos de artifício.')
for v in range(1, 11):
    sleep(1)
    print(v)
print('Feliz ano novo!')