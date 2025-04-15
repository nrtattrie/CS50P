
def main():

    date_split = []
    months = {"January": "1", "February": "2", "March": "3", "April": "4",
    "May": "5", "June": "6", "July": "7", "August": "8",
    "September": "9", "October": "10", "November": "11", "December": "12"}

    while True:
        try:
            date = input("Date: ")
            date_split = date.split("/")

            if  len(date_split) == 1:
                date_split = date.split(" ")
                if date_split[1].isalnum():
                    raise Exception()
                date_split[1] = date_split[1].rstrip(",")
                date_split[0] = months[date_split[0]]

            month = int(date_split[0])
            day = int(date_split[1])
            year = int(date_split[2])

            if month > 12 or day > 31:
                raise Exception()

        except Exception:
            print("Incorrect format, or Month exceeds 12, or Day exceeds 31")

        else:
            print(f"{year}-{month:02}-{day:02}")
            break

main()
