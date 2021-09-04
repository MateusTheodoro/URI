valores = input().split(' ')
d1 = float(valores[0])
d2 = float(valores[1])
d3 = float(valores[2])
decrescente = [d1, d2, d3]
novo = sorted(decrescente, key=float, reverse=True)
a = novo[0]
b = novo[1]
c = novo[2]
if a >= b + c:
    print('NAO FORMA TRIANGULO')
else:
    if (a ** 2) == (b ** 2) + (c ** 2):
        print('TRIANGULO RETANGULO')

    if (a ** 2) > (b ** 2) + (c ** 2):
        print('TRIANGULO OBTUSANGULO')

    if (a ** 2) < (b ** 2) + (c ** 2):
        print('TRIANGULO ACUTANGULO')

    if a == b == c:
        print('TRIANGULO EQUILATERO')

    if a == b != c or a == c != b or b == a != c or b == c != a or c == b != a or c == a != b:
        print('TRIANGULO ISOSCELES')
