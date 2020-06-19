"""
Faça um programa que calcule a diferença entre a soma dos quadrados dos primeiros 100 números naturais
e o quadrado da soma.
Exemplo:
A soma dos quadrados dos dez primeiros números naturais é:
1*1 + 2*2 + 3*3 + ... + 10*10 = 385
O quadrado da soma dos dez primeiros números naturais é:
(1 + 2 + 3 + ... + 10)*2 = 3025
A diferença entre a soma dos quadrados dos dez primeiros númeors naturais e o quadrado da soma
3025 - 385 = 2640
"""

soma_quadrados = 0
soma = 0
quadrado_soma = 0

for n in range(0, 100 + 1):
    if n > 0:
        n = n*n
        soma_quadrados += n
for n in range(0, 100 + 1):
    if n > 0:
        soma += n
    quadrado_soma = soma * soma

print(f'A soma dos quadrados dos 100 primeiros números naturais é: {soma_quadrados}')
print(f'O quadrado da soma dos 100 primeiros números naturais é: {quadrado_soma}')
print(f'A diferença entre a soma dos quadrados e o quadrado da soma é {quadrado_soma - soma_quadrados}')