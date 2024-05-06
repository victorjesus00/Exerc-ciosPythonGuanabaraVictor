#Exercício Python 33: Faça um programa que leia
#três números e mostre qual é o maior e qual é o menor.

primeiro = int(input('Digite o primeiro valor: '))
segundo = int(input('Digite o segundo valor: '))
terceiro = int(input('Digite o terceiro valor: '))

menor = primeiro
maior = segundo
#Menor ------------------------------------- 
if segundo < primeiro and segundo < terceiro:
    menor = segundo
if terceiro < primeiro and terceiro < segundo:
    menor = terceiro
#Maior ------------------------------------ 
if primeiro > segundo and primeiro > terceiro:
    maior = primeiro
if terceiro > segundo and terceiro > primeiro:
    maior = terceiro
    
print(f"O maior foi {maior}")
print(f"O menor foi {menor}")

    
