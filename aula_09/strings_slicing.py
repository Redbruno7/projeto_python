# AULA 09 - FATIAMENTO DE STRINGS
# Data: 05/11/2024

import os


print('=' * 70)
print('FATIAMENTO DE STRINGS')
print('=' * 70)

# Entrada
frase = 'String em Python!'

# Exibir a string original
print(f'String original: "{frase}"')
print('=' * 70)

# Fatiamento: Acessando partes específicas da string
# Primeiros 5 caracteres
primeiros_cinco = frase[:5] # 0: (Começo: 0), :5 (Fim: 4)
print(f'Primeiros cinco caracteres: "{primeiros_cinco}"')
print('.' * 70)

# Últimos 10 caracteres
ultimos_dez = frase[-10:] # -10: (Começa do último), :0 (Fim: -9)
print(f'Últimos dez caracteres: "{ultimos_dez}"')
print('.' * 70)

# Do quarto ao décimo caractere
quarto_decimo = frase[3:10] # 3: (Começo), :10 (Fim: 9)
print(f'Do quarto ao décimo caractere: "{quarto_decimo}"')
print('.' * 70)

# A cada dois caracteres
cada_dois = frase[::2] # 0: (Começo), :Último:, ::2 (Passo)
print(f'A cada dois caracteres: "{cada_dois}"')
print('.' * 70)

# Invertendo a string
invertida = frase[::-1] # 0: (Começo), :último: (Fim), ::-1 (Inversão)
print(f'String invertida: "{invertida}"')
print('=' * 70)