import os
from packs.diary import add_appointment


def register_appointment(diary_dict):
    os.system('cls')

    print('=' * 80)
    print('Appointment Register:')
    print('-' * 80)
    date = input('Enter appointment date (dd/mm/yyyy): ')
    print('-' * 80)
    description = input('Enter appointment description: ')
    print('=' * 80)
    print()

    add_appointment(diary_dict, date, description)

    print('=' * 80)
    print(f'Appointment agended for {date}: {description}')
    print('=' * 80)
    print()
