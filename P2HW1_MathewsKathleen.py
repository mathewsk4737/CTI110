# Kathleen Mathews
# 3/9/24
# P2HW1
# This program will take the input from the user about a trip's budget and expenses and give the
# output to the user of the expenses subtracted out of the budget to show the remainder. 


# This program will ask for a series of inputs from the user and then print an output that shows a series of expenses and remaining balance.
# The inputs for this program are Budget, name of destination, gas money, expense for accomodation, and food expense.
# The program will create variables and use their out put in the Travel Expense output.
# the first variable is "expense" which is the addition of the gas, food, and hotel into one variable
# the second variable named "rem" is the remaining amount of money the user has. This is calculated by taking the budget input from the begining and subtracting the expense variable calculated the line above it
# the last part of the program is the printed outputs where the location, initial budget, fuel, food, accomodation, and remaining balance are printed for the user to read. 

print('This program calculates and displays travel expenses')
print('')
print('Enter Budget:')
budget=int(input())
print('Enter your travel destination:')
place=input()
print('How much do you think you will spend on gas?')
gas=int(input())
print('Approximately, how much will you need for accomodation/hotel?')
hotel=int(input())
print('Last, how much do you need for food?')
food=int(input())

expense= gas + food + hotel
rem= budget - expense
x = ""

print('------------Travel Expenses------------')
print(f'Location: {x:>11}{place}')
print(f'Initial Budget: {x:>5}${budget:.2f}')
print(f'Fuel: {x:>15}${gas:.2f}')
print(f'Accomodation: {x:>7}${hotel:.2f}')
print(f'Food: {x:>15}${food:.2f}')
print('---------------------------------------')
print()
print(f'Remaining Balance: {x:>2}${rem:.2f}')
 
