import requests
import sys
import json


def main():
    amount = 0.0

    while True:
        try:
            bitcoin = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
            # print(json.dumps(amount.json(), indent=2))
            o = bitcoin.json()
            # print(o["bpi"]["USD"]["rate_float"])
            amount = o["bpi"]["USD"]["rate_float"]

            if len(sys.argv) != 2:
                raise Exception()

            n = float(sys.argv[1])

            if sys.argv[1].isalpha():
                raise Exception()

        except Exception:
            print("Missing or non-numeric command line argument")
            sys.exit(1)
        except ValueError:
            print("Please enter an argument that is a number")
            sys.exit(1)
        except requests.RequestException:
            sys.exit(1)
        else:
            break

    amount = n * float(amount)
    print(f"${amount:,.4f}")


if __name__ == "__main__":
    main()
