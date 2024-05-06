#Exercício Python 36: Escreva um programa para aprovar o empréstimo
# bancário para a compra de uma casa. Pergunte o valor da casa,
# o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o
# empréstimo será negado.





#Meu código =======================================================================
print( '-='*50)
casa = float(input('Digite o valor da casa que será comprada: R$'))
salario = float(input('Qual é o seu salário?: R$'))
anos = int(input('De quantos anos será o financiamento? R$'))
prestacao = casa / (anos * 12)
minimo =  salario * 30 / 100
print( '-='*50)
print(f'Para pagar uma casa de {casa} em {anos} anos', end='' )
print(f'A prestação será de {prestacao:.2f}')
print( '=-'*50)

if prestacao <= minimo:
    print("Aprovado")
else:
    print('Negado')
#=------------------------------------------------------------------------------------
    
    
    
    
    
    
#Guamabara=================================================================================================
casa = float(input('Valor da casa: R$'))
salario = float(input('Salario do comprador: R$'))
anos = int(input('Quantos anos de financiamento?'))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100
print(f'Para pagar uma casa de R${casa} em {anos} anos', end='')
print(f'a prestação será de R${prestacao:.2f}')
if prestacao <= minimo:
    print('Empréstimo pode ser concedido.')
else:
    print('Empréstimo negado')
#========================================================================================================