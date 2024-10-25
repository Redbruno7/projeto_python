# AULA 05 - ATIVIDADE D
# IMPLEMENTE UM PROGRAMA QUE RECEBA DOIS NÚMEROS E REALIZE A DIVISÃO, FORMATANDO O RESULTADO COM QUATRO CASAS DECIMAIS.
# Data: 25/10/2024

# Importar bibliotecas
import os

# Limpar terminal
os.system('cls')

# Título
print('=' * 70)
print('INSIRA OS VALORES PARA CÁLCULO')
print('=' * 70)

# Entrada
valor_1 = float(input('1º Valor: '))
valor_2 = float(input('2º Valor: '))

# Processamento
resultado = valor_1 / valor_2

# Saída
print('=' * 70)
print(f'O resultado da divisão dos valores fornecidos é: {resultado:.4f}.')
print('=' * 70)