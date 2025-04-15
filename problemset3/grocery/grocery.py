
def main():

    groceries = {}

    while True:
        try:
            item = input()
            item = item.upper()
            groceries[item] = groceries[item] + 1
        except EOFError:
            for key in sorted(groceries.keys()):
                print(groceries[key], key)
            break
        except KeyError:
            groceries[item] = 1


main()
