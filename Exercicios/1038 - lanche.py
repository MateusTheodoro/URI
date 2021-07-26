input_usuario = input().split(' ')
codigo = int(input_usuario[0])
qtd = int(input_usuario[1])

if codigo == 1:
    print(f'Total: R$ {qtd * 4:.2f}')

if codigo == 2:
    print(f'Total: R$ {qtd * 4.50:.2f}')

if codigo == 3:
    print(f'Total: R$ {qtd * 5:.2f}')

if codigo == 4:
    print(f'Total: R$ {qtd * 2:.2f}')

if codigo == 5:
    print(f'Total: R$ {qtd * 1.50:.2f}')
