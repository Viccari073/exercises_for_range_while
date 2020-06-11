"""
Faça um programa que leia um número inteiro positivo par N
e imprima todos os números pares de 0 até N, em ordem decrescente.
"""

from time import sleep

num = int(input('Digite um número inteiro par positivo: '))

while num == 0 or num < 0 or num % 2 != 0:
    print('Número inválido!')
    print('Digite um número par positivo ou diferente de 0.')
    num = int(input('Digite um número par: '))

print(f'A sequência em ordem decrescente com número pares de {num} até 0 é:')
for n in range(num, -1, -2):
    print(n, end=' ')
    sleep(0.3)
