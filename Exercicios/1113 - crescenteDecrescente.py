while True:
    numeros = input().split(' ')
    x = int(numeros[0])
    y = int(numeros[1])

    if x == y:
        break
    elif x > y:
        print('Decrescente')
    elif x < y:
        print('Crescente')
