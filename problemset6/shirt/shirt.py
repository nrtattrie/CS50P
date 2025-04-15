import sys
import os
from PIL import Image
from PIL import ImageOps


def main():

    try:
        # Checking correct number of arguments were used
        if len(sys.argv) != 3:
            raise Exception()

        # Checking whether file extensions are valid
        _, ext1 = os.path.splitext(sys.argv[1])
        _, ext2 = os.path.splitext(sys.argv[2])
        if ext1 == "" or ext2 == "":
            raise FileExistsError()

        # Checking to make sure the two extensions match
        if ext1 != ext2:
            raise Exception()

        # Opening shirt file
        with Image.open(sys.argv[1]) as before:
            with Image.open("shirt.png") as shirt:
                before = ImageOps.fit(before, shirt.size)
                before.paste(shirt, shirt)
                before.save(sys.argv[2])

    # Exceptions to catch
    except FileExistsError:
        print("Input or output do not have correct extension")
        sys.exit(1)
    except FileNotFoundError:
        print("File entered is not in this directory")
        sys.exit(1)
    except Exception:
        print("Incorrect number or type of command line arguments")
        sys.exit(1)



if __name__ == "__main__":
    main()
