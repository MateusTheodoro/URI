contador = 1
positivo = 0

while contador <= 6:
    valores = float(input())
    if valores > 0:
        positivo += 1
    contador += 1
print(f'{positivo} valores positivos')
