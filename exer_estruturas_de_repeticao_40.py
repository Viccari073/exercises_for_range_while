"""
Elabore um programa que faça leitura de vários números inteiros, até que se digite um número negativo.
O programa trm que retornar o maior e o menor número lido.
"""

lista_num = []

num = int(input('Digite um número:'))
lista_num.append(num)

while num > 0:
    num = int(input('Digite um número:'))
    lista_num.append(num)
    if num < 0:
        lista_num.pop()


print()
print(f'O maior numero digitado foi: {max(lista_num)}')
print(f'O menor número digitado foi: {min(lista_num)}')
