contador = 1
positivos = 0
soma = 0
while contador <= 6:
    nro = float(input())

    if nro > 0:
        positivos += 1
        soma = soma + nro

    contador += 1

print(f'{positivos} valores positivos')
print(f'{soma / positivos:.1f}')
