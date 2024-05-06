valor = float(input('Digite um valor em metros para ser convertido em CM e milimetros'))
valorC = valor / 100
valorMI= valor / 1000

print(f"Valor de {valor} em centimetros é {valorC:.5f}")
print(f'Valor de {valor} em milimetros é {valorMI:.5f}')