# Kathleen Mathews

# 3/3/24

# P2LAB2 

# The user will input 4 numbers and then will recieve the product and average of the four numbers with 0 and 3 decimal places 

#The user will be prompted to input 4 numbers into the program
print("Input 4 numbers and the program will give you the product and average")
num1=float(input())
num2=float(input())
num3=float(input())
num4=float(input())

#The average and product are calculated from the 4 numbers 
product_num= num1 * num2 * num3 * num4
avg_num=(num1 + num2 + num3 + num4) / 4


#Prints the product and average of the 4 inputed numbers once with no decimal place and then again with 3 decimal places 
print(f'{product_num:.0f} {avg_num:.0f}')
print(f'{product_num:.3f} {avg_num:.3f}')
