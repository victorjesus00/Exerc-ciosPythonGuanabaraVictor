#Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:

#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.


print('Formatando dois números inteiros.')
print('=-'*42)

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

resposta = 0 

while resposta != 5:
    print('[ 1 ] Para somar.')
    print('[ 2 ] Para multiplicar.')
    print('[ 3 ] Para descobrir qual é maior.')
    print('[ 4 ] Para digitar novos números.')
    print('[ 5 ] Para sair do programa. ')
    print('=-'*42)
    resposta = int(input('Qual formatação deseja realizar?: '))

    if resposta == 1:
        print(f'Resultado: {(n1 + n2)}')
    elif resposta == 2:
        print(f'Resultado: {n1 * n2}')
    elif resposta == 3:
        if n1 > n2:
            print(f"O maior é {n1}")
        elif n2 > n1:
            print(f'O maior é {n2}')
        elif n1 == n2:
            print(f'{n1} é igual á {n2}')
    elif resposta == 4:
        print('Informe os números novamente.')
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
    elif resposta == 5:
        print('Obrigado por usar meu programa, tchau!!!')
    else:
        print('Opção inexistente, tente novamente por favor.')
    print('-=-'*10)
print('Fim do programa! Volte sempre.')
        
        


        
        


        
        
        

    
    

