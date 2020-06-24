"""
Faça um algoritmo que converta uma velocidade expressa em km/h para m/s e vice e versa.
Você deve criar um menu com as duas opções de conversão e com uma opção para finalizar o programa.
O usuário poderá fazer quantas conversões desejar, sendo que o programa só será finalizado
quando a opção de finalizar for escolhida.
"""
print()
print('-' * 5, 'CONVERSOR KM/H - M/S', '-' * 5)

while True:
    print()
    print( '[1] Converter km/h para m/s'
           '\n[2] Converter m/s para k/h'
           '\n[3] Finalizar o programa')
    print()
    opcao = int(input('Digite usa opção: '))
    print()
    if opcao == 1:
        km_h = float(input('Digite a velocidade em km/h: '))
        m_s = km_h / 3.6
        print(f'A velocidade de {km_h} km/h equivale a {m_s} m/s')
    elif opcao == 2:
        m_s = float(input('Digite a velocidade em m/s: '))
        km_h = m_s * 3.6
        print(f'A velocidade de {m_s} m/s equivale a {km_h} km/h')
    elif opcao == 3:
        print('-' * 5, 'PROGRAMA FINALIZADO', '-' * 5)
        break
    else:
        print('Opção inválida!')


