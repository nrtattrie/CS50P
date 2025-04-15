
def main():
    due = 50

    while True:
        if due <= 0:
            due = due * -1
            print("Change Owed:", due)
            break

        print("Amount Due:", due)
        coin = input("Insert Coin: ")
        if coin == "25" or coin == "10" or coin == "5":
            due = due - int(coin)

main()
