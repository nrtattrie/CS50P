
def main():

    camel = input("camelCase: ")
    print(snake(camel))


def snake(camel):
    temp = ""
    for i in range(len(camel)):
        if camel[i].isupper():
            temp = temp + "_" + camel[i].lower()
        else:
            temp = temp + camel[i]

    return temp

main()
