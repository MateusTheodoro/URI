x = int(input())
contador = 1
pares = 0
while contador < 7:
    if x % 2 == 0:
        x += 1
        continue
    elif x % 2 != 0:
        print(x)
        x += 2
    contador += 1
