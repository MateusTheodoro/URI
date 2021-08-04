vezes = int(input())
contador = 1
while contador <= vezes:
    numeros = int(input())

    if numeros == 0:
        print('NULL')
    elif numeros % 2 == 0 and numeros > 0:
        print('EVEN POSITIVE')
    elif numeros % 2 != 0 and numeros > 0:
        print('ODD POSITIVE')
    elif numeros % 2 == 0 and numeros < 0:
        print('EVEN NEGATIVE')
    elif numeros % 2 != 0 and numeros < 0:
        print('ODD NEGATIVE')

    contador += 1
