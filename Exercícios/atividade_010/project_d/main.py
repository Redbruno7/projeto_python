# ALUNO: BRUNO C. RODGERS
# Data: 05/02/2025
# Crie uma função que receba uma temperatura em fahrenheit e retorne o valor em graus célsius.

import os


from modules.title import title
from modules.conversion import conversion

# Limpar terminal
def clear_terminal():
    os.system('cls')

clear_terminal()
title()

# Software
temp_c, temp_f = conversion()
print('-' * 80)
print(f'A temperatura de {temp_f} ºF, resulta em {temp_c} ºC.')
print('=' * 80)
print()

while True:
    print('=' * 80)
    try_again = input('Tentar novamente? (s/n): ').strip().lower()

    if try_again == 's':
        clear_terminal()
        title()

        temp_c, temp_f = conversion()

        print('-' * 80)
        print(f'A temperatura de {temp_f} ºF, resulta em {temp_c:.0f} ºC.')
        print('=' * 80)
        print()

    elif try_again == 'n':
        print('-' * 80)
        print('Sistema encerrado.')
        print('=' * 80)
        print()
        break

    else:
        print('-' * 80)
        print('Resposta inválida. Tente novamente.')
        print('=' * 80)
        print()