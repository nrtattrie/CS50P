from pyfiglet import Figlet
from random import choice
import sys

figlet = Figlet()


def main():

    if len(sys.argv) == 1:
        word = input("Input: ")
        figlet.setFont(font=choice(figlet.getFonts()))
        print(figlet.renderText(word))

    elif len(sys.argv) == 3:
        if sys.argv[1] != "-f" and sys.argv[1] != "--font":
            sys.exit("Invalid usage")

        if sys.argv[2] not in figlet.getFonts():
            sys.exit("Font not in FIGlet library")

        word = input("Input: ")
        figlet.setFont(font=sys.argv[2])
        print(figlet.renderText(word))

    else:
        sys.exit("Invalid usage")


main()
