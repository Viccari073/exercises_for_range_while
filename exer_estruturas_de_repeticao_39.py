"""
Faça um programa que calcule a área de um triângulo, cuja base e altura são fornecidas pelo usuário.
Esse programa não pode permitir a entrada de dados inválidos, ou seja, medidas menores ou iguais a 0.

area = b.h/2
"""

base = int(input('Defina a base do triângulo: '))
altura = int(input('Defina a altura do triângulo: '))

while base <= 0 or altura <= 0:
    print('Dados inválidos, digite um npumero maior que zero')
    base = int(input('Defina a base do triângulo: '))
    altura = int(input('Defina a altura do triângulo: '))

area = (base*altura) / 2
print(f'A área do triangulo é: {area}')

