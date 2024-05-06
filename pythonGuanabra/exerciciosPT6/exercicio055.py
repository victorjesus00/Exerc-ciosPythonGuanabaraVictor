#Exercício Python 55: Faça um programa 
# que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e 
# o menor peso lidos.

                            #Não consegui.

print('=-'*42)
for i in range(1, 6):
    peso = float(input(f'Qual o peso da {i}ª pessoa?: ')) 
    if i == 1: # <<<Esta condição significa que estou lendo o peso da primeira pessoa.
        
        maior = peso #SE FOR O PRIMEIRO, ele receberá o maior peso, e o menor peso, (pq só tem ele.)
        
        menor = peso
        
    else: # SE NÃO FOR O PRIMEIRO (o que vier depois).
        
        if peso > maior: #Se o PESO que eu acabei de ler, for MAIOR do que o peso que eu tenho, então este peso se torna o maior
             
            maior = peso #,então este peso se torna o maior 
            
        if peso < menor: # E Se o PESO que eu acabei de ler, for MENOR que o peso anterior (peso que eu tenho) então este peso se torna o menor
            menor = peso #então este peso se torna o menor
            
            
                #Prints.
print(f'O maior peso lido foi de {maior}KG.')
print(f'O menor peso lido foi de {menor}KG.')
    