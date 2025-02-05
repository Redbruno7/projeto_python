def conversion():
    print('=' * 80)
    while True:
        temp_f = input('Digite a temperatura em Fahrenheit: ').strip()

        if temp_f.replace('-', '').replace('.', '').isdigit():
            temp_f = float(temp_f)
            temp_c = (temp_f - 32) / 1.8

            return temp_c, temp_f
        
        print('-' * 80)
        print('Valor inválido. Tente novamente.')
        print('-' * 80)