# AULA 16 - MODULARIZAÇÃO - MAIN
# Data: 28/01/2024

import os


from modulos.modulo_somar import somar

while True:
    os.system('cls')

    # Título
    print('=' * 80)
    print('MODULARIZAÇÃO')
    print('=' * 80)
    print()

    print('=' * 80)
    a = input('Entre com o valor de A: ')
    print('-' * 80)
    b = input('Entre com o valor de B: ')
    print('=' * 80)
    print()
    
    if not a.replace('.', '', 1).isdigit() or not b.replace('.', '', 1).isdigit():
        print('=' * 80)
        print('Número inválido. Tente novamente.')
        continue
    
    