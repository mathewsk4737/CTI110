#Kathleen Mathews

#3/17/24

#P3LAB

#This program will take a year inputed by the user and return if the year is or is not a leap year

#This program makes a variable is_leap_year and sets it to false it asks and receives a year from the user into input_year variable
#then the input year will be checked to see if it is divisible by 4 if true then it will try and divide it by 100 and 400 if it is also true the
#is_leap_year variable will be set to true and the program will print the year and " - leap year" if false it will print "- not a leap year)


#Make the variable and get user's input
print("Enter a year to see if it is a leap year!")
is_leap_year = False
input_year = int(input())

#Check to see if the year is divisible by 4 by seeing if the remainder is 0
#If the year is divisible by 400 it is a leap year

if input_year % 4 == 0:
    if input_year % 100 == 0:
        if input_year % 400 == 0:
            is_leap_year = True
    else:
        is_leap_year = True

# Print the result for the user
if is_leap_year:
    print(f"{input_year}-leap year")
else:
    print(f"{input_year} not a leap year")
