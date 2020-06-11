"""
Faça um programa que leia um número inteiro positivo N e
imprima todos os números naturias de 0 até N em ordem crescente.
"""

from time import sleep

num = int(input('Digite um número inteiro positivo: '))

while num < 0:
    num = int(input('Digite um número inteiro positivo: '))

print(f'A sequencia em ordem crescente de 0 a {num} é:')
for n in range(0, num + 1, 1):
    print(n, end=' ')
    sleep(0.5)

