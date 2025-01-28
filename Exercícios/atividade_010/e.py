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
    data_list = []
    
    print('=' * 70)
    while True:
        
        height = input('Digite a altura: ').strip()

        if height.replace('.', '').isdigit():
            data_list.append(float(height))
            break

        else:
            print('-' * 70)
            print('Valor inválido. Tente novamente.')
            print('-' * 70)
        
    while True:
        print('-' * 70)
        weight = input('Digite o peso: ').strip()
        
        if weight.replace('.', '', 1).isdigit():
            data_list.append(float(weight))
            break

        else:
            print('-' * 70)
            print('Valor inválido. Tente novamente.')
    
    # Retornar valores "return a, b"
    return data_list

# Cálculo IMC
def imc_calculate(data_list):
    height, weight = data_list
    imc = weight / (height ** 2)
    return imc

# Classificação IMC
def classification(result):
    if result < 18.5:
        return 'Abaixo do peso ideal.'
    elif 18.5 <= result < 25:
        return 'Peso ideal.'
    elif 25 <= result < 30:
        return 'Acima do peso ideal.'
    elif 30 <= result < 35:
        return 'Obesidade grau um.'
    elif 35 <= result < 40:
        return 'Obesidade grau dois.'
    else:
        return'Obesidade grau três.'

# Tabela
def table():
    print('=' * 70)
    print('Tabela de classificação')
    print('-' * 70)
    print('1. 18.5 ou menos: Abaixo do Normal.')
    print('2. Entre 18.6 e 24.9: Normal.')
    print('3. Entre 25.0 e 29.9: Sobrepeso.')
    print('4. Entre 30.0 e 34.9: Obesidade grau I.')
    print('5. Entre 35.0 e 39.9: Obesidade grau II.')
    print('6. 40.0 ou mais: Obesidade grau III.')
    print('=' * 70)
    print()    

while True:

    # Invocar função
    clear_terminal()
    title()
    data_list = get_input()
    imc = imc_calculate(data_list)

    print('=' * 70)
    print(f'O IMC da pessoa informada é: {imc:.2f}')
    print('-' * 70)

    result = classification(imc)
    print(f'{result}')
    print('=' * 70)
    print()

    table()

    print('=' * 70)
    next = input('Tentar novamente? (s/n): ').strip().lower()

    if next == 'n':
        print('-' * 70)
        print('Sistema encerrado.')
        print('=' * 70)
        print()
        break
    
    elif next != 's':
        print('-' * 70)
        print('Resposta inválida. Tente novamente.')
        print('=' * 70)
        print()