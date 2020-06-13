"""
Faça um programa que leia um número inteiro positivo N e calcule a soma dos n primeiros números naturais.
"""

num = int(input('Digite um número positivo:'))
soma = 0
c = 0
while num < 0:
    num = int(input('Digite um número positivo:'))

print('A soma dos números:', end=' ')
for n in range(1, num):
    soma += n
    c += 1
    print(n, end=' ')

print(f'é {soma}')
