#import inflect
#p = inflect.engine()

def main():

    names = []
    while True:
        try:
            name = input("Name: ").strip()
            names.append(name)
        except EOFError:
            print()
            break

    farewell = "Adieu, adieu, to "

    if len(names) == 1:
        farewell = farewell + names[0]
    elif len(names) == 2:
        farewell = farewell + names[0] + " and " + names[1]
    else:
        n = len(names) - 1
        for i in range(n):
            farewell = farewell + names[i] + ", "
        farewell = farewell + "and " + names[len(names)-1]

    print(farewell)

main()
