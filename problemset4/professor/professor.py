import random

def main():
    #random.seed()
    level = get_level()

    score = 0
    for _ in range(10):
        wrong = 0
        x = generate_integer(level)
        y = generate_integer(level)
        while True:
            try:
                print(f"{x} + {y} = ", end="")
                answer = int(input().strip())
                if answer != (x+y):
                    raise Exception()
            except ValueError:
                print("Please enter an integer as your answer")
            except Exception:
                wrong += 1
                if wrong == 3:
                    print(f"{x} + {y} = {x+y}")
                    break
                else:
                    print("EEE")
            else:
                wrong = 0
                score += 1
                break

    print("Score:", score)


def get_level():
    while True:
        try:
            level = int(input("Level: ").strip())
            if level != 1 and level != 2 and level != 3:
                raise Exception()
        except Exception:
            print("Please enter a level of 1, 2, or 3")
        except ValueError:
            print("Please enter a number for level selection")
        else:
            break
    return level


def generate_integer(level):
    if level == 1:
        num = random.randint(0, 9)
    elif level == 2:
        num = random.randint(10, 99)
    elif level == 3:
        num = random.randint(100, 999)
    else:
        print("Invalid level passed to generate_integer")

    return num


if __name__ == "__main__":
    main()
