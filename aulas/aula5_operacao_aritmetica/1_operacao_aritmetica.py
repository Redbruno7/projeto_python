# AULA 05 - OPERAÇÕES ARITMÉTICAS
# Data: 24/10/2024

# Importar biblioteca do sistema operacional
import os

# Limpar terminal
os.system('cls')

# Título
print('-' * 70)
print('OPERADORES ARITMÉTICOS')
print('=' * 70)

# Entrada de Dados
print('\nº SOMA:')
print('-' * 70)
parcela_1 = float(input('Entre com a 1ª parcela: '))
parcela_2 = float(input('Entre com a 2ª parcela: '))


print('\nº SUBTRAÇÃO')
print('-' * 70)
minuendo = float(input('Entre com o minuendo: '))
subtraendo = float(input('Entre com o subtraendo: '))

print('\nº PRODUTO')
print('-' * 70)
multiplicando = float(input('Entre com o multiplicando: '))
multiplicador = float(input('Entre com o multiplicador: '))

print('\nº DIVISÃO')
print('-' * 70)
dividendo = float(input('Entre com o dividendo: '))
divisor = float(input('Entre com o divisor: '))

print('\nº DIVISÃO INTEIRA')
print('-' * 70)
numero_1 = float(input('Entre com o dividendo: '))
numero_2 = float(input('Entre com o divisor: '))

print('\nº MÓDULO')
print('-' * 70)
numero_3 = float(input('Entre com o dividendo: '))
numero_4 = float(input('Entre com o divisor: '))

print('\nº EXPONENCIAÇÃO')
print('-' * 70)
numero_5 = float(input('Entre com o número: '))
numero_6 = float(input('Entre com a potência: '))

print('\nº RADICIAÇÃO QUADRADA')
print('-' * 70)
numero_7 = float(input('Entre com o número: '))

print('\nº RADICIAÇÃO CÚBICA')
print('-' * 70)
numero_8 = float(input('Entre com o número: '))

# Processamento de operações
soma = parcela_1 + parcela_2
diferenca = minuendo - subtraendo
produto = multiplicando * multiplicador
quociente = dividendo / divisor
divisao_inteira = numero_1 // numero_2
modulo = numero_3 % numero_4
potencia = numero_5 ** numero_6
raiz_quadrada = numero_7 ** (1 / 2)
raiz_cubica = numero_8 ** (1 / 3)

# Saída de Dados
print('=' * 70)
print('RESULTADOS')
print('-' * 70)
print(f'\nA soma de {parcela_1} + {parcela_2} é: {soma}')
print(f'A subtração de {minuendo} - {subtraendo} é: {diferenca}')
print(f'A multiplicação de {multiplicando} x {multiplicador} é: {produto}')
print(f'A divisão de {dividendo} / {divisor} é: {quociente}')
print(f'A divisão inteira de {numero_1} : {numero_2} é: {divisao_inteira}')
print(f'O módulo de {numero_3} % {numero_4} é: {modulo}')
print(f'A exponenciação de {numero_5} ** {numero_6} é: {potencia}')
print(f'A raiz quadrada de {numero_7} é: {raiz_quadrada}')
print(f'A raiz cúbica de {numero_8} é: {raiz_cubica}')