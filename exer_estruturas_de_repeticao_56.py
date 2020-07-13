"""
Faça um programa que calcule a soma de todos os números primos abaixo de dois mil.
"""

limite = 2000
lista_primos = [2]

for numero in range(3, limite +1):
    for i in lista_primos:
        if numero % i == 0:
            break
    else:
        lista_primos.append(numero)


print(lista_primos)
print(sum(lista_primos))

# Estudos através do link: https://wiki.python.org.br/DeterminandoPrimos



