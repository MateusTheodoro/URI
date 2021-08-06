contador = 1
lista = []

while contador <= 100:
    numero = input()
    lista.append(int(numero))
    contador += 1
print(max(lista))
print(lista.index(max(lista)) + 1)
