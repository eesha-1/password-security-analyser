import string
import random

current_password = input("Please enter your current password: ") #Prompts user to input their current password

while current_password.strip() == "": #Checks if input is empty
    print("Invalid password, please enter password again. ") #Prompts user to enter password again
    current_password = input("Please enter your current password: ") #Prompts user to re-enter their current password

print(f"Analysing: {current_password}") #Prints Analysing with the users current password

score = 0 #Initialises password score to zero

if len(current_password) < 6:
    score = score + 0 #Awards zero points for a password equal to or under 6 characters
elif len(current_password) >= 6 and len(current_password) <= 9:
    score = score + 1 #Awards one point if length is between six and nine characters
else:
    score = score + 2 #Awards two points if character length is equal to or over ten

#Initially sets the password to contain no letters, numbers or symbols
has_letter = False
has_number = False
has_symbol = False

for character in current_password:
    if character.isalpha(): #If alphabetical letter
        has_letter = True
    elif character.isdigit(): #If number
        has_number = True
    else: #Else symbol
        has_symbol = True 

if has_letter and has_number and has_symbol:
    score = score + 3 
elif has_letter and has_number:
    score = score + 2
elif has_letter and has_symbol:
    score = score + 2
elif has_symbol and has_number:
    score = score + 2
elif has_letter:
    score = score + 1
elif has_number:
    score = score + 1
elif has_symbol:
    score = score + 1

#Checking lowercase and uppercase characters in the password
#initially sets the password to contain no lowercase or uppercase letters
has_lowercase = False 
has_uppercase = False

for character in current_password:
    if character.islower():
        has_lowercase = True
    elif character.isupper():
        has_uppercase = True

if has_lowercase and has_uppercase: #If password contains mix of uppercase and lowercase letters
    score = score + 2
elif has_lowercase:
     score = score + 1
elif has_uppercase:
     score = score + 1

print(f"Your password strength score is: {score} out of 7") #Prints password score

recommendation = input("Would you like a stronger and more secure password recommendation? ")
recommendation = recommendation.lower().strip() #Converts user input to lowercase and removes spaces
yes_response = ["yes", "yeah", "y", "yep", "sure", "ok", "okay"] #Stores yes inputs
no_response = ["no", "nope", "n", "nah"] #Stores no inputs

while recommendation not in yes_response and recommendation not in no_response:
    print ("Invalid response, please enter yes or no. ")
    recommendation = input("Would you like a stronger and more secure password recommendation? ")
    recommendation = recommendation.lower().strip() #Converts user input to lowercase and removes spaces
if recommendation in yes_response:
    print("Generating a secure password... ")
    acceptable_password = False
    while acceptable_password == False:
        characters = string.ascii_letters + string.digits + string.punctuation
        secure_password = "" #initially sets secure password to nothing
        for i in range(12): #Generates 12 random characters
            secure_password = secure_password + random.choice(characters)
        #Initially sets generated password to have no upper or lowercase letters or numbers, symbols   
        generated_has_letter = False
        generated_has_number = False
        generated_has_symbol = False
        generated_has_uppercase = False
        generated_has_lowercase = False

        for character in secure_password:
            if character.isalpha(): #If alphabetical letter
                generated_has_letter = True
            if character.isdigit(): #If number
                generated_has_number = True
            if not character.isalpha() and not character.isdigit():
                generated_has_symbol = True
            if character.isupper():
                generated_has_uppercase = True
            if character.islower():
                generated_has_lowercase = True 
        if generated_has_letter and generated_has_number and generated_has_symbol and generated_has_uppercase and generated_has_lowercase:
            acceptable_password = True
            print(f"Your recommended secure password is: {secure_password}") #Prints recommended secure password
                
elif recommendation in no_response:
    print("Ok, thank you for using our system. Stay safe! ")


