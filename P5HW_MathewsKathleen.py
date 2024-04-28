#Kathleen Mathews

#4/27/24

#P5HW

#This program will ask a person to take a math quiz where the user will be given three options to either do addition, subtraction, or leave the quiz.



#This program will first ask the user to select an option from the menu which lets them choose to do addition, subtraction, or leave the game.
#If the player chooses 1 for addition they will be then be given two numbers ranging from 1-100 then they have to enter in the correct answer.
#If they are wrong the quiz will give back either that they were too high or too low with their guess.
#When the user enters in the correct answer it will give them a congrats messages along with the number of guesses it took to get the right answer.  
#This process will be the the same for the subtraction option and will give the same messages.
#If the player selects option 3 the quiz will end and a farwell message will be given.

import random

def display_menu():
    print("")
    print("Welcome to Math Quiz")
    print("")
    print("MAIN MENU")
    print("1. Addition Random Numbers")
    print("2. Subtract Random Numbers")
    print("3. Exit")

def add_random_numbers():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    result = num1 + num2
    print(f"{num1} + {num2}")
    guesses = 0
    while True:
        answer = int(input("Enter your answer: "))
        guesses += 1
        if answer == result:
            print(f"Congratulations!!!! Your answer is correct.")
            print(f"Number of guesses: {guesses}")
            break
        elif answer < result:
            print("Sorry, guess is too low.")
        else:
            print("Sorry, guess is too high.")

def subtract_random_numbers():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    result = num1 - num2
    print(f"{num1} - {num2}")
    guesses = 0
    while True:
        answer = int(input("Enter your answer: "))
        guesses += 1
        if answer == result:
            print(f"Congratulations!!!! Your answer is correct.")
            print(f"Number of guesses: {guesses}")
            break
        elif answer < result:
            print("Sorry, guess is too low.")
        else:
            print("Sorry, guess is too high.")

def main():
    while True:
        display_menu()
        choice = input("Please choose one of the menu options: ")
        if choice == '1':
            add_random_numbers()
        elif choice == '2':
            subtract_random_numbers()
        elif choice == '3':
            print("Thank you for playing...")
            print("Bye!!")

            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
