#!/env/bin python3

from typing import *
from os import system
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
            # Raise a BlockingIOError to test the exception handling
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
    print()
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
