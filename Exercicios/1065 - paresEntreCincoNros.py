pares = 0
contador = 1

while contador <= 5:
    nro = int(input())
    if nro % 2 == 0:
        pares += 1
    contador += 1
print(f'{pares} valores pares')
