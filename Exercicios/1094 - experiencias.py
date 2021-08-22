vezes = int(input())
contador = 0
quantidade = 0
coelho = 0
rato = 0
sapo = 0
while contador < vezes:
    experimentos = input().split(' ')
    quantidadeanimal = int(experimentos[0])
    animal = str(experimentos[1])

    if animal == 'C':
        coelho += quantidadeanimal
        quantidade += quantidadeanimal

    elif animal == 'R':
        rato += quantidadeanimal
        quantidade += quantidadeanimal

    elif animal == 'S':
        sapo += quantidadeanimal
        quantidade += quantidadeanimal

    contador += 1

print(f'Total: {quantidade} cobaias')
print(f'Total de coelhos: {coelho}')
print(f'Total de ratos: {rato}')
print(f'Total de sapos: {sapo}')
print(f'Percentual de coelhos: {((coelho*100)/quantidade):.2f} %')
print(f'Percentual de ratos: {((rato*100)/quantidade):.2f} %')
print(f'Percentual de sapos: {((sapo*100)/quantidade):.2f} %')
