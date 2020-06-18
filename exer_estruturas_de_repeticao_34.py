"""
Faça um programa que calcule o menor número divisível por cada um dos números de 1 a 20.
Ex: 2520 é o menor número que pode se dividido por cada um dos números de 1 a 10, sem sobrar resto.
"""

from math import gcd
# gcd() retorna o maior divisor comum dos inteiros a e b.
# lcm vai retornar o menor múltiplo comun entre a e b.

numero = 1
for i in range(1, 21):
    numero = numero*i // gcd(numero, i)
print(numero)