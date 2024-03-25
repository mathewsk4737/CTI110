#Kathleen Mathews

#3/24/24

#P3HW1

#This project will take a users name, hours worked, and payrate and give the user the calculated out overtime, overtime pay, regular hours pay, and gross pay.



#This program takes the users name, hours worked, and payrate into the variables employee_name, hours_worked, and pay_rate. To do the calculations the variables overtime_pay and over_time are created
#The if statement is there if the user has more than 40 hours it will calculate the the overtime payrate, overtime pay, and regular pay.
#if the user has less than 40 hours it will just calculate the regular pay rate
#gross pay is regular pay multiplied by the payrate then all the outputs are printed: hours worked, payratem overtimem overtime pay, regular hours pay, and gross pay. 



#user input information
employee_name = input("Enter employee's name:")
hours_worked= float(input("Enter number of hours worked:"))
pay_rate= float(input("Enter employee's pay rate:"))

#calculate the total pay, overtime pay, and regular pay.
overTime_pay = 0.0
over_time = 0.0
if hours_worked > 40:
	over_time = hours_worked - 40
	ot_payRate = pay_rate + (pay_rate * 0.5)
	overTime_pay = over_time * ot_payRate
	reg_pay = 40 * pay_rate
else:
	reg_pay = hours_worked * pay_rate

#calculate gross pay
gross_pay = reg_pay + overTime_pay

#output 
print("------------------------------------")
print("Employee name:",employee_name)
print()
print("Hours Worked     Pay Rate         OverTime       OverTime Pay     RegHour Pay      Gross Pay")
print("-------------------------------------------------------------------------------------------------------")
print(f'{hours_worked:<17.2f}{pay_rate:<17.2f}{over_time:<15.2f}{overTime_pay:<17.2f}{reg_pay:<17.2f}{gross_pay:<17.2f}')
