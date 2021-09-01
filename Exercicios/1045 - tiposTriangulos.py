valores = input().split(' ')
a = float(valores[0])
b = float(valores[1])
c = float(valores[2])

if a >= (b + c):
    print('NAO FORMA TRIANGULO')

if (a ** 2) == (b ** 2) + (c ** 2):
    print('TRIANGULO RETANGULO')

if (a ** 2) > (b ** 2 + c ** 2):
    print('TRIANGULO OBTUSANGULO')

if (a ** 2) < (b ** 2 + c ** 2):
    print('TRIANGULO ACUTANGULO')

if a == b == c:
    print('TRIANGULO EQUILATERO')

if a == b != c or a == c != b or b == a != c or b == c != a or c == b != a or c == a != b:
    print('TRIANGULO ISOSCELES')
