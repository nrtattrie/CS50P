
def main():

    question = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")

    question = question.lower().lstrip().rstrip()

    match question:
        case "42" | "forty-two" | "forty two":
            print("Yes")
        case _:
            print("No")

main()
