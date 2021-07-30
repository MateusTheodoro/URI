valor = input().split(' ')
a = int(valor[0])
b = int(valor[1])

if a > b and a % b == 0:
    print(f'Sao Multiplos')
elif b > a and b % a == 0:
    print(f'Sao Multiplos')
else:
    print(f'Nao sao Multiplos')
