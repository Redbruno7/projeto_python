# AULA 05 - ATIVIDADE F
# ALUNO: BRUNO C. RODGERS
# DESENVOLVA UM PROGRAMA QUE PEÇA UM NÚMERO QUALQUER E CALCULE O DOBRO E O TRIPLO DESSE NÚMERO.
# Data: 25/10/2024

# Importar bibliotecas
import os

# Limpar terminal
os.system('cls')

# Título
print('=' * 70)
print('INSIRA O VALOR A SER MUILTIPLICADO')
print('=' * 70)

# Entrada
n1 = float(input('Digite um número: '))

# Processamento
dobro = n1 * 2
triplo = n1 * 3

# Saída
print('=' * 70)
print(f'O dobro do valor informado é: {dobro:.2f}.')
print(f'O triplo do valor informado é: {triplo:.2f}.')
print('=' * 70)