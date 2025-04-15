import csv
import sys
from tabulate import tabulate


def main():

    try:
        # print(len(sys.argv))

        if len(sys.argv) != 2:
            raise Exception()

        splitter = sys.argv[1].split(".")
        if splitter[len(splitter) - 1] != "csv":
            raise FileExistsError()

        filename = sys.argv[1]
        with open(filename) as file:
            reader = csv.reader(file)
            listOfLists = []
            for row in reader:
                listOfLists.append(row)

    except FileNotFoundError:
        print("File does not exist")
        sys.exit(1)
    except FileExistsError:
        print("File not a CSV file")
        sys.exit(1)
    except Exception:
        print("Too few or too many command-line arguments:", len(sys.argv))
        sys.exit(1)
    else:
        header = listOfLists[0]
        listOfLists.pop(0)
        print(tabulate(listOfLists, header, tablefmt="grid"))


if __name__ == "__main__":
    main()
