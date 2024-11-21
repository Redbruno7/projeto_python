# ATIVIDADE 003 - ATIVIDADE D
# ALUNO: BRUNO C. RODGERS
# Data: 04/11/2024
# FAÇA UM PROGRAMA QUE RECEBA UM ÂNGULO QUALQUER. 
# EM SEGUIDA, CALCULE O SENO, COSSENO E TANGENTE DO ÂNGULO. 
# LIMITE A SAÍDA A 2 CASAS DECIMAIS.

import os
import math


os.system('cls')

print('=' * 70)
print('CÁLCULO DE SENO, COSSENO E TANGENTE DE UM ÂNGULO')
print('=' * 70)

# Entrada
angulo = int(input('Insira um valor de ângulo para cálculo: '))

# Processamento
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

# Saída
print(f'O seno de {angulo} é: {seno:.2f}.')
print('-' * 70)
print(f'O cosseno de {angulo} é: {cosseno:.2f}.')
print('-' * 70)
print(f'A tangente de {angulo} é: {tangente:.2f}.')
print('=' * 70)