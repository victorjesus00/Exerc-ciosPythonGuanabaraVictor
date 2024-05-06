#Exercício Python 53: Crie um programa que leia uma frase qualquer
# e diga se ela é um palíndromo, desconsiderando os espaços. 
#Exemplos de palíndromos:

#APOS A SOPA, A SACADA DA CASA,
# A TORRE DA DERROTA,
# O LOBO AMA O BOLO,
# ANOTARAM A DATA DA MARATONA.

#Não consegui fazer.


frase = str(input('Digite a frase: ')).strip().upper() #<<<<<<Deixei separado com o 'strip' e deixei tudo em letra maiúscula com o 'upper'

palavra = frase.split() #<<<<<<<<<<Separei as palavras da fraase do input com o 'split'

junto = ''.join(palavra) #<<<<<<<Fiz uma variável com o valor da variavel 'palavra' mas coloquei o 'join' e a variavel dentro dele para ser a 'palavra' com tudo junto sem espaços.(no caso foi a aspas sem nada que ultilizei para isso.)

inverso = ''

for letra in range(len(junto) -1, -1, -1):    #<<<<<< Isso que deixou a string de trás para frente.  #Usei o len para pegar a última letra. Somou mais um (no caso seria (+1), mas como estamos fazendo ao contrário será (-1). ele vai até a primeira letra. E ele vai voltar (-1), vai andar um passo negativo.)
    
    inverso += (junto[letra]) #Usamos a varíavel 'inverso' que está vazia para transformala no 'junto' (que é a palavra (input) tudo junto sem espaços) e adicionamos a varíavel 'letra' que está dentro do for para se repetir(ela deixa as coisas de trás para frente). Então, assim o 'inverso' recebe a palavra de trás para frente (por conta da configuração do for) e sem espaços (por conta da configuração do 'junto com o parâmetro *join*)
    
print(junto, inverso)  #<<< Printamos o *junto*(frase toda junta sem espaços) e o *inverso*(frase toda junta sem espaços (DE TRÁS PARA FRENTE.))


#Fizemos uma condição para definir qual é PALÍNDROMO e qual não se encaixa como tal.
if inverso == junto:
    print('É um PALÍNDROMO (igual de trás para frente e vice versa.)')
else:
    print('Não é um PALÍNDROMO, (diferente de trás para frente e vice versa)')