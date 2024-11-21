# AULA 05 - ATIVIDADE I
# ALUNO: BRUNO C. RODGERS
# DESENVOLVA UM PROGRAMA QUE SOLICITE UM VALOR EM REAIS E CALCULE QUANTOS DÓLARES PODEM SER COMPRADOS COM ESSE VALOR.
# Data: 25/10/2024

# Importar bibliotecas
import os

# Limpar terminal
os.system('cls')

# Título
print('=' * 70)
print('INSIRA UM VALOR EM REAIS PARA CONVERSÃO EM DÓLAR')
print('=' * 70)

# Entrada
reais = float(input('Digite o valor: '))

# Processamento
dolar = reais * 5.71

# Saída
print('=' * 70)
print(f'O valor de R${reais} convertido em dólar resulta: US${dolar:.2f}.')
print('=' * 70)