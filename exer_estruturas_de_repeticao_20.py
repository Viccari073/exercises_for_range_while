"""
Ler uma sequência de números inteiros e determinar se eles são pares ou não.
Deverá ser informado o número de dados lidos e números de valores pares.
O processo termina quando for digitado o número 1000.
"""

num = int(input('Digite um número: '))

total = 0
pares = 0

while num != 1000:
    total += 1
    if num % 2 == 0:
        pares += 1
    num = int(input('Digite um número: '))
print(f'Foram informados {total} números e desses {pares} são pares.')
