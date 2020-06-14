"""
Faça um exercício que receba dois números. Calcule e mostre:

- a soma dos números pares desse intervalo de números, incluindo os números digitados.
- a multiplicação dos números ímpares desse intervalo, incluindo os digitados.
"""

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

lista = []
soma_par = 0
mult_impar = 1  # 1 pq todo número multiplicado por 0 é 0

while num1 > num2:
    print('O primeiro número deve ser MENOR que o segundo.')
    num1 = int(input('Digite o primeiro número: '))
    num2 = int(input('Digite o segundo número: '))
    print()

for n in range(num1, num2 + 1):
    if n % 2 == 0:
        soma_par += n
        lista.append(n)
    elif n % 2 == 1:
        mult_impar *= n
        lista.append(n)
print()
print(f'Os números entre {num1} e {num2} são: {lista}')
print(f'A soma dos números pares é: {soma_par}')
print(f'A multiplicação dos números ímpares é: {mult_impar}')



