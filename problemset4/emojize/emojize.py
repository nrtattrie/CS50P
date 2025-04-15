import emoji


def main():
    alias = input("Input: ")
    print("Output:", emoji.emojize(alias, language="alias"))


main()
