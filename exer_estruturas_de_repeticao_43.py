"""
Faça um programa que leia um número indeterminado de idades de indivíduos (pare quando for informada a idade 0),
e calcule a idade média desse grupo.
"""

lista_idades = []

idades = int(input('Digite uma idade: '))

while idades != 0:
    lista_idades.append(idades)
    idades = int(input('Digite outra idade: '))
    if idades <= 0:
        lista_idades.pop()
        break

soma = sum(lista_idades)
media = soma / (len(lista_idades))

print()
print(f'A média das idades digitas é: {media}')
