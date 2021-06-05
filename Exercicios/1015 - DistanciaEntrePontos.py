p1 = input().split(' ')
x1 = float(p1[0])
x2 = float(p1[1])

p2 = input().split(' ')
y1 = float(p1[0])
y2 =float(p2[1])

distancia = ( ( (pow(x2-x1,2)) +  (pow(y2-y1, 2)) ) / 2) ** 0.5

print(f'{distancia:.4f}')