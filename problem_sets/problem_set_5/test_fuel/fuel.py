def main():
    percentage = input('Fraction: ')
    converted_percentage = gauge(convert(percentage))
    print(converted_percentage)


def convert(percentage):
    x, y = percentage.split('/')
    x, y = int(x), int(y)
    result = x / y
    if y == 0:
        raise ZeroDivisionError
    if result > 1:
        raise ValueError
    result = round(result * 100)
    return result


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        converted_result = str(percentage) + "%"
        return converted_result


if __name__ == '__main__':
    main()
