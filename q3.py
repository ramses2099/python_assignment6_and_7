#!/env/bin python3

from typing import *
from os import system
import pickle

# Question-3. Modify the programs that you created Question-1 and Question-2 so they create and use a
# binary file instead of a CSV file. Otherwise, everything should work the same.
# Modify the CSV version of the write program
# 1. Open the mpg_write.py file that you created in exercise Question-l. Then, save it as
# mpg_write_binary.py in the same directory.
# 2. Modify this program so it saves the list as a binary file instead of a CSV file. The file should be
# named trips.bin.
# 3. Test the program to make sure it works. To do that, add statements that read the file at the end of
# the program and display the list that has been read.
# Modify the CSV version of the trip program
# 4. Open the mpg.py file that you created in exercise Question-2. Then, save it as mpg_binary.py.
# 5. Modify this program so it works the same as it did with the CSV file.
# 6. Test this program to make sure it works.

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
            miles_driven = float(input("Enter miles driven:\t"))
            if miles_driven <= 0:
                print("Entry must be greater than zero. Please try again.\n")
            else:
                return miles_driven
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
            gallons_used = float(input("Enter gallons of gas:\t"))
            if gallons_used <= 0:
                print("Entry must be greater than zero. Please try again.\n")
            else:
                return gallons_used
        except ValueError:
            print("Invalid input. Please enter a numeric value.\n")

def main():
    system('clear')
    # display a welcome message
    print("The Miles Per Gallon program")
    print()

    trips = []
    more = "y"
    while more.lower() == "y":
        miles_driven = get_miles_driven()
        gallons_used = get_gallons_used()
        mpg = round((miles_driven / gallons_used), 2)
        trips.append((miles_driven, gallons_used, mpg))
        print(f"Miles Per Gallon:\t{mpg}")
        print()

        more = input("More entries? (y or n): ")

    # Save the trips list as a binary file
    with open('trips.bin', 'wb') as file:
        pickle.dump(trips, file)

    # Read the binary file to verify it was written correctly
    with open('trips.bin', 'rb') as file:
        trips_from_file = pickle.load(file)
        print("\nTrips read from binary file:")
        for trip in trips_from_file:
            print(f"Miles Driven: {trip[0]}, Gallons Used: {trip[1]}, MPG: {trip[2]}")

    print("Bye!")

if __name__ == "__main__":
    main()

