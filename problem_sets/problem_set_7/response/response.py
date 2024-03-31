from validator_collection import validators


def main():
    if validate_the_email():
        print('Valid')
    else:
        print('Invalid')


def validate_the_email():
    email = input("What's your email address? ")
    try:
        if validators.email(email):
            return True
    except ValueError:
        return False


if __name__ == '__main__':
    main()
