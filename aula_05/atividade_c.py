# AULA 05 - ATIVIDADE C
# ELABORE UM PROGRAMA QUE RECEBA QUATRO NOTAS DE UM ALUNO E CALCULE A MÉDIA DESSAS NOTAS.
# Data: 25/10/2024

# Importar bibliotecas
import os

# Limpar terminal
os.system('cls')

# Título
print('=' * 70)
print('NOTAS')
print('=' * 70)

# Entrada
n1 = float(input('1ª Nota: '))
n2 = float(input('2ª Nota: '))
n3 = float(input('3ª Nota: '))
n4 = float(input('4ª Nota: '))

# Processamento
media = (n1 + n2 + n3 + n4) / 4

# Saída
print('=' * 70)
print(f'A média das notas informadas é de: {media}.')
print('=' * 70)