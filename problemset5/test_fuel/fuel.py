
def main():

    while True:
        try:
            fraction = input("Fraction: ")
            numer, denom = str(fraction).split("/")
            x = int(numer)
            y = int(denom)
            if y == 0:
                raise ZeroDivisionError()
            if x > y:
                raise Exception()
        except Exception:
            print("Tank can't be filled above full")
        except ZeroDivisionError:
            print("Cannot have zero in fraction's denominator")
        except ValueError:
            print("Incorrect input type - please enter whole numbers")
        else:
            num = convert(fraction)
            break

    print(gauge(num))


def convert(fraction):

    numer, denom = fraction.split("/")
    x = int(numer)
    y = int(denom)
    num = round((float(x/y)) * 100)
    return int(num)


def gauge(percentage):
    if percentage <= 1:
        return("E")
    elif 100 >= percentage >= 99:
        return("F")
    else:
        str_percentage = str(percentage) + "%"
        return(str_percentage)


if __name__ == "__main__":
    main()
