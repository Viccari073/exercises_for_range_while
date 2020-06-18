"""
Faça um programa que leia um valor N inteiro e positivo, calcule e mostre o valor E,
conforme a fórmula a seguir: E = 1 + 1/1! + 1/2! + 1/3! + 1/4!...+1/N!
"""

from math import factorial

num_final = int(input("Digite o termo final da sequência fatorial: "))
soma = 1

for n in range(1, num_final + 1):
    soma += 1 / factorial(n)

print(f"O resultado de E é igual a: {soma:.2f} ")