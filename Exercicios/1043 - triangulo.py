valores = input().split(' ')
a = float(valores[0])
b = float(valores[1])
c = float(valores[2])

if (a+b)>c and (a+c)>b and (b+a)>c and (b+c)>a and (c+a)>b and (c+b)>a:
    print(f'Perimetro = {a+b+c}')
else:
    print(f'Area = {((a + b) * c) / 2}')
