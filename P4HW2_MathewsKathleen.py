#Kathleen Mathews

#4/14/24

#P4HW2

#This program takes the name, pay rate, and hours worked of an employee and prints out its detailed information at the very end when the user inputs done to terminate the program it will display the totals of all employees entered into the program.



#This program first creates the variables for the program then it starts a loop for the user to enter employee data.
#It will prompt the user to enter in the employees name, hours worked and pay rate. Then it will calculate out the pay for the regular hours worked and the pay for the overtime hours worked. Afterwards it will calculate out the gross
#pay by adding the regular and overtime pay together. It will then print out the the employee's name and then the Hours Worked, Pay Rate, OverTime, OverTime Pay, RegHour Pay, and Gross Pay.
#Then the program will add all the information into the varaibles 
#Then the program restarts and asks for the next employee's name, but if the user enters done then the loop will terminate and all of the totals for all the employees entered will be displayed.



#create the variables for the totals
total_employees = 0
overtime_hours = 0
total_overtime = 0
total_regular = 0
total_gross = 0

#The main loop to enter in the employees data
while True:
    employee_name = input("Enter employee's name or 'done' to terminate: ")
    
    if employee_name.lower() == 'done':
        break
    
    hours_worked = float(input(f"How many hours did {employee_name} work? "))
    pay_rate = float(input(f"What is {employee_name}'s pay rate? "))
    
    #Calculate the regular pay or total_regular
    if hours_worked <= 40:
        regular_pay = hours_worked * pay_rate
        overtime_pay = 0
    #calculate the overtime pay or total_overtime and gross pay
    else:
        regular_pay = 40 * pay_rate
        overtime_hours = hours_worked - 40
        overtime_pay = overtime_hours * (pay_rate * 1.5)

    gross_pay = regular_pay + overtime_pay
    
    #Update totals
    total_employees += 1
    total_regular += regular_pay
    total_overtime += overtime_pay
    total_gross += gross_pay
    
    #print employee hours worked, payrate, overtime hours, overtime pay, regular pay, and gross pay
    print("------------------------------------")
    print("Employee name:",employee_name)
    print()
    print("Hours Worked     Pay Rate         OverTime       OverTime Pay     RegHour Pay      Gross Pay")
    print("-------------------------------------------------------------------------------------------------------")
    print(f'{hours_worked:<17.2f}{pay_rate:<17.2f}{overtime_hours:<15.2f}{total_overtime:<17.2f}${total_regular:<17.2f}${total_gross:<17.2f}')

    
#Prints the totals for the employees entered into the program
print(f"Total number of employees entered: {total_employees}")
print(f"Total amount paid for overtime: ${total_overtime:.2f}")
print(f"Total amount paid for regular hours: ${total_regular:.2f}")
print(f"Total amount paid in gross: ${total_gross:.2f}")
