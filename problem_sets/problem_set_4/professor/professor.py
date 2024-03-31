from random import randint


def main():
    level = get_level()
    problems, solutions = [], []
    for _ in range(10):
        first_number, second_number = generate_integer(level), generate_integer(level)
        solutions.append(str(first_number + second_number))
        problem = f'{first_number} + {second_number} = '
        problems.append(problem)
    right_answers = 0
    for i in range (10):
        for j in range (3):
            users_guess = input(f'{problems[i]}')
            if users_guess == solutions[i]:
                right_answers += 1
                break
            elif users_guess != solutions[i]:
                print('EEE')
                if j == 2:
                    print(f'{problems[i]} {solutions[i]}')
        if i == 9:
            print('Score:', right_answers)


def get_level():
    while True:
        try:
            level = int(input('Level: '))
        except ValueError:
            pass
        else:
            if level not in [1, 2, 3]:
                pass
            else:
                return level


def generate_integer(level):
    if level not in [1, 2, 3]:
        raise ValueError
    else:
        if level == 1:
            number = randint(0, 9)
        elif level == 2:
            number = randint(10, 99)
        else:
            number = randint(100, 999)
    return number


if __name__ == "__main__":
    main()
