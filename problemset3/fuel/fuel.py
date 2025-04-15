
def main():

    convert()


def convert():

    numer = 0
    denom = 0
    dec = 0.0

    while True:
        try:
            frac = input("Fraction: ")
            numer, denom = frac.split("/")
            x = int(numer)
            y = int(denom)
            dec = float(x/y)
            if dec > 1.0:
                raise Exception()
        except ValueError:
            print("Fraction must contain whole numbers")
        except ZeroDivisionError:
            print("Cannot have zero in fraction's denominator")
        except Exception:
            print("Tank can't be filled above full")
        else:
            break

    dec = dec * 100
    if dec <= 1.0:
        print("E")
    elif 100.0 >= dec >= 99.0:
        print("F")
    else:
        print(round(dec), "%", sep = "")

main()
