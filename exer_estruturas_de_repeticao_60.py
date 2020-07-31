"""
Faça um programa que leia vários números, cálcule e mostre:
a - A soma dos números digitados
b - A quantidade dos números digitados
c - A média dos números digitados
d - O maior número digitado
e - O menor número digitado
f - A média dos números pares
"""


def soma(*args):
    return f'A soma dos números digitados é: {sum(args)}'


def quantidade(*args):
    return f'Foram digitados {len(args)} números.'


def media(*args):
    m = sum(args) / len(args)
    return f'A média dos números digitados é: {m: .2f}'


def maior(*args):
    return f'O maior número digitado foi: {max(args)}'


def menor(*args):
    return f'O menonr número digitado foi: {min(args)}'


def soma_pares(*args):
    total = 0
    for par in args:
        if par % 2 == 0:
            total += par
    return f'A soma dos números pares digitados é: {total}'


lista_num = list()

while True:
    num = int(input('Digite um número: '))
    lista_num.append(num)
    if num <= 0:
        lista_num.pop()
        break

print('-' * 45)
print(soma(*lista_num))
print(quantidade(*lista_num))
print(media(*lista_num))
print(maior(*lista_num))
print(menor(*lista_num))
print(soma_pares(*lista_num))
