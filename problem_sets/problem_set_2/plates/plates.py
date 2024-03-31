def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if s[0:2].isalpha() and 2 <= len(s) <= 6 and s.isalnum() and right_digits(s):
        return True
    else:
        return False


def right_digits(s):
    flag = True
    digits = 0
    for character in s:
        if character.isdigit():
            digits += 1
            if character == '0' and digits == 1:
                flag = False
                break
        else:
            if digits != 0:
                flag = False
                break
    if flag:
        return True
    else:
        return False


main()
