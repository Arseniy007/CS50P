from tabulate import tabulate
import sys
import csv


def main():
    file_name = get_command_line()
    menu = get_menu(file_name)
    print(menu)


def get_command_line():
    if len(sys.argv) < 2:
        sys.exit('Too few command-line arguments')
    elif len(sys.argv) > 2:
        sys.exit('Too many command-line arguments')
    elif not sys.argv[1].endswith('.csv'):
        sys.exit('Not a CSV file')
    else:
        file_name = sys.argv[1]
        return file_name


def get_menu(file_name):
    tabel = []
    try:
        with open(f'{file_name}') as file:
            reader = csv.reader(file)
            for row in reader:
                tabel.append(row)
    except FileNotFoundError:
        sys.exit('File does not exist')
    else:
        return tabulate(tabel[1:], headers=tabel[0], tablefmt='grid')


if __name__ == '__main__':
    main()
