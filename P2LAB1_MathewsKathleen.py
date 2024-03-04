#Kathleen Mathews

#3/3/24

#P2LAB1_MathewsKathleen 

#This Project will take the inputs of cost per gallon and miles per gallon from the user and output the cost of taking a 20, 75, and 500 mile trip. 


#User input for the miles per gallon and the cost per gallon
print("Input the miles per gallon")
miles_per_gallon = float(input())
print("Input the cost per gallon")
cost_per_gallon = float(input())

#calculate the cost of gas for 20, 75, 500 miles trips
cost_20_miles = cost_per_gallon * 20 / miles_per_gallon
cost_75_miles = cost_per_gallon * 75 / miles_per_gallon
cost_500_miles = cost_per_gallon * 500 / miles_per_gallon

#Print the result from the above calculations for 25, 75, and 500 mile trips with 2 decimal places 
print("The cost to drive 20, 75, and 500 miles.")
print(f'{cost_20_miles:.2f} {cost_75_miles:.2f} {cost_500_miles:.2f}')
