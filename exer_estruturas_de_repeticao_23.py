"""
Faça um algoritmo que leia um número positivo e imprima seus divisores.
"""

num = int(input('Digite um número positivo: '))
c = 0

while num < 0:
    num = int(input('Digite um número positivo: '))

print(f'Os divisores de {num} são: ', end=' ')
for n in range(1, num + 1):
    if num % n == 0:
        print(n, end=' ')

