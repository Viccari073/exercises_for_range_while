"""
Faça um programa que some todos os números naturais abaixo de 1000 que são múltiplos de 3 e 5.
"""

soma = 0

for n in range(0, 1001):
    if n % 3 == 0 and n % 5 == 0:
        soma += n
print()
print(f'A soma dos números naturais abaixo de 1000 que são múltiplos de 3 e 5 é: {soma}')
