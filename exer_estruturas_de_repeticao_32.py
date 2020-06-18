"""
Faça um programa que simula o lançameto de dois dados, d1 e d2, n vezes. e tem como saída o número de cada dado
e a relação entre eles (<, >, =) de cada lançamento.
"""
from random import randint

n = int(input('Quantas vezes deseja jogar os dados? '))

quant = 0

for i in range(1, n +1):
    d1 = randint(1, 6)
    d2 = randint(1, 6)
    quant += 1
    dado1 = d1
    dado2 = d2
    print()
    print(f'{i}º lançamento:')
    print(f'O primeiro dado deu:{dado1}')
    print(f'O segundo dado deu:{dado2}')
    if dado1 > dado2:
        print('O resultado do primeiro dado é maior que o resultado do segundo dado!')
    elif dado2 > dado1:
        print('O resultado do segundo dado é maior que o resultado do primeiro dado!')
    elif dado1 == dado2:
        print('Os dois dados deram os mesmo resultados!')
    print()

 

