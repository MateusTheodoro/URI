nome = str(input())
salario = float(input())
vendas = float(input())
comissao = vendas * 15 / 100
print(f'TOTAL = R$ {salario + comissao:.2f}')
