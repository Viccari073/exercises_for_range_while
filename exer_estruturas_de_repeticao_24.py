"""
Escreva um programa que leia um número inteiro e calcule a soma de todos os divisores desse número,
com exeção dele próprio. Ex: a soma dos divisores do número 66 é 1 + 2 + 3 + 6 + 11 + 22 + 33 = 78
"""

num = int(input('Digite um número positivo: '))
soma = 0


while num < 0:
    num = int(input('Digite um número positivo: '))

print(f'Os divisores de {num} são: ', end=' ')
for n in range(1, num):
    if num % n == 0:
        soma += n
        print(n, end=' ')
print()
print(f'A soma dos divisores de {num} é: {soma}')
