"""
Dados n e dois números inteiros positivos, i e j, diferentes de 0,
imprimir em ordem crescente os n primeiros naturais que são múltiplos de i ou j e ou de ambos.
Exemplo: para n = 6, i = 2 e j = 3 a saída deverá ser: 0, 2, 3, 4, 6, 8.
"""

n = int(input('Digite um valor positivo e diferente de 0: '))
i = int(input('Digite um segundo valor positivo e diferente de 0: '))
j = int(input('Digite um terceiro valor positivo e diferente de 0: '))

c = 0
aux = 0

while True:
    if aux % i == 0 or aux % j == 0:
        print(aux)
        c += 1
    aux += 1
    if c == n:
        break



