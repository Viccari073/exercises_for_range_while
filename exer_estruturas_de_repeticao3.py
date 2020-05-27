"""
Faça um algoritmo utilizando o comando while que mostra uma contagem regressiva na tela,
iniciando em 10 e terminando em 0. Mostrar a mensagem "FIM" após a contagem.
"""

from time import sleep

c = 10

while c >= 0:
    print(c)
    c -= 1
    sleep(1)
print()
print('FIM')
