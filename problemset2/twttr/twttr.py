
def main():

  word = input("Input: ")
  out = ""

  # If I am being honest with myself,
  # there is most likely a cleaner way to do this.
  for i in range(len(word)):
    match word[i]:
      case "a" | "A" | "e" | "E" | "i" | "I" | "o" | "O" | "u" | "U":
        None
      case _:
        out = out + word[i]

  print("Output:", out)

main()
