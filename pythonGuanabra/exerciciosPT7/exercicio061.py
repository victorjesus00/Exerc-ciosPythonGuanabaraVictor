#Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro
#termo e a razão de uma PA, mostrando os 10 primeiros termos
#da progressão usando a estrutura while.

print('10 Primeiros termos da progressão.')

primeiro = int(input('Primeiro termo: ')) # primeiro termo

print('=-'*42)

razao = int(input('Razão da PA: ')) #Razao,

print('=-'*42)

cont = 1 # Aqui ele vai contar quantos termos foram. #CONTADOR.

while cont <= 10: #Enquanto o contador (cont) for menor ou igual á 10
    print(f'{primeiro} ', end=' ')#faço o print do resultado. primeiro + razao, ex primeiro = 5, razão = 2 = 7, o primeiro será acrescentado pela razão *10* vezes
    primeiro = primeiro + razao #primeiro recebe ele mesmo MAIS a razão,  (assim será feito o cálculo.). ele vai subindo pois o primeiro vai recebendo a ele mesmo + a razao.
    cont += 1 # de acordo com que estas somas vão acontecendo o contador vai somando MAIS 1, ATÉ ELE CHEGAR A 10, e assim vai parar de ser executado.
    
print('FIM.')
