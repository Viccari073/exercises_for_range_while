"""
Escreva um programa que receba como entrada o valor do saque realizado pelo cliente de um banco
e retorne quantas notas de cada valor serão necessárias para atender ao saque com a menor quantidade de notas possível.
Serão utilizadas notas de 100, 50, 20, 10, 5, 2 e 1 real.
"""

print('=' * 35)
print('{:^35}'.format('SAQUE'))
print('=' * 35)


def saque(reais):
    total = reais
    cedulas = 100
    total_cedulas = 0
    while True:
        if total >= cedulas:
            total -= cedulas
            total_cedulas += 1
        else:
            if total_cedulas > 0:
                print(f'Total de {total_cedulas} de R$ {cedulas}')
            if cedulas == 100:
                cedulas = 50
            elif cedulas == 50:
                cedulas = 20
            elif cedulas == 20:
                cedulas = 10
            elif cedulas == 10:
                cedulas = 5
            elif cedulas == 5:
                cedulas = 2
            elif cedulas == 2:
                cedulas = 1
            total_cedulas = 0
            if total == 0:
                break
    return f'Total de {total_cedulas} de R$ {cedulas}'


valor = int(input('Valor do saque: R$ '))
print(saque(valor))


"""
valor = int(input('Valor do saque: R$ '))
total = valor
cedulas = 100
total_cedulas = 0
while True:
    if total >= cedulas:
        total -= cedulas
        total_cedulas += 1
    else:
        if total_cedulas > 0:
            print(f'Total de {total_cedulas} de R$ {cedulas}')
        if cedulas == 100:
            cedulas = 50
        elif cedulas == 50:
            cedulas = 20
        elif cedulas == 20:
            cedulas = 10
        elif cedulas == 10:
            cedulas = 5
        elif cedulas == 5:
            cedulas = 2
        elif cedulas == 2:
             cedulas = 1
        total_cedulas = 0
        if total == 0:
            break
"""


