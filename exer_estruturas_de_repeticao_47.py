"""
Faça um programa que apresente um menu de opções para o cálculo das seguintes operações entre dois números:
- Adição (opção1)
- Subtração (opção2)
- Multiplicação (opção3)
- Divisão (opção4)
- Saída(opção5)

O programa deve possibilitar ao usuário a escolha da operaçao desejada, a exibiçao do resultado e a volta ao menu.
O programa só termina quando for escolhida a opção de saída(opção5).
"""

print()
print('Escolha a opçao de cálculo')
print()
while True:
      print('-=' * 15)
      print('OPÇÕES: '
            '\nAdição         [1]'
            '\nSubtração      [2]'
            '\nMultiplicação  [3]'
            '\nDivisão        [4]'
            '\nSaída          [5]')
      print()
      opcao = int(input('Digite sua opção: '))
      if opcao == 0 or opcao > 5:
            print('Opção inválida!')
            print()
      elif opcao == 5:
            print('-=' * 15)
            print('PROGRAMA FINALIZADO')
            break
      else:
            print('Defina os números: ')
            num1 = int(input('Primeiro número: '))
            num2 = int(input('Segundo número: '))
            if opcao == 1:
                  resposta = num1 + num2
                  print(f'{num1} + {num2} = {resposta}')
                  print()
            elif opcao == 2:
                  if num1 < num2:
                        print('O primeiro número deve ser maior que o segundo.')
                        print('Defina os números: ')
                        num1 = int(input('Primeiro número: '))
                        num2 = int(input('Segundo número:'))
                  if num1 >= num2:
                        resposta = num1 - num2
                        print(f'{num1} - {num2} = {resposta}')
            elif opcao == 3:
                  resposta = num1 * num2
                  print(f'{num1} * {num2} = {resposta}')
                  print()
            elif opcao == 4:
                  if num1 == 0 or num1 < num2:
                        print('O primerio número deve ser maior que 0.')
                        num1 = int(input('Primeiro número: '))
                        num2 = int(input('Segundo número:'))
                  else:
                        resposta = num1 / num2
                        print(f'{num1} / {num2} = {resposta}')
                        print()







