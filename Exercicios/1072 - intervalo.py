x = int(input())
contador = 1
dentro = 0
fora = 0

while contador <= x:
    y = int(input())

    if y >= 10 and y <= 20:
        dentro += 1
    else:
        fora += 1

    contador += 1

print(f'{dentro} in')
print(f'{fora} out')
