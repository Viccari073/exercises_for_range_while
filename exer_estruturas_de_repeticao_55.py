"""
Escrever um programa que leia um inteiro não negativo n e imprima a soma dos n primeiros numeros primos.
"""


def test_primo(n):
    if n == 1:  # 1 não é número primo
        return False
    for v in range(2, (int(n/2)+1)):  # Devemos procurar um dividsor de 2 até a metade do número.
        if n % v == 0:  # Se existir algum número divisor de 2, até a metade do número, não é primo!
            return False
    else:
        return True


# Programa principal:
soma = 0
numero = int(input('Digite um número inteiro:'))

while numero <= 1:
    print('Digite um número maior que 1!')
    numero = int(input('Digite um número inteiro:'))

for num in range(1, numero):
    if test_primo(num):
        soma += num

print(soma)









