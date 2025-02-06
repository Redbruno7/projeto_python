# ALUNO: BRUNO C. RODGERS
# Data: 06/02/2025
# Criar função:
# - Receber 2 números (1-10)
# Criar menú:
    # º Somar;
    # º Subtrair;
    # º Multiplicar;
    # º Dividir;
    # º Fazer a divisão inteira;
    # º Encontrar o resto da divisão.
    # - Escolher um número para operações (1-6).

import os


from modules.print import title, menu
from modules.iterate import get_numbers
from modules.calculate import perform_operate

# Limpeza terminal
def cls_terminal():
    os.system('cls')

# Nav
cls_terminal()
title()

# Software
list_num = []
for i in range(2):
    list_num.append(get_numbers(f'Digite o {i + 1}º número (1-10): ', 1, 10))

while True:
    cls_terminal()
    title()

    print('=' * 80)
    print(f'Números: {list_num}')
    print('=' * 80)
    print()

    menu()
    option = get_numbers('Escolha uma opção (1-7): ', 1, 7)

    if option == 7:
        print('=' * 80)
        print('Sistema encerrado.')
        print('=' * 80)
        print()
        break

    numb_operator = get_numbers('Digite um número operador (1-6): ', 1, 6)
    result_1, result_2 = perform_operate(list_num, option, numb_operator)

    # Output
    print('=' * 80)
    print(f'Resultado 1: {result_1}')
    print(f'Resultado 2: {result_2}')
    print('=' * 80)
    print()

    print('=' * 80)
    input('Pressione Enter para continuar.\n')