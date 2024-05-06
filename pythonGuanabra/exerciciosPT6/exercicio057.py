#Exercício Python 57: Faça um programa que leia o sexo de uma pessoa,
# mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação
# novamente até ter um valor correto.

print('Vamos ver qual é o seu sexo.')
print('-='*42)
sexo = str(input('Qual é o seu sexo?: [M/F] ')).upper()
print('-='*42)
while sexo != "M" and sexo != "F":
            sexo = str(input('Valor incorrreto, digite seu sexo: '))
if sexo not in 'Mm':
     print('Seu sexo é feminino')
elif sexo not in 'Ff':
    print('Seu sexo é masculino')
