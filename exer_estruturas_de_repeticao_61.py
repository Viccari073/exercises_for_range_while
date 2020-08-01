"""
Faça um porgrama que calcule o maior número palíndromo feito a partir do produto de dois números de 3 dígitos.
Ex: O maior palíndromo feito a partir do produto de dois números de dois dígitos é 9009 = 91*99.
"""

for i in range((999*999), (100*100), -1):
    if str(i) == str(i)[::-1]:
        print(f'O maior palíndromo a partir do produto de dois números de três dígitos é: {i}')
        break
