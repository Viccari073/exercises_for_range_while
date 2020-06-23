"""
Leia um número positivo do usuário, então, calcule e imprima a sequência Fibonacci até o primerio número superior lido.
Exemplo: se o usuário informou o número 30, a sequência Fibonacci a ser impressa será: 0 1 1 2 3 5 8 13 21 34.
"""
print()
print('Sequência Fibonacci')
print()
num = int(input('Digite um número positivo: '))
a = 0
b = 1
print(f'{a} --> {b}', end='')

while True:
    c = a + b
    print(f' --> {c}', end='')
    a = b
    b = c
    if c > num:
        break
print()




