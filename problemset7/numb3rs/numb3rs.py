import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):

    if match := re.search(r"^([1-9]\d{0,2})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", ip):
        if int(match.group(1)) < 0 or int(match.group(1)) > 255:
            #print("First group not in range")
            return False
        if int(match.group(2)) < 0 or int(match.group(2)) > 255:
            #print("Second group not in range")
            return False
        if int(match.group(3)) < 0 or int(match.group(3)) > 255:
            #print("Third group not in range")
            return False
        if int(match.group(4)) < 0 or int(match.group(4)) > 255:
            #print("Fourth group not in range")
            return False
        else:
            return True
    else:
        #print("Pattern not found")
        return False



if __name__ == "__main__":
    main()
