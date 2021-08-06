grenais = 0
vinter = 0
vgremio = 0
empates = 0

while True:
    times = input(). split(' ')
    inter = int(times[0])
    gremio = int(times[1])

    if inter > gremio:
        vinter += 1
    elif gremio > inter:
        vgremio += 1
    elif inter == gremio:
        empates +=1

    grenais += 1

    print('Novo grenal (1-sim 2-nao)')
    novogrenal = input()
    if novogrenal == '2':
        break
    else:
        continue
print(f'{grenais} grenais')
print(f'Inter:{vinter}')
print(f'Gremio:{vgremio}')
print(f'Empates:{empates}')
if vgremio > vinter:
    print('Gremio venceu mais')
elif vinter > vgremio:
    print('Inter venceu mais')
else:
    print('Nao houve vencedor')
