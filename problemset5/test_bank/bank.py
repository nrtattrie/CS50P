def main():
    greeting = input("Greeting: ")

    print("$" + str(value(greeting)))


def value(greeting):
    greeting = greeting.lower().strip()

    if greeting.find("hello") == 0:
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
