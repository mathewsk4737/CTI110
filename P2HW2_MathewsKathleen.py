#Kathleen Mathews

#3/10/24

#P2HW2

#This project will take the users input of their grades from 6 modules and then give the lowest, highest, sum, and average of the grades inputed

#The user will input their grades when prompted for all modules 1-6 the program will store the answer in a float titled module 1, module 2, etc.
#Next the list will be created called module_grades then the variables created above will be appended/added into the list
#The results will print the lowest grade, highest grade, the sum of all the grades,
#and finally the average of the grades which is calculated by taking the sum of module_grades and dividing it by the number of entries found in the len(). 

module1 = float(input("Enter grade for Module 1:"))
module2 = float(input("Enter grade for Module 2:"))
module3 = float(input("Enter grade for Module 3:"))
module4 = float(input("Enter grade for Module 4:"))
module5 = float(input("Enter grade for Module 5:"))
module6 = float(input("Enter grade for Module 6:"))

module_grades=[]

module_grades.append(module1)
module_grades.append(module2)
module_grades.append(module3)
module_grades.append(module4)
module_grades.append(module5)
module_grades.append(module6)

print("-------------Results----------------------")
print(f'Lowest grade:      {min(module_grades)}')
print(f'Highest grade :    {max(module_grades)}')
print(f'Sum of grades :    {sum(module_grades)}')
print(f'Average:           {sum(module_grades)/len(module_grades):.2f}')
print("----------------------------------------------------")


