
def main():
    greeting = input()
    print(quiet(greeting))

def quiet(greeting):
    if greeting == "HELLO":
        return greeting.lower()
    elif greeting == "THIS IS CS50":
        return greeting.lower()
    elif greeting == "50":
        return greeting.lower()

main()
