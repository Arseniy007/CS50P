import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    matches = main_test(s)
    if matches.group(2) == None:
        first, second = matches.group(1), matches.group(4)
        if matches.group(3) == 'AM':
            if first == '12':
                first = '00'
            if 0 < int(first) < 10:
                first = '0' + first
            if second == '12':
                    pass
            else:
                second = str(int(second) + 12)
        else:
            if second == '12':
                second = '00'
            if 0 < int(second) < 10:
                second = '0' + second
            if first == '12':
                pass
            else:
                first = str(int(first) + 12)
        return f'{first}:00 to {second}:00'
    else:
        first_hour, first_minutes = matches.group(1), matches.group(2)
        second_hour, second_minutes = matches.group(4), matches.group(5)
        if matches.group(3) == 'AM':
            if first_hour == '12':
                first_hour = '00'
            if 0 < int(first_hour) < 10:
                first_hour = '0' + first_hour
            if second_hour == '12':
                    pass
            else:
                second_hour = str(int(second_hour) + 12)
        else:
            if second_hour == '12':
                second_hour = '00'
            if 0 < int(second_hour) < 10:
                second_hour = '0' + second_hour
            if first_hour == '12':
                pass
            else:
                first_hour = str(int(first_hour) + 12)
        return f'{first_hour}:{first_minutes} to {second_hour}:{second_minutes}'


def main_test(s):
    if matches := re.search(r'^([0-9]+):?([0-9]+)? (AM|PM) to ([0-9]+):?([0-9]+)? (AM|PM)$', s):
        if test_the_time(matches):
            return matches
        else:
            raise ValueError
    else:
        raise ValueError


def test_the_time(matches):
    if matches.group(2) == None:
        first, second = int(matches.group(1)), int(matches.group(4))
        if 0 <= first <= 12 and 0 <= second <= 12:
            return True
        else:
            return False
    else:
        first_hour, first_minutes = int(matches.group(1)), int(matches.group(2))
        second_hour, second_minutes = int(matches.group(4)), int(matches.group(5))
        if 0 <= first_hour <= 12 and 0 <= second_hour <= 12 and 0 <= first_minutes < 60 and 0 <= second_minutes < 60:
            return True
        else:
            return False


if __name__ == "__main__":
    main()
