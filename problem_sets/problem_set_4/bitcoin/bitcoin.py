import requests
import sys


def main():
    users_number = get_float()
    converted_number = convert_to_usd(users_number)
    print(f'${converted_number:,.4f}')


def get_float():
    if len(sys.argv) == 2:
        while True:
            try:
                number = float(sys.argv[1])
            except IndexError:
                sys.exit('Missing command-line argument')
            except ValueError:
                sys.exit('Command-line argument is not a number')
            else:
                return number
    else:
        sys.exit('You need to put one argument!')


def convert_to_usd(number):
    try:
        response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    except requests.RequestException:
        pass
    else:
        response_json = response.json()
        rate = float(response_json['bpi']['USD']['rate_float'])
        return rate * number


if __name__ == '__main__':
    main()
