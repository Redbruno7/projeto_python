# AULA 05 - ATIVIDADE E
# ALUNO: BRUNO C. RODGERS
# FAÇA UM PROGRAMA QUE RECEBA UM NÚMERO INTEIRO E EXIBA SEU SUCESSOR E ANTECESSOR.
# Data: 25/10/2024

# Importar bibliotecas
import os

# Limpar terminal
os.system('cls')

# Título
print('=' * 70)
print('INSIRA O VALOR A SER VERIFICADO')
print('=' * 70)

# Entrada
n1 = int(input('Digite um valor inteiro: '))

# Processamento
antecessor = n1 - 1
sucessor = n1 + 1

# Saída
print('=' * 70)
print(f'O número antecessor do valor informado é: {antecessor}.')
print(f'Por outro lado, seu sucessor é: {sucessor}')
print('=' * 70)