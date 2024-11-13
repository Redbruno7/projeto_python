# ATIVIDADE 005 - ATIVIDADE K
# ALUNO: BRUNO C. RODGERS
# Data: 13/11/2024

import os


os.system('cls')

# Título
print('=' * 70)
print('VERIFICAÇÃO DE PALÍNDROMOS')
print('=' * 70)
print()

# Entrada
print('=' * 70)
frase = input('Digite uma palavra ou frase: ').strip().lower()
print('-' * 70)

# Inversão de strip
frase_invertida = frase[::-1]

# Condição para saída
if frase == frase_invertida:
    print('É palíndromo.')
else:
    print('Não é palíndromo.')
print('=' * 70)
print()