
def main():

    word = input("Input: ")
    print("Output:", shorten(word))


def shorten(word):
    out = ""
    for i in range(len(word)):
        match word[i]:
            case "a" | "A" | "e" | "E" | "i" | "I" | "o" | "O" | "u" | "U":
                None
            case _:
                out = out + word[i]
    return out


if __name__ == "__main__":
  main()
