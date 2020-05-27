"""
Faça um programa que peça ao usuário para digitar 10 valores e some-os.

"""

c = 0
soma = 0

while c < 10:
    n = int(input('Digite um número: '))
    c += 1
    soma = soma + n
print(f'A soma dos dez números digitados é {soma}')

