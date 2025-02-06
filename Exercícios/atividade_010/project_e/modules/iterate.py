def get_data():
    data_list = []
    
    print('=' * 80)
    while True:
        
        height = input('Digite a altura: ').strip()

        if height.replace('.', '').isdigit():
            data_list.append(float(height))
            break

        else:
            print('-' * 80)
            print('Valor inválido. Tente novamente.')
            print('-' * 80)
        
    while True:
        print('-' * 80)
        weight = input('Digite o peso: ').strip()
        
        if weight.replace('.', '', 1).isdigit():
            data_list.append(float(weight))
            print('=' * 80)
            print()
            break

        else:
            print('-' * 80)
            print('Valor inválido. Tente novamente.')
    
    # Retornar valores "return a, b"
    return data_list