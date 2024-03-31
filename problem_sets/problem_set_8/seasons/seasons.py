from datetime import date
import sys
import inflect


def main():
    print(convert_to_the_right_format(get_minutes(get_the_birthdate(input('Date of Birth: ')))))


def get_the_birthdate(users_date):
    try:
        year, mounth, day = users_date.split('-')
        if 1 <= int(mounth) <= 12 and 1 <= int(day) <= 31 and len(year) == 4 and year[0:2] in ['19', '20']:
          return users_date
        else:
            sys.exit('Invalid date')
    except ValueError:
        sys.exit('Invalid date')


def get_minutes(users_date):
    users_date = date.fromisoformat(users_date)
    current_date = date.today()
    passed_time = current_date - users_date
    minutes = int(passed_time.total_seconds() / 60)
    return minutes


def convert_to_the_right_format(minutes):
    p = inflect.engine()
    result = p.number_to_words(minutes).capitalize().replace('and ', '')
    return f'{result} minutes'


if __name__ == "__main__":
    main()
