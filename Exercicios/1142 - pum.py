nro = int(input())
a = 1
b = 2
c = 3
contador = 1
while nro >= contador:
    if a == 1:
        print(f'1 2 3 PUM')
        a += 4
        b += 4
        c += 4
    else:
        print(f'{a} {b} {c} PUM')
        a += 4
        b += 4
        c += 4

    contador += 1
