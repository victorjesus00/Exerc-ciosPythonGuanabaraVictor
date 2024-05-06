#Exercício Python 44: Elabore um programa que calcule o valor a ser
# pago por um produto, considerando o seu preço normal e condição de
# pagamento:

#– à vista dinheiro/cheque: 10% de desconto

#– à vista no cartão: 5% de desconto

#– em até 2x no cartão: preço formal 

#– 3x ou mais no cartão: 20% de juros

preco = float(input('qual o preço do produto?: '))

desconto10 = preco - ((preco * 10) / 100) 
desconto5 = preco - ((preco * 5) / 100)
cartao2x = preco / 2
cartao3x = preco + ((preco * 20) / 100)


print('[ 1 ] - PARA PAGAMENTO À VISTA DINHEIRO/CHEQUE: 10% DE DESCONTO. ')
print('[ 2 ] - À VISTA NO CARTÃO: 5% DE DESCONTO. ')
print('[ 3 ] - EM ATÉ 2X NO CARTÃO: PREÇO FORMAL. ')
print('[ 4 ] - 3X OU MAIS NO CARTÃO: 20% DE JUROS.')

opcao = int(input('Qual será o método de pagamento? R$: '))




if opcao == 1:
    print(f'Você receberá 10% de desconto e a compra sairá por R${desconto10} ')
elif opcao  == 2:
    print(f'Você receberá 5% de desconto, e o preço do produto será R${desconto5}')
elif opcao == 3:
    print(f'O pagamento será no cartão em 2x de R${cartao2x}.')
elif opcao == 4:
    print(f'O pagamento será no cartão em 3x ou mais e terá o júros de R${cartao3x}.')
else:
    print('Você não escolheu nenhuma das opções acima.')