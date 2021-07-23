"""
Leia um valor de ponto flutuante com duas casas decimais.
Este valor representa um valor monetário.
A seguir, calcule o menor número de notas e moedas possíveis no qual o valor pode ser decomposto.
As notas consideradas são de 100, 50, 20, 10, 5, 2. As moedas possíveis são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01.
A seguir mostre a relação de notas necessárias.

Entrada
O arquivo de entrada contém um valor de ponto flutuante N (0 ≤ N ≤ 1000000.00).

Saída
Imprima a quantidade mínima de notas e moedas necessárias para trocar o valor inicial, conforme exemplo fornecido.

Obs: Utilize ponto (.) para separar a parte decimal.

#ENTRADA
valor = float(input())

# NOTAS
cem = valor // 100
r = valor % 100

cinq = r // 50
r = r % 50

vinte = r // 20
r = r % 20

dez = r // 10
r = r % 10

cinco = r // 5
r = r % 5

dois = r // 2
r = r % 2

#MOEDAS

umreal = r // 1
r = r % 1

cinqcent = r // 0.50
r = r % 0.50

vintcinc = r // 0.25
r = r % 0.25

dezcent = r // 0.10
r = r % 0.10

cincocent = r // 0.05
r = r % 0.05

umcent = r // 0.01
r = r % 0.01

print(f'NOTAS:')
print(f'{cem:.0f} nota(s) de R$ 100.00')
print(f'{cinq:.0f} nota(s) de R$ 50.00')
print(f'{vinte:.0f} nota(s) de R$ 20.00')
print(f'{dez:.0f} nota(s) de R$ 10.00')
print(f'{cinco:.0f} nota(s) de R$ 5.00')
print(f'{dois:.0f} nota(s) de R$ 2.00')
print(f'MOEDAS:')
print(f'{umreal:.0f} moeda(s) de R$ 1.00')
print(f'{cinqcent:.0f} moeda(s) de R$ 0.50')
print(f'{vintcinc:.0f} moeda(s) de R$ 0.25')
print(f'{dezcent:.0f} moeda(s) de R$ 0.10')
print(f'{cincocent:.0f} moeda(s) de R$ 0.05')
print(f'{umcent:.0f} moeda(s) de R$ 0.01')
"""
notas = [100, 50, 20, 10, 5, 2]

for nota in notas:

    print(nota)
    