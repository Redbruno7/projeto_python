# AULA 16 - FUNÇÕES EM PYTHON - RETURN
# Data: 21/01/2024

import os


os.system('cls')

# Título
print('=' * 80)
print('DEF - RETURN')
print('=' * 80)
print()

# Definir função "def a(x, y):"
def calcular_velocidade_media(distancia, tempo):
    
    # Formular velocidade média "x = a / b"
    velocidade_media = distancia / tempo
    
    # Chamar variável "return x"
    return velocidade_media

# Entrada usuário "x = float(input('string'))"
print('=' * 80)
distancia = float(input('Digite a distância percorrida (em km): '))
print('-' * 80)
tempo = float(input('Digite o tempo gasto (em horas): '))
print('=' * 80)
print()


# Calcular com a função "x = função(x, y)"
velocidade = calcular_velocidade_media(distancia, tempo)

# Exibir resultado
print('=' * 80)
print(f'A velocidade média é {velocidade:.2f} km/h.')
print('=' * 80)
print()