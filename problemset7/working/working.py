import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):

    if matches := re.search(r"^(\d{1,2}):?(\d{2})?( AM| PM)? to (\d{1,2}):?(\d{2})?( AM| PM)?", s):
        start_hour = int(matches.group(1))
        end_hour = int(matches.group(4))
        if matches.group(2) != None:
            start_minute = int(matches.group(2))
        else:
            start_minute = 0
        if matches.group(5) != None:
            end_minute = int(matches.group(5))
        else:
            end_minute = 0

        if start_hour == 0 or end_hour == 0:
            raise ValueError()

        if start_hour > 12 or end_hour > 12 or start_minute > 59 or end_minute > 59:
            raise ValueError()

        if start_hour == 12 and matches.group(3) == " AM":
            start_hour = 0
        if end_hour == 12 and matches.group(6) == " AM":
            end_hour = 0

        if matches.group(3) == " PM" and start_hour < 12:
            start_hour = start_hour + 12
        if matches.group(6) == " PM" and end_hour < 12:
            end_hour = end_hour + 12

        return f"{start_hour:02}:{start_minute:02} to {end_hour:02}:{end_minute:02}"


    else:
        raise ValueError()




if __name__ == "__main__":
    main()
