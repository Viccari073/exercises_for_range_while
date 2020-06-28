"""
Faça um programa que SOME os termos de valor par da sequência Fibonacci, cujos valores não ultrapassem quantro milhões.
"""

print()
print('Soma dos números paraes da Sequência Fibonacci')
print()


a, b, soma_pares = 0, 1, 0
print(f'{a} --> {b}', end='')

while True:
    c = a + b
    if c > 4_000_000:
        break
    if a % 2 == 0:
        soma_pares += a
    print(f' --> {c}', end='')
    a = b
    b = c

print(f'\nA soma dos números pares é: {soma_pares}')



