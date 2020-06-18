"""
Faça um algoritmo que encontre o primeiro múltiplo de 11, 13 ou 17 após um número dado.
"""

num = int(input('Digite um número: '))


while num % 11 != 0:
    num += 1
    if num % 11 == 0:
        print(f'Após o número dado, o próximo número múltiplo de 11 é: {num}')

while num % 13 != 0:
    num += 1
    if num % 13 == 0:
        print(f'Após o número dado, o próximo número múltiplo de 13 é: {num}')

while num % 17 != 0:
    num += 1
    if num % 17 == 0:
        print(f'Após o número dado, o próximo número múltiplo de 13 é: {num}')
