valor = float(input())

if valor >= 0 and valor <= 25:
    print(f'Intervalo [0,25]')

elif valor > 25 and valor <= 50:
    print(f'Intervalo (25,50]')

elif valor > 50 and valor <= 75:
    print(f'Intervalo (50,75]')

elif valor > 75 and valor <= 100:
    print(f'Intervalo (75,100]')

else:
    print(f'Fora de intervalo')
