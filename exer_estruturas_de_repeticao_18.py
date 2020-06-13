"""
Escreva um algoritmo que leia certa quantidade de números e imprima o maior deles e quantas vezes o maior foi lido.
A quantidade de números a serem lidos deve ser fornecida pelo usuário.
"""

n = int(input('Digite uma qunatidade de números: '))

numeros = []

for num in range(n):
    numeros.append(int(input(f'Digite o {num + 1}º número: ')))

print(f'O maior valor foi {max(numeros)} e foi lido {numeros.count(max(numeros))} vezes.')
