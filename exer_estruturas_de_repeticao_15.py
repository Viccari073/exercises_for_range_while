"""
Faça um programa que leia um número inteiro positivo ímpar N
e imprima todos os números ímpares de 1 até N em ordem crescente.
"""
from time import sleep

num = int(input('Digite um número inteiro ímpar positivo: '))

while num < 0 or num == 0 or num % 2 == 0:
    print('Número inválido!')
    print('Digite um número ímpar positivo e diferente de 0.')
    num = int(input('Digite um número inteiro ímpar positivo: '))

print(f'A sequência crescente dos número ímpares de 1 a {num} é: ', end='')
for n in range(1, num+1, 2):
    print(n, end=' ')
    sleep(0.3)
