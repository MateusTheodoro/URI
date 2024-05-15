"""
Ajude o loctuor a gritar gol
Se a quantidade de "O's" (GOOOOOL) for maior ou igual a 5, o locutor gritará "GOL DO NOSSO TIME!"
Se a quantidade de "O'S" (GOOOL) for menor do que 5, o locturo gritará "GOL DO ADVSERÁRIO!"
"""

def gol(n):
    return "G" + ("O" * (n)) + ("L do nosso time!" if n >=5 else "L do adversário!")

n = int(input())

print(gol(n))
