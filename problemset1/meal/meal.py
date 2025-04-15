
def main():
    time = input("What time is it? ")
    time_float = convert(time)

    if 7.0 <= time_float <= 8.0:
        print("breakfast time")
    elif 12.0 <= time_float <= 13.0:
        print("lunch time")
    elif 18.0 <= time_float <= 19.0:
        print("dinner time")


def convert(time):

    time.strip()
    hours, minutes = time.split(":")
    time_float = float(hours) + (float(minutes)/60.0)
    return time_float


if __name__ == "__main__":
    main()
