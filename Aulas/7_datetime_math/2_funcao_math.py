# AULA 07 - FUNÇÃO INTERNA - MATH
# Data: 31/10/2024

import os
import math


os.system('cls')

# Título
print('=' * 70)
print('ESTUDO DA BIBLIOTECA MATEMÁTICA (MATH)')
print('=' * 70)

# Entrada
base = 2
expoente = 3
angulo = 30
radicando = 81
cateto_oposto = 5
cateto_adjacente = 10

# Processamento
potencia = math.pow(base, expoente)
raiz_quadrada = math.sqrt(radicando)
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
hipotenusa = math.hypot(cateto_oposto, cateto_adjacente)

# Saída
print(f'{base} elevado a {expoente} é igual a: {potencia}.')
print(f'A raiz quadrada de {radicando} é: {raiz_quadrada}.')
print(f'O seno de {angulo} é: {seno:.2f}.')
print(f'O cosseno de {angulo} é: {cosseno:.2f}.')
print(f'A tangente de {angulo} é: {tangente:.2f}.')
print(f'O valor da hipotenusa é: {hipotenusa:.2f}.')
print('~' * 70)