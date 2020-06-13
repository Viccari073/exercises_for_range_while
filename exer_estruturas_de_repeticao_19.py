"""
Escreva um algoritmo qu eleia um número inteiro entre 100 e 999
e imprima na saída cada um dos algarismos que compõem o número.
"""
from time import sleep

num = input('Digete um número entre 100 e 999: ')

while int(num) < 100 or int(num) > 999:
    print('Número inválido!')
    num = input('Digete um número entre 100 e 999: ')

if 100 <= int(num) <= 999:
    for n in num:
        print(n)
        sleep(0.3)
