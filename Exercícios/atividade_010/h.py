# ALUNO: BRUNO C. RODGERS
# Data: 23/01/2025
# º Crie um programa de cadastro:
#   - Código do cliente;
#   - Nome;
#   - Altura;
#   - Peso;
# ° Imprimir:
#   - Dados dos clientes;
#   - Média altura;
#   - Média peso.
# º Finalizar programa com código "0"

import os

# Limpeza terminal
def cls_terminal():
    os.system('cls')

def title():
    print('=' * 80)
    print('FUNÇÃO - CADASTRO ACADEMIA'.center(80))
    print('=' * 80)
    print()

def client_dict():
    client_dict = {}

    print('=' * 80)
    while True:
        code = input('Código do cliente: ').strip()
        print('-' * 80)
        
        if code.isdigit():
            code = int(code)
            client_dict['codigo'] = code
            break

        print('Código inválido. Tente novamente.')
        print('-' * 80)

    while True:
        name = input('Nome do cliente: ').strip()
        print('-' * 80)

        if name:
            client_dict['nome'] = name
            break

        print('Nome inválido. Tente novamente.')
        print('-' * 80)

    while True:
        height = input('Altura do cliente: ').strip()
        print('-' * 80)

        if height.replace('.', '', 1).isdigit():
            height = float(height)
            client_dict['altura'] = height
            break

        print('Altura inválida. Tente novamente.')
        print('-' * 80)

    while True:
        weight = input('Peso do cliente: ').strip()

        if weight.replace('.', '', 1).isdigit():
            weight = float(weight)
            client_dict['peso'] = weight
            print('=' * 80)
            print()
            break

        print('-' * 80)
        print('Peso inválido. Tente novamente.')
        print('-' * 80)
    
    return client_dict

# Nav
cls_terminal()
title()

# Software
client_list = []
while True:
    client_list.append(client_dict())

    print('=' * 80)
    option_exit = input(
        'Aperte "0" para sair ou "Enter" para continuar cadastrando: '
        ).strip()
    print('=' * 80)
    print()

    if option_exit != '0':
        continue

    else:
        cls_terminal()
        title()

        if client_list:
            total_height = sum(i['altura'] for i in client_list)
            total_weight = sum(i['peso'] for i in client_list)
            average_height = total_height / len(client_list)
            average_weight = total_weight / len(client_list)

        # Output
        print('=' * 80)
        print('Lista de clientes:')
        print('=' * 80)
        print()
        
        for i in client_list:
            print('=' * 80)
            for key, value in i.items():
                print(f'{key}: {value}')
            print('=' * 80)
            print()

        print('=' * 80)
        print(f'Média de altura: {average_height:.2f}')
        print('-' * 80)
        print(f'Média de peso: {average_weight:.2f}')
        print('=' * 80)
        print()
        break