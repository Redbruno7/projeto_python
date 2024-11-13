# AULA 05 - ATIVIDADE G
# ALUNO: BRUNO C. RODGERS
# CRIE UM PROGRAMA QUE CONVERTA UMA MEDIDA EM METROS PARA CENTÍMETROS E MILÍMETROS.
# Data: 25/10/2024

# Importar bibliotecas
import os

# Limpar terminal
os.system('cls')

# Título
print('=' * 70)
print('INSIRA A METRAGEM PARA CONVERSÃO')
print('=' * 70)

# Entrada
m = float(input('Digite uma metragem: '))

# Processamento
cm = m * 100
mm = m * 1000

# Saída
print('=' * 70)
print(f'A medida fornecida convertida para centímetros resulta em: {cm:.2f} cm.')
print(f'A medida fornecida convertida para milímetros resulta em: {mm:.2f} mm.')
print('=' * 70)