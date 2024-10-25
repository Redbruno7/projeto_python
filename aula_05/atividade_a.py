# AULA 05 - ATIVIDADE A
# DESENVOLVA UM PROGRAMA QUE SOLICITE TRÊS VALORES AO USUÁRIO. EM SEGUIDA, CALCULE E EXIBA A SOMA E A MULTIPLICAÇÃO DESSES VALORES.
# Data: 25/10/2024

# Importar biblioteca do sistema operacional
import os

# Limpar terminal
os.system('cls')

# Título
print('-' * 70)
print('SOMA E MULTIPLICAÇÃO DE 3 VALORES')
print('=' * 70)

# Entrada de dados
numero_1 = float(input('1º Valor: '))
numero_2 = float(input('2º Valor: '))
numero_3 = float(input('3º Valor: '))

# Processamento de operações
soma = numero_1 + numero_2 + numero_3
multiplicacao = numero_1 * numero_2 * numero_3

# Saída de dados
print('=' * 70)
print(f'A soma dos três valores fornecidos é: {soma:.2f}')
print('-' * 70)
print(f'Já os três valores multiplicados resulta em: {multiplicacao:.2f}')
print('=' * 70)