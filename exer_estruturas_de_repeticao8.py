"""
Escreva um programa que leia 10 números e escreva o menor valor lido e o maior valor lido.
"""

menor = 0
maior = 0

for n in range(1, 11):
    numero = int(input(f'Digite o {n}º número: '))
    if n == 1:
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
print(menor)
print(maior)
