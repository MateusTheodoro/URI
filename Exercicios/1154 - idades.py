idades = []
contador = 0
while True:
    idade_usuario = float(input())
    if idade_usuario < 0:
        break
    else:
        idades.append(idade_usuario)
        contador += 1
somadasidades = sum(idades)
print(f'{somadasidades / contador:.2f}')
