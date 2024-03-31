import sys


def main():
    file_name = get_command_line()
    final_number = count_lines(file_name)
    print(final_number)


def get_command_line():
    if len(sys.argv) < 2:
        sys.exit('Too few command-line arguments')
    elif len(sys.argv) > 2:
        sys.exit('Too many command-line arguments')
    elif not sys.argv[1].endswith('.py'):
        sys.exit('Not a Python file')
    else:
        return sys.argv[1]


def count_lines():
    number_of_lines = 0
    try:
        with open(f'{file_name}') as file:
            for line in file:
                if line.lstrip().startswith('#') or line.isspace():
                    pass
                else:
                    number_of_lines += 1
    except FileNotFoundError:
        sys.exit('File does not exist')

    else:
        return number_of_lines


if __name__ == '__main__':
    main()
