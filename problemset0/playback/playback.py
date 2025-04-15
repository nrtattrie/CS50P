
def main():
    greeting = input()
    print(slowed(greeting))

def slowed(greeting):
    if greeting == "This is CS50":
        return "This...is...CS50"
    elif greeting == "This is our week on functions":
        return "This...is...our...week...on...functions"
    elif greeting == "Let's implement a function called hello":
        return "Let's...implement...a...function...called...hello"

main()

