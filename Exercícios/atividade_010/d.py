# ALUNO: BRUNO C. RODGERS
# Data: 23/01/2025
# Crie uma função que receba uma temperatura em fahrenheit e retorne o valor em graus célsius.


import os


# Definir função "def function()"
def clear_terminal():
    os.system('cls')

def conversion():
    
    # Looping condicional "while bool:"
    while True:
        
        # Iterar usuário "a = input(str)"
        temp_f = input('Digite a temperatura em Fahrenheit: ').strip()
        
        # Condicionar número (Racionais) "if a.replace.isdigit()"
        if temp_f.replace('-', '').replace('.', '').isdigit():
            
            # Casting inteiro "a = int(a)"
            temp_f = float(temp_f)
            
            # Converter ºF para ºC "ºC = (ºF - 32) / 1.8"
            temp_c = (temp_f - 32) / 1.8

            # Retornar celsius "return"
            return temp_c, temp_f
        
        # Fechar condição "else:"
        else:
            print('-' * 70)
            print('Valor inválido. Tente novamente.')
            print('-' * 70)

def title():
    print('=' * 70)
    print('FUNÇÃO - CONVERSÃO DE TEMPERATURA')
    print('=' * 70)
    print()

# Título
title()

# Chamar função "a = function()"
print('=' * 70)
temp_c, temp_f = conversion()
print('-' * 70)
print(f'A temperatura de {temp_f} ºF, resulta em {temp_c} ºC.')
print('=' * 70)
print()

while True:
    print('=' * 70)
    next = input('Tentar novamente? (s/n): ').strip().lower()
    
    if next == 's':
        clear_terminal()
        title()
        
        print('=' * 70)
        temp_c, temp_f = conversion()
        print('-' * 70)
        print(f'A temperatura de {temp_f} ºF, resulta em {temp_c:.0f} ºC.')
        print('=' * 70)
        print()
        
    elif next == 'n':
        
        print('-' * 70)
        print('Sistema encerrado.')
        print('=' * 70)
        print()
        
        # Quebrar loop "break"
        break
    
    else:
        print('-' * 70)
        print('Resposta inválida. Tente novamente.')
        print('=' * 70)
        print()