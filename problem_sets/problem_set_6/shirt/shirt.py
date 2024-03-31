import sys
from PIL import Image, ImageOps


def main():
    file_names = get_command_line()
    input_file, output_file = file_names[0], file_names[1]
    create_an_image(input_file, output_file)


def get_command_line():
    if len(sys.argv) < 3:
        sys.exit('Too few command-line arguments')
    elif len(sys.argv) > 3:
        sys.exit('Too many command-line arguments')
    else:
        input, output = sys.argv[1], sys.argv[2]
        input_extension, output_extension = input.split('.')[1], output.split('.')[1]
        if input_extension and output_extension not in ['png', 'jpg', 'jpeg']:
            sys.exit('Invalid output')
        elif input_extension != output_extension:
            sys.exit('Input and output have different extensions')
        else:
            return [input, output]


def create_an_image(input_file, output_file):
    try:
        input_photo = Image.open(f'{input_file}')
    except FileNotFoundError:
        sys.exit('Input does not exist')
    else:
        shirt = Image.open('shirt.png')
        shirt_size = shirt.size
        right_size_photo = ImageOps.fit(image=input_photo, size=shirt_size)
        right_size_photo.paste(shirt, shirt)
        right_size_photo.save(f'{output_file}')


if __name__ == '__main__':
    main()
