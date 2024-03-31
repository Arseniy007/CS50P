def main():
    line = input('Describe your mood: ')
    final_line = convert(line)
    print(final_line)


def convert(line):
    line = line.replace(':)', '🙂')
    line = line.replace(':(', '🙁')
    return line


main()