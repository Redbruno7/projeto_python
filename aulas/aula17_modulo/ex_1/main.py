# ALUNO: BRUNO CADENGUE RODGERS
# Data: 28/01/2024

import os


from modulos.modulo_somar import somar
from modulos.modulo_multiplicar import multiplicar as multi
from modulos.modulo_dividir import dividir


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
        print('Valor de A ou B inválido. Tente novamente.')
        print('=' * 80)
        print()

        print('=' * 80)
        pause = input('Pressione Enter para continuar: ')
        continue
    
    a = float(a)
    b = float(b)
    
    resultado_soma = somar(a, b)
    resultado_produto = multi(a, b)
    resultado_divisao, erro = dividir(a, b)
    
    print('=' * 80)
    print('CÁLCULOS MATEMÁTICOS')
    print('=' * 80)
    print(f'Cálculo da soma: {resultado_soma}')
    print('-' * 80)
    print(f'Cálculo do produto: {resultado_produto}')
    print(f'Cálculo da divisão: {resultado_divisao}, {erro}')
    print('=' * 80)
    print()
    
    print('=' * 80)
    exit = input('Deseja sair do programa? (s/n): ').strip().lower()
    if exit == 's':
        print('-' * 80)
        print('Sistema encerrado.')
        print('=' * 80)
        print()
        break