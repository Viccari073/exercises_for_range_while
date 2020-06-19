"""
Escreva um programa que verifique quais números entre 1000 e 9999 (inclusive)
possuem a propriedade seguinte: a soma dos dois dígitos de mais baixa ordem
com os dois dígitos de mais alta ordem elevada ao quadrado é igual ao próprio número.
Por exemplo:
30+25 = 55
55*55 = 3025
"""

for valor in range(1000, 10000):
    aux = (int(str(valor)[:2])) + (int(str(valor)[2:]))
    aux = aux * aux
    if valor == aux:
        print(f'O valor {valor} possui a propriedade.')
