#!/env/bin python3

import csv
from typing import *
from os import system
import pickle

# Question-4. Modify the Future Value program so the user can’t cause the program to crash by entering an
# invalid int or float value.
# 1. In Pycharm, open the future_value.py (available in eConestoga with this assignment)
# 2. Review the code and study the get_number() and get_integer() functions. Note that they receive
# three arguments: the prompt for a user entry, the low value that the entry must be greater than, and
# the high value that the entry must be less than or equal to. Then, review the calling statements in
# the main() function and note how these functions are used.
# 3. Test the program. Note that you can cause the program to crash by entering values that can’t be
# converted to float and int values.
# 4. Add exception handling to the get_number() and get_integer() functions so the user has to enter
# valid float and int values. Then, test these changes to make sure the exception handling and the
# data validation work correctly.

#!/usr/bin/env python3

def get_input(prompt, low, high, is_float=True)->float|int:
    """
    This function get data from user low, high
    
    Parameters:
    prompt:str
    low: float | int
    hight: float | int
    
    Returns:
    float | int
    """ 
    while True:
        try:
            number = float(input(prompt)) if is_float else int(input(prompt))
            if number > low and number <= high:
                return number
            else:
                print(f"Entry must be greater than {low} "
                      f"and less than or equal to {high}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def calculate_future_value(monthly_investment, yearly_interest, years)->float:
    """
    This function calculate futer value
    
    Parameters:
    monthly_investment: float
    yearly_interest: float
    years: int
    
    Returns:
    float
    """     
    # convert yearly values to monthly values
    monthly_interest_rate = yearly_interest / 12 / 100
    months = years * 12

    # calculate future value
    future_value = 0.0
    for i in range(months):
        future_value += monthly_investment
        monthly_interest = future_value * monthly_interest_rate
        future_value += monthly_interest

    return future_value

def main():
    choice = "y"
    while choice.lower() == "y":
        # get input from the user
        monthly_investment = get_input("Enter monthly investment:\t", 0, 1000)
        yearly_interest_rate = get_input("Enter yearly interest rate:\t", 0, 15)
        years = get_input("Enter number of years:\t\t", 0, 50, is_float=False)

        # get and display future value
        future_value = calculate_future_value(
            monthly_investment, yearly_interest_rate, years)
        
        print()
        print(f"Future value:\t\t\t{round(future_value, 2)}")
        print()

        # see if the user wants to continue
        choice = input("Continue? (y/n): ")
        print()

    print("Bye!")

if __name__ == "__main__":
    main()
