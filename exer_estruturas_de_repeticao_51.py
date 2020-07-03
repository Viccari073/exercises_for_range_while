"""
Um funcionário recebe um aumento anual. Em 1995 foi contratado por R$ 2000.00. Em 1996, recebeu um aumento de 1,5%.
A partir de 1997, os aumentos sempre correspondem ao dobro do ano anterior.

Faça um programa que determine o salário atual do funcionário.
"""

from datetime import datetime


def reajuste_salario(salario):
    aumento = 1.5
    ano_inicial = 2015
    ano_atual = datetime.now().year
    while ano_inicial <= ano_atual:
        salario = salario + ((salario * aumento) / 100)
        aumento *= aumento
        ano_inicial += 1
    return salario


valor = float(input('Digite o salário: R$ '))
print(f'R$ {reajuste_salario(valor): .2f}')

