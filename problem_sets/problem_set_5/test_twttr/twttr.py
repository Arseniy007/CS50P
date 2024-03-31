def main():
    word = input('Write something and I will remove some vowels from it: ')
    print(shorten(word))


def shorten(word):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = ''
    for letter in word:
        if letter not in vowels:
            result += letter
    return result


if __name__ == "__main__":
    main()
