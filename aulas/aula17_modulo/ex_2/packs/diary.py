def add_appointment(diary_dict, date, description):
    if date not in diary_dict:
        diary_dict[date] = []

    diary_dict[date].append(description)


def appointment_list(diary_dict, date=None):
    if date:
        if date in diary_dict:
            print('=' * 80)
            print(f'Appointment {date}')

            for i in diary_dict[date]:
                print('-' * 80)
                print(f'- {i}')

        else:
            print('-' * 80)
            print(f'Without appointment founded for {date}.')

        print('=' * 80)
        print()

    else:
        if not diary_dict:
            print('=' * 80)
            print('Whithout appointment agended.')

        else:
            for date, appointment in diary_dict.items():
                print('=' * 80)
                print(f'Appointment {date}:')

                for i in appointment:
                    print('-' * 80)
                    print(f'- {i}')

                print('=' * 80)
                print()
