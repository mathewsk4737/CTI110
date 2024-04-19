#Kathleen Mathews

#4/14/24

#P4HW1

#This project will ask the users for the number of score and then ask the user to input their scores and then print out the lowest score, list of scores, score average, and letter grade.


#First the program will ask the user to give the amount of scores they need to input and store it in the var num_scores
#Then the program will create the list scores to store all the scores into. Then for the user to input their scores a for loop will start and prompt them to enter in a score.
#If the score is not valid it will tell the user that the score is invaild and ask them to reenter it again. afterwards the scores will be appended to the scores list
#Next the program will calculate out the lowest score, remove the lowest score and then get the averages of the scores entered. A if else statement is used with the scores average to determine the letter grade
#Now the program will print out the results to the user which are lowest score, the lost of scores, scores average, and the letter grade.


#Prompts user to input the number of grades they want to enter and then creating the list to store the scores into
num_scores = int(input("How many scores do you want to enter? "))
scores = []

#loop that will ask the user to input the scores. if a score is not valid it will reprompt the user to enter it in again. 
for i in range(num_scores):
    score = float(input("Enter score #{}: ".format(i + 1)))
    if score < 0 or score > 100:
        print("INVALID score entered!!!!")
        print("Please enter a score between 0 and 100.")
        while True:
            score = float(input("Enter score #{} again: ".format(i + 1)))
            if 0 <= score <= 100:
                break
    
#Add the valid score to the scores list
scores.append(score)

#Calculating the lowest score, dropping the lowest score and average of the list            
lowest_score = min(scores)
scores.remove(lowest_score)
average_score = sum(scores) / len(scores)


#Determining the letter grade for the calculated average
if 90 <= average_score <= 100:
    grade = 'A'
elif 80 <= average_score < 90:
    grade = 'B'
elif 70 <= average_score < 80:
    grade = 'C'
elif 60 <= average_score < 70:
    grade = 'D'
else:
    grade = 'F'


#Print the results
print("\n--------------Results-----------")
print(f"Lowest Score  : {lowest_score}")
print("Modified List :", scores)
print(f"Scores Average: {average_score:.2f}")
print(f"Grade         : {grade}")
print("\n---------------------------------")
