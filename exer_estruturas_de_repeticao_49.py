"""
O funcionário chamado Carlos tem um colega chamado João que recebe um salário que equivale a um terço do seu salário.
Carlos gosta de fazer aplicações na caderneta de poupança e vai aplicar seu salário integralmente nela, pois está
rendendo 2% ao mês. João aplicará seu salário integralmente no fundo de renda fixa, que está rendendo 5% ao mês.

Construa um programa que deverá calcular e mostrar a quantidade de meses necessários para que o valor pertencente a
João iguale ou ultrapasse o valor pertencente a Carlos.

Teste com outros valores para as taxas.
"""

salario_carlos = float(input('Escreva o salário de Carlos: R$ '))
salario_joao = salario_carlos / 3
print(f'O salário de João é: R$ {salario_joao: .2f}')

rend_carlos = salario_carlos * (2/100)
rend_joao = salario_joao * (5/100)

meses = 1
while rend_joao < rend_carlos:
    rend_carlos *= meses
    rend_joao *= meses
    meses += 1
if rend_joao >= rend_carlos:
    print(f'Para igualar ou ultrapassar o valor de Carlos, João levou {meses} meses.')
