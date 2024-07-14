#!/usr/bin/env python3
        
def get_number(prompt, low, high):
    ''' 
    Get a float value from the user between low and high
    
    Parameters:
    prompt:str
    low: float
    hight: float
    
    Returns:
    number :float
    '''
    while True:
        try:
            number = float(input(prompt))
            if number > low and number <= high:
                is_valid = True
                return number
            else:
                print(f"Entry must be greater than {low} " 
                    f"and less than or equal to {high}.")
                continue
        except ValueError:
            print("Invalid input. Please enter a float value.")

def get_integer(prompt, low, high):
    ''' 
    Get an integer value from the user between low and high
    
    Parameters:
    prompt:str
    low: float
    hight: float
    
    Returns:
    number:float
    '''
    while True:
        try:
            number = int(input(prompt))
            if number > low and number <= high:
                is_valid = True
                return number
            else:
                print(f"Entry must be greater than {low} " 
                    f"and less than or equal to {high}.")
                continue
        except ValueError:
            print("Invalid input. Please enter an integer value.")


def calculate_future_value(monthly_investment, yearly_interest, years):
    ''' 
    Calcuate the future value of an investment
    
    Parameters:
    monthly_investment: float
    yearly_interest: float
    years: int
    
    Returns:
    future_value: float
    '''
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
    while True:
        # get input from the user
        print()
        print("Future Value Calculator\n")
        monthly_investment = get_number("Enter monthly investment:\t", 0, 1000)
        yearly_interest_rate = get_number("Enter yearly interest rate:\t", 0, 15)
        years = get_integer("Enter number of years:\t\t", 0, 50)

        # get and display future value
        future_value = calculate_future_value(
            monthly_investment, yearly_interest_rate, years)
        
        print()
        print(f"Future value:\t\t\t{round(future_value, 2)}")
        print()

        # see if the user wants to continue
        while True:
            choice = input("Continue? (y/n): ")
            if choice.lower() == "y":
                break
            elif choice.lower() == "n":
                print("Bye!")
                exit()
            else:
                print("Invalid input. Please enter 'y' or 'n'.")
    
if __name__ == "__main__":
    main()
