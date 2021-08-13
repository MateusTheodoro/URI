salario = float(input())
base = salario
imposto = 0

if salario <= 2000:
    print('Isento')
else:
    if base > 4500:
        imposto = imposto + ((base - 4500) * (28 / 100))
        base = 4500
    if base > 3000:
        imposto = imposto + ((base - 3000) * (18 / 100))
        base = 3000
    if base > 2000:
        imposto = imposto + ((base - 2000) * (8 / 100))
        base = 2000

    print(f'R$ {imposto:.2f}')
