# ALUNO: BRUNO C. RODGERS
# Data: 23/01/2025
# Crie uma função que receba a altura e peso de uma pessoa. Depois retorne o seu IMC.


import os

# Limpeza de terminal
def clear_terminal():
    os.system('cls')

# Título
def title():
    print('=' * 70)
    print('FUNÇÃO - CÁLCULO IMC')
    print('=' * 70)
    print()

# Receber informações
def get_input():

    # Loop condicional "while bool:"
    while True:
        print('=' * 70)
        heigth = input('Digite a altura: ').strip()

        # Condicionar existência "if a.replace('old', 'new', count).isdigit():"
        if heigth.replace('.', '', 1).isdigit():

            # Quebrar loop "break"
            break

        # Fechar condição "else:"
        else:
            print('-' * 70)
            print('Valor inválido. Tente novamente.')
            print('-' * 70)
        
    while True:
        print('-' * 70)
        weigth = input('Digite o peso: ').strip()
        
        if weigth.replace('.', '', 1).isdigit():
            break

        else:
            print('-' * 70)
            print('Valor inválido. Tente novamente.')
            print('-' * 70)
    
    # Retornar valores "return a, b"
    return heigth, weigth

# Cálculo IMC
def imc_calculate(height, weight):
    imc = weight * (height ** 2)
    return imc

# Programa Principal
title()
height, weight = get_input()
imc = imc_calculate(height, weight)

print('=' * 70)
print(f'O IMC da pessoa informada é: {imc}')
print('=' * 70)
print()

while True:
    print('=' * 70)
    next = input('Tentar novamente? (s/n): ').strip().lower()
    
    if next == 's':
        title()
        height, weight = get_input()
        imc = imc_calculate(height, weight)

        print('=' * 70)
        print(f'O IMC da pessoa informada é: {imc}')
        print('=' * 70)
        print()
        
    elif next == 'n':
        
        print('-' * 70)
        print('Sistema encerrado.')
        print('=' * 70)
        print()
        break
    
    else:
        print('-' * 70)
        print('Resposta inválida. Tente novamente.')
        print('=' * 70)
        print()