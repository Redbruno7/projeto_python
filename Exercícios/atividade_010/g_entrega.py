# ALUNO: BRUNO C. RODGERS
# Data: 23/01/2025
# Criar função:
# - Receber 2 números (1-10)
# Criar menú:
    # º Somar;
    # º Subtrair;
    # º Multiplicar;
    # º Dividir;
    # º Fazer a divisão inteira;
    # º Encontrar o resto da divisão.
    # - Escolher um número para operações (1-6).


import os


os.system('cls')

# Definir função "def a():"
def operations_function(num_1, num_2):
            
    # Criar loop while "while bool:"
    while True:
                
        # Iterar usuário com casting "a = int(input(str))"
        print('=' * 80)
        num_2 = int(
            input('Digite um valor para fazer a operação (1-6): '))
                
        # Condicionar entrada "if a > int and a < int:"
        if num_2 > 0 and num_2 < 7:
            
            # Quebra loop
            break

        else:
            print('Número inválido. Tente novamente.')
            print('-' * 80)
            
        
# Título
print('=' * 80)
print('FUNÇÃO - OPERAÇÕES')
print('=' * 80)
print()

# Criar lista "list = []"
list_1 = []

# Criar loop for "for i in range(int):"
print('-' * 80)
for i in range(2):

    # Criar loop while "while bool:"
    while True:
        
        # Iterar usuário com casting "a = input(str)"
        num_1 = int(input(f'Digite o {i + 1}º número (1-10): '))
        print('-' * 80)

        # Condicionar entrada "if a > int or a < int:"
        if num_1 > 0 and num_1 < 11:

            # Adicionar número na lista sem espaçamento "list.append(a)"
            list_1.append(num_1)
            break
                    
        # Quebrar loop "break"
        else:
            print('Número inválido. Tente novamente.')
            print('-' * 80)
print()

# Criar loop while "while bool:"
while True:
        
    # Menu
    print('=' * 80)
    print('Menú de opções')
    print('=' * 80)
    print('1. Somar (+).')
    print('-' * 80)
    print('2. Subtrair (-).')
    print('-' * 80)
    print('3. Multiplicar (*).')
    print('-' * 80)
    print('4. Dividir (/).')
    print('-' * 80)
    print('5. Calcular divisão inteira (//).')
    print('-' * 80)
    print('6. Calcular resto de divisão (%).')
    print('=' * 80)
    print()
        
    # Iterar usuário sem espaçamento "a = input(str)"
    print('=' * 80)
    option = input('Digite uma opção (1-6): ')
    print('=' * 80)
    print()
    
    