#!/env/bin python3

import csv
from typing import *
from os import system
import pickle

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
