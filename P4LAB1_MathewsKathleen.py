#Kathleen Mathews

#4/7/24

#P4LAB1

#This Lab will use turtle to draw a triangle and Square

#First this lab will import and create the turtle program. Then it will create the Turtle object
#Then it will create the counter variable then the first while loop to create the square.The counter will start at zero then increase by one every loop until it reaches 4 when the while loop will stop.
#Each pass through the while loop will create one side of the square. After the while loop is finished the counter will be set to zero for the triangle while loop. This  while loops is terminated when the counter goes above 3.

#import and create turtle object
import turtle
t = turtle.Turtle()

#Drawing the square
#set the counter
count = 0
while count < 4:
    t.forward(100)          
    t.left(90)             
    count += 1

#Move the turtle for the next shape
t.penup()
t.goto(110, 50)
t.pendown()

#Drawing the triangle
#reset the counter
count = 0
while count < 3:
    t.forward(100)          
    t.left(120)        
    count += 1

#Wait for the user to close the window
turtle.done()
