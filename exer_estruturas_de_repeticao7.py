"""
Faça um programa que leia 10 inteiros positivos, ignorando os não positivos, e imprima sua média.
"""

c = 0
soma = 0

for n in range(1, 11):
    numeros = int(input(f'Digite o {n}º número: '))
    while numeros <= 0:
        print('Digite um número positivo!')
        numeros = int(input(f'Digite o {n}º número: '))
        c += 1
    soma = soma + numeros

media = soma / 10
print(f'A média dos números positivos é: {media}')
