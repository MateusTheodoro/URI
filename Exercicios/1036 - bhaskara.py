num = input().split(' ')
a = float(num[0])
b = float(num[1])
c = float(num[2])

delta = (b ** 2) - (4 * a * c)

if delta < 0 or delta == 0 or a == 0:
    print("Impossivel calcular")
else:
    r1 = (- b + (delta ** 0.5)) / (2 * a)
    print(f'R1 = {r1:.5f}')
    r2 = (- b - (delta ** 0.5)) / (2 * a)
    print(f'R2 = {r2:.5f}')