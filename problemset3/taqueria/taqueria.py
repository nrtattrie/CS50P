
def main():
    menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    get_total(menu)


def get_total(menu):
    cost = 0.0
    while True:
        try:
            order = input("Item: ")
            order = order.title()
            if order not in menu:
                raise KeyError()
        except KeyError:
            print("Item not in menu")
        except EOFError:
            print()
            break
        else:
            cost = cost + menu[order]
            print(f"Total: ${cost:.2f}")
    return

main()
