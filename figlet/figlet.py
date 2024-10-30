from pyfiglet import Figlet
import pyfiglet
import random


import sys

figlet = Figlet()


if len(sys.argv) == 3:
    L = figlet.getFonts()
    if not  sys.argv[1] == "-f" or  sys.argv[1] == "--font"  or  sys.argv[2] not in L:
        sys.exit("Invalid usage")
    else:
        str = input('entre ur text')
        font = sys.argv[2]
        figlet = pyfiglet.Figlet(font=f'{font}')
        print(figlet.renderText(str))

if len(sys.argv) == 2:
    sys.exit("Invalid usage")

elif len(sys.argv) == 1:
    str = input('entre ur text')
    L = figlet.getFonts()
    font = random.choice(L)
    figlet = pyfiglet.Figlet(font=f'{font}')
    print(figlet.renderText(str))




