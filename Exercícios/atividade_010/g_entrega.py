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
def numbers():

    # Criar lista "list = []"
    list_1 = []

    # Loop for "for i in range(int):"
    print('-' * 80)
    for i in range(2):
    
        # Criar loop while "while bool:"
        while True:

            # Iterar usuário "a = input(str)"
            num_1 = input(f'Digite o {i + 1}º número (1-10): ')
            print('-' * 80)

            # Verificar número "if a.isdigit():"
            if num_1.isdigit():

                # Casting inteiro "a = int(a)"
                num_1 = int(num_1)
                
                # Condicionar entrada "if a > int or a < int:"
                if num_1 > 0 and num_1 < 11:

                    # Adicionar na lista "list.append(a)"
                    list_1.append(num_1)

                    # Quebrar loop (break)
                    break

                else:
                    print('Número inválido. Tente novamente.')
                    print('-' * 80)
            else:
                print('Número inválido. Tente novamente.')
                print('-' * 80)
    print()
    
    # Retornar lista "return list"
    return list_1

# Definir função "def function():"
def operator():
    
    # Criar loop while "while bool:"
    print('=' * 80)
    while True:

        # Iterar usuário com casting "a = input(str)"
        num_2 = input('Digite o valor para realizar a operação (1-6): ')

        # Verificar número "if a.isdigit():"
        if num_2.isdigit():

            # Casting inteiro "a = int(a)"
            num_2 = int(num_2)
            
            # Condicionar entrada "if a > int and a < int:"
            if num_2 > 0 and num_2 < 7:
                print('=' * 80)
                print()

                # Retornar variável "return a"
                return num_2

            else:
                print('-' * 80)
                print('Número inválido. Tente novamente.')
                print('-' * 80)
        else:
            print('-' * 80)
            print('Número inválido. Tente novamente.')
            print('-' * 80)

# Definir função "def function()"
def operation(num_1, num_2):

    # Dividir lista
    operation_1 = num_1[0]
    operation_2 = num_1[-1]

    # Somar
    add_1 = operation_1 + num_2
    add_2 = operation_2 + num_2

    return add_1, add_2

    
      
# Título
print('=' * 80)
print('FUNÇÃO - OPERAÇÕES')
print('=' * 80)
print()

# Chamar função "a = function()"
num_1 = numbers()

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

    # Opção 1
    if option == '1':

        # Chamar função "a, b = function(x, y)"
        num_2 = operator()
        add_1, add_2 = operation(num_1, num_2)
        print('=' * 80)
        print(f'Soma 1: {add_1}')
        print('-' * 80)
        print(f'Soma 2: {add_2}')
        print('=' * 80)
        print()

    # Opção 2
    if option == '2':

        #Chamar função
        num_2 = operator()


    # Pausa
    print('=' * 80)
    pause = input('Pressione Enter para continuar.')
    print('=' * 80)
    print()