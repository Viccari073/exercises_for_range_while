"""
Faça um programa que conte quantos números primos existem entre a e b, onde a e b são números informados pelo usuário.
"""


print('-' * 30)
print(f'{"Números primos de a a b":^30}')
print('-' * 30)

a = int(input('Escolha um valor positivo para a: '))
b = int(input('Escolha um valor positivo para b: '))

while a <= 1:
    print('\033[31mNúmero menor ou igual a 1. Tente novamente!\033[m')
    a = int(input('Escolha um valor positivo para a: '))
    b = int(input('Escolha um valor positivo para b: '))
    if a > 1:
        break

lista_primos = []

for x in range(a, b+1):
    cont = 0
    for y in range(1, x+1):
        if x % y == 0:
            cont += 1
    if cont <= 2:
        lista_primos.append(x)


print(lista_primos)
print(f'Existem {len(lista_primos)} números primos entre {a} e {b}.')






