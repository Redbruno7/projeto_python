# ATIVIDADE 003 - ATIVIDADE G
# Data: 04/11/2024
# FAÇA UM PROGRAMA QUE PEÇA OS VALORES DE A, B E C DE UMA EQUAÇÃO DO 2º GRAU. 
# CALCULE AS RAÍZES DA EQUAÇÃO DO 2º GRAU SEGUINDO A FÓRMULA: Δ = B² - 4AC, X = (-B ± RAIZ(Δ)) / (2A).

import os
import math


os.system('cls')

print('=' * 70)
print('CÁLCULO DE EQUAÇÃO DE SEGUNDO GRAU')
print('=' * 70)

# Entrada
a = float(input('Entre com o valor de "a": '))
b = float(input('Entre com o valor de "b": '))
c = float(input('Entre com o valor de "c": '))

# Processamento
delta = (b ** 2) - (4 * a * c)
raiz_1 = (- b + delta) / (2 * a)
raiz_2 = (- b - delta) / (2 * a)

# Saída
print(f'As raízes encontradas para esta equação são: {raiz_1:.2f} e {raiz_2:.2f}.')
print('=' * 70)