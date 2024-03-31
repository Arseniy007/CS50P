def main():
    percentage = convert("Fraction: ")
    print(percentage)


def convert(prompt):
    while True:
        try:
            x, y = input(prompt).split("/")
            x, y = int(x), int(y)
            result = x / y
            if result <= 1:
                break
        except (ValueError, ZeroDivisionError):
            pass
    if result <= 0.1:
        return "E"
    elif result >= 0.9:
        return "F"
    else:
        converted_result = str((round(result * 100))) + "%"
        return converted_result


main()
