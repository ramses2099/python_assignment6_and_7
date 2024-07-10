#!/env/bin python3

from typing import *
from os import system


# Question-5. In this exercise, you’ll modify the Movies List 2.0 program so it does more exception handling.
# You’ll also use a raise statement to test for exceptions.
# 1. In Pycharm, open movies2.py (available in eConestoga with this assignment)
# 2. Add data validation to the add_movie() function so the year entry is a valid integer that’s greater than zero.
# Then, test this change.
# 3. Modify the write_movies() function so it also handles any OSError exceptions by displaying the class
# name and error message of the exception object and exiting the program
# 4. Test this by using a raise statement in the try block that raises a BlockingIOError. This is one of the child
# classes of the OSError. Then, comment out the raise statement.
# 5. In the read_movies() function, comment out the two statements in the except clause for the
# FileNotFoundError. Instead, use this except clause to return the empty movies list that’s initialized in the try
# block. This should cause

import csv
import sys

FILENAME = "movies.csv"

def exit_program()->None:
    print("Terminating program.")
    sys.exit()

def read_movies():
    try:
        movies = []
        with open(FILENAME, newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                movies.append(row)
        return movies
    except FileNotFoundError as e:
        print(f"Could not find {FILENAME} file.")
        return movies  # Return empty list if file is not found
    except Exception as e:
        print(type(e), e)
        exit_program()

def write_movies(movies)->None:
    try:
        with open(FILENAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(movies)
            # raise BlockingIOError("Testing exception handling")  # Uncomment to test
    except OSError as e:
        print(f"OSError: {type(e).__name__} - {e}")
        exit_program()
    except Exception as e:
        print(type(e), e)
        exit_program()

def list_movies(movies):
    for i, movie in enumerate(movies, start=1):
        print(f"{i}. {movie[0]} ({movie[1]})")
    print()
    
def add_movie(movies):
    name = input("Name: ")
    while True:
        year = input("Year: ")
        try:
            year = int(year)
            if year <= 0:
                raise ValueError("Year must be greater than zero.")
            break
        except ValueError as e:
            print(f"Invalid year: {e}. Please try again.")
    movie = [name, year]
    movies.append(movie)
    write_movies(movies)
    print(f"{name} was added.\n")

def delete_movie(movies)->None:
    while True:
        try:
            number = int(input("Number: "))
        except ValueError:
            print("Invalid integer. Please try again.")
            continue
        if number < 1 or number > len(movies):
            print("There is no movie with that number. Please try again.")
        else:
            break
    movie = movies.pop(number - 1)
    write_movies(movies)
    print(f"{movie[0]} was deleted.\n")

def display_menu()->None:
    print("The Movie List program")
    print()
    print("COMMAND MENU")
    print("list - List all movies")
    print("add -  Add a movie")
    print("del -  Delete a movie")
    print("exit - Exit program")
    print()    

def main():
    display_menu()
    movies = read_movies()
    while True:        
        command = input("Command: ")
        if command.lower() == "list":
            list_movies(movies)
        elif command.lower() == "add":
            add_movie(movies)
        elif command.lower() == "del":
            delete_movie(movies)
        elif command.lower() == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")
    print("Bye!")

if __name__ == "__main__":
    main()
