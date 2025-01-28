# Função receber números
def get_numbers():
    
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