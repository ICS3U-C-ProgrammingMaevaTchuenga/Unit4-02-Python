#!/usr/bin/env python3
# Created By: Maeva Tchuenga
# Date: 09, 12 2026
#  this program is to find the factorial of a number using a function
import decimal


def main():

    # Get the number from the user
    user_input = input("Enter a positive number: ")
    user_number = float(user_input)
    while True:
        try:
            # Check if the input is a positive number
            if user_number >= 2 and user_number.is_integer():
                print(f"The factorial of {user_number} is {user_number}!")
            elif user_number == 0 or user_number == 1:
                print(f"The factorial of {user_number} is 1.")
                return
            elif user_number == decimal(str(user_number)).as_tuple().exponent < 0:
                print(f"Sorry! The {user_input} is  a decimal number.")
                break
            else:
                print(f"Sorry! The {user_input} is a negative number.")
                break

        except Exception:
            print(f"Sorry! The {user_input} is not an integer.")

            counter = 0
            factorial = 1
            while counter < user_number:
                counter += 1
            factorial *= counter
            print(f"The factorial of {user_number} is {factorial}.")


if __name__ == "__main__":
    main()
