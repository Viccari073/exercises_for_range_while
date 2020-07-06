"""
Escreva um programa que leia um número inteiro positivo n e em seguida imprima n linhas do chamado
c.

Ex:
Para n = 6 temos:

1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
16 17 18 19 20 21
"""

n = int(input('Digite um número: '))

c = 1
for i in range(n + 1):
    for f in range(i):
        print(c, end=' ')
        c += 1
    print()




