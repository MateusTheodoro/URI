# Leitura dos valores de entrada
X = int(input())
Y = int(input())

# Se X for maior que Y, trocamos os valores para garantir que X seja o menor valor
if X > Y:
    X, Y = Y, X

# Inicializamos a soma dos ímpares como 0
soma_impares = 0

# Percorremos os números de X+1 até Y-1 (excluindo X e Y)
for i in range(X+1, Y):
    # Se o número for ímpar, somamos ao total
    if i % 2 != 0:
        soma_impares += i

# Imprimimos a soma dos ímpares
print(soma_impares)
