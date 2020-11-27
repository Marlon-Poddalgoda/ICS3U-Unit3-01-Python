# Created by Marlon Poddalgoda
# Created on November 2020
# This program adds 2 user inputted numbers


def main():
    # this function calculates 2 user inputted numbers

    print("This program does basic addition.")

    # input
    first_number = int(input("Enter your first number: "))
    second_number = int(input("Enter your second number: "))

    # process
    answer = first_number + second_number

    # output
    print("")
    print("{0} + {1} = {2}".format(first_number, second_number, answer))


if __name__ == "__main__":
    main()
