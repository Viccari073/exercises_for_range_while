"""
Faça um programa que calcule o terno pitagórico a, b, c, para o qual a + b + c = 1000.
Um terno pitagórico é um conjunto de três números naturais a, b, c, para qual:
a*a + b*b = c*c
Por exemplo:
3*3 + 4*4 = 9 + 16 = 25 = 5*5
"""

print('Os ternos pitagóricos cuja a soma é igual a 1000 são: ')
for a in range(0, 1000):
    for b in range(a + 1, 1000):
        c = 1000 - a - b
        if (a * a) + (b * b) == c * c:
            print(f'{a, b, c} ')
