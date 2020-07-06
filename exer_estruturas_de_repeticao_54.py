"""
Faça um programa que receba um número inteiro maior do que 1, e verifique se o número fornecido é primo ou não.
"""

num = int(input('Digite um número maior do que 1: '))

while num <= 1:
    print('\033[31mNúmero menor ou igual a 1. Tente novamente!\033[m')
    num = int(input('Digite um número maior do que 1: '))
    if num > 1:
        break

div = 0
for c in range(1, num + 1):
    if num % c == 0:
        div += 1

if div == 2:
    print(f'{num} é um número primo!')
else:
    print(f'{num} não é um número primo!')


