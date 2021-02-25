produto1 = input().split(' ')
a = int(produto1[0])
b = int(produto1[1])
c = float(produto1[2])

produto2 = input().split(' ')
e = int(produto2[0])
f = int(produto2[1])
g = float(produto2[2])

aPagar = (b * c) + (f * g)

print(f'VALOR A PAGAR: R$ {aPagar:.2f}')
