def get_numbers(prompt, min_value, max_value):
    print('=' * 80)
    while True:
        num_1 = input(prompt)

        if num_1.isdigit():
            num_1 = int(num_1)

            if min_value <= num_1 <= max_value:
                print('=' * 80)
                print()
                return num_1

            else:
                print('-' * 80)
                print('Número inválido. Tente novamente.')
                print('-' * 80)