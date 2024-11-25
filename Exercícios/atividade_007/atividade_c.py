# ATIVIDADE 007 - ATIVIDADE C
# ALUNO: BRUNO C. RODGERS
# Data: 25/11/2024
# Utilizando o exercício anterior, coloque todas as listas em ordem crescente de valor

import os
import random


os.system('cls')

# Título
print('=' * 220)
print('Lista de 1 a 100 em ordem crescente:')
print('=' * 220)
print()

# Entrada
lista = random.sample(range(1, 101), 50)

# Ordenação crescente
lista.sort()

# Saída
print('=' * 220)
print(f'Lista Crescente: {lista}')
print('=' * 220)
print()