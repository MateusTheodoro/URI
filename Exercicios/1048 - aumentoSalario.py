salario = float(input())

if salario <= 400:
    print(f'Novo salario: {salario + (salario * (15 / 100)):.2f}')
    print(f'Reajuste ganho: {(salario * (15 / 100)):.2f}')
    print(f'Em percentual: 15 %')
elif salario <= 800:
    print(f'Novo salario: {salario + (salario * (12 / 100)):.2f}')
    print(f'Reajuste ganho: {(salario * (12 / 100)):.2f}')
    print(f'Em percentual: 12 %')
elif salario <= 1200:
    print(f'Novo salario: {salario + (salario * (10 / 100)):.2f}')
    print(f'Reajuste ganho: {(salario * (10 / 100)):.2f}')
    print(f'Em percentual: 10 %')
elif salario <= 2000:
    print(f'Novo salario: {salario + (salario * (7 / 100)):.2f}')
    print(f'Reajuste ganho: {(salario * (7 / 100)):.2f}')
    print(f'Em percentual: 7 %')
else:
    print(f'Novo salario: {salario + (salario * (4 / 100)):.2f}')
    print(f'Reajuste ganho: {(salario * (4 / 100)):.2f}')
    print(f'Em percentual: 4 %')
