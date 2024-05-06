#Exercício Python 62: Melhore o DESAFIO 61,
# perguntando para o usuário se ele quer mostrar
# mais alguns termos. O programa encerrará quando
# ele disser que quer mostrar 0 termos.

#  CONSEGUI.


print('Termos da progressão.')

primeiro = int(input('Primeiro termo: ')) # primeiro termo

print('=-'*42)

razao = int(input('Razão da PA: ')) #Razao,

print('=-'*42)

vezes = int(input('Quantas vezes será executado?', ))
cont = 1 # Aqui ele vai contar quantos termos foram. #CONTADOR.

while cont <= vezes: #Enquanto o contador (cont) for menor ou igual á 10
    print(f'{primeiro} ', end='')#faço o print do resultado. primeiro + razao, ex primeiro = 5, razão = 2 = 7, o primeiro será acrescentado pela razão *10* vezes
    primeiro = primeiro + razao #primeiro recebe ele mesmo MAIS a razão,  (assim será feito o cálculo.). ele vai subindo pois o primeiro vai recebendo a ele mesmo + a razao.
    cont += 1 # de acordo com que estas somas vão acontecendo o contador vai somando MAIS 1, ATÉ ELE CHEGAR A 10, e assim vai parar de ser executado.

print('PAUSA.')


deseja = int(input('Deseja mostrar mais quantos?: ', ))
quantos = deseja
for quantos in range(deseja) :
    print(f'{primeiro} ', end= ' ' )#faço o print do resultado. primeiro + razao, ex primeiro = 5, razão = 2 = 7, o primeiro será acrescentado pela razão *10* vezes
    primeiro = primeiro + razao #primeiro recebe ele mesmo MAIS a razão,  (assim será feito o cálculo.). ele vai subindo pois o primeiro vai recebendo a ele mesmo + a razao.
    cont += 1 # de acordo com que estas somas vão acontecendo o contador vai somando MAIS 1, ATÉ ELE CHEGAR A 10, e assim vai parar de ser executado.
    
print(f'O total de termos executado foi de {cont + 1}', )
   
        
print('FIM.', )
