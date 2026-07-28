from pyfiglet import Figlet
import sys
import random

figlet = Figlet()
fonts = figlet.getFonts()

if len(sys.argv) == 3:
    if sys.argv[1] not in ["-f", "--font"] or sys.argv[2] not in fonts:
        sys.exit("Invalid usage")
    else:
        s = input("Input: ")
        figlet.setFont(font=sys.argv[2])
        print(figlet.renderText(s))
elif len(sys.argv) == 1:
    s = input("Input: ")
    figlet.setFont(font=random.choice(fonts))
    print(figlet.renderText(s))
else:
    sys.exit("Invalid usage")
