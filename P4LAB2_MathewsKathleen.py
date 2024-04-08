#Kathleen Mathews

#4/7/24

#P4LAB2

#This Lab will take the users input of two intergers and print the number inbetween them in increments of 5.

#This program will prompt the user to input two integers and store them into the varaibles integer_one and integer_two.
#The program will then do a if else statement. If the second integer is less than the first integer inputed the program will print
#"Second integer can't be less than the first." Else the program will preform a while loop where it will print the numbers in increments of 5.


#User prompted to enter two integers 
print("Enter two intergers.")
#Get the user's input integers
integer_one = int(input())
integer_two = int(input())

#Check if integer two is less than interger one
if integer_two < integer_one:
    print("Second integer can't be less than the first.")
else:
    #Output the the amount between the two numbers in increments of 5
    current_integer = integer_one
    while current_integer <= integer_two:
        print(current_integer, end=' ')
        current_integer += 5
print("")
