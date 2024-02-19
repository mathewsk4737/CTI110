# Kathleen Mathews
# 2/18/24
# P1HW2
# This program will take the input from the user about a trip's budget and expenses and give the output to the user of the expenses subtracted out of the budget to show the remainder. 

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

print('------------Travel Expenses------------')
print('Location:',place)
print('Initial Budget:',budget)
print('')
print('Fuel:',gas)
print('Accomodation:',hotel)
print('Food:',food)
print('')
print('Remaining Balance:',rem)
