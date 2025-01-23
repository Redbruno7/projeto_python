# ALUNO: BRUNO C. RODGERS
# Data: 23/01/2025
# Criar função:
# º Receber lista de números.
# º Retornar 2 listas (pares, ímpares)
# º Retornar quantidade (pares, ímpares)


import os


os.system('cls')

# Título
print('=' * 70)
print('FUNÇÃO NÚMEROS PARES / ÍMPARES')
print('=' * 70)
print()

# Definir função "def a():"
def numbers():
    
    # Criar lista "list = []"
    number_list = []
    even_list = []
    odd_list = []
    
    # Criar contadores "a = 0"
    even_count = 0
    odd_count = 0
    
    # Iteração usuário sem espaço"a = input(str).strip()"
    print('=' * 70)
    number_input = input('Digite números separados por vígula: ').strip()
    print('=' * 70)
    print()
    
    # Iterar na lista divida "for i in list:"
    for i in number_input.split(','):
        
        # Adicionar entrada na lista sem espaços com casting "list.append(int(a.strip()))"
        number_list.append(int(i.strip()))    
        
    # Iterar na lista "for i in list:"
    for i in number_list:
        
        # Condicionar par / ímpar "if i % int == int:"
        if i % 2 == 0:
            even_list.append(i)
            even_count += 1
            
        else:
            odd_list.append(i)
            odd_count += 1

    # Retornar resultados "return a, b"
    return even_list, odd_list, even_count, odd_count

# Chamar função
even_list, odd_list, even_count, odd_count = numbers()
print('=' * 70)
print(f'Lista par: {even_list}')
print(f'Quantidade de elementos: {even_count}')
print('-' * 70)
print(f'Lista ímpar: {odd_list}')
print(f'Quantidade de elementos: {odd_count}')
print('=' * 70)
print()