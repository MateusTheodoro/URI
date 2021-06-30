num = int(input(''))

horas = num // 3600
r = num % 3600

minutos = r // 60
r = r % 60

segundos = r

print(f'{horas}:{minutos}:{segundos}')
