
def main():
    greeting = input()
    print(response(greeting))


def response(greeting):
    if greeting == "Hello :)":
        return "Hello 🙂"
    elif greeting == "Goodbye :(":
        return "Goodbye 🙁"
    elif greeting == "Hello :) Goodbye :(":
        return "Hello 🙂 Goodbye 🙁"


main()
