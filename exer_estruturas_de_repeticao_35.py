"""
Faça um rpograma que some os números ímpares contidos em um intervalo definido pelo usuário.

O usuário define o valor inicial e final deste intervalo e o programa deve somar todos os números
ímpares nesse intervalo.

Caso o usuário digite um intervlado inválido (começando po um valor maior que o final) dece ser escrito
uma mensagem de erro na tela ('Intervalo inválido') e o programa termina.

Exemplo de tela de saída:
Digite o valor inicial e valor final: 5    10
Soma dos ímpares neste interalo: 21
"""

print('Digite o valor inicial e valor final: ')
inicial = int(input())
final = int(input())
soma_impares = 0

if inicial > final:
    print('Intervalo inválido!')
else:
    for c in range(inicial, final + 1):
        if c % 2 != 0:
            soma_impares += c
    print(f'A soma dos números ímpares no intervaldo de {inicial} a {final} é: {soma_impares}')
