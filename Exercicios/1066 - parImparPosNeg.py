contador = 1
negativo = 0
positivo = 0
pares = 0
impares = 0

while contador <= 5:

    nro = int(input())

    if nro % 2 == 0:
        pares += 1
    if nro % 2 != 0:
        impares += 1
    if nro > 0:
        positivo += 1
    if nro < 0:
        negativo += 1
    contador += 1

print(f'{pares} valor(es) par(es)')
print(f'{impares} valor(es) impar(es)')
print(f'{positivo} valor(es) positivo(s)')
print(f'{negativo} valor(es) negativo(s)')
