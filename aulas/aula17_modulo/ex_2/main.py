# STUDENT: BRUNO C. RODGERS
# DATE: 13/02/2025

import os
from packs.register import register_appointment
from packs.show import show_diary


def main():
    os.system('cls')

    diary_dict = {}

    while True:
        print('=' * 80)
        print('Appointment Diary:')
        print('-' * 80)
        print('1. Register appointment.')
        print('2. Show appointments.')
        print('3. Exit.')
        print('-' * 80)
        option = input('Enter option (1-3): ')
        print('=' * 80)
        print()

        if option == '1':
            register_appointment(diary_dict)

        elif option == '2':
            show_diary(diary_dict)

        elif option == '3':
            print('=' * 80)
            print('Shutdown System.')
            print('=' * 80)
            print()

        else:
            print('=' * 80)
            print('Invalid option. Try again.')
            print('=' * 80)
            print()

if __name__ == '__main__':
    main()