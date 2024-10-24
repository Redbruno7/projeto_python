# EXTRA - RADICIAÇÃO
# Data: 24/10/2024

# Importar biblioteca do sistema operacional
import os

# Limpar terminal
os.system('cls')

# Título
print('-' * 70)
print('RADICIAÇÃO')
print('=' * 70)

# Entrada de dados
numero_1 = float(input('Entre com o número: '))
numero_2 = float(input('Entre com a raiz: '))

# Processamento
raiz = numero_1 ** (1 / numero_2)

# Saída de Dados
print(f'A raiz de {numero_1} por {numero_2} é {raiz:.2f}')