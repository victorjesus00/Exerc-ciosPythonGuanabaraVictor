n = int(input('Digite um número para calcular seu fatorial:  '))
contador = n 
fatorial = 1
print(f'Calculando o fatorial de {n}!!:', end="")
while contador > 0:
    print(f'{contador} ', end=' ')
    print('X' if contador > 1 else '= ', end=' ')
    
    fatorial = fatorial * contador
    
    contador = contador - 1
    print(f'{fatorial}')
