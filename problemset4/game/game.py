import random
import sys

def main():

    while True:
        try:
            level = int(input("Level: "))
            if level < 1:
                raise Exception()
        except ValueError:
            print("Please enter a positive integer")
        except Exception:
            print("Please enter a positive integer")
        else:
            break

    rando = random.randrange(1, level)

    while True:
        try:
            guess = int(input("Guess: "))
            if guess < 1:
                raise Exception()

        except ValueError:
            print("Please enter a positive integer")

        except Exception:
            print("Please guess a number greater than zero and less than or equal to the level")

        else:
            if guess == rando:
                print("Just right!")
                sys.exit()
                break
            elif guess > rando:
                print("Too large!")
            else:
                print("Too small!")


if __name__ == "__main__":
    main()
