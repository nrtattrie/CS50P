from datetime import date
import sys
import inflect
import re

p = inflect.engine()

def main():
    dob = input("Date of Birth: ")
    if re.search(r"^\d{4}-\d{2}-\d{2}$", dob):
        print(convert(dob))
    else:
        sys.exit(1)


def convert(dob):
    birthday = date.fromisoformat(dob)
    today = date.today()
    delta = abs(today - birthday)
    minutes = delta.days * 24 * 60
    rent = p.number_to_words(minutes)
    rent = rent.replace(" and ", " ").capitalize()
    return(f"{rent} minutes")


if __name__ == "__main__":
    main()
