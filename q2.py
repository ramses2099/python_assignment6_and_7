#!/env/bin python3

import csv
from typing import *
from os import system

# Question-2. Modify the Miles Per Gallon program so it adds to the data in the file that you created in
# Question-1 above. This program should display the data for each trip that’s entered in a CSV file as shown
# below:
# The Miles Per Gallon program
# Distance Gallons MPG
# 225 17 13.24
# 1374 64 21.47
# 2514 79 31.82
# Enter miles driven: 274
# Enter gallons of gas: 18.5
# Miles Per Gallon: 14.81
# Distance Gallons MPG
# 225 17 13.24
# 1374 64 21.47
# 2514 79 31.82
# 274.0 18.5 14.81
# More entries? (y or n):
# 1. In Pycharm, open the mpg.py file (available on eConestoga with this assignment)
# 2. Add a write_trips() function that writes the data from a two-dimensional list named trips that’s
# passed to it as an argument. This list contains the data for each trip that’s entered, and it should be
# written to a CSV file named trips.csv. As the console above shows, the data for each trip consists of
# miles driven, gallons of gas used, and the calculated MPG value.
# 3. Add a read_trips() function that reads the data from the trips.csv file and returns the data for the
# trips in a two-dimensional list named trips.
# 4. Add a list_trips() function that displays the data in the trips list on the console, as shown above.
# 5. Enhance the main() function so it starts by getting the data from the CSV file and listing it as shown
# above.
# 6. Enhance the main() function so it adds the last trip that’s entered to the trips list after it calculates
# the MPG. Then, display the data for the updated trips list.
# 7. Test all aspects of the program until you’re sure that it works correctly.


def get_positive_float(prompt: str)->float:
    """
    This function get data from user and convert to float value
    
    Parameters:
    prompt: str
    
    Returns:
    float
    """   
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            else:
                print("Entry must be greater than zero. Please try again.\n")
        except ValueError:
            print("Invalid input. Please enter a numeric value.\n")

def write_trips(trips:List)->None:
    """
    This function write data in a csv file named 'trips.csv'
    
    Parameters:
    trips:List
    
    Returns:
    None
    """   
    with open('trips.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Distance", "Gallons", "MPG"])
        writer.writerows(trips)

def read_trips()->List:
    """
    This function read data from csv file named 'trips.csv'
    
    Parameters:
    trips:List
    
    Returns:
    List
    """
    trips = []
    try:
        with open('trips.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header
            for row in reader:
                trips.append([float(row[0]), float(row[1]), float(row[2])])
    except FileNotFoundError:
        pass
    return trips

def list_trips(trips:List)->None:
    """
    This function show a list for console
    
    Parameters:
    trips:List
    
    Returns:
    None
    """
    print("Distance Gallons MPG")
    for trip in trips:
        print(f"{trip[0]} {trip[1]} {trip[2]}")

def main():
    # display a welcome message
    print("The Miles Per Gallon program")
    print()

    trips = read_trips()
    if trips:
        list_trips(trips)
        print()

    more = "y"
    while more.lower() == "y":
        miles_driven = get_positive_float("Enter miles driven:\t")
        gallons_used = get_positive_float("Enter gallons of gas:\t")
                                 
        mpg = round((miles_driven / gallons_used), 2)
        print(f"Miles Per Gallon:\t{mpg}")
        print()
        
        trips.append([miles_driven, gallons_used, mpg])
        list_trips(trips)
        print()

        more = input("More entries? (y or n): ").strip().lower()
    
    write_trips(trips)
    print("Bye!")

if __name__ == "__main__":
    main()
