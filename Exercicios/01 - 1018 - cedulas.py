valor = 180
notas = [100, 50, 20, 10, 5, 2]

print('NOTAS: ')
for x in notas:
    print(f'{int(valor / x)} nota(s) de R$ {x:.2f}')
    valor %= x
