import sys
import csv


def main():
    file_names = get_command_line()
    old_file, new_file = file_names[0], file_names[1]
    old_info = read_the_file(old_file)
    create_new_file(old_info, new_file)


def get_command_line():
    if len(sys.argv) < 3:
        sys.exit('Too few command-line arguments')
    elif len(sys.argv) > 3:
        sys.exit('Too many command-line arguments')
    else:
        file_names = [sys.argv[1], sys.argv[2]]
        return file_names


def read_the_file(file_name):
    students = []
    try:
        with open(f'{file_name}') as file:
            reader = csv.DictReader(file)
            for row in reader:
                students.append({'name': row['name'], 'house': row['house']})
    except FileNotFoundError:
        sys.exit(f'Could not read {file_name}')
    else:
        return students


def create_new_file(old_info, new_file):
    with open(f'{new_file}', 'w') as file:
        writer = csv.DictWriter(file, fieldnames=['first', 'last', 'house'])
        writer.writeheader()
        for student in old_info:
            last, first = student['name'].split(', ')
            house = student['house']
            writer.writerow({'first': first, 'last': last, 'house': house})
    return None


if __name__ == '__main__':
    main()
