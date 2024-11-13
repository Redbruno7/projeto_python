# AULA 05 - ATIVIDADE J
# ALUNO: BRUNO C. RODGERS
# ELABORE UM PROGRAMA QUE PEÇA AS DIMENSÕES DE UM RETÂNGULO E CALCULE SEU PERÍMETRO.
# Data: 25/10/2024

# Importar bibliotecas
import os

# Limpar terminal
os.system('cls')

# Título
print('=' * 70)
print('INSIRA AS DIMENSÕES DO RETÂNGULO')
print('=' * 70)

# Entrada
base = float(input('Insira o valor da base: '))
altura = float(input('Insira o valor da altura: '))

# Processamento
perimetro = (2 * base) + (2 * altura)

# Saída
print('=' * 70)
print(f'O valor do perímetro do retângulo proposto resulta em: {perimetro:.2f}.')
print('=' * 70)