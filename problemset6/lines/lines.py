import sys

def main():

    try:
        count = 0
        if len(sys.argv) != 2:
            raise Exception()
        list = sys.argv[1].split(".")

        if list[len(list) - 1] != "py":
            raise FileExistsError()
        filename = sys.argv[1]

        with open(filename) as file:
            lines = file.readlines()
        for line in lines:
            line = line.lstrip()
            if line.startswith("#"):
                pass
            elif line.strip() == "":
                pass
            else:
                count += 1

    except FileNotFoundError:
        print("File does not exist")
        sys.exit(1)
    except FileExistsError:
        print("File not a python file")
        sys.exit(1)
    except Exception:
        print("Too few or too many command-line arguments")
        sys.exit(1)
    else:
        print(count)


if __name__ == "__main__":
    main()
