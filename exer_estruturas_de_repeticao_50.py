"""
Chico tem 1.50 metro e cresce 2 centímetros por ano, enquanto Zé tem 1.10 metros e cresce 3 centímetros por ano.
Escreva um programa que clacule e imprima quantos anos serão necessários para que Zé seja maior que Chico.
"""

alt_chico = 1.50
alt_ze = 1.10


ano = 1

while alt_ze < alt_chico:
    alt_chico += 0.01
    alt_ze += 0.03
    ano += 1
    if alt_ze > alt_chico:
        break
print(f'Zé demorou {ano} anos para ficar maior que Chico.')
print(f'Após {ano} anos, Chico ficou com {alt_chico: .2f} metros e Zé ficou com {alt_ze: .2f} metros.')



