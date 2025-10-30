#A programme for classifying people's ages 
#date: 23 October 2025

name = input ("Please provide your name -->")
print("Hello", name) #greeting with user's name
print("I am an age classification program.")
#int function and input function for user to put in age
age = int(input("Please provide your current age in years -->"))
#while loop if user puts in a negative number
while age < 0:
    print("Age cannot be a negative number. Please try again.")
    age = int(input("Please provide your current age -->")) #exits out of while loop
#if, elif and else statements to classify user's age
if age <= 2:
    print("You are a baby.")
elif age <= 12:
    print("You are a child.") #elif statement used because there is more than 2 outcomes
elif age <= 17:
    print("You are a teenager.")
elif age <= 64:
    print ("You are an adult.")
else: 
    print("You are a pensioner.")

  
