def main():
    answer = input('Tell me what time it is: ')
    time = convert(answer)
    if 7.0 <= time <= 8.0:
        print('breakfast time')
    elif 12.0 <= time <= 13.0:
        print('lunch time')
    elif 18.0 <= time <= 19.0:
        print('dinner time')


def convert(time):
    hours, minutes = time.split(":")
    minutes_10 = float(minutes) / 60
    time = float(hours) + minutes_10
    return time


if __name__ == "__main__":
    main()
