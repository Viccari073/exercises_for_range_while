"""
Faça um programa que leia um número inteiro positivo par N
e imprima todos os númeors pares de 0 até N em ordem crescente.
"""
from time import sleep

num_par = int(input('Digite um número par: '))

while num_par == 0 or num_par < 0 or num_par % 2 != 0:
    print('Número inválido!')
    print('Digite um número par positivo ou diferente de 0.')
    num_par = int(input('Digite um número par: '))

print(f'A sequência em ordem crescente com número pares de 0 a {num_par} é:')
for n in range(0, num_par + 1, 2):
    print(n, end=' ')
    sleep(0.3)
