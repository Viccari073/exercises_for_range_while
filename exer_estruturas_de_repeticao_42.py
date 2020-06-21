"""
Faça um programa que leia um conjunto não determinado de valores, um de cada vez,
e escreva pra cada um dos valores lidos, o quadrado, o cubo e a raiz quadrada.

Finalize a entrada de dados com um valor negativo ou zero.
"""


lista_num = []

num = int(input('Digite um número: '))
lista_num.append(num)

while num > 0:
    num = int(input('Digite outro número: '))
    lista_num.append(num)
    if num <= 0:
        lista_num.pop()
        break
print()
print(f'Os valores digitados foram: {lista_num}')
print()

for n in lista_num:
    quadrados = n * n
    cubo = n * n * n
    raiz = n ** (1/2)
    print(f'O quadrado de {n} é: {quadrados}')
    print(f'O cubo de {n} é {cubo}')
    print(f'A raiz quadrada de {n} é: {raiz: .2f}')
    print()
