# AULA 16 - FUNÇÕES EM PYTHON - RETURN
# Data: 21/01/2024

import os


os.system('cls')

# Título
print('=' * 80)
print('FUNÇÃO - RETURN')
print('=' * 80)
print()

# Definir função "def função(a, b, c, d):"
def calcular_vm_media(espaco, tempo, espaco_un, tempo_un): 
    
    # Condicionar variável "if a == string:"
    if espaco_un == 'metros':
        
        # Converter valor "x = x / int"
        espaco = espaco / 1000
    
    # Condicionar variável "if a == string:"
    if tempo_un == 'minutos':
        
        # Converter valor "x = x / int"
        tempo = tempo / 60
        
    # Calcular variável "x = a / b"
    vm_media = espaco / tempo
    
    # Retornar função "return x"
    return vm_media

# Entrada usuário minúsculo "x = cast(input('string')).lower()"
print('=' * 80)
espaco = float(input('Digite a distância percorrida: '))
print('-' * 80)
espaco_un = input('A distância é em km ou metros? ').lower()
print('-' * 80)
tempo = float(input('Digite o tempo gasto: '))
print('-' * 80)
tempo_un = input('O tempo é em horas ou minutos? ').lower()
print('=' * 80)
print()

# Invocar função "x = função(a, b, c, d)"
vm = calcular_vm_media(espaco, tempo, espaco_un, tempo_un)

# Exibir resultado com duas casas decimais "print(f'{x:.2f}')"
print('=' * 80)
print(f'A velocidade média é {vm:.2f} {espaco_un} / {tempo_un}.')
print('=' * 80)
print()