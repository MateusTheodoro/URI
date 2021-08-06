qtd_vezes = int(input())
contador = 1
while qtd_vezes >= contador:
    notas = input().split(' ')
    n1 = float(notas[0])
    n2 = float(notas[1])
    n3 = float(notas[2])

    media = ((2 * n1) + (3 * n2) + (5 * n3)) / (2 + 3 + 5)

    print(f'{media:.1f}')

    contador += 1
