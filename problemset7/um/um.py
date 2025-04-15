import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    matches = re.findall(r"\bum\b", s, re.IGNORECASE)

    for match in matches:
        print(match)

    return len(matches)





if __name__ == "__main__":
    main()
