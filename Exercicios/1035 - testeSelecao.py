"""
xLeia 4 valores inteiros A, B, C e D. 
A seguir, se B for maior do que C e se D for maior do que A, e a soma de C com D for maior que a soma de A e B e se C e D,
 ambos, forem positivos e se a variável A for par escrever a mensagem "Valores aceitos", senão escrever "Valores nao aceitos".
---Entrada---
Quatro números inteiros A, B, C e D.
---Saída---
Mostre a respectiva mensagem após a validação dos valores.
"""
num = input().split(' ')
a = int(num[0])
b = int(num[1])
c = int(num[2])
d = int(num[3])

if b > c and d > a and (c + d) > (a + b) and (a % 2 == 0):
    print('Valores aceitos')
else:
    print('Valores nao aceitos')
