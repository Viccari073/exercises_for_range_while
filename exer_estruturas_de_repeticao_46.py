"""
Faça um programa que gera um número aleatório de 1 a 1000.
O usuário deve tentar acertar qual o número gerado, a cada tentativa o programa deverá informar se o chute
é menor ou maior que o número gerado.
O programa acaba quando o usuário acertar o número gerado.
O programa também deverá informar em quantas tentativas o número foi descoberto.
"""

from random import randint

print('=' * 3, 'ACERTE O NÚMERO DE 1 A 1000', '=' * 3)
print()
numero = randint(1, 1000)
palpite = int(input('De seu palpite:'))

cont = 0
while True:
    if palpite < numero:
        print()
        print('Seu palpite é menor! Escolha um número maior.')
        palpite = int(input('De seu palpite:'))
        cont += 1
    elif palpite > numero:
        print()
        print('Seu palpite é maior! Escolha um número menor.')
        palpite = int(input('De seu palpite:'))
        cont += 1
    elif palpite == numero:
        print()
        print(f'Você acertou! Depois de {cont} tentativas!')
        break
