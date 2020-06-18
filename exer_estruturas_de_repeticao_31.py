"""
Faça um programa que calcule e escreva o valor de S:

S = 1/1 + 3/2 + 5/3 + 7/4 ... 99/50
"""

soma = 0
numerador = 1
denominador = 1

for i in range(1, 51):
    soma += numerador / denominador
    numerador += 2
    denominador += 1

print(f'S ={soma: .2f}')
