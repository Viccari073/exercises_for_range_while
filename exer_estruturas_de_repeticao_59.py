"""
Escreva um programa que leia o número de habitantes de uma determinada cidade, o valor do kwh, e para cada
habitante entre com os seguintes dados: consumo do mês e o código do consumidor (1 - Residencial,
2 - Comercial, 3 - Industrial). No final, imprima o maior, o menor e a média do consumo dos habitantes, e por
fim o total de consumo de cada categoria de consumidor.
"""
# -> Entrada
# numero de habitantes
# quantos kwh cada habitante utilizou (solicitar primeiramente o código)
# código do consumidor (1, 2 ou 3)


# -> Saída
# Maior, menor e média de consumo dos habitantes
# Total (soma) de consumo pro cada categoria (1, 2 e 3) --> soma_res / soma_com / soma_ind


soma_res = 0
soma_com = 0
soma_ind = 0
cidade = str(input('Defina a cidade: '))
habitantes = int(input(f'Digite o número de habitantes de {cidade}: '))
consumo_hab_total = list()


def calculo(kwh, reais):
    valor_pagar = kwh * reais
    return f'Valor a pagar: R$ {valor_pagar: .2f}'


for h in range(1, habitantes + 1):
    print()
    print('OPÇÕES:\n'
          '[1] - Residencial\n'
          '[2] - Comercial\n'
          '[3] - Indústrial\n'
          '[4] - Sair')
    opcao = int(input(f'Que tipo de consumidor é o habitante {h}: '))
    if opcao == 1:
        kwh1 = float(input('Digite o consumo dessa residencia: '))
        kwh_residencial = 0.62  # valor genérico
        print(calculo(kwh1, kwh_residencial))
        soma_res += kwh1
        consumo_hab_total.append(kwh1)
    if opcao == 2:
        kwh2 = float(input(f'Digite o consumo desse comercio: '))
        kwh_comercial = 0.54  # valor genérico
        print(calculo(kwh2, kwh_comercial))
        soma_com += kwh2
        consumo_hab_total.append(kwh2)
    if opcao == 3:
        kwh3 = float(input(f'Digite o consumo dessa indústria: '))
        kwh_industrial = 0.50  # valor genérico
        print(calculo(kwh3, kwh_industrial))
        soma_ind += kwh3
        consumo_hab_total.append(kwh3)
    if opcao == 4:
        break

print('-' * 30)
print(f'{"DETALHES GERAIS":^30}')
print('-' * 30)
print(f'Maior consumo: {max(consumo_hab_total): .4f} kWh')
print(f'Menor consumo: {min(consumo_hab_total): .4f} kWh')
print(f'Média de consumo: {(soma_res + soma_com + soma_ind) / 3: .4f}')
print(f'O total consumido por residencias foi de: {soma_res: .4f} kWh')
print(f'O total consumido por comércios foi de: {soma_com: .4f} Kwh')
print(f'O total consumido por indústrias foi de: {soma_ind: .4f} kWh')
