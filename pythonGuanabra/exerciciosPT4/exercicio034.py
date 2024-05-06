#Exercício Python 34: Escreva um programa que pergunte o
# salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.


salario = float(input('Digite seu salário: R$'))

aumento10 = salario + ((salario / 100) * 10)

aumento15 = salario + ((salario/ 100) * 15)

if salario >= 1250.00:
    print(f'Voce receberá um aumento de 10%, e seu novo salário será: R$:{aumento10:.2f}')
else:
    print(f"Voce receberá um aumento de 15%, e seu novo salário será: R${aumento15:.2f}")


