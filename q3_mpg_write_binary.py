import pickle
from typing import List

def get_miles_driven() -> float:
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
            if miles_driven > 0:
                return miles_driven
            else:
                print("Entry must be greater than zero. Please try again.\n")
        except ValueError:
            print("Invalid input. Please enter a numeric value.\n")

def get_gallons_used() -> float:
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
            if gallons_used > 0:
                return gallons_used
            else:
                print("Entry must be greater than zero. Please try again.\n")
        except ValueError:
            print("Invalid input. Please enter a numeric value.\n")

def save_trips_to_binary(trips: List) -> None:
    '''  
    Save data to a binary file named 'trips.bin'
    
    Parameters:
    trips (list of float)
    
    Returns:
    None
    '''
    with open('trips.bin', 'wb') as file:
        pickle.dump(trips, file)

def read_trips_from_binary() -> List:
    ''' 
    Read data from a binary file named 'trips.bin'
    
    Parameters:
    None
    
    Returns:
    list of float
    '''
    try:
        with open('trips.bin', 'rb') as file:
            trips_from_file = pickle.load(file)
            print("\nTrips read from binary file:")
            for trip in trips_from_file:
                print(f"Miles Driven: {trip[0]}, Gallons Used: {trip[1]}, MPG: {trip[2]}")
    except (FileNotFoundError, EOFError):
        return []

def main():
    print()
    print("The Miles Per Gallon program\n")

    trips = [] # list of trips

    while True:
        miles_driven = get_miles_driven()
        gallons_used = get_gallons_used()

        mpg = round((miles_driven / gallons_used), 2)
        print(f"Miles Per Gallon:\t{mpg}\n")

        trips.append([miles_driven, gallons_used, mpg])

        while True:
            more = input("More entries? (y or n): ").strip().lower()
            if more in ["y", "yes"]:
                break
            elif more in ["n", "no"]:
                save_trips_to_binary(trips)
                read_trips_from_binary() # read data from binary file
                print("Bye!")
                return
            else:
                print("Invalid input. Please enter 'y' or 'n'.\n")

if __name__ == "__main__":
    main()
