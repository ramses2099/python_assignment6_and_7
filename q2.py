#!/env/bin python3

import csv
from typing import *
from os import system


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

    while True:
        miles_driven = get_positive_float("Enter miles driven:\t")
        gallons_used = get_positive_float("Enter gallons of gas:\t")

        mpg = round((miles_driven / gallons_used), 2)
        print(f"Miles Per Gallon:\t{mpg}")
        print()
        
        trips.append([miles_driven, gallons_used, mpg])
        list_trips(trips)
        print()

        while True:
            more = input("More entries? (y or n): ").strip().lower()
            if more in ["y", "yes"]:
                break
            elif more in ["n", "no"]:
                write_trips(trips)
                print("Bye!")
                return  # Exit the main function
            else:
                print("Invalid input. Please try again.\n")


if __name__ == "__main__":
    main()
