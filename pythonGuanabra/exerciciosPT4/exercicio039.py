#Exercício Python 39: Faça um programa
# que leia o ano de nascimento de um jovem
# e informe, de acordo com a sua idade, se
# ele ainda vai se alistar ao serviço militar, 
# se é a hora exata de se alistar ou se já passou
# do tempo do alistamento.
# Seu programa também deverá mostrar
# o tempo que falta ou que passou do prazo.

from datetime import date

print('Verificando se você já pode alistar!!')
print('=-'*42)

anonasc = int(input("Qual ano você nasceu: "))
idade =  date.today().year - anonasc
alistamento = 18
passouprazo = idade - alistamento
quantofalta = alistamento - idade

if idade == 18:
    print('Está na hora de se alistar, vagabundo!')
elif idade > 18:
    print(f'Já passou da hora de se alistar, você passou {passouprazo} ano(s) do tempo ideal de alistamento.')
elif idade < 18:
    print(f'Não está na hora de se alistar, ainda faltam {quantofalta} ano(s) para você poder se alistar.')