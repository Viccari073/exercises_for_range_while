"""
Faça um programa que leia 10 inteiros e imprima sua média.
"""

c = 0
soma = 0

for n in range(1, 7):
    numeros = int(input(f'Digite o {n}º número: '))
    c += 0
    soma = soma + numeros

media = soma / 6
print(f'A média dos seis números digitados é: {media}')
