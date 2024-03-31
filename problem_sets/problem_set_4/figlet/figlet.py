from pyfiglet import Figlet
import random
import sys


figlet = Figlet()
fonts = figlet.getFonts()


if len(sys.argv) == 3:
    if sys.argv[1] != '-f' and sys.argv[1] != '--font' or sys.argv[2] not in fonts:
        sys.exit('Invalid usage')
    else:
        line = input('Input: ')
        figlet.setFont(font=sys.argv[2])
        print(figlet.renderText(line))
elif len(sys.argv) == 1:
    line = input('Input: ')
    figlet.setFont(font=random.choice(fonts))
    print(figlet.renderText(line))
else:
    sys.exit('Invalid usage')
