# ATIVIDADE 007 - ATIVIDADE G
# ALUNO: BRUNO C. RODGERS
# Data: 22/11/2024
# Faça um programa que sorteia os números da Mega Sena e da Lotofácil

import os
import random


os.system('cls')

# Título
print('=' * 70)
print('Simulador de sorteio da Mega Sena e Lotofácil:')
print('=' * 70)
print()

# Entrada
mega_sena = random.sample(range(1, 61), 6)

# Saída
