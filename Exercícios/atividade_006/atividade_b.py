# ATIVIDADE 006 - ATIVIDADE B
# ALUNO: BRUNO C. RODGERS
# Data: 22/11/2024
# Crie uma lista com 5 números inteiros. Depois imprima a soma desses valores.

import os


os.system('cls')

# Título
print('=' * 70)
print('Soma de valores de uma lista')
print('=' * 70)
print()

# Flag
soma = 0

# Entrada
lista = []

# Iteração 5 números inteiros
print('-' * 70)
for i in range(1, 6):
    numero = int(input(f'Digite o {i}º valor: '))
    print('-' * 70)
    
    # Inserção de valor
    lista.append(numero)

    # Soma dos valores
    soma += numero
print()

# Saída soma
print('=' * 70)
print(f'A soma dos valores é: {soma}')
print('=' * 70)
print()