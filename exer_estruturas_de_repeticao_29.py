"""
Escreva um programa para calcular o valor da série, para 5 termos:
S = 0 + 1/2! + 2/4! + 3/6! + ...
"""

from math import factorial

c = 0  # pode ser escrito assim também: c = s = 0
s = 0

for n in range(2, 9, 2):
    c += 1
    razao = c/factorial(n)
    s += razao
print(f'S = {s}')
