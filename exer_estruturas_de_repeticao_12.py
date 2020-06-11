"""
Faça um programa que leia um número inteiro positivo N
e imprima todos os números naturais de 0 até N em ordem decrescente.
"""

from time import sleep

num = int(input('Digite um número inteiro positivo: '))

while num < 0:
    num = int(input('Digite um número inteiro positivo: '))

print(f'A sequencia decrescente de {num} até 0 é:')
for n in range(num, -1, -1):
    print(n, end=' ')
    sleep(0.5)
