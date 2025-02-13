import os
from packs.diary import appointment_list


def show_diary(diary_dict):
    os.system('cls')

    print('=' * 80)
    print('Apointment Agended:')
    print('-' * 80)
    option = input('All appointments or appointment for Date (a/d): ').lower()

    if option == 'a':
        appointment_list(diary_dict)
        print('=' * 80)
        print()

    elif option == 'd':
        print('-' * 80)
        date = input('Enter appointment date (dd/mm/yyyy): ')
        appointment_list(diary_dict, date)
        print('=' * 80)
        print()

    else:
        print('-' * 80)
        print('Invalid option. Try again.')
        print('-' * 80)
