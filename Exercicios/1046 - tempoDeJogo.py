horas = input().split(' ')
a = int(horas[0])
b = int(horas[1])

if a == b:
    print(f'O JOGO DUROU 24 HORA(S)')
elif a > b:
    print(f'O JOGO DUROU {(24-a) + b} HORA(S)')
elif b > a:
    print(f'O JOGO DUROU {b-a} HORA(S)')
