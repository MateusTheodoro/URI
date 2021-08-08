contador = 0
media = 0
while contador < 2:
    nota = float(input())
    if nota > 10 or nota < 0:
        print('nota invalida')
        continue
    else:
        media += nota
    contador += 1
print(f'media = {media / 2:.2f}')
