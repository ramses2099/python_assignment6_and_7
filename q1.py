import csv
from typing import *
# from os import system

# Question-1. Modify the Miles Per Gallon program so it stores the data for each calculation in a CSV file.
# 1. In PyCharm, open the mpg_write.py file (available in eConestoga with this assignment)
# 2. Review the code and run the program so you remember how it works.
# 3. Enhance the program so it stores the data for each calculation, or trip, in a two-dimensional list. For
# each calculation, these values should be put in the list: miles driven, gallons of gas used, and the
# calculated MPG value.
# 4. Enhance the program so it saves the data in the list to a file named trips.csv when the user wants to
# exit from the program.
# 5. Test the program to make sure it works. To do that, you can open the CSV file with a spreadsheet
# program like Excel.
# 6. Take a screen shot of the spreadsheet


def get_miles_driven()->float:
    """
    This function get data from user miles driven
    
    Parameters:
    None
    
    Returns:
    float
    """    
    while True:
        try:
            miles_driven:float = float(input("Enter miles driven:\t"))
            if miles_driven > 0:
                return miles_driven
            else:
                print("Entry must be greater than zero. Please try again.\n")
        except ValueError:
            print("Invalid input. Please enter a numeric value.\n")

def get_gallons_used()->float:
    """
    This function get data from user gallons used
    
    Parameters:
    None
    
    Returns:
    float
    """    
    while True:
        try:
            gallons_used:float = float(input("Enter gallons of gas:\t"))
            if gallons_used > 0:
                return gallons_used
            else:
                print("Entry must be greater than zero. Please try again.\n")
        except ValueError:
            print("Invalid input. Please enter a numeric value.\n")

def save_trips_to_csv(trips:List)->None:
    """
    This function save data to a csv file named 'trips.csv'
    
    Parameters:
    trips (list of float)
    
    Returns:
    None
    """
    with open('trips.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Miles Driven", "Gallons Used", "MPG"])
        writer.writerows(trips)

def main():
    print()
    print("The Miles Per Gallon program\n")

    trips = []  # List to store trip data

    while True:
        miles_driven = get_miles_driven()
        gallons_used = get_gallons_used()

        mpg = round((miles_driven / gallons_used), 2)
        print(f"Miles Per Gallon:\t{mpg}\n")

        # Store the trip data
        trips.append([miles_driven, gallons_used, mpg])

        while True: # Validation for more entries
            more = input("More entries? (y or n): ").strip().lower()
            if more in ["y", "yes"]:
                break
            elif more in ["n", "no"]:
                # Save the trip data to a CSV file
                save_trips_to_csv(trips)
                print("Bye! The trip data has been saved to trips.csv.")
                return
            else:
                print("Invalid input. Please enter 'y' or 'n'.\n")

if __name__ == "__main__":
    main()
