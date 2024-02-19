#Kathleen Mathews
#2/18/24
#P1HW1
#In this assignment the user will input a integer and the program will
#output the squared and cubed answer. Then the user will input a second integer
#that will be added and multiplied to the first integer.

print('Enter integer:')
num=int(input())
print('You entered:', num)
square_num = num * num
cube_num = num * num * num
print(num,'squared is', square_num)
print('and',num,'cubed is', cube_num,"!!")
print('Enter another integer:')
num2=int(input())
sum = num + num2
multi= num * num2
print(num,'+',num2,'is',sum)
print(num,'*',num2,'is',multi)

