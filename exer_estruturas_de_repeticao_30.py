"""
Faça um programa para calcular as seguintes sequencias:
1 + 2 + 3 + 4 + 5 + ... + n
1 - 2 + 3 - 4 + 5 + ... + (2n - 1)
1 + 3 + 5 + 7 + ... + (2n -1)
"""

n = int(input('Digite um valor: '))
req = (2 * n) - 1

# Sequência 01
s = 0
for i in range(1, n + 1):
    s += i
print(f'Sequência_1 = {s}')

# Sequência 02
som = 0

for i in range(1, req + 1):
    if i % 2 == 0:
        som -= i
    else:
        som += i
print(f'Sequência_2 = {som}')


# Sequência 03
soma = 0
for i in range(1, req + 1, 2):
    soma += i
print(f'Sequência_3 = {soma}')
