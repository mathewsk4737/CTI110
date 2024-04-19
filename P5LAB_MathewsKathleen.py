#Kathleen Mathews

#4/17/24

#P5LAB

#This Lab will take the year inputed by the user and then output whether it is a leap year.

#This program will first ask the user to input the year that they want to see if it is a leap year and store it in the var year. Then it will go through the function days_in_feb to see if it is a leap year.
#the first if statement will see if the year is divisable by 4 is not then it is not a leap year if so it will go onto the next if statement. The next statement will see if the tear is a century by dividing
#it by 100. If so it will go onto the next statement if it is not it is leap year. In the final statment the function will check if the year is divisable by 400 if so it is a leap year if not then it is not a leap year.
#then the result if stored into the var result then the answer is printed for the user. 


#Prompt the user to input a year
year = int(input("Enter a year to check if it is a leap year: "))
#start the function
def days_in_feb(user_year):
    #see if the year can be divided by 4 by using mod to check for a remainder of zero
    if user_year % 4 == 0:
        #check if it is a century year 
        if user_year % 100 == 0:
            #if the century year is divisble by 400 if so then it is a leap year 
            if user_year % 400 == 0: 
                return 29  
            else:
                return 28  
        else:
            return 29  
    else:
        return 28
#put the result into a variable 
result = days_in_feb(year)
#print the answer to the user
print(f"{year} has {result} days in February.")
