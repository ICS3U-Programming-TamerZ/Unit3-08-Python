#!/usr/bin/env python3

# Created By: Tamer Zreg
# Date: Oct. 20, 2022
# This program checks if a year is a leap year.


def main():
    # Gets the user's year
    user_year = input("Enter a year: ")
    print("")

    # Tries casting the user's year to an integer.
    try:
        user_year = int(user_year)

    # Restarts program if an exception is thrown
    except ValueError:
        print("You must enter an integer.\n")
        return main()

    # Checks if user_year is divisible by 4
    if user_year % 4 == 0:

        # Checks if user_year is divisible by 100
        if user_year % 100 == 0:

            # Checks if user_year is divisible by 400
            if user_year % 400 == 0:
                print(f"{user_year} is a leap year.\n")

            # Code executed if user_year is not divisible by 400
            else:
                print(f"{user_year} is not a leap year.\n")

        # Code executed if user_year is not divisible by 100
        else:
            print(f"{user_year} is a leap year.\n")

    # Code executed if user_year is not divisible by 4
    else:
        print(f"{user_year} is not a leap year.\n")


if __name__ == "__main__":
    main()
