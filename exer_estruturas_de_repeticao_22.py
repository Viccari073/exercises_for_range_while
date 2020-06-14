"""
Escreva um programa completo que permita a qualquer aluno introduzir, pelo teclado, uma sequência arbitrária
de notas (válidas de 10 a 20) e que mostre na tela, como resultado, a correspondente média aritimética.
O número de notas com que o aluno pretende efetuar o cálculo não será fornecido ao programa, o qual terminará
quando for introduzido um valor que não seja válido.
"""


nota = 0
c = 0
media = 0
soma = 0

while nota >= 10 or nota <= 20:
    nota = float(input('Digite a nota: '))
    if nota < 10 or nota > 20:
        break
    c += 1
    soma += nota


media = soma / c
print(f'A média aritimetica é: {media}')
