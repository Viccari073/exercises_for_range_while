"""
Faça um programa que calcule e mostre a soma dos 50 primeiros números pares.
"""

c = 0
soma = 0

print('Os números pares até 50 são: ')
for n in range(1, 51):
    c += 1
    if n % 2 == 0:
        print(n, end=' ')
        soma = soma + n
print()
print(f'A soma desses números é {soma}')
