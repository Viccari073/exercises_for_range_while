"""
Faça um programa que some os números primos existentes entre a e b, onde a e b são números informados peslo usuário.
"""

print('-' * 30)
print(f'{"Soma dos números primos entre a e b":^30}')
print('-' * 30)

a = int(input('Defina o valor de a: '))
b = int(input('Defina o valor de b: '))


while a <= 1:
    print('\033[31mO valor de a deve ser maior que 1!\033[m')
    a = int(input('Defina o valor de a: '))
    b = int(input('Defina o valor de b: '))
    if a > 1:
        break

lista_primos = list()

for x in range(a, b+1):
    cont = 0
    for y in range(1, x+1):
        if x % y == 0:
            cont += 1
    if cont <= 2:
        lista_primos.append(x)

print(f'Os números primos entre {a} e {b} são: {lista_primos}')
print(f'A soma dos números primtos entre {a} e {b} é: {sum(lista_primos)}')
