"""
Faça um programa que calcula a associação em pararelo de dois resistores R1 e R2,
fornecidos pelo usuário via teclado.

O programa fica pedindo estes valores e calculando até que o usuário entre com um valor para a resistância igual a 0.

R = R1*R2 / R1 + R2
"""

r1 = float(input('Digite o valor do resistor 1: '))
r2 = float(input('Digite o valor do resistor 2: '))

while r1 != 0 or r2 != 0:
    r = (r1 * r2) / (r1 + r2)
    print(f'A assossicação em pararelo para esses valores de R1 e R2 é: {r: .2f}')
    print()
    r1 = float(input('Digite o valor do resistor 1: '))
    r2 = float(input('Digite o valor do resistor 2: '))
    if r1 == 0 or r2 == 0:
        break

