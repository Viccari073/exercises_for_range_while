"""
Faça um programa que leia um número inteiro positivo ímpar N
e imprima todos os números ímpares de 1 a N em ordem decrescente.
"""

from time import sleep

num = int(input('Digite um número ímpar positivo: '))

while num < 0 or num == 0 or num % 2 == 0:
    print('Número inválido!')
    print('Digite um número ímpar positivo e diferente de 0.')
    num = int(input('Digite um número ímpar positivo: '))

print(f'A sequência decrescente dos número ímpares de {num} a 1 é: ', end='')
for n in range(num, 0, -2):
    print(n, end=' ')
    sleep(0.3)
