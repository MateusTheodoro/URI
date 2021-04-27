numero = input().split(' ')
a = int(numero[0])
b = int(numero[1])
c = int(numero[2])
MaiorAB = (a+b+abs(a-b)) / 2
if c > MaiorAB:
    print(f'{c} eh o maior')
else:
    print(f'{MaiorAB:.0f} eh o maior')
