import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if matches := re.search(r'^([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+)$', ip):
        first, second, third, fourth = int(matches.group(1)), int(matches.group(2)), int(matches.group(3)), int(matches.group(4))
        if 0 <= first <= 255 and 0 <= second <= 255 and 0 <= third <= 255 and 0 <= fourth <= 255:
            return True
        else:
            return False
    else:
        return False


if __name__ == "__main__":
    main()
