contador = 1
negativo = 0
positivo = 0
pares = 0

while contador <= 5:

    nro = int(input())

    if nro < 0:
        negativo += 1
    elif nro > 0:
        positivo += 1
    elif nro % 2 == 0:
        pares += 1
    contador += 1

print(negativo)
print(positivo)
print(pares)
