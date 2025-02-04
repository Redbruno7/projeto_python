def register_student():
    data_dict = {}

    print('=' * 80)
    while True:
        name = input('Digite o nome do aluno: ').strip()
        print('-' * 80)

        if name:
            data_dict['nome'] = name
            break

        print('Nome inválido. Tente novamente.')
        print('-' * 80)

    while True:
        register = input('Digite a matrícula do aluno: ').strip()
        print('-' * 80)

        if register.isdigit():
            register = int(register)
            data_dict['matricula'] = register
            break

        print('Matrícula inválida. Tente novamente.')
        print('-' * 80)

    while True:
        birth = input(
            'Digite a data de nascimento do aluno (dd/mm/aaaa): ').strip()

        if len(birth) == 10 and birth[
            2
            ] == '/' and birth[
                5
                ] == '/' and birth.replace('/', '').isdigit():
            data_dict['nascimento'] = birth
            break

        print('-' * 80)
        print('Data de nascimento inválida. Tente no formato (dd/mm/aaaa).')
        print('-' * 80)
    
    print('=' * 80)
    print()

    return data_dict