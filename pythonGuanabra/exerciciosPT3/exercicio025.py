#Exercício Python 25:
# Crie um programa que leia
# o nome de uma pessoa e diga
# se ela tem “SILVA” no nome


#Resolução 1.
#-----------------------------------------------------#
nome = str(input('Qual é seu nome? '))

if 'Silva' in nome:
    print('Tem Silva no seu nome!!')   
          
else:                                              
    print('Não tem silva no seu nome.')            
#------------------------------------------------------#

n0m3 = str(input('Qual teu nome?: '))
silva = ('SILVA'in n0m3.upper())
print(f'Seu nome tem Silva? {silva}')