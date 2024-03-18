#Kathleen Mathews

#3/17/24

#P3HW1

#This program will take the grades for 6 modules and store them into a list then the program will print the lowest, highest, sum, average, and letter grade for the user


#The user will input their grades when prompted for all modules 1-6 the program will store the answer in a float titled module 1, module 2, etc.
#Next the list will be created called grades and the modules will be added into it
#The program will then assign variables for low, high, sum, and average  
#The results will print the lowest grade, highest grade, the sum of all the grades, and the average of the grades
#Then the program will print the letter grade for the user by using If Else statements  

# Enter grades for six modules
mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

#add grades entered to a list

grades = [mod_1,mod_2,mod_3,mod_4,mod_5,mod_6]

#TO DO: determine lowest, highest , sum and average for grades
low = min(grades)
high = max(grades)
sum = sum(grades)
avg = sum/len(grades)


print("-------------Results----------------------")
print(f'Lowest grade:      {low}')
print(f'Highest grade :    {high}')
print(f'Sum of grades :    {sum}')
print(f'Average:           {avg:.2f}')
print("----------------------------------------------------")

# determine letter grade for average
if avg >= 90:
    print('Your grade is: A')
else:
    if avg >= 80:
     print('Your grade is: B')
    else:
        if avg >= 70:
            print('Your grade is: C')
        else:
            if avg >= 60:
                print('your grade is: D')
            else:
                print('Your grade is: F') 
