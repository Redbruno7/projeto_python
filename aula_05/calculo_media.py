# AULA 05 - OPERAÇÕES ARITMÉTICAS
# Data: 24/10/2024

# Importar biblioteca do sistema operacional
import os

# Limpar terminal
os.system('cls')

# Título
print('=' * 70)
print('CÁLCULO DE MÉDIA')
print('=' * 70)

# Entrada de dados
nota1 = float(input('1ª nota: '))
nota2 = float(input('2ª nota: '))
nota3 = float(input('3ª nota: '))
nota4 = float(input('4ª nota: '))

# Processamento de operações
soma = nota1 + nota2 + nota3 + nota4
media = (nota1 + nota2 + nota3 + nota4) / 4

# Saída
print('=' * 70)
print('° NOTAS')
print(f'Nota 1: {nota1} | Nota 2: {nota2} | '
      f'Nota 3: {nota3} | Nota 4: {nota4}')
print('-' * 70)
print(f'Média: {media}')
print('-' * 70)