# ALUNO: BRUNO C. RODGERS
# Data: 06/02/2025
# Crie uma função que receba a altura e peso de uma pessoa. Depois retorne o seu IMC.

import os


from modules.print import title, chart
from modules.iterate import get_data
from modules.calculate import imc_calculate, classify

# Limpeza terminal
def clear_terminal():
    os.system('cls')

# Nav
clear_terminal()
title()
    
# Software
data_list = get_data()
imc = imc_calculate(data_list)
result = classify(imc)

# Output
print('=' * 80)
print(f'O IMC da pessoa informada é: {imc:.2f}')
print('-' * 80)
print(f'Classificação: {result}')
print('=' * 80)
print()

chart()

while True:
    print('=' * 80)
    try_again = input('Tentar novamente? (s/n): ').strip().lower()

    if try_again == 's':
        clear_terminal()
        title()
        
        data_list = get_data()
        imc = imc_calculate(data_list)
        result = classify(imc)

        print('=' * 80)
        print(f'O IMC da pessoa informada é: {imc:.2f}')
        print('-' * 80)
        print(f'Classificação: {result}')
        print('=' * 80)
        print()

        chart()

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