#Exercício Python 15: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

print('ALUGUEL DE CARROS.')
km = float(input('Quantos KM foram rodados? '))
dias = float(input('Por quantos dias o carro foi usado? '))
precoporkm = dias  * 60
kmrodado = km  * 0.15

total = precoporkm + kmrodado

print(f'Voce vai pagar R$:{total:.2f} por {km} percorridos e {dias}  ')