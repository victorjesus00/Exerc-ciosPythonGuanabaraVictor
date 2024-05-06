#Exercício Python 040: Crie um programa que leia duas notas de um
# aluno e calcule sua média, mostrando uma mensagem no final, de 
#acordo com a média atingida:

#– Média abaixo de 5.0: REPROVADO

#– Média entre 5.0 e 6.9: RECUPERAÇÃO

#– Média 7.0 ou superior: APROVADO

n1 = float(input('Qual foi a primeira nota?: '))
n2 = float(input('Segunda nota: '))
m = (n1 + n2) / 2

print(f'Sua média foi {m} e você está:')

if m < 5.0:
    print('REPROVADO!!!!!')
    
elif m >= 5.0 and m <= 6.9:
    print('de RECUPERAÇÃO!!!')
    
else:
    print('APROVADO!!!')