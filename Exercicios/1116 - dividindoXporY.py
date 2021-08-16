qtdvezes = int(input())
contador = 0
while qtdvezes > contador:
    divisao = input().split(' ')
    x = int(divisao[0])
    y = int(divisao[1])

    if y == 0:
        print('divisao impossivel')
    else:
        print(f'{float(x / y):.1f}')
    contador += 1
