x = int(input())
y = int(input())
if x >= y:
    valores = list(range(y, x + 1))

    soma = []

    for valor in valores:
        if valor % 13 != 0:
            soma.append(valor)
else:
    valores = list(range(x, y + 1))

    soma = []

    for valor in valores:
        if valor % 13 != 0:
            soma.append(valor)

soma = sum(soma)
print(soma)
