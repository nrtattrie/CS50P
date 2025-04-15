import csv
import sys


def main():

    try:
        # Check whether correct number of arguments were made in command line
        if len(sys.argv) != 3:
            raise Exception()


        # Check whether the first file name is of type CSV
        splitter = sys.argv[1].split(".")
        if splitter[len(splitter) - 1] != "csv":
            raise FileExistsError()

        # Check whether the second file name is of type CSV
        splitter = sys.argv[2].split(".")
        if splitter[len(splitter) - 1] != "csv":
            raise FileExistsError()

        with open(sys.argv[1]) as before:
            reader = csv.reader(before)
            with open(sys.argv[2], "w") as after:
                writer = csv.DictWriter(after, fieldnames=["first", "last", "house"])
                writer.writeheader()
                for row in reader:
                    if row[0].find(",") != -1:
                        last, first = row[0].split(",")
                        house = row[1]
                        writer.writerow(
                            {
                                "first": first.strip(),
                                "last": last.strip(),
                                "house": house,
                            }
                        )

    except FileNotFoundError:
        print("File does not exist")
        sys.exit(1)
    except FileExistsError:
        print("File not a CSV file")
        sys.exit(1)
    except Exception:
        print("Too few or too many command-line arguments:", len(sys.argv))
        sys.exit(1)


if __name__ == "__main__":
    main()
