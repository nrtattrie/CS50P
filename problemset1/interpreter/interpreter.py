def main():
    exp = input("Expression: ").strip()

    x_str, sep, temp = exp.partition(" ")
    y = temp[0]

    junk, sep, z_str = exp.partition(y)

    x_str = x_str.strip()
    z_str = z_str.strip()

    x = float(x_str)
    z = float(z_str)

    if y == "+":
        print(x+z)
    if y == "-":
        print(x-z)
    if y == "*":
        print(x*z)
    if y == "/":
        print(x/z)


main()
