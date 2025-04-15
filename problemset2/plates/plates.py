def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not s_len(s):
        return False

    if not two_alphas(s):
        return False

    if not alphanumeric(s):
        return False

    if not first_num_zero(s):
        return False

    if not middle_nums(s):
        return False

    return True


def s_len(s):
    if 6 >= len(s) >= 2:
        return True
    else:
        return False


def two_alphas(s):
    if s[0].isalpha() and s[1].isalpha():
        return True
    else:
        return False


def alphanumeric(s):
    if not s.isalnum():
        return False
    return True


def first_num_zero(s):
    first_num_found = False

    for i in range(len(s)):
        if not first_num_found and s[i].isdigit():
            if s[i] == "0":
                return False
            else:
                first_num_found = True
    return True


def middle_nums(s):
    ending_alpha_found = False
    i = len(s) - 1

    # If there are no numbers in s, then there cannot be middle numbers
    if s.isalpha():
        return True

    # Initializing indices for iterative search
    if s[i].isalpha():
        alpha_ind = i
        digit_ind = len(s)
        ending_alpha_found = True
    elif s[i].isdigit():
        digit_ind = i
        alpha_ind = -1
    i = i - 1 # Decrementing i: No need to recheck last index

    while i >= 0:
        if s[i].isalpha() and ending_alpha_found == False:
            alpha_ind = i
            ending_alpha_found = True
        elif s[i].isdigit():
            digit_ind = i

        if ending_alpha_found and digit_ind < alpha_ind:
            return False

        i = i - 1

    return True

main()
