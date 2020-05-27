"""
Faça um programa que leia um número inteito N e depois imprima os N primeiros números naturais ímpares:
"""

numero = int(input('Digite um número inteiro: '))
print(f'Os números ímpares até o {numero} são: ')

for n in range(0, numero):
    if n % 2 != 0:
        print(n, end=' ')
